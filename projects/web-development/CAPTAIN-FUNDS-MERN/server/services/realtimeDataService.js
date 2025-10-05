import Campaign from '../models/campaignmodel.js';
import { emitToAdmins, emitToCampaign, broadcastToAll } from '../socket/socketHandler.js';

// Real-time data simulation service
class RealtimeDataService {
  constructor() {
    this.isRunning = false;
    this.simulationInterval = null;
    this.activeSimulations = new Map();

    // Mock data pools for realistic simulation
    this.donorNames = [
      'Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Ross', 'Edward Norton',
      'Fiona Green', 'George Lucas', 'Helen Troy', 'Ian Fleming', 'Julia Roberts',
      'Kevin Spacey', 'Linda Carter', 'Michael Jordan', 'Nancy Drew', 'Oliver Twist'
    ];

    this.donationMessages = [
      'Keep up the great work!', 'Making a difference!', 'Hope this helps',
      'For a better future', 'Support local initiatives', 'Amazing cause!',
      'Every bit counts', 'Changing lives', 'Proud to contribute',
      'Together we can', 'Impact matters', 'Building community'
    ];
  }

  // Start real-time simulation
  startSimulation() {
    if (this.isRunning) return;

    console.log('🚀 Starting MongoDB-based real-time simulation...');
    this.isRunning = true;

    // Generate real-time activity every 10-30 seconds
    this.simulationInterval = setInterval(() => {
      this.generateRealtimeActivity();
    }, Math.random() * 20000 + 10000); // 10-30 seconds

    // Generate campaign progress updates every 5-15 seconds
    setInterval(() => {
      this.updateCampaignProgress();
    }, Math.random() * 10000 + 5000);

    // Simulate new campaigns every 2-5 minutes
    setInterval(() => {
      this.simulateNewCampaign();
    }, Math.random() * 180000 + 120000);

    return true;
  }

  // Stop real-time simulation
  stopSimulation() {
    if (!this.isRunning) return;

    console.log('🛑 Stopping real-time simulation...');
    this.isRunning = false;

    if (this.simulationInterval) {
      clearInterval(this.simulationInterval);
      this.simulationInterval = null;
    }

    // Clear all active simulations
    this.activeSimulations.clear();

    return true;
  }

