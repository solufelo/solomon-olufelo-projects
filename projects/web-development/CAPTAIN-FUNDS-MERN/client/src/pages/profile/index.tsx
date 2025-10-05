import {
  Typography,
  Card,
  Form,
  Input,
  Button,
  Avatar,
  Row,
  Col,
  Statistic,
  Upload,
  message,
  Divider,
  Tag,
} from "antd";
import {
  ProfileOutlined,
  EditOutlined,
  UserOutlined,
  CameraOutlined,
  SaveOutlined,
  LockOutlined,
  MailOutlined,
  PhoneOutlined,
  EnvironmentOutlined,
} from "@ant-design/icons";
import { useState, useEffect } from "react";
import axios from "axios";
import userStore from "../../store/users-store";

const { Title, Text } = Typography;

interface ProfileData {
  name: string;
  email: string;
  phone?: string;
  location?: string;
  bio?: string;
  website?: string;
}

interface UserStats {
  totalCampaigns: number;
  totalDonations: number;
  totalAmountDonated: number;
  totalAmountRaised: number;
}

function ProfilePage() {
  const { currentUser, setCurrentUser } = userStore();
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  const [editing, setEditing] = useState(false);
  const [userStats, setUserStats] = useState<UserStats>({
    totalCampaigns: 0,
    totalDonations: 0,
    totalAmountDonated: 0,
    totalAmountRaised: 0,
  });
  const [profileImage, setProfileImage] = useState<string>("");

  useEffect(() => {
    fetchUserStats();
    if (currentUser) {
      setProfileImage(currentUser.profileImage || "");
    }
  }, [currentUser]);

  const fetchUserStats = async () => {
    try {
      const token = localStorage.getItem("token");
      if (!token) return;

      // Fetch donation stats
      const statsResponse = await axios.get(
        `${import.meta.env.VITE_API_URL}/donations/stats/user`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setUserStats({
        totalCampaigns: 0, // Would need campaign creation feature to track this
        totalDonations: statsResponse.data.stats.totalDonations,
        totalAmountDonated: statsResponse.data.stats.totalAmount,
        totalAmountRaised: 0, // This would be calculated differently
      });
    } catch (error: any) {
      console.error("Error fetching user stats:", error);
      // Keep default values if API call fails
    }
  };

  const onFinish = async (values: ProfileData) => {
    try {
      setLoading(true);

      const token = localStorage.getItem("token");
      const response = await axios.put(
        `${import.meta.env.VITE_API_URL}/users/profile`,
        values,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.data.success) {
        message.success("Profile updated successfully");
        setCurrentUser(response.data.user);
        setEditing(false);
      }
    } catch (error: any) {
      const errorMessage =
        error?.response?.data?.message || "Failed to update profile";
      message.error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleImageUpload = async (file: File) => {
    try {
      const formData = new FormData();
      formData.append("profileImage", file);

      const token = localStorage.getItem("token");
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}/upload/profile-image`,
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        }
      );

      if (response.data.success) {
        setProfileImage(response.data.imageUrl);
        message.success("Profile image updated successfully");
      }
    } catch (error: any) {
      message.error("Failed to upload image");
    }
  };

  const uploadProps = {
    beforeUpload: (file: File) => {
      const isJpgOrPng =
        file.type === "image/jpeg" || file.type === "image/png";
      if (!isJpgOrPng) {
        message.error("You can only upload JPG/PNG file!");
        return false;
      }
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isLt2M) {
        message.error("Image must smaller than 2MB!");
        return false;
      }

      handleImageUpload(file);
      return false;
    },
    showUploadList: false,
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6">
        <Title level={1} className="flex items-center gap-3">
          <ProfileOutlined />
          Profile
        </Title>
        <Text type="secondary">
          Manage your personal information and account settings
        </Text>
      </div>

      <Row gutter={[24, 24]}>
        {/* Profile Information */}
        <Col xs={24} lg={16}>
          <Card
            title="Personal Information"
            extra={
              <Button
                icon={editing ? <SaveOutlined /> : <EditOutlined />}
                onClick={() => setEditing(!editing)}
                type={editing ? "primary" : "default"}
              >
                {editing ? "Cancel" : "Edit"}
              </Button>
            }
          >
            <Form
              form={form}
              layout="vertical"
              initialValues={{
                name: currentUser?.name,
                email: currentUser?.email,
                phone: currentUser?.phone || "",
                location: currentUser?.location || "",
                bio: currentUser?.bio || "",
                website: currentUser?.website || "",
              }}
              onFinish={onFinish}
            >
              <Row gutter={16}>
                <Col xs={24} sm={12}>
                  <Form.Item
                    name="name"
                    label="Full Name"
                    rules={[
                      { required: true, message: "Please enter your name" },
                    ]}
                  >
                    <Input
                      prefix={<UserOutlined />}
                      disabled={!editing}
                      placeholder="Enter your full name"
                    />
                  </Form.Item>
                </Col>
                <Col xs={24} sm={12}>
                  <Form.Item
                    name="email"
                    label="Email Address"
                    rules={[
                      { required: true, message: "Please enter your email" },
                      { type: "email", message: "Please enter a valid email" },
                    ]}
                  >
                    <Input
                      prefix={<MailOutlined />}
                      type="email"
                      disabled={!editing}
                      placeholder="Enter your email"
                    />
                  </Form.Item>
                </Col>
              </Row>

              <Row gutter={16}>
                <Col xs={24} sm={12}>
                  <Form.Item name="phone" label="Phone Number">
                    <Input
                      prefix={<PhoneOutlined />}
                      disabled={!editing}
                      placeholder="Enter your phone number"
                    />
                  </Form.Item>
                </Col>
                <Col xs={24} sm={12}>
                  <Form.Item name="location" label="Location">
                    <Input
                      prefix={<EnvironmentOutlined />}
                      disabled={!editing}
                      placeholder="Enter your location"
                    />
                  </Form.Item>
                </Col>
              </Row>

              <Row gutter={16}>
                <Col xs={24} sm={12}>
                  <Form.Item name="website" label="Website">
                    <Input
                      disabled={!editing}
                      placeholder="Enter your website URL"
                    />
                  </Form.Item>
                </Col>
              </Row>

              <Form.Item name="bio" label="Bio">
                <Input.TextArea
                  rows={4}
                  disabled={!editing}
                  placeholder="Tell us about yourself..."
                  maxLength={500}
                  showCount
                />
              </Form.Item>

              {editing && (
                <Form.Item>
                  <Button
                    type="primary"
                    htmlType="submit"
                    loading={loading}
                    icon={<SaveOutlined />}
                  >
                    Save Changes
                  </Button>
                </Form.Item>
              )}
            </Form>
          </Card>

          {/* Password Change Card */}
          <Card title="Security Settings" className="mt-6">
            <div className="mb-4">
              <Text>
                Keep your account secure by regularly updating your password.
              </Text>
            </div>
            <Button icon={<LockOutlined />} type="default">
              Change Password
            </Button>
          </Card>
        </Col>

        {/* Profile Summary */}
        <Col xs={24} lg={8}>
          <Card title="Profile Summary">
            <div className="text-center mb-6">
              <div className="relative inline-block">
                <Avatar size={100} src={profileImage} icon={<UserOutlined />} />
                <Upload {...uploadProps}>
                  <Button
                    type="primary"
                    shape="circle"
                    size="small"
                    icon={<CameraOutlined />}
                    className="absolute bottom-0 right-0"
                  />
                </Upload>
              </div>
              <div className="mt-4">
                <Title level={4} className="mb-1">
                  {currentUser?.name}
                </Title>
                <Text type="secondary">{currentUser?.email}</Text>
                <div className="mt-2">
                  <Tag color={currentUser?.isAdmin ? "red" : "blue"}>
                    {currentUser?.isAdmin ? "Administrator" : "Standard User"}
                  </Tag>
                  <Tag color={currentUser?.isActive ? "green" : "red"}>
                    {currentUser?.isActive ? "Active" : "Inactive"}
                  </Tag>
                </div>
              </div>
            </div>

            <Divider />

            <div className="space-y-3">
              <div className="flex justify-between">
                <Text>Member Since:</Text>
                <Text strong>September 2024</Text>
              </div>
              <div className="flex justify-between">
                <Text>Last Login:</Text>
                <Text strong>Today</Text>
              </div>
            </div>
          </Card>

          {/* Enhanced Stats Card */}
          <Card title="Activity Statistics" className="mt-4">
            <Row gutter={[16, 16]}>
              <Col span={12}>
                <Statistic
                  title="Campaigns Created"
                  value={userStats.totalCampaigns}
                  valueStyle={{ color: "#1890ff" }}
                />
              </Col>
              <Col span={12}>
                <Statistic
                  title="Donations Made"
                  value={userStats.totalDonations}
                  valueStyle={{ color: "#52c41a" }}
                />
              </Col>
              <Col span={12}>
                <Statistic
                  title="Amount Donated"
                  value={userStats.totalAmountDonated}
                  precision={2}
                  prefix="$"
                  valueStyle={{ color: "#f5222d" }}
                />
              </Col>
              <Col span={12}>
                <Statistic
                  title="Amount Raised"
                  value={userStats.totalAmountRaised}
                  precision={2}
                  prefix="$"
                  valueStyle={{ color: "#722ed1" }}
                />
              </Col>
            </Row>
          </Card>

          {/* Account Actions */}
          <Card title="Account Actions" className="mt-4">
            <div className="space-y-3">
              <Button block type="default">
                Download Account Data
              </Button>
              <Button block type="default">
                Privacy Settings
              </Button>
              <Button block danger type="text">
                Deactivate Account
              </Button>
            </div>
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default ProfilePage;
