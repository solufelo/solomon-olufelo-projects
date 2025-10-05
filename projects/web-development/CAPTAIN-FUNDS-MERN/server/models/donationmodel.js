import mongoose from "mongoose";

const donationSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
    required: true
  },
  campaignId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Campaign",
    required: true
  },
  amount: {
    type: Number,
    required: true,
    min: [1, "Donation amount must be at least $1"]
  },
  message: {
    type: String,
    maxlength: [500, "Message cannot exceed 500 characters"],
    default: ""
  },
  isAnonymous: {
    type: Boolean,
    default: false
  },
  paymentMethod: {
    type: String,
    enum: ["credit_card", "paypal", "bank_transfer", "crypto", "other"],
    default: "credit_card"
  },
  paymentStatus: {
    type: String,
    enum: ["pending", "completed", "failed", "refunded"],
    default: "completed" // For now, assume all donations are completed
  },
  transactionId: {
    type: String,
    default: null
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Index for better query performance
donationSchema.index({ userId: 1, createdAt: -1 });
donationSchema.index({ campaignId: 1, createdAt: -1 });

// Update the updatedAt field on save
donationSchema.pre("save", function(next) {
  this.updatedAt = new Date();
  next();
});

const Donation = mongoose.model("Donation", donationSchema);

export default Donation;
