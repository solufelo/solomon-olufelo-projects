import express from "express";
import { createServer } from "http";
import dotenv from "dotenv";
import dbConfig from "./config/db-config.js";
import userRoutes from "./routes/user-routes.js";
import usersRoutes from "./routes/users-routes.js";
import campaignsRoutes from "./routes/campaigns-routes.js";
import donationsRoutes from "./routes/donations-routes.js";
import settingsRoutes from "./routes/settings-routes.js";
import adminCampaignsRoutes from "./routes/admin-campaigns-routes.js";
import uploadRoutes from "./routes/upload-routes.js";
import simulationRoutes from "./routes/simulation-routes.js";
import cookieParser from "cookie-parser";
import cors from "cors";
import { initializeSocket } from "./socket/socketHandler.js";
import emailService from "./services/emailService.js";
import realtimeDataService from "./services/realtimeDataService.js";

dotenv.config();

const app = express();
const server = createServer(app);
const port = process.env.PORT || 5000;

// Initialize database
dbConfig();

// Initialize Socket.IO
const io = initializeSocket(server);

// CORS configuration
app.use(cors({
  origin: "http://localhost:5173",
  credentials: true
}));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// Routes
app.use("/api/users", userRoutes); // Legacy auth routes
app.use("/api/users", usersRoutes); // Enhanced user management
app.use("/api/users/settings", settingsRoutes); // User settings routes
app.use("/api/campaigns", campaignsRoutes); // Public campaign routes
app.use("/api/donations", donationsRoutes); // Donation management routes
app.use("/api/admin/campaigns", adminCampaignsRoutes); // Admin campaign routes
app.use("/api/upload", uploadRoutes); // File upload routes
app.use("/api/simulation", simulationRoutes); // Simulation control routes

// Health check and API info
app.get("/", (req, res) => {
  res.json({
    message: "🚀 Captain Funds API Server",
    version: "2.0.0",
    status: "running",
    features: [
      "✅ MongoDB Integration",
      "✅ Real-time Socket.IO",
      "✅ File Upload System",
      "✅ Email Notifications",
      "✅ Admin Management",
      "✅ Campaign System",
      "✅ User Authentication"
    ],
    endpoints: {
      users: "/api/users",
      campaigns: "/api/campaigns",
      admin: "/api/admin/campaigns",
      upload: "/api/upload",
      simulation: "/api/simulation"
    },
    realtime: "Socket.IO enabled",
    timestamp: new Date().toISOString()
  });
});

// API Health Check
app.get("/api/health", async (req, res) => {
  try {
    // Test email service
    const emailTest = await emailService.testEmailConfig();
    
    res.json({
      status: "healthy",
      services: {
        database: "connected",
        socketio: "active",
        email: emailTest.success ? "connected" : "warning",
        upload: "ready",
        simulation: "running"
      },
      uptime: process.uptime(),
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    res.status(500).json({
      status: "unhealthy",
      error: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

// Start real-time data simulation
realtimeDataService.startSimulation();

// Start server with Socket.IO support
server.listen(port, () => {
  console.log(`
🚀 Captain Funds Server Started!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📡 Server: http://localhost:${port}
🔥 Socket.IO: Real-time features enabled
📧 Email: ${process.env.NODE_ENV === 'production' ? 'Production ready' : 'Development mode'}
☁️  Upload: Cloudinary integration
🗄️  Database: MongoDB connected
🎭 Real-time Simulation: Running (MongoDB-based)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Features Active:
   • Real-time campaign updates & donations
   • File upload system with Cloudinary
   • Email notifications system
   • Admin user management (CRUD)
   • Complete MongoDB integration
   • Live activity simulation

🎯 Simulation Features:
   • Realistic donation generation (10-30s intervals)
   • Campaign progress updates (5-15s intervals)
   • New campaign creation (2-5 minute intervals)
   • Goal achievement notifications
   • Live statistics from MongoDB

🎯 Ready for full-scale fundraising platform!
  `);
}); 