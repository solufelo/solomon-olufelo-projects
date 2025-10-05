import mongoose from "mongoose";
import dotenv from "dotenv";

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

dotenv.config();

const sampleCampaigns = [
  {
    title: "Help for Education",
    description:
      "Supporting underprivileged children with educational resources and school supplies for a better future.",
    organizer: "Education Foundation",
    image: "/api/placeholder/400/300",
    EventTargetAmount: 10000,
    EventCurrentAmount: 2500,
    status: "active",
    EventCategory: "Education",
    location: "New York, NY",
    endDate: new Date("2024-12-01"),
    isActive: true,
    isApproved: true,
    isFeatured: true,
  },
  {
    title: "Medical Emergency Fund",
    description:
      "Emergency medical assistance for community members in need of urgent care and treatment.",
    organizer: "Community Health Center",
    image: "/api/placeholder/400/300",
    EventTargetAmount: 5000,
    EventCurrentAmount: 1200,
    status: "active",
    EventCategory: "Healthcare",
    location: "Los Angeles, CA",
    endDate: new Date("2024-11-15"),
    isActive: true,
    isApproved: true,
  },
  {
    title: "Community Development",
    description:
      "Infrastructure development and improvement projects for our local community and neighborhoods.",
    organizer: "City Development Board",
    image: "/api/placeholder/400/300",
    EventTargetAmount: 15000,
    EventCurrentAmount: 8750,
    status: "active",
    EventCategory: "Community",
    location: "Chicago, IL",
    endDate: new Date("2024-10-30"),
    isActive: true,
    isApproved: true,
    isFeatured: true,
  },
  {
    title: "Environmental Conservation",
    description:
      "Protecting our local environment through tree planting, clean-up initiatives, and wildlife preservation.",
    organizer: "Green Earth Society",
    image: "/api/placeholder/400/300",
    EventTargetAmount: 8000,
    EventCurrentAmount: 3200,
    status: "active",
    EventCategory: "Environment",
    location: "Austin, TX",
    endDate: new Date("2024-11-30"),
    isActive: true,
    isApproved: true,
  },
  {
    title: "Animal Shelter Support",
    description:
      "Providing food, medical care, and shelter for abandoned and rescued animals in our community.",
    organizer: "Animal Welfare League",
    image: "/api/placeholder/400/300",
    EventTargetAmount: 6000,
    EventCurrentAmount: 4200,
    status: "active",
    EventCategory: "Animals",
    location: "Seattle, WA",
    endDate: new Date("2024-12-15"),
    isActive: true,
    isApproved: true,
    isFeatured: true,
  },
  {
    title: "Youth Sports Program",
    description:
      "Supporting youth sports teams with equipment, coaching, and facilities to promote healthy lifestyles.",
    organizer: "Youth Sports Foundation",
    image: "/api/placeholder/400/300",
    EventTargetAmount: 12000,
    EventCurrentAmount: 6800,
    status: "active",
    EventCategory: "Youth",
    location: "Miami, FL",
    endDate: new Date("2024-11-20"),
    isActive: true,
    isApproved: true,
  },
];

const seedDatabase = async () => {
  try {
    // Connect to MongoDB
    await mongoose.connect(process.env.MONGODB_URL || process.env.MONGODB_URI || process.env.DB_URI);
    console.log("Connected to MongoDB");

    // Clear existing campaigns
    await Campaign.deleteMany({});
    console.log("Cleared existing campaigns");

    // Insert sample campaigns
    const insertedCampaigns = await Campaign.insertMany(sampleCampaigns);
    console.log(`Successfully inserted ${insertedCampaigns.length} campaigns`);

    console.log("Database seeded successfully!");
  } catch (error) {
    console.error("Error seeding database:", error);
  } finally {
    await mongoose.connection.close();
    console.log("Database connection closed");
  }
};

// Run the seed function
seedDatabase();
