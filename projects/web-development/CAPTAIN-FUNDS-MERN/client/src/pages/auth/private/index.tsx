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
} from "antd";
import {
  DashboardOutlined,
  FundOutlined,
  DollarOutlined,
  TeamOutlined,
  TrophyOutlined,
  RiseOutlined,
  HeartOutlined,
  CalendarOutlined,
  EyeOutlined,
} from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import userStore from "../../../store/users-store";
import type { Campaign } from "../../../interfaces/index";

const { Title, Text } = Typography;

interface DashboardStats {
  totalCampaigns: number;
  totalDonations: number;
  totalAmountRaised: number;
  activeCampaigns: number;
  successRate: number;
  monthlyGrowth: number;
}

interface RecentActivity {
  id: string;
  type: "donation" | "campaign" | "milestone";
  title: string;
  description: string;
  amount?: number;
  timestamp: string;
  avatar?: string;
}

function Homepage() {
  const navigate = useNavigate();
  const { currentUser } = userStore();
  const [dashboardStats, setDashboardStats] = useState<DashboardStats>({
    totalCampaigns: 0,
    totalDonations: 0,
    totalAmountRaised: 0,
    activeCampaigns: 0,
    successRate: 0,
    monthlyGrowth: 0,
  });

  const [featuredCampaigns, setFeaturedCampaigns] = useState<Campaign[]>([]);
  const [recentActivity, setRecentActivity] = useState<RecentActivity[]>([]);

  useEffect(() => {
    fetchDashboardData();
  }, [currentUser]);

  const fetchDashboardData = async () => {
    try {
      // Mock data - replace with real API calls
      setDashboardStats({
        totalCampaigns: 12,
        totalDonations: 347,
        totalAmountRaised: 45750.0,
        activeCampaigns: 8,
        successRate: 87.5,
        monthlyGrowth: 23.4,
      });

      setFeaturedCampaigns([
        {
          _id: "1",
          title: "Emergency Medical Fund",
          description: "Supporting urgent medical needs in the community",
          organizer: "Medical Foundation",
          image: "/api/placeholder/300/200",
          EventTargetAmount: 10000,
          EventCurrentAmount: 7500,
          status: "active",
          EventCategory: "Healthcare",
          location: "New York, NY",
          endDate: new Date("2024-12-01"),
          isActive: true,
          isApproved: true,
          isFeatured: true,
        },
        {
          _id: "2",
          title: "Education for All",
          description:
            "Providing educational resources to underprivileged children",
          organizer: "Education First",
          image: "/api/placeholder/300/200",
          EventTargetAmount: 15000,
          EventCurrentAmount: 8200,
          status: "active",
          EventCategory: "Education",
          location: "Los Angeles, CA",
          endDate: new Date("2024-11-15"),
          isActive: true,
          isApproved: true,
          isFeatured: true,
        },
      ]);

      setRecentActivity([
        {
          id: "1",
          type: "donation",
          title: "New Donation Received",
          description: "John Smith donated to Medical Emergency Fund",
          amount: 150,
          timestamp: "2 hours ago",
          avatar: "JS",
        },
        {
          id: "2",
          type: "campaign",
          title: "Campaign Milestone",
          description: "Education Fund reached 50% of target",
          timestamp: "5 hours ago",
          avatar: "EF",
        },
        {
          id: "3",
          type: "donation",
          title: "New Donation Received",
          description: "Sarah Wilson donated to Community Project",
          amount: 75,
          timestamp: "1 day ago",
          avatar: "SW",
        },
        {
          id: "4",
          type: "milestone",
          title: "Goal Achieved!",
          description: "Environmental Project reached its target",
          timestamp: "2 days ago",
          avatar: "EP",
        },
      ]);
    } catch (error) {
      console.error("Error fetching dashboard data:", error);
    }
  };

  const getActivityIcon = (type: string) => {
    switch (type) {
      case "donation":
        return <HeartOutlined className="text-green-500" />;
      case "campaign":
        return <FundOutlined className="text-blue-500" />;
      case "milestone":
        return <TrophyOutlined className="text-gold" />;
      default:
        return <CalendarOutlined />;
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Welcome Header */}
      <div className="mb-8">
        <Title level={1} className="flex items-center gap-3">
          <DashboardOutlined />
          Dashboard
        </Title>
        <Text type="secondary" className="text-lg">
          Welcome back, {currentUser?.name}! Here's what's happening with your
          fundraising activities.
        </Text>
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
            />
            <div className="mt-2">
              <Text type="secondary">
                {dashboardStats.activeCampaigns} active
              </Text>
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
            />
            <div className="mt-2">
              <Text type="secondary">
                This month: +{dashboardStats.monthlyGrowth}%
              </Text>
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
            />
            <div className="mt-2">
              <RiseOutlined className="text-green-500" />
              <Text type="secondary" className="ml-1">
                +{dashboardStats.monthlyGrowth}% growth
              </Text>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="Success Rate"
              value={dashboardStats.successRate}
              precision={1}
              suffix="%"
              valueStyle={{
                color: dashboardStats.successRate >= 80 ? "#52c41a" : "#faad14",
              }}
            />
            <div className="mt-2">
              <Text type="secondary">Campaign completion rate</Text>
            </div>
          </Card>
        </Col>
      </Row>

      <Row gutter={[24, 24]}>
        {/* Featured Campaigns */}
        <Col xs={24} lg={16}>
          <Card
            title="Featured Campaigns"
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
                        <div className="h-32 bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center">
                          <FundOutlined className="text-white text-2xl" />
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

        {/* Recent Activity */}
        <Col xs={24} lg={8}>
          <Card
            title="Recent Activity"
            extra={<Button type="text">View All</Button>}
          >
            <List
              dataSource={recentActivity}
              renderItem={(item) => (
                <List.Item>
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
                              : "#fff7e6",
                        }}
                      >
                        {item.avatar}
                      </Avatar>
                    }
                    title={
                      <div className="flex justify-between items-center">
                        <Text strong>{item.title}</Text>
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

          {/* Quick Actions */}
          <Card title="Quick Actions" className="mt-4">
            <div className="space-y-3">
              <Button
                block
                type="primary"
                icon={<FundOutlined />}
                onClick={() => navigate("/admin/campaigns")}
              >
                Create Campaign
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

export default Homepage;
