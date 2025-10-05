import {
  Typography,
  Card,
  Form,
  Input,
  Button,
  Switch,
  Divider,
  Select,
  Slider,
  message,
  Modal,
  Row,
  Col,
  Space,
  Alert,
} from "antd";
import {
  SettingOutlined,
  UserOutlined,
  BellOutlined,
  SafetyOutlined,
  DeleteOutlined,
  ExportOutlined,
  KeyOutlined,
  EyeInvisibleOutlined,
} from "@ant-design/icons";
import { useState } from "react";
import axios from "axios";
import userStore from "../../store/users-store";

const { Title, Text } = Typography;
const { Option } = Select;

interface NotificationSettings {
  emailNotifications: boolean;
  campaignUpdates: boolean;
  donationAlerts: boolean;
  marketingEmails: boolean;
  weeklyReports: boolean;
  mobilePushNotifications: boolean;
}

interface PrivacySettings {
  profileVisibility: "public" | "private" | "donors-only";
  showDonationHistory: boolean;
  showCampaignActivity: boolean;
  allowContactFromOrganizers: boolean;
}

interface SecuritySettings {
  twoFactorEnabled: boolean;
  sessionTimeout: number;
  loginAlerts: boolean;
}

function SettingsPage() {
  const { currentUser } = userStore();
  const [loading, setLoading] = useState(false);
  const [passwordModalVisible, setPasswordModalVisible] = useState(false);
  const [deleteModalVisible, setDeleteModalVisible] = useState(false);

  const [notificationForm] = Form.useForm();
  const [privacyForm] = Form.useForm();
  const [securityForm] = Form.useForm();
  const [passwordForm] = Form.useForm();

  const [notificationSettings, setNotificationSettings] =
    useState<NotificationSettings>({
      emailNotifications: true,
      campaignUpdates: true,
      donationAlerts: true,
      marketingEmails: false,
      weeklyReports: true,
      mobilePushNotifications: true,
    });

  const [privacySettings, setPrivacySettings] = useState<PrivacySettings>({
    profileVisibility: "public",
    showDonationHistory: false,
    showCampaignActivity: true,
    allowContactFromOrganizers: true,
  });

  const [securitySettings, setSecuritySettings] = useState<SecuritySettings>({
    twoFactorEnabled: false,
    sessionTimeout: 30,
    loginAlerts: true,
  });

  const onNotificationFinish = async (values: NotificationSettings) => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      await axios.put(
        `${import.meta.env.VITE_API_URL}/users/settings/notifications`,
        values,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      setNotificationSettings(values);
      message.success("Notification settings updated successfully");
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to update settings"
      );
    } finally {
      setLoading(false);
    }
  };

  const onPrivacyFinish = async (values: PrivacySettings) => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      await axios.put(
        `${import.meta.env.VITE_API_URL}/users/settings/privacy`,
        values,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      setPrivacySettings(values);
      message.success("Privacy settings updated successfully");
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to update settings"
      );
    } finally {
      setLoading(false);
    }
  };

  const onSecurityFinish = async (values: SecuritySettings) => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      await axios.put(
        `${import.meta.env.VITE_API_URL}/users/settings/security`,
        values,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      setSecuritySettings(values);
      message.success("Security settings updated successfully");
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to update settings"
      );
    } finally {
      setLoading(false);
    }
  };

  const handlePasswordChange = async (values: any) => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      await axios.put(
        `${import.meta.env.VITE_API_URL}/users/settings/change-password`,
        {
          currentPassword: values.currentPassword,
          newPassword: values.newPassword,
        },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      message.success("Password changed successfully");
      setPasswordModalVisible(false);
      passwordForm.resetFields();
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to change password"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleAccountDeletion = async () => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      await axios.delete(
        `${import.meta.env.VITE_API_URL}/users/settings/account`,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      message.success("Account deleted successfully");
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      window.location.href = "/login";
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to delete account"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleDataExport = async () => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      const response = await axios.get(
        `${import.meta.env.VITE_API_URL}/users/settings/export-data`,
        {
          headers: { Authorization: `Bearer ${token}` },
          responseType: "blob",
        }
      );

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", `${currentUser?.name}-data-export.json`);
      document.body.appendChild(link);
      link.click();
      link.remove();

      message.success("Data exported successfully");
    } catch (error: any) {
      message.error("Failed to export data");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6">
        <Title level={1} className="flex items-center gap-3">
          <SettingOutlined />
          Settings
        </Title>
        <Text type="secondary">
          Manage your account preferences and settings
        </Text>
      </div>

      <Row gutter={[24, 24]}>
        {/* Notification Settings */}
        <Col xs={24} lg={12}>
          <Card title="Notification Settings" icon={<BellOutlined />}>
            <Form
              form={notificationForm}
              layout="vertical"
              initialValues={notificationSettings}
              onFinish={onNotificationFinish}
            >
              <div className="space-y-4">
                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Email Notifications</Text>
                    <br />
                    <Text type="secondary">Receive updates via email</Text>
                  </div>
                  <Form.Item
                    name="emailNotifications"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Campaign Updates</Text>
                    <br />
                    <Text type="secondary">
                      Get notified about campaign progress
                    </Text>
                  </div>
                  <Form.Item
                    name="campaignUpdates"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Donation Alerts</Text>
                    <br />
                    <Text type="secondary">
                      Notifications when you receive donations
                    </Text>
                  </div>
                  <Form.Item
                    name="donationAlerts"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Weekly Reports</Text>
                    <br />
                    <Text type="secondary">
                      Weekly summary of your activity
                    </Text>
                  </div>
                  <Form.Item
                    name="weeklyReports"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Marketing Emails</Text>
                    <br />
                    <Text type="secondary">Receive promotional content</Text>
                  </div>
                  <Form.Item
                    name="marketingEmails"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Mobile Push Notifications</Text>
                    <br />
                    <Text type="secondary">
                      Push notifications on mobile devices
                    </Text>
                  </div>
                  <Form.Item
                    name="mobilePushNotifications"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>
              </div>

              <div className="mt-6">
                <Button type="primary" htmlType="submit" loading={loading}>
                  Save Notification Settings
                </Button>
              </div>
            </Form>
          </Card>
        </Col>

        {/* Privacy Settings */}
        <Col xs={24} lg={12}>
          <Card title="Privacy Settings" icon={<EyeInvisibleOutlined />}>
            <Form
              form={privacyForm}
              layout="vertical"
              initialValues={privacySettings}
              onFinish={onPrivacyFinish}
            >
              <Form.Item
                name="profileVisibility"
                label="Profile Visibility"
                help="Control who can see your profile information"
              >
                <Select>
                  <Option value="public">Public - Anyone can see</Option>
                  <Option value="donors-only">
                    Donors Only - Only people who donated
                  </Option>
                  <Option value="private">Private - Only you can see</Option>
                </Select>
              </Form.Item>

              <div className="space-y-4">
                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Show Donation History</Text>
                    <br />
                    <Text type="secondary">
                      Display your donation history publicly
                    </Text>
                  </div>
                  <Form.Item
                    name="showDonationHistory"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Show Campaign Activity</Text>
                    <br />
                    <Text type="secondary">
                      Display campaigns you've supported
                    </Text>
                  </div>
                  <Form.Item
                    name="showCampaignActivity"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Allow Contact from Organizers</Text>
                    <br />
                    <Text type="secondary">
                      Let campaign organizers contact you
                    </Text>
                  </div>
                  <Form.Item
                    name="allowContactFromOrganizers"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>
              </div>

              <div className="mt-6">
                <Button type="primary" htmlType="submit" loading={loading}>
                  Save Privacy Settings
                </Button>
              </div>
            </Form>
          </Card>
        </Col>

        {/* Security Settings */}
        <Col xs={24} lg={12}>
          <Card title="Security Settings" icon={<SafetyOutlined />}>
            <Form
              form={securityForm}
              layout="vertical"
              initialValues={securitySettings}
              onFinish={onSecurityFinish}
            >
              <div className="space-y-4">
                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Two-Factor Authentication</Text>
                    <br />
                    <Text type="secondary">
                      Add extra security to your account
                    </Text>
                  </div>
                  <Form.Item
                    name="twoFactorEnabled"
                    valuePropName="checked"
                    noStyle
                  >
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <Form.Item
                  name="sessionTimeout"
                  label="Session Timeout (minutes)"
                  help="How long to stay logged in when inactive"
                >
                  <Slider
                    min={5}
                    max={120}
                    marks={{
                      5: "5m",
                      30: "30m",
                      60: "1h",
                      120: "2h",
                    }}
                  />
                </Form.Item>

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Login Alerts</Text>
                    <br />
                    <Text type="secondary">
                      Get notified of new login attempts
                    </Text>
                  </div>
                  <Form.Item name="loginAlerts" valuePropName="checked" noStyle>
                    <Switch />
                  </Form.Item>
                </div>
              </div>

              <div className="mt-6 space-y-3">
                <Button
                  type="primary"
                  htmlType="submit"
                  loading={loading}
                  block
                >
                  Save Security Settings
                </Button>
                <Button
                  icon={<KeyOutlined />}
                  onClick={() => setPasswordModalVisible(true)}
                  block
                >
                  Change Password
                </Button>
              </div>
            </Form>
          </Card>
        </Col>

        {/* Account Management */}
        <Col xs={24} lg={12}>
          <Card title="Account Management" icon={<UserOutlined />}>
            <div className="space-y-4">
              <div>
                <Text strong>Account Information</Text>
                <div className="mt-2 space-y-2">
                  <div className="flex justify-between">
                    <Text>Account Type:</Text>
                    <Text strong>
                      {currentUser?.isAdmin ? "Administrator" : "Standard User"}
                    </Text>
                  </div>
                  <div className="flex justify-between">
                    <Text>Account Status:</Text>
                    <Text
                      strong
                      className={
                        currentUser?.isActive
                          ? "text-green-600"
                          : "text-red-600"
                      }
                    >
                      {currentUser?.isActive ? "Active" : "Inactive"}
                    </Text>
                  </div>
                  <div className="flex justify-between">
                    <Text>Member Since:</Text>
                    <Text strong>September 2024</Text>
                  </div>
                </div>
              </div>

              <Divider />

              <div>
                <Text strong>Data Management</Text>
                <div className="mt-3 space-y-3">
                  <Button
                    icon={<ExportOutlined />}
                    onClick={handleDataExport}
                    loading={loading}
                    block
                  >
                    Export My Data
                  </Button>
                  <Alert
                    message="Data Export"
                    description="Download all your personal data including profile, donations, and campaign activity."
                    type="info"
                    showIcon
                  />
                </div>
              </div>

              <Divider />

              <div>
                <Text strong className="text-red-600">
                  Danger Zone
                </Text>
                <div className="mt-3">
                  <Button
                    danger
                    icon={<DeleteOutlined />}
                    onClick={() => setDeleteModalVisible(true)}
                    block
                  >
                    Delete Account
                  </Button>
                  <Alert
                    className="mt-2"
                    message="Warning"
                    description="This action cannot be undone. All your data will be permanently deleted."
                    type="warning"
                    showIcon
                  />
                </div>
              </div>
            </div>
          </Card>
        </Col>
      </Row>

      {/* Password Change Modal */}
      <Modal
        title="Change Password"
        open={passwordModalVisible}
        onCancel={() => setPasswordModalVisible(false)}
        footer={null}
      >
        <Form
          form={passwordForm}
          layout="vertical"
          onFinish={handlePasswordChange}
        >
          <Form.Item
            name="currentPassword"
            label="Current Password"
            rules={[
              { required: true, message: "Please enter your current password" },
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item
            name="newPassword"
            label="New Password"
            rules={[
              { required: true, message: "Please enter a new password" },
              { min: 8, message: "Password must be at least 8 characters" },
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item
            name="confirmPassword"
            label="Confirm New Password"
            rules={[
              { required: true, message: "Please confirm your new password" },
              ({ getFieldValue }) => ({
                validator(_, value) {
                  if (!value || getFieldValue("newPassword") === value) {
                    return Promise.resolve();
                  }
                  return Promise.reject(new Error("Passwords do not match"));
                },
              }),
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item>
            <Space>
              <Button type="primary" htmlType="submit" loading={loading}>
                Change Password
              </Button>
              <Button onClick={() => setPasswordModalVisible(false)}>
                Cancel
              </Button>
            </Space>
          </Form.Item>
        </Form>
      </Modal>

      {/* Delete Account Modal */}
      <Modal
        title="Delete Account"
        open={deleteModalVisible}
        onCancel={() => setDeleteModalVisible(false)}
        onOk={handleAccountDeletion}
        okText="Delete Account"
        okType="danger"
        confirmLoading={loading}
      >
        <Alert
          message="This action cannot be undone"
          description="Are you sure you want to permanently delete your account? All your data, campaigns, and donation history will be lost forever."
          type="error"
          showIcon
          className="mb-4"
        />
        <Text>
          Type <Text strong>DELETE</Text> to confirm:
        </Text>
        <Input placeholder="Type DELETE to confirm" className="mt-2" />
      </Modal>
    </div>
  );
}

export default SettingsPage;
