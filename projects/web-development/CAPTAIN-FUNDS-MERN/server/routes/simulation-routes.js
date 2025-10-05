import express from 'express';
import Campaign from '../models/campaignmodel.js';
import realtimeDataService from '../services/realtimeDataService.js';

const router = express.Router();

// Middleware to check if user is authenticated
const authMiddleware = (req, res, next) => {
  try {
    const token = req.header('Authorization')?.replace('Bearer ', '');
    if (!token) {
      return res.status(401).json({ message: 'Access denied. No token provided.' });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET || 'fallback-secret');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ message: 'Invalid token.' });
  }
};

// Middleware to check if user is admin
const adminMiddleware = (req, res, next) => {
  if (!req.user.isAdmin) {
    return res.status(403).json({ message: 'Access denied. Admin privileges required.' });
  }
  next();
};

// Get simulation status
router.get('/status', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const status = realtimeDataService.getStatus();
    res.json({
      success: true,
      status
    });
  } catch (error) {
    console.error('Error getting simulation status:', error);
    res.status(500).json({
      success: false,
      message: 'Error getting simulation status'
    });
  }
});

// Start simulation
router.post('/start', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const result = realtimeDataService.startSimulation();
    res.json({
      success: true,
      message: result ? 'Simulation started' : 'Simulation already running',
      running: result
    });
  } catch (error) {
    console.error('Error starting simulation:', error);
    res.status(500).json({
      success: false,
      message: 'Error starting simulation'
    });
  }
});

// Stop simulation
router.post('/stop', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const result = realtimeDataService.stopSimulation();
    res.json({
      success: true,
      message: result ? 'Simulation stopped' : 'Simulation already stopped',
      running: !result
    });
  } catch (error) {
    console.error('Error stopping simulation:', error);
    res.status(500).json({
      success: false,
      message: 'Error stopping simulation'
    });
  }
});

// Seed database with sample campaigns
router.post('/seed', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    // Check if campaigns already exist
    const existingCount = await Campaign.countDocuments();
    if (existingCount > 0) {
      return res.json({
        success: true,
        message: 'Database already has campaigns. Skipping seed.',
        existingCount
      });
    }

    const sampleCampaigns = [
      {
        title: 'Support Local Education Initiative',
        description: 'Help provide educational resources and technology to underprivileged students in our community. Your donation will directly impact learning opportunities for children who need it most.',
        organizer: 'Community Education Foundation',
        image: `/api/placeholder/400/300?text=Education`,
        EventTargetAmount: 25000,
        EventCurrentAmount: 8750,
        status: 'active',
        EventCategory: 'Education',
        location: 'Springfield, IL',
        endDate: new Date(Date.now() + 45 * 24 * 60 * 60 * 1000), // 45 days from now
        isActive: true,
        isApproved: true,
        isFeatured: true,
        isDeleted: false
      },
      {
        title: 'Medical Equipment for Community Hospital',
        description: 'Critical medical equipment needed for emergency care and patient treatment. Help save lives by supporting our local healthcare facility.',
        organizer: 'Healthcare Alliance',
        image: `/api/placeholder/400/300?text=Medical`,
        EventTargetAmount: 50000,
        EventCurrentAmount: 32500,
        status: 'active',
        EventCategory: 'Healthcare',
        location: 'Riverside, CA',
        endDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000), // 30 days from now
        isActive: true,
        isApproved: true,
        isFeatured: true,
        isDeleted: false
      },
      {
        title: 'Environmental Cleanup Project',
        description: 'Join us in cleaning up our local parks and waterways. Help preserve our environment for future generations through community action.',
        organizer: 'Green Initiative',
        image: `/api/placeholder/400/300?text=Environment`,
        EventTargetAmount: 15000,
        EventCurrentAmount: 6200,
        status: 'active',
        EventCategory: 'Environment',
        location: 'Portland, OR',
        endDate: new Date(Date.now() + 60 * 24 * 60 * 60 * 1000), // 60 days from now
        isActive: true,
        isApproved: true,
        isFeatured: false,
        isDeleted: false
      },
      {
        title: 'Youth Sports Program',
        description: 'Support our youth sports program that provides free coaching, equipment, and facilities for underprivileged children to develop physically and mentally.',
        organizer: 'Youth Sports League',
        image: `/api/placeholder/400/300?text=Sports`,
        EventTargetAmount: 30000,
        EventCurrentAmount: 15800,
        status: 'active',
        EventCategory: 'Community',
        location: 'Austin, TX',
        endDate: new Date(Date.now() + 25 * 24 * 60 * 60 * 1000), // 25 days from now
        isActive: true,
        isApproved: true,
        isFeatured: true,
        isDeleted: false
      },
      {
        title: 'Animal Shelter Expansion',
        description: 'Help us expand our animal shelter to accommodate more rescued pets and provide better care facilities for animals in need.',
        organizer: 'Animal Rescue Network',
        image: `/api/placeholder/400/300?text=Animals`,
        EventTargetAmount: 75000,
        EventCurrentAmount: 42000,
        status: 'active',
        EventCategory: 'Animals',
        location: 'Denver, CO',
        endDate: new Date(Date.now() + 90 * 24 * 60 * 60 * 1000), // 90 days from now
        isActive: true,
        isApproved: true,
        isFeatured: false,
        isDeleted: false
      },
      {
        title: 'Senior Citizen Support Center',
        description: 'Build a community center for seniors providing meals, healthcare support, and social activities to improve quality of life.',
        organizer: 'Senior Services Alliance',
        image: `/api/placeholder/400/300?text=Seniors`,
        EventTargetAmount: 40000,
        EventCurrentAmount: 18500,
        status: 'active',
        EventCategory: 'Humanitarian',
        location: 'Seattle, WA',
        endDate: new Date(Date.now() + 40 * 24 * 60 * 60 * 1000), // 40 days from now
        isActive: true,
        isApproved: true,
        isFeatured: false,
        isDeleted: false
      }
    ];

    const createdCampaigns = await Campaign.insertMany(sampleCampaigns);

    res.json({
      success: true,
      message: `Successfully seeded database with ${createdCampaigns.length} campaigns`,
      campaigns: createdCampaigns.map(c => ({
        id: c._id,
        title: c.title,
        target: c.EventTargetAmount,
        category: c.EventCategory
      }))
    });

  } catch (error) {
    console.error('Error seeding database:', error);
    res.status(500).json({
      success: false,
      message: 'Error seeding database',
      error: error.message
    });
  }
});

