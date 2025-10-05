import { Router } from "express";
import { authenticateToken } from "../middleware/auth.js";
import UserModel from "../models/user-model.js";
import bcrypt from "bcryptjs";

const router = Router();

// All settings routes require authentication
router.use(authenticateToken);

// GET /api/users/settings - Get user settings
router.get("/", async (req, res) => {
  try {
    const user = await UserModel.findById(req.user._id).select(
      "notificationSettings privacySettings securitySettings"
    );

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    res.status(200).json({
      success: true,
      settings: {
        notifications: user.notificationSettings || {},
        privacy: user.privacySettings || {},
        security: user.securitySettings || {}
      }
    });
  } catch (error) {
    console.error("Error fetching settings:", error);
    res.status(500).json({
      success: false,
      message: "Error fetching settings",
      error: error.message
    });
  }
});

// PUT /api/users/settings/notifications - Update notification settings
router.put("/notifications", async (req, res) => {
  try {
    const { emailNotifications, campaignUpdates, donationAlerts, marketingEmails, weeklyReports, mobilePushNotifications } = req.body;

    const user = await UserModel.findByIdAndUpdate(
      req.user._id,
      {
        $set: {
          "notificationSettings.emailNotifications": emailNotifications,
          "notificationSettings.campaignUpdates": campaignUpdates,
          "notificationSettings.donationAlerts": donationAlerts,
          "notificationSettings.marketingEmails": marketingEmails,
          "notificationSettings.weeklyReports": weeklyReports,
          "notificationSettings.mobilePushNotifications": mobilePushNotifications,
          "notificationSettings.updatedAt": new Date()
        }
      },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    res.status(200).json({
      success: true,
      message: "Notification settings updated successfully",
      settings: user.notificationSettings
    });
  } catch (error) {
    console.error("Error updating notification settings:", error);
    res.status(500).json({
      success: false,
      message: "Error updating notification settings",
      error: error.message
    });
  }
});

// PUT /api/users/settings/privacy - Update privacy settings
router.put("/privacy", async (req, res) => {
  try {
    const { profileVisibility, showDonationHistory, showCampaignActivity, allowContactFromOrganizers } = req.body;

    const user = await UserModel.findByIdAndUpdate(
      req.user._id,
      {
        $set: {
          "privacySettings.profileVisibility": profileVisibility,
          "privacySettings.showDonationHistory": showDonationHistory,
          "privacySettings.showCampaignActivity": showCampaignActivity,
          "privacySettings.allowContactFromOrganizers": allowContactFromOrganizers,
          "privacySettings.updatedAt": new Date()
        }
      },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    res.status(200).json({
      success: true,
      message: "Privacy settings updated successfully",
      settings: user.privacySettings
    });
  } catch (error) {
    console.error("Error updating privacy settings:", error);
    res.status(500).json({
      success: false,
      message: "Error updating privacy settings",
      error: error.message
    });
  }
});

// PUT /api/users/settings/security - Update security settings
router.put("/security", async (req, res) => {
  try {
    const { twoFactorEnabled, sessionTimeout, loginAlerts } = req.body;

    const user = await UserModel.findByIdAndUpdate(
      req.user._id,
      {
        $set: {
          "securitySettings.twoFactorEnabled": twoFactorEnabled,
          "securitySettings.sessionTimeout": sessionTimeout,
          "securitySettings.loginAlerts": loginAlerts,
          "securitySettings.updatedAt": new Date()
        }
      },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    res.status(200).json({
      success: true,
      message: "Security settings updated successfully",
      settings: user.securitySettings
    });
  } catch (error) {
    console.error("Error updating security settings:", error);
    res.status(500).json({
      success: false,
      message: "Error updating security settings",
      error: error.message
    });
  }
});

// PUT /api/users/change-password - Change password
router.put("/change-password", async (req, res) => {
  try {
    const { currentPassword, newPassword } = req.body;

    if (!currentPassword || !newPassword) {
      return res.status(400).json({
        success: false,
        message: "Current password and new password are required"
      });
    }

    if (newPassword.length < 8) {
      return res.status(400).json({
        success: false,
        message: "New password must be at least 8 characters long"
      });
    }

    // Get user with password
    const user = await UserModel.findById(req.user._id).select("+password");

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    // Verify current password
    const isValidPassword = await bcrypt.compare(currentPassword, user.password);
    if (!isValidPassword) {
      return res.status(400).json({
        success: false,
        message: "Current password is incorrect"
      });
    }

    // Hash new password
    const hashedPassword = await bcrypt.hash(newPassword, 10);

    // Update password
    await UserModel.findByIdAndUpdate(req.user._id, {
      password: hashedPassword,
      passwordChangedAt: new Date()
    });

    res.status(200).json({
      success: true,
      message: "Password changed successfully"
    });
  } catch (error) {
    console.error("Error changing password:", error);
    res.status(500).json({
      success: false,
      message: "Error changing password",
      error: error.message
    });
  }
});

// GET /api/users/export-data - Export user data
router.get("/export-data", async (req, res) => {
  try {
    const user = await UserModel.findById(req.user._id).select("-password");

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    // In a real app, you would also fetch donations, campaigns, etc.
    const exportData = {
      user: {
        id: user._id,
        name: user.name,
        email: user.email,
        isAdmin: user.isAdmin,
        isActive: user.isActive,
        createdAt: user.createdAt,
        profileImage: user.profileImage,
        bio: user.bio,
        website: user.website,
        location: user.location
      },
      settings: {
        notifications: user.notificationSettings,
        privacy: user.privacySettings,
        security: user.securitySettings
      },
      exportDate: new Date(),
      note: "This export contains your personal data from Captain Funds"
    };

    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Content-Disposition', `attachment; filename=${user.name}-data-export.json`);
    res.status(200).json(exportData);
  } catch (error) {
    console.error("Error exporting data:", error);
    res.status(500).json({
      success: false,
      message: "Error exporting data",
      error: error.message
    });
  }
});

// DELETE /api/users/account - Delete user account
router.delete("/account", async (req, res) => {
  try {
    // In a production app, you would also:
    // 1. Delete all donations made by this user
    // 2. Handle any campaigns created by this user
    // 3. Send confirmation email
    // 4. Add account deletion to audit log

    const user = await UserModel.findByIdAndDelete(req.user._id);

    if (!user) {
      return res.status(404).json({
        success: false,
        message: "User not found"
      });
    }

    res.status(200).json({
      success: true,
      message: "Account deleted successfully"
    });
  } catch (error) {
    console.error("Error deleting account:", error);
    res.status(500).json({
      success: false,
      message: "Error deleting account",
      error: error.message
    });
  }
});

export default router;
