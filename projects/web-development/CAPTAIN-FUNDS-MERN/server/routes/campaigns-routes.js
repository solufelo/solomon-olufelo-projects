import Campaign from "../models/campaignmodel.js";
import Donation from "../models/donationmodel.js";
import UserModel from "../models/user-model.js";
import { Router } from "express";
import { authenticateToken, requireAdmin } from "../middleware/auth.js";
import emailService from "../services/emailService.js";

const router = Router();

// GET /api/campaigns - Get all active, approved campaigns for public view
router.get("/", async (req, res) => {
  try {
    const campaigns = await Campaign.find({
      isActive: true,
      isApproved: true,
      isDeleted: false
    }).sort({ createdAt: -1 });
    
    res.status(200).json({
      success: true,
      campaigns,
      count: campaigns.length
    });
  } catch (error) {
    console.error("Error fetching campaigns:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching campaigns",
      error: error.message
    });
  }
});

// GET /api/campaigns/:id - Get single campaign by ID
router.get("/:id", async (req, res) => {
  try {
    const campaign = await Campaign.findById(req.params.id);
    
    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    res.status(200).json({
      success: true,
      campaign
    });
  } catch (error) {
    console.error("Error fetching campaign:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching campaign",
      error: error.message
    });
  }
});

// POST /api/campaigns/:id/donate - Make a donation to a campaign
router.post("/:id/donate", authenticateToken, async (req, res) => {
  try {
    const { amount, message, isAnonymous, paymentMethod } = req.body;

    if (!amount || amount <= 0) {
      return res.status(400).json({
        success: false,
        message: "Valid donation amount is required"
      });
    }

    const campaign = await Campaign.findById(req.params.id);

    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    if (!campaign.isActive || !campaign.isApproved || campaign.isDeleted) {
      return res.status(400).json({
        success: false,
        message: "Campaign is not available for donations"
      });
    }

    if (campaign.endDate < new Date()) {
      return res.status(400).json({
        success: false,
        message: "Campaign has ended"
      });
    }

    // Create donation record
    const donation = await Donation.create({
      userId: req.user._id,
      campaignId: req.params.id,
      amount,
      message: message || "",
      isAnonymous: isAnonymous || false,
      paymentMethod: paymentMethod || "credit_card",
      paymentStatus: "completed"
    });

    // Update campaign current amount
    const oldAmount = campaign.EventCurrentAmount;
    campaign.EventCurrentAmount += amount;
    await campaign.save();

    // Send email notifications asynchronously (don't block response)
    setImmediate(async () => {
      try {
        // Get donor information (only if not anonymous)
        const donor = await UserModel.findById(req.user._id).select('name email');
        const donorName = donation.isAnonymous ? 'Anonymous Donor' : (donor?.name || 'Valued Supporter');

        // Send donation confirmation to donor
        if (!donation.isAnonymous && donor?.email) {
          await emailService.sendDonationConfirmation(
            donor.email,
            donor.name,
            campaign.title,
            amount,
            campaign.organizer
          );
        }

        // Send notification to campaign organizer
        // Note: In a real app, you'd need to store organizer email in campaign or user model
        // For now, we'll skip this as it requires additional setup

        console.log('Email notifications sent for donation');
      } catch (error) {
        console.error('Error sending donation emails:', error);
      }
    });

    // Check if campaign goal was reached
    if (campaign.EventCurrentAmount >= campaign.EventTargetAmount && oldAmount < campaign.EventTargetAmount) {
      setImmediate(async () => {
        try {
          // Send goal reached notification (would need organizer email)
          console.log(`Campaign "${campaign.title}" has reached its goal!`);
        } catch (error) {
          console.error('Error sending goal reached notification:', error);
        }
      });
    }

    res.status(200).json({
      success: true,
      message: "Donation successful",
      campaign,
      donation,
      donationAmount: amount
    });
  } catch (error) {
    console.error("Error processing donation:", error);
    res.status(500).json({
      success: false,
      message: "Error processing donation",
      error: error.message
    });
  }
});

export default router;