  // Generate realistic real-time donation activity
  async generateRealtimeActivity() {
    try {
      // Get active campaigns from MongoDB
      const activeCampaigns = await Campaign.find({
        isActive: true,
        isApproved: true,
        isDeleted: false,
        EventCurrentAmount: { $lt: '$EventTargetAmount' }
      }).limit(5);

      if (activeCampaigns.length === 0) return;

      // Select random campaign
      const campaign = activeCampaigns[Math.floor(Math.random() * activeCampaigns.length)];

      // Generate realistic donation amount ($5-$500)
      const donationAmount = Math.floor(Math.random() * 495) + 5;

      // Don't exceed target amount
      if (campaign.EventCurrentAmount + donationAmount > campaign.EventTargetAmount) {
        return;
      }

      // Generate donor info
      const donorName = this.donorNames[Math.floor(Math.random() * this.donorNames.length)];
      const message = Math.random() > 0.5 ?
        this.donationMessages[Math.floor(Math.random() * this.donationMessages.length)] : null;

      // Update campaign in MongoDB
      const updatedCampaign = await Campaign.findByIdAndUpdate(
        campaign._id,
        { $inc: { EventCurrentAmount: donationAmount } },
        { new: true }
      );

      if (!updatedCampaign) return;

      // Prepare donation data
      const donationData = {
        campaignId: campaign._id,
        campaignTitle: campaign.title,
        campaignOrganizer: campaign.organizer,
        donorName,
        donorEmail: `${donorName.toLowerCase().replace(' ', '.')}@example.com`,
        amount: donationAmount,
        message,
        isAnonymous: Math.random() > 0.8,
        paymentMethod: ['credit_card', 'paypal', 'bank_transfer'][Math.floor(Math.random() * 3)],
        paymentStatus: 'completed',
        transactionId: `TXN_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
        createdAt: new Date(),
        donationType: 'simulated'
      };

      // Emit real-time updates via Socket.IO
      emitToCampaign(campaign._id, 'campaign-updated', {
        campaignId: campaign._id,
        newAmount: updatedCampaign.EventCurrentAmount,
        donation: donationData,
        isSimulation: true
      });

      emitToAdmins('new-donation', donationData);
      broadcastToAll('live-activity', {
        type: 'donation',
        data: donationData,
        timestamp: new Date().toISOString()
      });

      // Check if campaign reached its goal
      if (updatedCampaign.EventCurrentAmount >= updatedCampaign.EventTargetAmount) {
        await this.handleGoalReached(updatedCampaign);
      }

      console.log(`💝 Simulated donation: $${donationAmount} to "${campaign.title}" by ${donorName}`);

    } catch (error) {
      console.error('Error generating realtime activity:', error);
    }
  }

  // Update campaign progress with realistic data
  async updateCampaignProgress() {
    try {
      const campaigns = await Campaign.find({
        isActive: true,
        isApproved: true,
        isDeleted: false
      }).limit(3);

      if (campaigns.length === 0) return;

      const campaign = campaigns[Math.floor(Math.random() * campaigns.length)];

      // Send progress update
      broadcastToAll('campaign-progress', {
        campaignId: campaign._id,
        title: campaign.title,
        currentAmount: campaign.EventCurrentAmount,
        targetAmount: campaign.EventTargetAmount,
        progress: Math.round((campaign.EventCurrentAmount / campaign.EventTargetAmount) * 100),
        lastUpdate: new Date().toISOString(),
        isSimulation: true
      });

    } catch (error) {
      console.error('Error updating campaign progress:', error);
    }
  }

  // Simulate new campaign creation
  async simulateNewCampaign() {
    try {
      const campaignTitles = [
        'Support Local Education Initiative',
        'Medical Equipment for Community Hospital',
        'Environmental Cleanup Project',
        'Youth Sports Program Development',
        'Senior Citizen Support Center',
        'Animal Shelter Expansion',
        'Local Food Bank Support',
        'Community Garden Project',
        'Technology Access Program',
        'Arts and Culture Festival'
      ];

      const organizers = [
        'Community Foundation', 'Local Hospital', 'Green Initiative',
        'Youth Sports League', 'Senior Services', 'Animal Rescue',
        'Food Bank Network', 'Garden Society', 'Tech Access', 'Arts Council'
      ];

      const categories = [
        'Education', 'Healthcare', 'Environment', 'Community',
        'Animals', 'Humanitarian', 'Arts', 'Technology'
      ];

      const locations = [
        'New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX',
        'Phoenix, AZ', 'Philadelphia, PA', 'San Antonio, TX', 'San Diego, CA'
      ];

      // Create new campaign
      const newCampaign = new Campaign({
        title: campaignTitles[Math.floor(Math.random() * campaignTitles.length)],
        description: 'This is an important community project that needs your support to make a real difference in our community.',
        organizer: organizers[Math.floor(Math.random() * organizers.length)],
        image: `/api/placeholder/400/300?text=${Date.now()}`,
        EventTargetAmount: Math.floor(Math.random() * 50000) + 10000,
        EventCurrentAmount: 0,
        status: 'active',
        EventCategory: categories[Math.floor(Math.random() * categories.length)],
        location: locations[Math.floor(Math.random() * locations.length)],
        endDate: new Date(Date.now() + (Math.random() * 30 + 15) * 24 * 60 * 60 * 1000), // 15-45 days
        isActive: true,
        isApproved: true,
        isFeatured: Math.random() > 0.7,
        isDeleted: false
      });

      const savedCampaign = await newCampaign.save();

      // Emit new campaign event
      broadcastToAll('new-campaign', {
        campaign: savedCampaign,
        isSimulation: true
      });

      console.log(`🆕 New simulated campaign created: "${savedCampaign.title}"`);

    } catch (error) {
      console.error('Error simulating new campaign:', error);
    }
  }

  // Handle when campaign reaches its goal
  async handleGoalReached(campaign) {
    try {
      // Update campaign status
      await Campaign.findByIdAndUpdate(campaign._id, {
        isActive: false,
        status: 'completed'
      });

      // Emit goal reached event
      broadcastToAll('goal-reached', {
        campaignId: campaign._id,
        title: campaign.title,
        organizer: campaign.organizer,
        finalAmount: campaign.EventCurrentAmount,
        targetAmount: campaign.EventTargetAmount,
        isSimulation: true
      });

      console.log(`🎯 Campaign goal reached: "${campaign.title}"`);

    } catch (error) {
      console.error('Error handling goal reached:', error);
    }
  }

  // Get current simulation status
  getStatus() {
    return {
      isRunning: this.isRunning,
      activeSimulations: this.activeSimulations.size,
      lastActivity: new Date().toISOString()
    };
  }

  // Get live statistics from MongoDB
  async getLiveStats() {
    try {
      const [
        totalCampaigns,
        activeCampaigns,
        totalRaised,
        recentDonations
      ] = await Promise.all([
        Campaign.countDocuments(),
        Campaign.countDocuments({ isActive: true, isApproved: true, isDeleted: false }),
        Campaign.aggregate([{ $group: { _id: null, total: { $sum: '$EventCurrentAmount' } } }]),
        Campaign.find({ isActive: true, isApproved: true, isDeleted: false })
          .sort({ updatedAt: -1 })
          .limit(5)
      ]);

      return {
        totalCampaigns,
        activeCampaigns,
        totalRaised: totalRaised[0]?.total || 0,
        averageDonation: totalRaised[0]?.total ? totalRaised[0].total / (recentDonations.length * 10) : 0,
        recentCampaigns: recentDonations.map(c => ({
          id: c._id,
          title: c.title,
          progress: Math.round((c.EventCurrentAmount / c.EventTargetAmount) * 100),
          raised: c.EventCurrentAmount
        }))
      };
    } catch (error) {
      console.error('Error getting live stats:', error);
      return null;
    }
  }
}

// Export singleton instance
const realtimeDataService = new RealtimeDataService();
export default realtimeDataService;
