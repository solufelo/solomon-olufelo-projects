import mongoose from "mongoose";

const campaignSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  organizer: { type: String, required: true },
  image: { type: String, required: true },
  EventTargetAmount: { type: Number, required: true },
  EventCurrentAmount: { type: Number, required: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now },
  status: { type: String, required: true, default: "active" },
  EventCategory: { type: String, required: true },
  location: { type: String, required: true },
  endDate: { type: Date, required: true },
  isActive: { type: Boolean, default: true },
  isDeleted: { type: Boolean, default: false },
  isFeatured: { type: Boolean, default: false },
  isApproved: { type: Boolean, default: false },
  isRejected: { type: Boolean, default: false },
  isArchived: { type: Boolean, default: false },
});

const Campaign = mongoose.model("Campaign", campaignSchema);

export default Campaign;