// Clear all campaigns (for testing)
router.delete('/clear', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const result = await Campaign.deleteMany({});

    res.json({
      success: true,
      message: `Cleared ${result.deletedCount} campaigns from database`
    });
  } catch (error) {
    console.error('Error clearing campaigns:', error);
    res.status(500).json({
      success: false,
      message: 'Error clearing campaigns'
    });
  }
});

// Get simulation analytics
router.get('/analytics', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const [
      totalCampaigns,
      activeCampaigns,
      totalRaised,
      avgProgress,
      campaignsByCategory
    ] = await Promise.all([
      Campaign.countDocuments(),
      Campaign.countDocuments({ isActive: true, isApproved: true }),
      Campaign.aggregate([{ $group: { _id: null, total: { $sum: '$EventCurrentAmount' } } }]),
      Campaign.aggregate([
        {
          $match: { isActive: true, isApproved: true }
        },
        {
          $group: {
            _id: null,
            avgProgress: {
              $avg: { $multiply: [{ $divide: ['$EventCurrentAmount', '$EventTargetAmount'] }, 100] }
            }
          }
        }
      ]),
      Campaign.aggregate([
        {
          $match: { isActive: true, isApproved: true }
        },
        {
          $group: {
            _id: '$EventCategory',
            count: { $sum: 1 },
            totalRaised: { $sum: '$EventCurrentAmount' }
          }
        }
      ])
    ]);

    res.json({
      success: true,
      analytics: {
        totalCampaigns,
        activeCampaigns,
        totalRaised: totalRaised[0]?.total || 0,
        avgProgress: avgProgress[0]?.avgProgress || 0,
        campaignsByCategory: campaignsByCategory.map(cat => ({
          category: cat._id,
          count: cat.count,
          totalRaised: cat.totalRaised
        }))
      }
    });
  } catch (error) {
    console.error('Error getting analytics:', error);
    res.status(500).json({
      success: false,
      message: 'Error getting analytics'
    });
  }
});

export default router;
