import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const simulationService = {
  // Get simulation status
  async getStatus() {
    try {
      const response = await apiClient.get('/simulation/status');
      return response.data;
    } catch (error) {
      console.error('Error getting simulation status:', error);
      throw error;
    }
  },

  // Start simulation
  async startSimulation() {
    try {
      const response = await apiClient.post('/simulation/start');
      return response.data;
    } catch (error) {
      console.error('Error starting simulation:', error);
      throw error;
    }
  },

  // Stop simulation
  async stopSimulation() {
    try {
      const response = await apiClient.post('/simulation/stop');
      return response.data;
    } catch (error) {
      console.error('Error stopping simulation:', error);
      throw error;
    }
  },

  // Seed database with sample data
  async seedDatabase() {
    try {
      const response = await apiClient.post('/simulation/seed');
      return response.data;
    } catch (error) {
      console.error('Error seeding database:', error);
      throw error;
    }
  },

  // Clear all campaigns
  async clearDatabase() {
    try {
      const response = await apiClient.delete('/simulation/clear');
      return response.data;
    } catch (error) {
      console.error('Error clearing database:', error);
      throw error;
    }
  },

  // Get simulation analytics
  async getAnalytics() {
    try {
      const response = await apiClient.get('/simulation/analytics');
      return response.data;
    } catch (error) {
      console.error('Error getting analytics:', error);
      throw error;
    }
  }
};

export default simulationService;
