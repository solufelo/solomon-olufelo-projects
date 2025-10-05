import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  isAdmin: { type: Boolean, default: false },
  isActive: { type: Boolean, default: true },
  phone: { type: String, default: "" },
  bio: { type: String, default: "" },
  website: { type: String, default: "" },
  location: { type: String, default: "" },
  profileImage: { type: String, default: "" },
  passwordChangedAt: { type: Date },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now },

  // Notification Settings
  notificationSettings: {
    emailNotifications: { type: Boolean, default: true },
    campaignUpdates: { type: Boolean, default: true },
    donationAlerts: { type: Boolean, default: true },
    marketingEmails: { type: Boolean, default: false },
    weeklyReports: { type: Boolean, default: true },
    mobilePushNotifications: { type: Boolean, default: true },
    updatedAt: { type: Date, default: Date.now }
  },

  // Privacy Settings
  privacySettings: {
    profileVisibility: { type: String, enum: ["public", "private", "donors-only"], default: "public" },
    showDonationHistory: { type: Boolean, default: false },
    showCampaignActivity: { type: Boolean, default: true },
    allowContactFromOrganizers: { type: Boolean, default: true },
    updatedAt: { type: Date, default: Date.now }
  },

  // Security Settings
  securitySettings: {
    twoFactorEnabled: { type: Boolean, default: false },
    sessionTimeout: { type: Number, default: 30 },
    loginAlerts: { type: Boolean, default: true },
    updatedAt: { type: Date, default: Date.now }
  }
});

const UserModel = mongoose.model("User", userSchema);

export default UserModel;