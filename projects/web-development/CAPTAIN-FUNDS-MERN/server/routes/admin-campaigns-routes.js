import Campaign from "../models/campaignmodel.js";
import { Router } from "express";

const router = Router();

// Middleware to check if user is authenticated (you'll need to implement this)
const authMiddleware = (req, res, next) => {
  // For now, just pass through - implement proper auth later
  next();
};

// Middleware to check if user is admin (you'll need to implement this)
const adminMiddleware = (req, res, next) => {
  // For now, just pass through - implement proper admin check later
  next();
};

// GET /api/admin/campaigns - Get all campaigns for admin management
router.get("/", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const campaigns = await Campaign.find({ isDeleted: false })
      .sort({ createdAt: -1 });
    
    res.status(200).json({
      success: true,
      campaigns,
      count: campaigns.length
    });
  } catch (error) {
    console.error("Error fetching admin campaigns:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching campaigns",
      error: error.message
    });
  }
});

// POST /api/admin/campaigns - Create new campaign
router.post("/", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const {
      title,
      description,
      organizer,
      image,
      EventTargetAmount,
      EventCategory,
      location,
      endDate
    } = req.body;

    // Validation
    if (!title || !description || !organizer || !EventTargetAmount || !EventCategory || !location || !endDate) {
      return res.status(400).json({
        success: false,
        message: "All required fields must be provided"
      });
    }

    if (EventTargetAmount <= 0) {
      return res.status(400).json({
        success: false,
        message: "Target amount must be greater than 0"
      });
    }

    const campaign = new Campaign({
      title,
      description,
      organizer,
      image: image || "/api/placeholder/400/300",
      EventTargetAmount,
      EventCurrentAmount: 0,
      EventCategory,
      location,
      endDate: new Date(endDate),
      status: "active",
      isActive: true,
      isApproved: true // Auto-approve admin created campaigns
    });

    const savedCampaign = await campaign.save();

    res.status(201).json({
      success: true,
      message: "Campaign created successfully",
      campaign: savedCampaign
    });
  } catch (error) {
    console.error("Error creating campaign:", error);
    res.status(500).json({
      success: false,
      message: "Error creating campaign",
      error: error.message
    });
  }
});

// PUT /api/admin/campaigns/:id - Update campaign
router.put("/:id", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const campaign = await Campaign.findById(req.params.id);
    
    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    const updateData = { ...req.body };
    
    // Convert endDate to Date object if provided
    if (updateData.endDate) {
      updateData.endDate = new Date(updateData.endDate);
    }
    
    // Update updatedAt timestamp
    updateData.updatedAt = new Date();

    const updatedCampaign = await Campaign.findByIdAndUpdate(
      req.params.id,
      updateData,
      { new: true, runValidators: true }
    );

    res.status(200).json({
      success: true,
      message: "Campaign updated successfully",
      campaign: updatedCampaign
    });
  } catch (error) {
    console.error("Error updating campaign:", error);
    res.status(500).json({
      success: false,
      message: "Error updating campaign",
      error: error.message
    });
  }
});

// DELETE /api/admin/campaigns/:id - Soft delete campaign
router.delete("/:id", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const campaign = await Campaign.findById(req.params.id);
    
    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    // Soft delete
    campaign.isDeleted = true;
    campaign.isActive = false;
    campaign.updatedAt = new Date();
    await campaign.save();

    res.status(200).json({
      success: true,
      message: "Campaign deleted successfully"
    });
  } catch (error) {
    console.error("Error deleting campaign:", error);
    res.status(500).json({
      success: false,
      message: "Error deleting campaign",
      error: error.message
    });
  }
});

// PATCH /api/admin/campaigns/:id/approve - Approve campaign
router.patch("/:id/approve", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const campaign = await Campaign.findByIdAndUpdate(
      req.params.id,
      { 
        isApproved: true,
        isRejected: false,
        updatedAt: new Date()
      },
      { new: true }
    );

    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    res.status(200).json({
      success: true,
      message: "Campaign approved successfully",
      campaign
    });
  } catch (error) {
    console.error("Error approving campaign:", error);
    res.status(500).json({
      success: false,
      message: "Error approving campaign",
      error: error.message
    });
  }
});

// PATCH /api/admin/campaigns/:id/reject - Reject campaign
router.patch("/:id/reject", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const campaign = await Campaign.findByIdAndUpdate(
      req.params.id,
      { 
        isRejected: true,
        isApproved: false,
        isActive: false,
        updatedAt: new Date()
      },
      { new: true }
    );

    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    res.status(200).json({
      success: true,
      message: "Campaign rejected successfully",
      campaign
    });
  } catch (error) {
    console.error("Error rejecting campaign:", error);
    res.status(500).json({
      success: false,
      message: "Error rejecting campaign",
      error: error.message
    });
  }
});

// PATCH /api/admin/campaigns/:id/feature - Toggle featured status
router.patch("/:id/feature", authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const campaign = await Campaign.findById(req.params.id);
    
    if (!campaign) {
      return res.status(404).json({
        success: false,
        message: "Campaign not found"
      });
    }

    campaign.isFeatured = !campaign.isFeatured;
    campaign.updatedAt = new Date();
    await campaign.save();

    res.status(200).json({
      success: true,
      message: `Campaign ${campaign.isFeatured ? 'featured' : 'unfeatured'} successfully`,
      campaign
    });
  } catch (error) {
    console.error("Error toggling featured status:", error);
    res.status(500).json({
      success: false,
      message: "Error updating campaign",
      error: error.message
    });
  }
});

export default router;
