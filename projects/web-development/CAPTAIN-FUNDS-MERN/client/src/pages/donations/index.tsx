import {
  Typography,
  Card,
  Table,
  Button,
  Tag,
  Space,
  Statistic,
  Row,
  Col,
  Modal,
  Form,
  Input,
  Select,
  Switch,
  message,
  Tabs,
  Tooltip,
  Empty,
} from "antd";
import {
  DollarOutlined,
  PlusOutlined,
  EyeOutlined,
  DownloadOutlined,
  HeartOutlined,
  CreditCardOutlined,
  ReloadOutlined,
  StopOutlined,
} from "@ant-design/icons";
import { useState, useEffect } from "react";
import userStore from "../../store/users-store";
import donationService from "../../services/donationService";
import type { Donation } from "../../interfaces/index";

const { Title, Text } = Typography;
const { Option } = Select;
const { TextArea } = Input;

interface DonationStats {
  totalDonations: number;
  totalAmount: number;
  averageDonation: number;
  monthlyTotal: number;
  successfulDonations: number;
  pendingDonations: number;
}

interface RecurringDonation {
  id: string;
  campaignId: string;
  campaignTitle: string;
  amount: number;
  frequency: "weekly" | "monthly" | "quarterly" | "yearly";
  nextDonationDate: Date;
  isActive: boolean;
}

