import Donation from "../models/donationmodel.js";
import Campaign from "../models/campaignmodel.js";
import { Router } from "express";
import { authenticateToken } from "../middleware/auth.js";

const router = Router();

// GET /api/donations - Get user's donation history
router.get("/", authenticateToken, async (req, res) => {
  try {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const skip = (page - 1) * limit;

    const donations = await Donation.find({ userId: req.user._id })
      .populate("campaignId", "title organizer image")
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit);

    const total = await Donation.countDocuments({ userId: req.user._id });

    res.status(200).json({
      success: true,
      donations,
      pagination: {
        page,
        limit,
        total,
        pages: Math.ceil(total / limit)
      }
    });
  } catch (error) {
    console.error("Error fetching donations:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching donations",
      error: error.message
    });
  }
});

// GET /api/donations/:id - Get single donation by ID
router.get("/:id", authenticateToken, async (req, res) => {
  try {
    const donation = await Donation.findOne({
      _id: req.params.id,
      userId: req.user._id
    }).populate("campaignId", "title organizer image");

    if (!donation) {
      return res.status(404).json({
        success: false,
        message: "Donation not found"
      });
    }

    res.status(200).json({
      success: true,
      donation
    });
  } catch (error) {
    console.error("Error fetching donation:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching donation",
      error: error.message
    });
  }
});

// POST /api/donations - Create a new donation (alternative to campaign/:id/donate)
router.post("/", authenticateToken, async (req, res) => {
  try {
    const { campaignId, amount, message, isAnonymous, paymentMethod } = req.body;

    if (!campaignId || !amount || amount <= 0) {
      return res.status(400).json({
        success: false,
        message: "Campaign ID and valid donation amount are required"
      });
    }

    // Verify campaign exists and is available for donations
    const campaign = await Campaign.findById(campaignId);
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
      campaignId,
      amount,
      message: message || "",
      isAnonymous: isAnonymous || false,
      paymentMethod: paymentMethod || "credit_card",
      paymentStatus: "completed"
    });

    // Update campaign's current amount
    campaign.EventCurrentAmount += amount;
    await campaign.save();

    // Populate campaign data for response
    await donation.populate("campaignId", "title organizer image");

    res.status(201).json({
      success: true,
      message: "Donation successful",
      donation,
      campaign: {
        title: campaign.title,
        newCurrentAmount: campaign.EventCurrentAmount,
        targetAmount: campaign.EventTargetAmount
      }
    });
  } catch (error) {
    console.error("Error creating donation:", error);
    res.status(500).json({
      success: false,
      message: "Error processing donation",
      error: error.message
    });
  }
});

// GET /api/donations/campaign/:campaignId - Get donations for a specific campaign (public)
router.get("/campaign/:campaignId", async (req, res) => {
  try {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 20;
    const skip = (page - 1) * limit;

    const donations = await Donation.find({
      campaignId: req.params.campaignId,
      isAnonymous: false,
      paymentStatus: "completed"
    })
      .populate("userId", "name")
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit);

    const total = await Donation.countDocuments({
      campaignId: req.params.campaignId,
      isAnonymous: false,
      paymentStatus: "completed"
    });

    res.status(200).json({
      success: true,
      donations,
      pagination: {
        page,
        limit,
        total,
        pages: Math.ceil(total / limit)
      }
    });
  } catch (error) {
    console.error("Error fetching campaign donations:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching donations",
      error: error.message
    });
  }
});

// GET /api/donations/stats/user - Get user's donation statistics
router.get("/stats/user", authenticateToken, async (req, res) => {
  try {
    const userId = req.user._id;

    const stats = await Donation.aggregate([
      { $match: { userId, paymentStatus: "completed" } },
      {
        $group: {
          _id: null,
          totalDonations: { $sum: 1 },
          totalAmount: { $sum: "$amount" },
          averageDonation: { $avg: "$amount" },
          largestDonation: { $max: "$amount" }
        }
      }
    ]);

    const userStats = stats.length > 0 ? stats[0] : {
      totalDonations: 0,
      totalAmount: 0,
      averageDonation: 0,
      largestDonation: 0
    };

    res.status(200).json({
      success: true,
      stats: userStats
    });
  } catch (error) {
    console.error("Error fetching donation stats:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching donation statistics",
      error: error.message
    });
  }
});

export default router;
