import {
  Form,
  Input,
  InputNumber,
  Select,
  DatePicker,
  Upload,
  Button,
  Card,
  Row,
  Col,
  Switch,
  message,
  Typography,
  Divider,
  Tag,
  Progress,
} from "antd";
import {
  PlusOutlined,
  UploadOutlined,
  SaveOutlined,
  EyeOutlined,
  DeleteOutlined,
} from "@ant-design/icons";
import { useState } from "react";
import axios from "axios";
import type { Campaign } from "../interfaces/index";

const { Title, Text } = Typography;
const { Option } = Select;
const { TextArea } = Input;

interface CampaignFormProps {
  initialValues?: Partial<Campaign>;
  onSubmit: (values: any) => Promise<void>;
  onCancel?: () => void;
  loading?: boolean;
  mode?: "create" | "edit";
}

const CampaignForm: React.FC<CampaignFormProps> = ({
  initialValues,
  onSubmit,
  onCancel,
  loading = false,
  mode = "create",
}) => {
  const [form] = Form.useForm();
  const [imageList, setImageList] = useState<any[]>([]);
  const [previewVisible, setPreviewVisible] = useState(false);
  const [previewImage, setPreviewImage] = useState("");

  const categories = [
    "Education",
    "Healthcare",
    "Environment",
    "Community Development",
    "Emergency Relief",
    "Arts & Culture",
    "Sports & Recreation",
    "Technology",
    "Animal Welfare",
    "Human Rights",
    "Religious",
    "Other",
  ];

  const handleImageUpload = async (file: File) => {
    const formData = new FormData();
    formData.append("image", file);

    try {
      const token = localStorage.getItem("token");
      const response = await axios.post(
        "/api/upload/campaign-image",
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        }
      );

      return response.data.imageUrl;
    } catch (error) {
      message.error("Failed to upload image");
      throw error;
    }
  };

  const uploadProps = {
    beforeUpload: (file: File) => {
      const isImage = file.type.startsWith("image/");
      if (!isImage) {
        message.error("You can only upload image files!");
        return false;
      }

      const isLt5M = file.size / 1024 / 1024 < 5;
      if (!isLt5M) {
        message.error("Image must be smaller than 5MB!");
        return false;
      }

      return false; // Prevent auto upload
    },
    onChange: ({ fileList }) => setImageList(fileList),
    onPreview: (file) => {
      setPreviewImage(file.url || file.thumbUrl);
      setPreviewVisible(true);
    },
    listType: "picture-card" as const,
    maxCount: 1,
  };

  const handleFinish = async (values: any) => {
    try {
      // Upload image if present
      if (imageList.length > 0 && imageList[0].originFileObj) {
        const imageUrl = await handleImageUpload(imageList[0].originFileObj);
        values.image = imageUrl;
      }

      // Format the data to match backend model
      const campaignData = {
        ...values,
        EventTargetAmount: values.targetAmount,
        EventCurrentAmount: values.currentAmount || 0,
        EventCategory: values.category,
        endDate: values.endDate.toISOString(),
        isActive: values.isActive ?? true,
        isApproved: values.isApproved ?? false,
        isFeatured: values.isFeatured ?? false,
      };

      await onSubmit(campaignData);
      form.resetFields();
      setImageList([]);
    } catch (error) {
      console.error("Error submitting campaign:", error);
    }
  };

  const handlePreview = () => {
    const values = form.getFieldsValue();
    const progressPercent =
      values.currentAmount && values.targetAmount
        ? Math.round((values.currentAmount / values.targetAmount) * 100)
        : 0;

    return (
      <Card title="Campaign Preview" className="mt-6">
        <div className="bg-gradient-to-r from-blue-400 to-purple-500 h-48 flex items-center justify-center mb-4 rounded">
          {imageList.length > 0 ? (
            <img
              src={imageList[0].thumbUrl}
              alt="Campaign"
              className="w-full h-full object-cover rounded"
            />
          ) : (
            <div className="text-white text-center">
              <UploadOutlined className="text-4xl mb-2" />
              <div>Campaign Image Preview</div>
            </div>
          )}
        </div>

        <Title level={4}>{values.title || "Campaign Title"}</Title>
        <Text type="secondary" className="block mb-2">
          <strong>Organizer:</strong> {values.organizer || "Organizer Name"}
        </Text>
        <Text type="secondary" className="block mb-2">
          <strong>Category:</strong> {values.category || "Category"} •{" "}
          <strong>Location:</strong> {values.location || "Location"}
        </Text>
        <Text type="secondary" className="block mb-4">
          {values.description || "Campaign description will appear here..."}
        </Text>

        {values.targetAmount && (
          <div className="mb-4">
            <div className="flex justify-between mb-2">
              <Text strong>
                ${(values.currentAmount || 0).toLocaleString()} raised
              </Text>
              <Text type="secondary">
                of ${values.targetAmount.toLocaleString()} goal
              </Text>
            </div>
            <Progress percent={progressPercent} strokeColor="#52c41a" />
          </div>
        )}

        <div className="flex gap-2">
          {values.category && <Tag color="blue">{values.category}</Tag>}
          {values.location && <Tag color="green">{values.location}</Tag>}
          {values.isFeatured && <Tag color="gold">Featured</Tag>}
          {values.isApproved && <Tag color="green">Approved</Tag>}
        </div>
      </Card>
    );
  };

  return (
    <div>
      <Form
        form={form}
        layout="vertical"
        initialValues={initialValues}
        onFinish={handleFinish}
        className="campaign-form"
      >
        <Row gutter={[24, 0]}>
          {/* Left Column - Basic Information */}
          <Col xs={24} lg={12}>
            <Card title="Basic Information" className="h-full">
              <Form.Item
                name="title"
                label="Campaign Title"
                rules={[
                  { required: true, message: "Please enter campaign title" },
                  { min: 10, message: "Title must be at least 10 characters" },
                  { max: 100, message: "Title must not exceed 100 characters" },
                ]}
              >
                <Input placeholder="Enter compelling campaign title" />
              </Form.Item>

              <Form.Item
                name="description"
                label="Description"
                rules={[
                  {
                    required: true,
                    message: "Please enter campaign description",
                  },
                  {
                    min: 50,
                    message: "Description must be at least 50 characters",
                  },
                  {
                    max: 2000,
                    message: "Description must not exceed 2000 characters",
                  },
                ]}
              >
                <TextArea
                  rows={6}
                  placeholder="Describe your campaign, its goals, and why it matters..."
                  showCount
                  maxLength={2000}
                />
              </Form.Item>

              <Row gutter={16}>
                <Col span={12}>
                  <Form.Item
                    name="organizer"
                    label="Organizer"
                    rules={[
                      {
                        required: true,
                        message: "Please enter organizer name",
                      },
                    ]}
                  >
                    <Input placeholder="Organization or person name" />
                  </Form.Item>
                </Col>
                <Col span={12}>
                  <Form.Item
                    name="category"
                    label="Category"
                    rules={[
                      { required: true, message: "Please select a category" },
                    ]}
                  >
                    <Select placeholder="Select campaign category">
                      {categories.map((category) => (
                        <Option key={category} value={category}>
                          {category}
                        </Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
              </Row>

              <Form.Item
                name="location"
                label="Location"
                rules={[{ required: true, message: "Please enter location" }]}
              >
                <Input placeholder="City, State, Country" />
              </Form.Item>
            </Card>
          </Col>

          {/* Right Column - Financial & Settings */}
          <Col xs={24} lg={12}>
            <Card title="Financial Information" className="mb-6">
              <Row gutter={16}>
                <Col span={12}>
                  <Form.Item
                    name="targetAmount"
                    label="Target Amount ($)"
                    rules={[
                      { required: true, message: "Please enter target amount" },
                      {
                        type: "number",
                        min: 100,
                        message: "Minimum target is $100",
                      },
                    ]}
                  >
                    <InputNumber
                      className="w-full"
                      placeholder="0.00"
                      min={100}
                      step={100}
                      formatter={(value) =>
                        `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ",")
                      }
                      parser={(value) => value!.replace(/\$\s?|(,*)/g, "")}
                    />
                  </Form.Item>
                </Col>
                <Col span={12}>
                  <Form.Item
                    name="currentAmount"
                    label="Current Amount ($)"
                    help="Leave blank for new campaigns"
                  >
                    <InputNumber
                      className="w-full"
                      placeholder="0.00"
                      min={0}
                      step={10}
                      formatter={(value) =>
                        `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ",")
                      }
                      parser={(value) => value!.replace(/\$\s?|(,*)/g, "")}
                    />
                  </Form.Item>
                </Col>
              </Row>

              <Form.Item
                name="endDate"
                label="End Date"
                rules={[{ required: true, message: "Please select end date" }]}
              >
                <DatePicker
                  className="w-full"
                  placeholder="Select campaign end date"
                  disabledDate={(current) => current && current < new Date()}
                />
              </Form.Item>
            </Card>

            <Card title="Campaign Settings">
              <div className="space-y-4">
                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Active Campaign</Text>
                    <br />
                    <Text type="secondary">
                      Campaign is accepting donations
                    </Text>
                  </div>
                  <Form.Item name="isActive" valuePropName="checked" noStyle>
                    <Switch defaultChecked />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Featured Campaign</Text>
                    <br />
                    <Text type="secondary">
                      Display prominently on homepage
                    </Text>
                  </div>
                  <Form.Item name="isFeatured" valuePropName="checked" noStyle>
                    <Switch />
                  </Form.Item>
                </div>

                <Divider />

                <div className="flex justify-between items-center">
                  <div>
                    <Text strong>Approved</Text>
                    <br />
                    <Text type="secondary">
                      Campaign is approved for public viewing
                    </Text>
                  </div>
                  <Form.Item name="isApproved" valuePropName="checked" noStyle>
                    <Switch />
                  </Form.Item>
                </div>
              </div>
            </Card>
          </Col>
        </Row>

        {/* Image Upload Section */}
        <Card title="Campaign Image" className="mt-6">
          <Form.Item
            name="image"
            label="Upload Campaign Image"
            help="Upload a compelling image that represents your campaign. Recommended size: 1200x600px, Max size: 5MB"
          >
            <Upload {...uploadProps}>
              {imageList.length >= 1 ? null : (
                <div>
                  <PlusOutlined />
                  <div style={{ marginTop: 8 }}>Upload Image</div>
                </div>
              )}
            </Upload>
          </Form.Item>
        </Card>

        {/* Preview Section */}
        {handlePreview()}

        {/* Action Buttons */}
        <Card className="mt-6">
          <div className="flex justify-between">
            <Button
              type="default"
              icon={<EyeOutlined />}
              onClick={() => setPreviewVisible(true)}
            >
              Preview Campaign
            </Button>

            <div className="space-x-3">
              {onCancel && <Button onClick={onCancel}>Cancel</Button>}
              <Button
                type="primary"
                htmlType="submit"
                loading={loading}
                icon={<SaveOutlined />}
                size="large"
              >
                {mode === "create" ? "Create Campaign" : "Update Campaign"}
              </Button>
            </div>
          </div>
        </Card>
      </Form>
    </div>
  );
};

export default CampaignForm;
