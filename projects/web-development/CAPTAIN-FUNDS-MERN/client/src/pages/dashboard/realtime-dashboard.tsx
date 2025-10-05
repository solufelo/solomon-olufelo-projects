import { useEffect, useState } from "react";
import {
  Typography,
  Card,
  Row,
  Col,
  Statistic,
  Button,
  List,
  Avatar,
  Progress,
  Tag,
  Badge,
  Alert,
  Space,
  Divider,
} from "antd";
import {
  DashboardOutlined,
  FundOutlined,
  DollarOutlined,
  TeamOutlined,
  TrophyOutlined,
  RiseOutlined,
  HeartOutlined,
  EyeOutlined,
  ThunderboltOutlined,
  WifiOutlined,
  CloseCircleOutlined,
} from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import userStore from "../../store/users-store";
import useSocket from "../../hooks/useSocket";
import simulationService from "../../services/simulationService";
import type { Campaign } from "../../interfaces/index";

const { Title, Text } = Typography;

interface DashboardStats {
  totalCampaigns: number;
  totalDonations: number;
  totalAmountRaised: number;
  activeCampaigns: number;
  averageDonation: number;
}

interface RecentActivity {
  id: string;
  type: "donation" | "campaign" | "milestone" | "user";
  title: string;
  description: string;
  amount?: number;
  timestamp: string;
  avatar?: string;
  isRealTime?: boolean;
}

