import { Server } from 'socket.io';
import realtimeDataService from '../services/realtimeDataService.js';

let io;

export const initializeSocket = (server) => {
  io = new Server(server, {
    cors: {
      origin: "http://localhost:5173",
      methods: ["GET", "POST"],
      credentials: true
    }
  });

  io.on('connection', (socket) => {
    console.log(`User connected: ${socket.id}`);

    // Join user to their personal room for notifications
    socket.on('join-user-room', (userId) => {
      socket.join(`user-${userId}`);
      console.log(`User ${userId} joined their room`);
    });

    // Join campaign room for real-time updates
    socket.on('join-campaign', (campaignId) => {
      socket.join(`campaign-${campaignId}`);
      console.log(`User joined campaign room: ${campaignId}`);
    });

    // Leave campaign room
    socket.on('leave-campaign', (campaignId) => {
      socket.leave(`campaign-${campaignId}`);
      console.log(`User left campaign room: ${campaignId}`);
    });

    // Join admin room for admin notifications
    socket.on('join-admin-room', () => {
      socket.join('admin-room');
      console.log('Admin user joined admin room');
    });

    // Handle real-time donation updates
    socket.on('donation-made', (data) => {
      // Broadcast to campaign room
      socket.to(`campaign-${data.campaignId}`).emit('campaign-updated', {
        campaignId: data.campaignId,
        newAmount: data.newAmount,
        donation: data.donation
      });

      // Broadcast to admin room
      socket.to('admin-room').emit('new-donation', data);

      console.log(`Donation broadcast for campaign: ${data.campaignId}`);
    });

    // Handle campaign status updates
    socket.on('campaign-status-changed', (data) => {
      // Broadcast to all users
      io.emit('campaign-status-update', data);
      console.log(`Campaign status update broadcast: ${data.campaignId}`);
    });

    // Handle new campaign creation
    socket.on('campaign-created', (data) => {
      // Broadcast to all users
      io.emit('new-campaign', data);
      console.log(`New campaign broadcast: ${data.campaignId}`);
    });

    // Handle user status updates (admin only)
    socket.on('user-status-changed', (data) => {
      // Broadcast to admin room
      socket.to('admin-room').emit('user-status-update', data);
      
      // Notify the affected user
      socket.to(`user-${data.userId}`).emit('account-status-changed', {
        isActive: data.isActive,
        message: data.isActive ? 'Your account has been activated' : 'Your account has been deactivated'
      });
      
      console.log(`User status update broadcast: ${data.userId}`);
    });

    // Handle live statistics updates from MongoDB
    socket.on('request-live-stats', async () => {
      try {
        const liveStats = await realtimeDataService.getLiveStats();
        if (liveStats) {
          socket.emit('live-stats-update', liveStats);
        }
      } catch (error) {
        console.error('Error fetching live stats:', error);
        socket.emit('live-stats-error', { message: 'Failed to fetch live statistics' });
      }
    });

    // Handle simulation control (admin only)
    socket.on('start-simulation', () => {
      const result = realtimeDataService.startSimulation();
      socket.emit('simulation-status', {
        running: result,
        message: result ? 'Real-time simulation started' : 'Simulation already running'
      });
    });

    socket.on('stop-simulation', () => {
      const result = realtimeDataService.stopSimulation();
      socket.emit('simulation-status', {
        running: !result,
        message: result ? 'Real-time simulation stopped' : 'Simulation already stopped'
      });
    });

    socket.on('get-simulation-status', () => {
      const status = realtimeDataService.getStatus();
      socket.emit('simulation-status', status);
    });

    // Handle notification events
    socket.on('send-notification', (data) => {
      if (data.type === 'user') {
        socket.to(`user-${data.userId}`).emit('notification', {
          title: data.title,
          message: data.message,
          type: data.notificationType || 'info',
          timestamp: new Date().toISOString()
        });
      } else if (data.type === 'admin') {
        socket.to('admin-room').emit('notification', {
          title: data.title,
          message: data.message,
          type: data.notificationType || 'info',
          timestamp: new Date().toISOString()
        });
      } else if (data.type === 'broadcast') {
        io.emit('notification', {
          title: data.title,
          message: data.message,
          type: data.notificationType || 'info',
          timestamp: new Date().toISOString()
        });
      }
    });

    // Handle disconnection
    socket.on('disconnect', () => {
      console.log(`User disconnected: ${socket.id}`);
    });
  });

  return io;
};

// Helper functions to emit events from other parts of the application
export const emitToUser = (userId, event, data) => {
  if (io) {
    io.to(`user-${userId}`).emit(event, data);
  }
};

export const emitToCampaign = (campaignId, event, data) => {
  if (io) {
    io.to(`campaign-${campaignId}`).emit(event, data);
  }
};

export const emitToAdmins = (event, data) => {
  if (io) {
    io.to('admin-room').emit(event, data);
  }
};

export const broadcastToAll = (event, data) => {
  if (io) {
    io.emit(event, data);
  }
};

export const getIO = () => io;
