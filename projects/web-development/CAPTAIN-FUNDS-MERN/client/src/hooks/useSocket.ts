import { useEffect, useRef, useState } from 'react';
import { io, Socket } from 'socket.io-client';
import { message, notification } from 'antd';
import userStore from '../store/users-store';

interface UseSocketReturn {
  socket: Socket | null;
  isConnected: boolean;
  joinCampaign: (campaignId: string) => void;
  leaveCampaign: (campaignId: string) => void;
  emitDonation: (donationData: any) => void;
  emitCampaignUpdate: (campaignData: any) => void;
  requestLiveStats: () => void;
}

export const useSocket = (): UseSocketReturn => {
  const socketRef = useRef<Socket | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const { currentUser } = userStore();

  useEffect(() => {
    // Initialize socket connection
    if (!socketRef.current) {
      socketRef.current = io(import.meta.env.VITE_SOCKET_URL || 'http://localhost:5000', {
        transports: ['websocket'],
        autoConnect: true,
      });

      const socket = socketRef.current;

      // Connection event handlers
      socket.on('connect', () => {
        console.log('Socket connected:', socket.id);
        setIsConnected(true);

        // Join user-specific room
        if (currentUser?._id) {
          socket.emit('join-user-room', currentUser._id);
        }

        // Join admin room if user is admin
        if (currentUser?.isAdmin) {
          socket.emit('join-admin-room');
        }
      });

      socket.on('disconnect', () => {
        console.log('Socket disconnected');
        setIsConnected(false);
      });

      // Campaign update handlers with MongoDB sync
      socket.on('campaign-updated', (data) => {
        console.log('Campaign updated:', data);
        // Dispatch to trigger re-renders in components
        window.dispatchEvent(new CustomEvent('campaign-updated', { detail: data }));
      });

      socket.on('new-campaign', (data) => {
        console.log('New campaign created:', data);
        if (data.isSimulation) {
          notification.success({
            message: 'New Campaign Added!',
            description: `🎭 "${data.campaign.title}" has been created`,
            placement: 'topRight',
          });
        } else {
          notification.success({
            message: 'New Campaign!',
            description: `${data.campaign.title} has been created`,
            placement: 'topRight',
          });
        }
        window.dispatchEvent(new CustomEvent('new-campaign', { detail: data }));
      });

      socket.on('campaign-status-update', (data) => {
        console.log('Campaign status updated:', data);
        window.dispatchEvent(new CustomEvent('campaign-status-update', { detail: data }));
      });

      socket.on('campaign-progress', (data) => {
        console.log('Campaign progress update:', data);
        window.dispatchEvent(new CustomEvent('campaign-progress', { detail: data }));
      });

      socket.on('goal-reached', (data) => {
        console.log('Campaign goal reached:', data);
        notification.success({
          message: '🎯 Goal Achieved!',
          description: `"${data.title}" has reached its funding goal!`,
          placement: 'topRight',
          duration: 0, // Don't auto-close
        });
        window.dispatchEvent(new CustomEvent('goal-reached', { detail: data }));
      });

      // Donation handlers with simulation support
      socket.on('new-donation', (data) => {
        console.log('New donation received:', data);
        if (currentUser?.isAdmin) {
          if (data.donationType === 'simulated') {
            notification.success({
              message: 'New Simulated Donation!',
              description: `🎭 $${data.amount} donated to ${data.campaignTitle}`,
              placement: 'topRight',
            });
          } else {
            notification.success({
              message: 'New Donation!',
              description: `$${data.amount} donated to ${data.campaignTitle}`,
              placement: 'topRight',
            });
          }
        }
        window.dispatchEvent(new CustomEvent('new-donation', { detail: data }));
      });

      // Live activity feed
      socket.on('live-activity', (data) => {
        console.log('Live activity:', data);
        window.dispatchEvent(new CustomEvent('live-activity', { detail: data }));
      });

      // Live statistics updates
      socket.on('live-stats-update', (data) => {
        console.log('Live stats updated:', data);
        window.dispatchEvent(new CustomEvent('live-stats-update', { detail: data }));
      });

      // User status updates
      socket.on('user-status-update', (data) => {
        console.log('User status updated:', data);
        window.dispatchEvent(new CustomEvent('user-status-update', { detail: data }));
      });

      socket.on('account-status-changed', (data) => {
        if (data.isActive) {
          message.success(data.message);
        } else {
          message.error(data.message);
        }
      });

      // General notifications
      socket.on('notification', (data) => {
        console.log('Notification received:', data);
        
        const notificationType = data.type === 'error' ? 'error' : 
                                data.type === 'warning' ? 'warning' : 
                                data.type === 'info' ? 'info' : 'success';

        notification[notificationType]({
          message: data.title,
          description: data.message,
          placement: 'topRight',
          duration: 5,
        });
      });

      // Error handling
      socket.on('connect_error', (error) => {
        console.error('Socket connection error:', error);
        setIsConnected(false);
      });
    }

    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
        socketRef.current = null;
        setIsConnected(false);
      }
    };
  }, [currentUser]);

  // Helper functions
  const joinCampaign = (campaignId: string) => {
    if (socketRef.current) {
      socketRef.current.emit('join-campaign', campaignId);
    }
  };

  const leaveCampaign = (campaignId: string) => {
    if (socketRef.current) {
      socketRef.current.emit('leave-campaign', campaignId);
    }
  };

  const emitDonation = (donationData: any) => {
    if (socketRef.current) {
      socketRef.current.emit('donation-made', donationData);
    }
  };

  const emitCampaignUpdate = (campaignData: any) => {
    if (socketRef.current) {
      socketRef.current.emit('campaign-status-changed', campaignData);
    }
  };

  const requestLiveStats = () => {
    if (socketRef.current) {
      socketRef.current.emit('request-live-stats');
    }
  };

  // Simulation control methods
  const startSimulation = () => {
    if (socketRef.current) {
      socketRef.current.emit('start-simulation');
    }
  };

  const stopSimulation = () => {
    if (socketRef.current) {
      socketRef.current.emit('stop-simulation');
    }
  };

  const getSimulationStatus = () => {
    if (socketRef.current) {
      socketRef.current.emit('get-simulation-status');
    }
  };

  return {
    socket: socketRef.current,
    isConnected,
    joinCampaign,
    leaveCampaign,
    emitDonation,
    emitCampaignUpdate,
    requestLiveStats,
    startSimulation,
    stopSimulation,
    getSimulationStatus,
  };
};

export default useSocket;