function RealtimeDashboard() {
  const navigate = useNavigate();
  const { currentUser } = userStore();
  const {
    socket,
    isConnected,
    requestLiveStats,
    startSimulation,
    stopSimulation,
    getSimulationStatus,
  } = useSocket();

  const [dashboardStats, setDashboardStats] = useState<DashboardStats>({
    totalCampaigns: 0,
    totalDonations: 0,
    totalAmountRaised: 0,
    activeCampaigns: 0,
    averageDonation: 0,
  });

  const [featuredCampaigns, setFeaturedCampaigns] = useState<Campaign[]>([]);
  const [recentActivity, setRecentActivity] = useState<RecentActivity[]>([]);
  const [statsLoading, setStatsLoading] = useState(true);
  const [simulationRunning, setSimulationRunning] = useState(true);
  const [simulationStatus, setSimulationStatus] =
    useState<string>("Checking...");
  const [simulationLoading, setSimulationLoading] = useState(false);
  const [databaseSeeded, setDatabaseSeeded] = useState(false);

  useEffect(() => {
    // Initialize with mock data
    initializeDashboard();

    // Set up real-time event listeners
    if (typeof window !== "undefined") {
      const handleLiveStatsUpdate = (event: any) => {
        const stats = event.detail;
        setDashboardStats(stats);
        setStatsLoading(false);
      };

      const handleNewDonation = (event: any) => {
        const donation = event.detail;
        addRealtimeActivity({
          id: `donation-${Date.now()}`,
          type: "donation",
          title: "New Donation Received! 💝",
          description: `$${donation.amount} donated to ${donation.campaignTitle}`,
          amount: donation.amount,
          timestamp: "Just now",
          isRealTime: true,
        });

        // Update stats
        setDashboardStats((prev) => ({
          ...prev,
          totalDonations: prev.totalDonations + 1,
          totalAmountRaised: prev.totalAmountRaised + donation.amount,
        }));
      };

      const handleNewCampaign = (event: any) => {
        const campaign = event.detail;
        addRealtimeActivity({
          id: `campaign-${Date.now()}`,
          type: "campaign",
          title: "New Campaign Created! 🚀",
          description: `${campaign.title} by ${campaign.organizer}`,
          timestamp: "Just now",
          isRealTime: true,
        });

        // Update stats
        setDashboardStats((prev) => ({
          ...prev,
          totalCampaigns: prev.totalCampaigns + 1,
          activeCampaigns: prev.activeCampaigns + 1,
        }));
      };

      const handleCampaignUpdate = (event: any) => {
        const update = event.detail;
        addRealtimeActivity({
          id: `update-${Date.now()}`,
          type: "milestone",
          title: "Campaign Progress! 📈",
          description: `${update.campaignTitle} received a new donation`,
          amount: update.donation?.amount,
          timestamp: "Just now",
          isRealTime: true,
        });
      };

      const handleUserUpdate = (event: any) => {
        const user = event.detail;
        addRealtimeActivity({
          id: `user-${Date.now()}`,
          type: "user",
          title: "User Activity 👤",
          description: `${user.name} ${
            user.isActive ? "activated" : "deactivated"
          }`,
          timestamp: "Just now",
          isRealTime: true,
        });
      };

      // Add event listeners
      window.addEventListener("live-stats-update", handleLiveStatsUpdate);
      window.addEventListener("new-donation", handleNewDonation);
      window.addEventListener("new-campaign", handleNewCampaign);
      window.addEventListener("campaign-updated", handleCampaignUpdate);
      window.addEventListener("user-status-update", handleUserUpdate);

      // Request initial live stats
      if (isConnected) {
        requestLiveStats();
      }

      // Cleanup
      return () => {
        window.removeEventListener("live-stats-update", handleLiveStatsUpdate);
        window.removeEventListener("new-donation", handleNewDonation);
        window.removeEventListener("new-campaign", handleNewCampaign);
        window.removeEventListener("campaign-updated", handleCampaignUpdate);
        window.removeEventListener("user-status-update", handleUserUpdate);
      };
    }
  }, [isConnected, requestLiveStats]);

  const initializeDashboard = () => {
    // Mock initial data
    setDashboardStats({
      totalCampaigns: 42,
      totalDonations: 1247,
      totalAmountRaised: 89432,
      activeCampaigns: 28,
      averageDonation: 71.75,
    });

    setFeaturedCampaigns([
      {
        _id: "1",
        title: "Help Build Community Garden",
        description: "Creating a sustainable garden for local families",
        organizer: "Green Initiative",
        image: "/api/placeholder/400/300",
        EventTargetAmount: 15000,
        EventCurrentAmount: 8750,
        createdAt: new Date(),
        updatedAt: new Date(),
        status: "active",
        EventCategory: "Environment",
        location: "Portland, OR",
        endDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
        isActive: true,
        isApproved: true,
        isFeatured: true,
      },
      {
        _id: "2",
        title: "Emergency Medical Fund",
        description: "Supporting families with urgent medical needs",
        organizer: "Healthcare Heroes",
        image: "/api/placeholder/400/300",
        EventTargetAmount: 25000,
        EventCurrentAmount: 18200,
        createdAt: new Date(),
        updatedAt: new Date(),
        status: "active",
        EventCategory: "Healthcare",
        location: "Seattle, WA",
        endDate: new Date(Date.now() + 45 * 24 * 60 * 60 * 1000),
        isActive: true,
        isApproved: true,
        isFeatured: true,
      },
    ]);

    setRecentActivity([
      {
        id: "1",
        type: "donation",
        title: "Donation Received",
        description: "Sarah Wilson donated $125 to Education Fund",
        amount: 125,
        timestamp: "5 minutes ago",
        avatar: "SW",
      },
      {
        id: "2",
        type: "campaign",
        title: "Campaign Created",
        description: "New campaign: Community Sports Center",
        timestamp: "12 minutes ago",
        avatar: "CS",
      },
      {
        id: "3",
        type: "milestone",
        title: "Goal Milestone",
        description: "Medical Fund reached 75% of target",
        timestamp: "1 hour ago",
        avatar: "MF",
      },
    ]);

    setStatsLoading(false);
  };

  const addRealtimeActivity = (activity: RecentActivity) => {
    setRecentActivity((prev) => [activity, ...prev.slice(0, 9)]); // Keep only 10 most recent
  };

  const getActivityIcon = (type: string) => {
    switch (type) {
      case "donation":
        return <HeartOutlined className="text-green-500" />;
      case "campaign":
        return <FundOutlined className="text-blue-500" />;
      case "milestone":
        return <TrophyOutlined className="text-gold" />;
      case "user":
        return <TeamOutlined className="text-purple-500" />;
      default:
        return <DashboardOutlined />;
    }
  };

  // Enhanced simulation control handlers
  const handleStartSimulation = async () => {
    try {
      setSimulationLoading(true);
      setSimulationStatus("Starting...");

      const result = await simulationService.startSimulation();
      setSimulationRunning(true);
      setSimulationStatus(result.message);

      // Also emit via Socket.IO
      startSimulation();

      message.success(result.message);
    } catch (error: any) {
      setSimulationStatus("Failed to start");
      message.error(
        error?.response?.data?.message || "Failed to start simulation"
      );
    } finally {
      setSimulationLoading(false);
    }
  };

  const handleStopSimulation = async () => {
    try {
      setSimulationLoading(true);
      setSimulationStatus("Stopping...");

      const result = await simulationService.stopSimulation();
      setSimulationRunning(false);
      setSimulationStatus(result.message);

      // Also emit via Socket.IO
      stopSimulation();

      message.success(result.message);
    } catch (error: any) {
      setSimulationStatus("Failed to stop");
      message.error(
        error?.response?.data?.message || "Failed to stop simulation"
      );
    } finally {
      setSimulationLoading(false);
    }
  };

  const handleGetSimulationStatus = async () => {
    try {
      const result = await simulationService.getStatus();
      setSimulationRunning(result.status.isRunning);
      setSimulationStatus(`Running: ${result.status.isRunning ? "Yes" : "No"}`);
      message.info(
        `Simulation ${result.status.isRunning ? "running" : "stopped"}`
      );
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to get simulation status"
      );
    }
  };

  const handleSeedDatabase = async () => {
    try {
      setSimulationLoading(true);
      const result = await simulationService.seedDatabase();

      if (result.success) {
        setDatabaseSeeded(true);
        message.success(
          `Database seeded with ${result.campaigns?.length || 0} campaigns!`
        );
        // Refresh data
        requestLiveStats();
      } else {
        message.warning(result.message);
      }
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to seed database"
      );
    } finally {
      setSimulationLoading(false);
    }
  };

  const connectionStatus = isConnected ? (
    <Badge status="success" text="Real-time Connected" />
  ) : (
    <Badge status="error" text="Disconnected" />
  );

  const simulationStatusBadge = simulationRunning ? (
    <Badge status="processing" text="Simulation Running" />
  ) : (
    <Badge status="default" text="Simulation Stopped" />
  );

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header with Connection Status */}
      <div className="mb-8">
        <div className="flex justify-between items-start">
          <div>
            <Title level={1} className="flex items-center gap-3">
              <DashboardOutlined />
              Real-time Dashboard
              <ThunderboltOutlined className="text-yellow-500" />
            </Title>
            <Text type="secondary" className="text-lg">
              Welcome back, {currentUser?.name}! Live updates from your
              fundraising platform.
            </Text>
          </div>
          <div className="text-right">
            <Space direction="vertical" size="small">
              <div className="flex items-center gap-2">
                {isConnected ? (
                  <WifiOutlined className="text-green-500" />
                ) : (
                  <CloseCircleOutlined className="text-red-500" />
                )}
                {connectionStatus}
              </div>
              <div className="flex items-center gap-2">
                <ThunderboltOutlined className="text-yellow-500" />
                {simulationStatusBadge}
              </div>
              <div className="flex gap-2 flex-wrap">
                <Button
                  size="small"
                  onClick={requestLiveStats}
                  loading={statsLoading}
                  disabled={!isConnected}
                >
                  Refresh Live Data
                </Button>
                <Button
                  size="small"
                  type={simulationRunning ? "default" : "primary"}
                  onClick={
                    simulationRunning
                      ? handleStopSimulation
                      : handleStartSimulation
                  }
                  loading={simulationLoading}
                  disabled={!isConnected}
                >
                  {simulationRunning ? "Stop Simulation" : "Start Simulation"}
                </Button>
                <Button
                  size="small"
                  onClick={handleGetSimulationStatus}
                  disabled={!isConnected}
                >
                  Status
                </Button>
                {!databaseSeeded && (
                  <Button
                    size="small"
                    type="primary"
                    onClick={handleSeedDatabase}
                    loading={simulationLoading}
                    disabled={!isConnected}
                  >
                    Seed Database
                  </Button>
                )}
              </div>
            </Space>
          </div>
        </div>

        {!isConnected && (
          <Alert
            message="Real-time Connection Lost"
            description="Some features may not work properly. Please check your connection."
            type="warning"
            showIcon
            className="mt-4"
          />
        )}
      </div>

      {/* Statistics Cards */}
      <Row gutter={[24, 24]} className="mb-8">
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="Total Campaigns"
              value={dashboardStats.totalCampaigns}
              prefix={<FundOutlined />}
              valueStyle={{ color: "#1890ff" }}
              loading={statsLoading}
            />
            <div className="mt-2">
              <Text type="secondary">
                {dashboardStats.activeCampaigns} active
              </Text>
              <div className="flex gap-1 mt-1">
                <Tag color="blue" className="text-xs">
                  LIVE
                </Tag>
                <Tag color="green" className="text-xs">
                  MongoDB
                </Tag>
              </div>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="Total Donations"
              value={dashboardStats.totalDonations}
              prefix={<HeartOutlined />}
              valueStyle={{ color: "#52c41a" }}
              loading={statsLoading}
            />
            <div className="mt-2">
              <RiseOutlined className="text-green-500" />
              <Text type="secondary" className="ml-1">
                Real-time tracking
              </Text>
              <Tag color="green" className="text-xs ml-2">
                MongoDB
              </Tag>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="Amount Raised"
              value={dashboardStats.totalAmountRaised}
              precision={2}
              prefix="$"
              valueStyle={{ color: "#722ed1" }}
              loading={statsLoading}
            />
            <div className="mt-2">
              <Text type="secondary">Live updates</Text>
              <div className="flex gap-1 mt-1">
                <Tag color="purple" className="text-xs">
                  SYNC
                </Tag>
                <Tag color="green" className="text-xs">
                  MongoDB
                </Tag>
              </div>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="Avg Donation"
              value={dashboardStats.averageDonation}
              precision={2}
              prefix="$"
              valueStyle={{ color: "#f5222d" }}
              loading={statsLoading}
            />
            <div className="mt-2">
              <Text type="secondary">Per contribution</Text>
              <Tag color="green" className="text-xs mt-1">
                MongoDB
              </Tag>
            </div>
          </Card>
        </Col>
      </Row>

      <Row gutter={[24, 24]}>
        {/* Featured Campaigns */}
        <Col xs={24} lg={16}>
          <Card
            title={
              <div className="flex items-center gap-2">
                <span>Featured Campaigns</span>
                <ThunderboltOutlined className="text-yellow-500" />
                <Tag color="orange">LIVE UPDATES</Tag>
              </div>
            }
            extra={
              <Button type="primary" onClick={() => navigate("/campaigns")}>
                View All Campaigns
              </Button>
            }
          >
            <Row gutter={[16, 16]}>
              {featuredCampaigns.map((campaign) => {
                const progressPercent = Math.round(
                  (campaign.EventCurrentAmount / campaign.EventTargetAmount) *
                    100
                );

                return (
                  <Col xs={24} md={12} key={campaign._id}>
                    <Card
                      size="small"
                      className="h-full"
                      cover={
                        <div className="h-32 bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center relative">
                          <FundOutlined className="text-white text-2xl" />
                          <div className="absolute top-2 right-2">
                            <Tag color="gold">Featured</Tag>
                          </div>
                          <div className="absolute top-2 left-2">
                            <Badge
                              status={isConnected ? "processing" : "default"}
                              text={isConnected ? "LIVE" : "OFFLINE"}
                              style={{ color: "white", fontSize: "10px" }}
                            />
                          </div>
                        </div>
                      }
                      actions={[
                        <Button
                          key="view"
                          type="text"
                          icon={<EyeOutlined />}
                          onClick={() => navigate(`/campaigns/${campaign._id}`)}
                        >
                          View
                        </Button>,
                        <Button
                          key="donate"
                          type="text"
                          icon={<HeartOutlined />}
                          className="text-green-600"
                        >
                          Donate
                        </Button>,
                      ]}
                    >
                      <Card.Meta
                        title={campaign.title}
                        description={
                          <div>
                            <Text type="secondary" className="block mb-2">
                              {campaign.description.substring(0, 60)}...
                            </Text>
                            <div className="mb-2">
                              <Tag color="blue">{campaign.EventCategory}</Tag>
                              <Tag color="green">{campaign.location}</Tag>
                            </div>
                            <div className="mb-2">
                              <Text strong>
                                ${campaign.EventCurrentAmount.toLocaleString()}
                              </Text>
                              <Text type="secondary">
                                {" "}
                                of $
                                {campaign.EventTargetAmount.toLocaleString()}
                              </Text>
                            </div>
                            <Progress
                              percent={progressPercent}
                              strokeColor="#52c41a"
                              size="small"
                            />
                          </div>
                        }
                      />
                    </Card>
                  </Col>
                );
              })}
            </Row>
          </Card>
        </Col>

        {/* Real-time Activity Feed */}
        <Col xs={24} lg={8}>
          <Card
            title={
              <div className="flex items-center gap-2">
                <span>Live Activity Feed</span>
                <ThunderboltOutlined className="text-yellow-500" />
                {isConnected && <Badge status="processing" />}
              </div>
            }
            extra={<Button type="text">View All</Button>}
          >
            <List
              dataSource={recentActivity}
              renderItem={(item) => (
                <List.Item
                  className={
                    item.isRealTime
                      ? "bg-yellow-50 border-yellow-200 rounded p-2"
                      : ""
                  }
                >
                  <List.Item.Meta
                    avatar={
                      <Avatar
                        icon={getActivityIcon(item.type)}
                        style={{
                          backgroundColor:
                            item.type === "donation"
                              ? "#f6ffed"
                              : item.type === "campaign"
                              ? "#e6f7ff"
                              : item.type === "milestone"
                              ? "#fff7e6"
                              : "#f9f0ff",
                        }}
                      >
                        {item.avatar}
                      </Avatar>
                    }
                    title={
                      <div className="flex justify-between items-center">
                        <Text strong>
                          {item.title}
                          {item.isRealTime && (
                            <Tag color="orange" size="small" className="ml-2">
                              NEW
                            </Tag>
                          )}
                        </Text>
                        {item.amount && (
                          <Text className="text-green-600">
                            +${item.amount}
                          </Text>
                        )}
                      </div>
                    }
                    description={
                      <div>
                        <Text type="secondary">{item.description}</Text>
                        <br />
                        <Text type="secondary" className="text-xs">
                          {item.timestamp}
                        </Text>
                      </div>
                    }
                  />
                </List.Item>
              )}
            />
          </Card>

          {/* Simulation Analytics */}
          <Card
            title={
              <div className="flex items-center gap-2">
                <span>Simulation Analytics</span>
                <ThunderboltOutlined className="text-yellow-500" />
              </div>
            }
            className="mt-4"
          >
            <div className="grid grid-cols-2 gap-4">
              <div className="text-center">
                <div className="text-2xl font-bold text-green-600">10-30s</div>
                <div className="text-sm text-gray-500">Donation Interval</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-blue-600">5-15s</div>
                <div className="text-sm text-gray-500">Progress Updates</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-purple-600">2-5m</div>
                <div className="text-sm text-gray-500">New Campaigns</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-orange-600">🎭</div>
                <div className="text-sm text-gray-500">MongoDB Synced</div>
              </div>
            </div>
            <Divider />
            <div className="text-center">
              <Text type="secondary">
                All simulation data is stored in and retrieved from MongoDB for
                realistic behavior
              </Text>
            </div>
          </Card>

          {/* Quick Actions */}
          <Card title="Quick Actions" className="mt-4">
            <div className="space-y-3">
              <Button
                block
                type="primary"
                icon={<FundOutlined />}
                onClick={() => navigate("/campaigns")}
              >
                View Live Campaigns
              </Button>
              <Button
                block
                icon={<DollarOutlined />}
                onClick={() => navigate("/donations")}
              >
                View Donations
              </Button>
              <Button
                block
                icon={<TeamOutlined />}
                onClick={() => navigate("/users")}
                disabled={!currentUser?.isAdmin}
              >
                Manage Users
              </Button>
              <Button
                block
                icon={<TrophyOutlined />}
                onClick={() => navigate("/reports")}
              >
                View Reports
              </Button>
            </div>
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default RealtimeDashboard;