function DonationsPage() {
  const [loading, setLoading] = useState(false);
  const [donations, setDonations] = useState<Donation[]>([]);
  const [recurringDonations, setRecurringDonations] = useState<
    RecurringDonation[]
  >([]);
  const [donationStats, setDonationStats] = useState<DonationStats>({
    totalDonations: 0,
    totalAmount: 0,
    averageDonation: 0,
    monthlyTotal: 0,
    successfulDonations: 0,
    pendingDonations: 0,
  });

  const [donateModalVisible, setDonateModalVisible] = useState(false);
  const [recurringModalVisible, setRecurringModalVisible] = useState(false);
  const [selectedCampaign, setSelectedCampaign] = useState<any>(null);
  const [activeTab, setActiveTab] = useState("1");

  const [donateForm] = Form.useForm();
  const [recurringForm] = Form.useForm();

  useEffect(() => {
    fetchDonations();
    fetchRecurringDonations();
    fetchDonationStats();
  }, []);

  const fetchDonations = async () => {
    try {
      setLoading(true);
      const userDonations = await donationService.getUserDonations();
      setDonations(userDonations);
    } catch (error) {
      console.error("Error fetching donations:", error);
      message.error("Failed to fetch donations");
    } finally {
      setLoading(false);
    }
  };

  const fetchRecurringDonations = async () => {
    try {
      const recurring = await donationService.getRecurringDonations();
      setRecurringDonations(recurring);
    } catch (error) {
      console.error("Error fetching recurring donations:", error);
    }
  };

  const fetchDonationStats = async () => {
    try {
      const stats = await donationService.getDonationStats();
      setDonationStats({
        totalDonations: stats.totalDonations,
        totalAmount: stats.totalAmount,
        averageDonation: stats.averageDonation,
        monthlyTotal: stats.monthlyTotal || 0,
        successfulDonations: stats.totalDonations, // Assume all are successful for now
        pendingDonations: 0,
      });
    } catch (error) {
      console.error("Error fetching donation stats:", error);
      // Fallback to calculating from donations array
      setDonationStats({
        totalDonations: donations.length,
        totalAmount: donations.reduce((sum, d) => sum + d.amount, 0),
        averageDonation:
          donations.length > 0
            ? donations.reduce((sum, d) => sum + d.amount, 0) / donations.length
            : 0,
        monthlyTotal: donations
          .filter((d) => {
            const donationDate = new Date(d.createdAt || "");
            const currentMonth = new Date().getMonth();
            return donationDate.getMonth() === currentMonth;
          })
          .reduce((sum, d) => sum + d.amount, 0),
        successfulDonations: donations.filter(
          (d) => d.paymentStatus === "completed"
        ).length,
        pendingDonations: donations.filter((d) => d.paymentStatus === "pending")
          .length,
      });
    }
  };

  const handleDonate = async (values: any) => {
    try {
      setLoading(true);

      // Create payment intent
      const paymentIntent = await donationService.createPaymentIntent(
        selectedCampaign.id,
        values.amount
      );

      // Process donation
      await donationService.processDonation({
        campaignId: selectedCampaign.id,
        amount: values.amount,
        message: values.message,
        isAnonymous: values.isAnonymous || false,
        paymentMethod: values.paymentMethod,
        paymentIntentId: paymentIntent.id,
      });

      message.success("Donation processed successfully!");
      setDonateModalVisible(false);
      donateForm.resetFields();
      fetchDonations();
      fetchDonationStats();
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to process donation"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleRecurringDonation = async (values: any) => {
    try {
      setLoading(true);

      await donationService.createRecurringDonation({
        campaignId: selectedCampaign.id,
        amount: values.amount,
        frequency: values.frequency,
        paymentMethodId: values.paymentMethodId,
      });

      message.success("Recurring donation set up successfully!");
      setRecurringModalVisible(false);
      recurringForm.resetFields();
      fetchRecurringDonations();
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to set up recurring donation"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadReceipt = async (donationId: string) => {
    try {
      const blob = await donationService.downloadReceipt(donationId);
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = `receipt-${donationId}.pdf`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
      message.success("Receipt downloaded successfully");
    } catch (error) {
      message.error("Failed to download receipt");
    }
  };

  const handleCancelRecurring = async (recurringId: string) => {
    try {
      await donationService.cancelRecurringDonation(recurringId);
      message.success("Recurring donation canceled successfully");
      fetchRecurringDonations();
    } catch (error) {
      message.error("Failed to cancel recurring donation");
    }
  };

  const donationColumns = [
    {
      title: "Campaign",
      dataIndex: "campaignTitle",
      key: "campaignTitle",
      render: (title: string, record: Donation) => (
        <div>
          <div className="font-medium">{title}</div>
          <div className="text-sm text-gray-500">
            {new Date(record.createdAt || "").toLocaleDateString()}
          </div>
        </div>
      ),
    },
    {
      title: "Amount",
      dataIndex: "amount",
      key: "amount",
      render: (amount: number, record: Donation) => (
        <div>
          <div className="font-semibold text-green-600">
            ${amount.toFixed(2)}
          </div>
          {record.processingFee > 0 && (
            <div className="text-xs text-gray-500">
              Fee: ${record.processingFee.toFixed(2)}
            </div>
          )}
        </div>
      ),
    },
    {
      title: "Payment Method",
      dataIndex: "paymentMethod",
      key: "paymentMethod",
      render: (method: string) => {
        const methodMap: Record<string, { label: string; color: string }> = {
          credit_card: { label: "Credit Card", color: "blue" },
          paypal: { label: "PayPal", color: "gold" },
          bank_transfer: { label: "Bank Transfer", color: "green" },
          crypto: { label: "Cryptocurrency", color: "purple" },
        };
        const methodInfo = methodMap[method] || {
          label: method,
          color: "default",
        };
        return <Tag color={methodInfo.color}>{methodInfo.label}</Tag>;
      },
    },
    {
      title: "Status",
      dataIndex: "paymentStatus",
      key: "paymentStatus",
      render: (status: string) => {
        const statusMap: Record<string, { color: string; label: string }> = {
          pending: { color: "orange", label: "Pending" },
          completed: { color: "green", label: "Completed" },
          failed: { color: "red", label: "Failed" },
          refunded: { color: "purple", label: "Refunded" },
        };
        const statusInfo = statusMap[status] || {
          color: "default",
          label: status,
        };
        return <Tag color={statusInfo.color}>{statusInfo.label}</Tag>;
      },
    },
    {
      title: "Actions",
      key: "actions",
      render: (record: Donation) => (
        <Space>
          <Tooltip title="View Details">
            <Button size="small" icon={<EyeOutlined />} />
          </Tooltip>
          {record.paymentStatus === "completed" && (
            <Tooltip title="Download Receipt">
              <Button
                size="small"
                icon={<DownloadOutlined />}
                onClick={() => handleDownloadReceipt(record._id!)}
              />
            </Tooltip>
          )}
        </Space>
      ),
    },
  ];

  const recurringColumns = [
    {
      title: "Campaign",
      dataIndex: "campaignTitle",
      key: "campaignTitle",
    },
    {
      title: "Amount",
      dataIndex: "amount",
      key: "amount",
      render: (amount: number) => (
        <span className="font-semibold text-green-600">
          ${amount.toFixed(2)}
        </span>
      ),
    },
    {
      title: "Frequency",
      dataIndex: "frequency",
      key: "frequency",
      render: (frequency: string) => (
        <Tag color="blue">
          {frequency.charAt(0).toUpperCase() + frequency.slice(1)}
        </Tag>
      ),
    },
    {
      title: "Next Donation",
      dataIndex: "nextDonationDate",
      key: "nextDonationDate",
      render: (date: Date) => new Date(date).toLocaleDateString(),
    },
    {
      title: "Status",
      dataIndex: "isActive",
      key: "isActive",
      render: (isActive: boolean) => (
        <Tag color={isActive ? "green" : "red"}>
          {isActive ? "Active" : "Inactive"}
        </Tag>
      ),
    },
    {
      title: "Actions",
      key: "actions",
      render: (record: RecurringDonation) => (
        <Space>
          <Button size="small" icon={<EyeOutlined />}>
            View
          </Button>
          <Button
            size="small"
            danger
            icon={<StopOutlined />}
            onClick={() => handleCancelRecurring(record.id)}
          >
            Cancel
          </Button>
        </Space>
      ),
    },
  ];

  // Mock campaigns for donation modal
  const mockCampaigns = [
    {
      id: "1",
      title: "Help for Education",
      targetAmount: 10000,
      currentAmount: 2500,
    },
    {
      id: "2",
      title: "Medical Emergency Fund",
      targetAmount: 5000,
      currentAmount: 1200,
    },
    {
      id: "3",
      title: "Community Development",
      targetAmount: 15000,
      currentAmount: 8750,
    },
  ];

  const tabItems = [
    {
      key: "1",
      label: "My Donations",
      children: (
        <Table
          columns={donationColumns}
          dataSource={donations}
          loading={loading}
          rowKey="_id"
          pagination={{
            pageSize: 10,
            showSizeChanger: true,
            showQuickJumper: true,
            showTotal: (total, range) =>
              `${range[0]}-${range[1]} of ${total} donations`,
          }}
        />
      ),
    },
    {
      key: "2",
      label: "Recurring Donations",
      children: (
        <div>
          <div className="mb-4 flex justify-between items-center">
            <Text type="secondary">
              Manage your recurring donations and set up new ones
            </Text>
            <Button
              type="primary"
              icon={<ReloadOutlined />}
              onClick={() => setRecurringModalVisible(true)}
            >
              Set Up Recurring Donation
            </Button>
          </div>
          <Table
            columns={recurringColumns}
            dataSource={recurringDonations}
            rowKey="id"
            pagination={false}
            locale={{
              emptyText: (
                <Empty
                  description="No recurring donations set up"
                  image={Empty.PRESENTED_IMAGE_SIMPLE}
                />
              ),
            }}
          />
        </div>
      ),
    },
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <div>
          <Title level={1} className="flex items-center gap-3">
            <DollarOutlined />
            Donations
          </Title>
          <Text type="secondary">
            Track and manage your personal donation history
          </Text>
        </div>
        <Space>
          <Button
            type="primary"
            icon={<PlusOutlined />}
            size="large"
            onClick={() => setDonateModalVisible(true)}
          >
            Make Donation
          </Button>
        </Space>
      </div>

      {/* Statistics Cards */}
      <Row gutter={[16, 16]} className="mb-6">
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Total Donations"
              value={donationStats.totalDonations}
              prefix={<HeartOutlined />}
              valueStyle={{ color: "#1890ff" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Total Amount"
              value={donationStats.totalAmount}
              prefix="$"
              precision={2}
              valueStyle={{ color: "#3f8600" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Average Donation"
              value={donationStats.averageDonation}
              prefix="$"
              precision={2}
              valueStyle={{ color: "#722ed1" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="This Month"
              value={donationStats.monthlyTotal}
              prefix="$"
              precision={2}
              valueStyle={{ color: "#f5222d" }}
            />
          </Card>
        </Col>
      </Row>

      {/* Donation Tabs */}
      <Card>
        <Tabs activeKey={activeTab} onChange={setActiveTab} items={tabItems} />
      </Card>

      {/* Donation Modal */}
      <Modal
        title="Make a Donation"
        open={donateModalVisible}
        onCancel={() => setDonateModalVisible(false)}
        footer={null}
        width={600}
      >
        <Form form={donateForm} layout="vertical" onFinish={handleDonate}>
          <Form.Item
            name="campaignId"
            label="Select Campaign"
            rules={[{ required: true, message: "Please select a campaign" }]}
          >
            <Select
              placeholder="Choose a campaign to support"
              onChange={(value) => {
                const campaign = mockCampaigns.find((c) => c.id === value);
                setSelectedCampaign(campaign);
              }}
            >
              {mockCampaigns.map((campaign) => (
                <Option key={campaign.id} value={campaign.id}>
                  <div>
                    <div className="font-medium">{campaign.title}</div>
                    <div className="text-sm text-gray-500">
                      ${campaign.currentAmount.toLocaleString()} / $
                      {campaign.targetAmount.toLocaleString()} raised
                    </div>
                  </div>
                </Option>
              ))}
            </Select>
          </Form.Item>

          <Row gutter={16}>
            <Col span={12}>
              <Form.Item
                name="amount"
                label="Donation Amount"
                rules={[
                  { required: true, message: "Please enter an amount" },
                  { type: "number", min: 1, message: "Minimum donation is $1" },
                ]}
              >
                <Input
                  type="number"
                  prefix="$"
                  placeholder="0.00"
                  min={1}
                  step={0.01}
                />
              </Form.Item>
            </Col>
            <Col span={12}>
              <Form.Item
                name="paymentMethod"
                label="Payment Method"
                rules={[
                  { required: true, message: "Please select payment method" },
                ]}
              >
                <Select placeholder="Select payment method">
                  <Option value="credit_card">
                    <CreditCardOutlined /> Credit Card
                  </Option>
                  <Option value="paypal">PayPal</Option>
                  <Option value="bank_transfer">Bank Transfer</Option>
                  <Option value="crypto">Cryptocurrency</Option>
                </Select>
              </Form.Item>
            </Col>
          </Row>

          <Form.Item name="message" label="Message (Optional)">
            <TextArea
              rows={3}
              placeholder="Leave a message of support..."
              maxLength={500}
              showCount
            />
          </Form.Item>

          <Form.Item name="isAnonymous" valuePropName="checked">
            <Switch /> Make this donation anonymous
          </Form.Item>

          <Form.Item>
            <Space>
              <Button type="primary" htmlType="submit" loading={loading}>
                Donate Now
              </Button>
              <Button onClick={() => setDonateModalVisible(false)}>
                Cancel
              </Button>
            </Space>
          </Form.Item>
        </Form>
      </Modal>

      {/* Recurring Donation Modal */}
      <Modal
        title="Set Up Recurring Donation"
        open={recurringModalVisible}
        onCancel={() => setRecurringModalVisible(false)}
        footer={null}
        width={600}
      >
        <Form
          form={recurringForm}
          layout="vertical"
          onFinish={handleRecurringDonation}
        >
          <Form.Item
            name="campaignId"
            label="Select Campaign"
            rules={[{ required: true, message: "Please select a campaign" }]}
          >
            <Select
              placeholder="Choose a campaign to support"
              onChange={(value) => {
                const campaign = mockCampaigns.find((c) => c.id === value);
                setSelectedCampaign(campaign);
              }}
            >
              {mockCampaigns.map((campaign) => (
                <Option key={campaign.id} value={campaign.id}>
                  {campaign.title}
                </Option>
              ))}
            </Select>
          </Form.Item>

          <Row gutter={16}>
            <Col span={12}>
              <Form.Item
                name="amount"
                label="Donation Amount"
                rules={[
                  { required: true, message: "Please enter an amount" },
                  { type: "number", min: 1, message: "Minimum donation is $1" },
                ]}
              >
                <Input
                  type="number"
                  prefix="$"
                  placeholder="0.00"
                  min={1}
                  step={0.01}
                />
              </Form.Item>
            </Col>
            <Col span={12}>
              <Form.Item
                name="frequency"
                label="Frequency"
                rules={[{ required: true, message: "Please select frequency" }]}
              >
                <Select placeholder="Select frequency">
                  <Option value="weekly">Weekly</Option>
                  <Option value="monthly">Monthly</Option>
                  <Option value="quarterly">Quarterly</Option>
                  <Option value="yearly">Yearly</Option>
                </Select>
              </Form.Item>
            </Col>
          </Row>

          <Form.Item
            name="paymentMethodId"
            label="Payment Method"
            rules={[
              { required: true, message: "Please select payment method" },
            ]}
          >
            <Select placeholder="Select saved payment method">
              <Option value="card_123">**** **** **** 1234 (Visa)</Option>
              <Option value="card_567">**** **** **** 5678 (MasterCard)</Option>
            </Select>
          </Form.Item>

          <Form.Item>
            <Space>
              <Button type="primary" htmlType="submit" loading={loading}>
                Set Up Recurring Donation
              </Button>
              <Button onClick={() => setRecurringModalVisible(false)}>
                Cancel
              </Button>
            </Space>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
}

export default DonationsPage;
