import { useEffect, useRef, useState } from 'react';
import { io } from 'socket.io-client';
import userStore from '../store/users-store';

const useSocket = () => {
  const socketRef = useRef(null);
  const [isConnected, setIsConnected] = useState(false);
  const [connectionError, setConnectionError] = useState(null);
  const { currentUser } = userStore();

  useEffect(() => {
    // Initialize socket connection
    const socket = io(import.meta.env.VITE_SOCKET_URL || 'http://localhost:5000', {
      transports: ['websocket', 'polling'],
      upgrade: true,
    });

    socketRef.current = socket;

    // Connection events
    socket.on('connect', () => {
      console.log('Connected to server');
      setIsConnected(true);
      setConnectionError(null);

      // Join user-specific room if user is logged in
      if (currentUser?._id) {
        socket.emit('join-user-room', currentUser._id);

        // Join admin room if user is admin
        if (currentUser.isAdmin) {
          socket.emit('join-admin-room');
        }
      }
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from server');
      setIsConnected(false);
    });

    socket.on('connect_error', (error) => {
      console.error('Connection error:', error);
      setConnectionError(error.message);
      setIsConnected(false);
    });

    // Campaign events
    socket.on('campaign-updated', (data) => {
      console.log('Campaign updated:', data);
      // Emit custom event for components to listen to
      window.dispatchEvent(new CustomEvent('campaign-updated', { detail: data }));
    });

    socket.on('new-campaign', (data) => {
      console.log('New campaign created:', data);
      window.dispatchEvent(new CustomEvent('new-campaign', { detail: data }));
    });

    socket.on('campaign-progress', (data) => {
      console.log('Campaign progress update:', data);
      window.dispatchEvent(new CustomEvent('campaign-progress', { detail: data }));
    });

    socket.on('goal-reached', (data) => {
      console.log('Campaign goal reached:', data);
      window.dispatchEvent(new CustomEvent('goal-reached', { detail: data }));
    });

    // Donation events
    socket.on('new-donation', (data) => {
      console.log('New donation:', data);
      window.dispatchEvent(new CustomEvent('new-donation', { detail: data }));
    });

    // Live activity events
    socket.on('live-activity', (data) => {
      console.log('Live activity:', data);
      window.dispatchEvent(new CustomEvent('live-activity', { detail: data }));
    });

    // Live stats events
    socket.on('live-stats-update', (data) => {
      console.log('Live stats update:', data);
      window.dispatchEvent(new CustomEvent('live-stats-update', { detail: data }));
    });

    socket.on('live-stats-error', (error) => {
      console.error('Live stats error:', error);
      window.dispatchEvent(new CustomEvent('live-stats-error', { detail: error }));
    });

    // Admin events
    socket.on('user-status-update', (data) => {
      console.log('User status update:', data);
      window.dispatchEvent(new CustomEvent('user-status-update', { detail: data }));
    });

    // Notification events
    socket.on('notification', (data) => {
      console.log('Notification received:', data);
      window.dispatchEvent(new CustomEvent('notification', { detail: data }));
    });

    // Account events
    socket.on('account-status-changed', (data) => {
      console.log('Account status changed:', data);
      window.dispatchEvent(new CustomEvent('account-status-changed', { detail: data }));
    });

    // Simulation events
    socket.on('simulation-status', (data) => {
      console.log('Simulation status:', data);
      window.dispatchEvent(new CustomEvent('simulation-status', { detail: data }));
    });

    // Cleanup on unmount
    return () => {
      socket.disconnect();
      socketRef.current = null;
    };
  }, [currentUser]);

  // Join campaign room
  const joinCampaign = (campaignId) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('join-campaign', campaignId);
    }
  };

  // Leave campaign room
  const leaveCampaign = (campaignId) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('leave-campaign', campaignId);
    }
  };

  // Send donation event
  const sendDonation = (donationData) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('donation-made', donationData);
    }
  };

  // Send campaign status change
  const sendCampaignStatusChange = (campaignData) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('campaign-status-changed', campaignData);
    }
  };

  // Send new campaign event
  const sendNewCampaign = (campaignData) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('campaign-created', campaignData);
    }
  };

  // Send user status change (admin only)
  const sendUserStatusChange = (userData) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('user-status-changed', userData);
    }
  };

  // Request live stats
  const requestLiveStats = () => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('request-live-stats');
    }
  };

  // Send notification
  const sendNotification = (notificationData) => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('send-notification', notificationData);
    }
  };

  // Simulation controls
  const startSimulation = () => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('start-simulation');
    }
  };

  const stopSimulation = () => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('stop-simulation');
    }
  };

  const getSimulationStatus = () => {
    if (socketRef.current && isConnected) {
      socketRef.current.emit('get-simulation-status');
    }
  };

  return {
    socket: socketRef.current,
    isConnected,
    connectionError,
    joinCampaign,
    leaveCampaign,
    sendDonation,
    sendCampaignStatusChange,
    sendNewCampaign,
    sendUserStatusChange,
    requestLiveStats,
    sendNotification,
    startSimulation,
    stopSimulation,
    getSimulationStatus,
  };
};

export default useSocket;
