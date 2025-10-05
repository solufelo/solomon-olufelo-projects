import {
  Modal,
  Form,
  Input,
  Button,
  Select,
  Switch,
  Row,
  Col,
  Space,
  Typography,
  Progress,
  message,
  Card,
  Divider,
  Tag,
} from "antd";
import {
  HeartOutlined,
  CreditCardOutlined,
  LockOutlined,
  GiftOutlined,
} from "@ant-design/icons";
import { useState } from "react";
import donationService from "../services/donationService";
import type { Campaign } from "../interfaces/index";

const { Title, Text } = Typography;
const { Option } = Select;
const { TextArea } = Input;

interface DonationModalProps {
  visible: boolean;
  onCancel: () => void;
  campaign: Campaign | null;
  onSuccess?: () => void;
}

const DonationModal: React.FC<DonationModalProps> = ({
  visible,
  onCancel,
  campaign,
  onSuccess,
}) => {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  const [selectedAmount, setSelectedAmount] = useState<number | null>(null);

  const quickAmounts = [25, 50, 100, 250, 500, 1000];

  const handleDonate = async (values: any) => {
    if (!campaign) return;

    try {
      setLoading(true);

      // For now, we'll use the direct donation endpoint
      // In a production app, you would integrate with Stripe/PayPal here
      const response = await donationService.processDirectDonation({
        campaignId: campaign._id!,
        amount: values.amount,
        message: values.message,
        isAnonymous: values.isAnonymous || false,
        paymentMethod: values.paymentMethod,
      });

      message.success("Thank you for your generous donation! 🎉");
      form.resetFields();
      onCancel();
      onSuccess?.();
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to process donation"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleQuickAmount = (amount: number) => {
    setSelectedAmount(amount);
    form.setFieldsValue({ amount });
  };

  const progressPercent = campaign
    ? Math.round(
        (campaign.EventCurrentAmount / campaign.EventTargetAmount) * 100
      )
    : 0;

  const remainingAmount = campaign
    ? campaign.EventTargetAmount - campaign.EventCurrentAmount
    : 0;

  return (
    <Modal
      title={null}
      open={visible}
      onCancel={onCancel}
      footer={null}
      width={700}
      className="donation-modal"
    >
      {campaign && (
        <div>
          {/* Campaign Header */}
          <div className="mb-6">
            <div className="flex items-center gap-3 mb-4">
              <HeartOutlined className="text-red-500 text-2xl" />
              <Title level={3} className="mb-0">
                Support {campaign.title}
              </Title>
            </div>

            <Card className="bg-gray-50 border-0">
              <div className="mb-4">
                <div className="flex justify-between items-center mb-2">
                  <Text strong>
                    ${campaign.EventCurrentAmount.toLocaleString()} raised
                  </Text>
                  <Text type="secondary">
                    of ${campaign.EventTargetAmount.toLocaleString()} goal
                  </Text>
                </div>
                <Progress
                  percent={progressPercent}
                  strokeColor="#52c41a"
                  className="mb-2"
                />
                <div className="flex justify-between text-sm">
                  <Text type="secondary">
                    ${remainingAmount.toLocaleString()} remaining
                  </Text>
                  <Text type="secondary">
                    {Math.max(
                      0,
                      Math.floor(
                        (new Date(campaign.endDate).getTime() - Date.now()) /
                          (1000 * 60 * 60 * 24)
                      )
                    )}{" "}
                    days left
                  </Text>
                </div>
              </div>

              <div className="flex gap-2 flex-wrap">
                <Tag color="blue">{campaign.EventCategory}</Tag>
                <Tag color="green">{campaign.location}</Tag>
                <Tag color="purple">{campaign.organizer}</Tag>
              </div>
            </Card>
          </div>

          <Divider />

          {/* Donation Form */}
          <Form
            form={form}
            layout="vertical"
            onFinish={handleDonate}
            initialValues={{
              isAnonymous: false,
              paymentMethod: "credit_card",
            }}
          >
            {/* Quick Amount Selection */}
            <Form.Item label="Select Amount">
              <div className="grid grid-cols-3 gap-3 mb-4">
                {quickAmounts.map((amount) => (
                  <Button
                    key={amount}
                    type={selectedAmount === amount ? "primary" : "default"}
                    onClick={() => handleQuickAmount(amount)}
                    className="h-12 text-lg font-medium"
                  >
                    ${amount}
                  </Button>
                ))}
              </div>
            </Form.Item>

            {/* Custom Amount */}
            <Row gutter={16}>
              <Col span={12}>
                <Form.Item
                  name="amount"
                  label="Custom Amount"
                  rules={[
                    { required: true, message: "Please enter an amount" },
                    {
                      type: "number",
                      min: 1,
                      message: "Minimum donation is $1",
                    },
                  ]}
                >
                  <Input
                    type="number"
                    prefix="$"
                    placeholder="Enter custom amount"
                    min={1}
                    step={0.01}
                    size="large"
                    onChange={(e) => {
                      const value = parseFloat(e.target.value);
                      setSelectedAmount(isNaN(value) ? null : value);
                    }}
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
                  <Select placeholder="Select payment method" size="large">
                    <Option value="credit_card">
                      <Space>
                        <CreditCardOutlined />
                        Credit Card
                      </Space>
                    </Option>
                    <Option value="paypal">PayPal</Option>
                    <Option value="bank_transfer">Bank Transfer</Option>
                    <Option value="crypto">Cryptocurrency</Option>
                  </Select>
                </Form.Item>
              </Col>
            </Row>

            {/* Message */}
            <Form.Item name="message" label="Leave a Message (Optional)">
              <TextArea
                rows={3}
                placeholder="Share why this cause matters to you..."
                maxLength={500}
                showCount
              />
            </Form.Item>

            {/* Anonymous Option */}
            <Form.Item name="isAnonymous" valuePropName="checked">
              <Space>
                <Switch />
                <Text>Make this donation anonymous</Text>
              </Space>
            </Form.Item>

            {/* Security Notice */}
            <Card className="bg-blue-50 border-blue-200 mb-6">
              <div className="flex items-center gap-2">
                <LockOutlined className="text-blue-600" />
                <Text className="text-blue-800">
                  Your payment information is secure and encrypted. We never
                  store your payment details.
                </Text>
              </div>
            </Card>

            {/* Action Buttons */}
            <Form.Item>
              <Space className="w-full justify-end">
                <Button onClick={onCancel} size="large">
                  Cancel
                </Button>
                <Button
                  type="primary"
                  htmlType="submit"
                  loading={loading}
                  size="large"
                  icon={<GiftOutlined />}
                  className="bg-green-500 border-green-500 hover:bg-green-600"
                >
                  Donate Now
                </Button>
              </Space>
            </Form.Item>
          </Form>
        </div>
      )}
    </Modal>
  );
};

export default DonationModal;
