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
  Progress,
  Tooltip,
  Modal,
  message,
  Popconfirm,
} from "antd";
import {
  FundOutlined,
  PlusOutlined,
  EditOutlined,
  DeleteOutlined,
  EyeOutlined,
  CheckCircleOutlined,
  CloseCircleOutlined,
  StarOutlined,
} from "@ant-design/icons";
import { useState } from "react";
import type { Campaign } from "../../../interfaces/index";
import CampaignForm from "../../../components/CampaignForm";
import campaignService from "../../../services/campaignService";

const { Title, Text } = Typography;

function AdminCampaignManagement() {
  const [campaigns, setCampaigns] = useState<Campaign[]>(() => {
    // Sample campaigns matching backend model - replace with real API data
    return [
      {
        _id: "1",
        title: "Help for Education",
        description:
          "Supporting underprivileged children with educational resources and school supplies for a better future.",
        organizer: "Education Foundation",
        image: "/api/placeholder/400/300",
        EventTargetAmount: 10000,
        EventCurrentAmount: 6500,
        status: "active",
        EventCategory: "Education",
        location: "New York, NY",
        endDate: new Date("2024-12-15"),
        isActive: true,
        isApproved: true,
        isFeatured: true,
        isDeleted: false,
        isRejected: false,
        isArchived: false,
      },
      {
        _id: "2",
        title: "Medical Emergency Fund",
        description:
          "Urgent medical assistance for families in need of critical healthcare support.",
        organizer: "Healthcare Heroes",
        image: "/api/placeholder/400/300",
        EventTargetAmount: 25000,
        EventCurrentAmount: 8750,
        status: "active",
        EventCategory: "Healthcare",
        location: "Los Angeles, CA",
        endDate: new Date("2024-11-30"),
        isActive: true,
        isApproved: false,
        isFeatured: false,
        isDeleted: false,
        isRejected: false,
        isArchived: false,
      },
      {
        _id: "3",
        title: "Community Garden Project",
        description:
          "Creating sustainable community gardens to promote healthy living and environmental awareness.",
        organizer: "Green Community Initiative",
        image: "/api/placeholder/400/300",
        EventTargetAmount: 15000,
        EventCurrentAmount: 12300,
        status: "active",
        EventCategory: "Environment",
        location: "Portland, OR",
        endDate: new Date("2024-10-20"),
        isActive: true,
        isApproved: true,
        isFeatured: false,
        isDeleted: false,
        isRejected: false,
        isArchived: false,
      },
    ];
  });

  const [loading, setLoading] = useState(false);
  const [formModalVisible, setFormModalVisible] = useState(false);
  const [selectedCampaign, setSelectedCampaign] = useState<Campaign | null>(
    null
  );
  const [formMode, setFormMode] = useState<"create" | "edit">("create");

  const handleCreateCampaign = () => {
    setSelectedCampaign(null);
    setFormMode("create");
    setFormModalVisible(true);
  };

  const handleEditCampaign = (campaign: Campaign) => {
    setSelectedCampaign(campaign);
    setFormMode("edit");
    setFormModalVisible(true);
  };

  const handleDeleteCampaign = async (campaignId: string) => {
    try {
      setLoading(true);
      await campaignService.deleteCampaign(campaignId);
      setCampaigns(campaigns.filter((c) => c._id !== campaignId));
      message.success("Campaign deleted successfully");
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to delete campaign"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleToggleApproval = async (
    campaignId: string,
    isApproved: boolean
  ) => {
    try {
      setLoading(true);
      if (isApproved) {
        await campaignService.approveCampaign(campaignId);
      } else {
        await campaignService.rejectCampaign(campaignId);
      }

      setCampaigns(
        campaigns.map((c) => (c._id === campaignId ? { ...c, isApproved } : c))
      );

      message.success(
        `Campaign ${isApproved ? "approved" : "rejected"} successfully`
      );
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to update campaign"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleToggleFeatured = async (campaignId: string) => {
    try {
      setLoading(true);
      await campaignService.toggleFeatured(campaignId);

      setCampaigns(
        campaigns.map((c) =>
          c._id === campaignId ? { ...c, isFeatured: !c.isFeatured } : c
        )
      );

      message.success("Campaign featured status updated");
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to update campaign"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleFormSubmit = async (values: any) => {
    try {
      setLoading(true);

      if (formMode === "create") {
        const newCampaign = await campaignService.createCampaign(values);
        setCampaigns([...campaigns, newCampaign]);
        message.success("Campaign created successfully");
      } else if (selectedCampaign) {
        const updatedCampaign = await campaignService.updateCampaign(
          selectedCampaign._id!,
          values
        );
        setCampaigns(
          campaigns.map((c) =>
            c._id === selectedCampaign._id ? updatedCampaign : c
          )
        );
        message.success("Campaign updated successfully");
      }

      setFormModalVisible(false);
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || `Failed to ${formMode} campaign`
      );
    } finally {
      setLoading(false);
    }
  };

  const columns = [
    {
      title: "Campaign",
      dataIndex: "title",
      key: "title",
      width: 250,
      render: (title: string, record: Campaign) => (
        <div>
          <div className="font-medium text-gray-900">{title}</div>
          <div className="text-sm text-gray-500 mt-1">
            by {record.organizer}
          </div>
        </div>
      ),
    },
    {
      title: "Progress",
      key: "progress",
      width: 200,
      render: (_, record: Campaign) => {
        const percentage = Math.round(
          (record.EventCurrentAmount / record.EventTargetAmount) * 100
        );
        return (
          <div>
            <div className="flex justify-between text-sm mb-1">
              <span className="font-medium text-green-600">
                ${record.EventCurrentAmount.toLocaleString()}
              </span>
              <span className="text-gray-500">
                ${record.EventTargetAmount.toLocaleString()}
              </span>
            </div>
            <Progress
              percent={percentage}
              size="small"
              strokeColor="#52c41a"
              showInfo={false}
            />
            <div className="text-xs text-gray-500 mt-1">
              {percentage}% funded
            </div>
          </div>
        );
      },
    },
    {
      title: "Category",
      dataIndex: "EventCategory",
      key: "EventCategory",
      width: 120,
      render: (category: string) => <Tag color="blue">{category}</Tag>,
    },
    {
      title: "Location",
      dataIndex: "location",
      key: "location",
      width: 150,
    },
    {
      title: "Status",
      dataIndex: "status",
      key: "status",
      width: 120,
      render: (status: string, record: Campaign) => {
        let color = "default";
        let text = status;

        if (record.isApproved) {
          color = "green";
          text = "Approved";
        } else if (record.isRejected) {
          color = "red";
          text = "Rejected";
        } else {
          color = "orange";
          text = "Pending";
        }

        return (
          <div>
            <Tag color={color}>{text}</Tag>
            {record.isFeatured && <Tag color="gold">Featured</Tag>}
          </div>
        );
      },
    },
    {
      title: "End Date",
      dataIndex: "endDate",
      key: "endDate",
      width: 120,
      render: (date: Date) => new Date(date).toLocaleDateString(),
    },
    {
      title: "Actions",
      key: "actions",
      width: 200,
      render: (_, record: Campaign) => (
        <Space>
          <Tooltip title="View Details">
            <Button size="small" icon={<EyeOutlined />} />
          </Tooltip>
          <Tooltip title="Edit Campaign">
            <Button
              size="small"
              icon={<EditOutlined />}
              onClick={() => handleEditCampaign(record)}
            />
          </Tooltip>
          <Tooltip
            title={record.isApproved ? "Reject Campaign" : "Approve Campaign"}
          >
            <Button
              size="small"
              type={record.isApproved ? "default" : "primary"}
              icon={
                record.isApproved ? (
                  <CloseCircleOutlined />
                ) : (
                  <CheckCircleOutlined />
                )
              }
              onClick={() =>
                handleToggleApproval(record._id!, !record.isApproved)
              }
            />
          </Tooltip>
          <Tooltip
            title={
              record.isFeatured ? "Remove from Featured" : "Mark as Featured"
            }
          >
            <Button
              size="small"
              type={record.isFeatured ? "primary" : "default"}
              icon={<StarOutlined />}
              onClick={() => handleToggleFeatured(record._id!)}
            />
          </Tooltip>
          <Popconfirm
            title="Are you sure you want to delete this campaign?"
            description="This action cannot be undone."
            onConfirm={() => handleDeleteCampaign(record._id!)}
            okText="Yes, Delete"
            cancelText="Cancel"
          >
            <Tooltip title="Delete Campaign">
              <Button size="small" danger icon={<DeleteOutlined />} />
            </Tooltip>
          </Popconfirm>
        </Space>
      ),
    },
  ];

  // Calculate statistics
  const totalCampaigns = campaigns.length;
  const activeCampaigns = campaigns.filter((c) => c.status === "active").length;
  const totalRaised = campaigns.reduce(
    (sum, campaign) => sum + campaign.EventCurrentAmount,
    0
  );
  const totalGoal = campaigns.reduce(
    (sum, campaign) => sum + campaign.EventTargetAmount,
    0
  );
  const approvedCampaigns = campaigns.filter((c) => c.isApproved).length;
  const featuredCampaigns = campaigns.filter((c) => c.isFeatured).length;

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <div>
          <Title level={1} className="flex items-center gap-3">
            <FundOutlined />
            Campaign Management
          </Title>
          <Text type="secondary">
            Create, manage, and monitor all fundraising campaigns
          </Text>
        </div>
        <Button
          type="primary"
          icon={<PlusOutlined />}
          size="large"
          onClick={handleCreateCampaign}
        >
          Create Campaign
        </Button>
      </div>

      {/* Statistics Cards */}
      <Row gutter={[16, 16]} className="mb-6">
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Total Campaigns"
              value={totalCampaigns}
              prefix={<FundOutlined />}
              valueStyle={{ color: "#1890ff" }}
            />
            <div className="mt-2">
              <Text type="secondary">{activeCampaigns} active</Text>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Total Raised"
              value={totalRaised}
              prefix="$"
              precision={0}
              valueStyle={{ color: "#3f8600" }}
            />
            <div className="mt-2">
              <Text type="secondary">
                of ${totalGoal.toLocaleString()} goal
              </Text>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Approved"
              value={approvedCampaigns}
              valueStyle={{ color: "#52c41a" }}
            />
            <div className="mt-2">
              <Text type="secondary">
                {Math.round((approvedCampaigns / totalCampaigns) * 100)}%
                approval rate
              </Text>
            </div>
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Featured"
              value={featuredCampaigns}
              valueStyle={{ color: "#722ed1" }}
            />
            <div className="mt-2">
              <Text type="secondary">prominently displayed</Text>
            </div>
          </Card>
        </Col>
      </Row>

      {/* Campaigns Table */}
      <Card title="All Campaigns">
        <Table
          columns={columns}
          dataSource={campaigns}
          rowKey="_id"
          loading={loading}
          scroll={{ x: 1200 }}
          pagination={{
            pageSize: 10,
            showSizeChanger: true,
            showQuickJumper: true,
            showTotal: (total, range) =>
              `${range[0]}-${range[1]} of ${total} campaigns`,
          }}
        />
      </Card>

      {/* Campaign Form Modal */}
      <Modal
        title={`${formMode === "create" ? "Create New" : "Edit"} Campaign`}
        open={formModalVisible}
        onCancel={() => setFormModalVisible(false)}
        footer={null}
        width={1200}
        className="campaign-form-modal"
        destroyOnClose
      >
        <CampaignForm
          mode={formMode}
          initialValues={selectedCampaign || undefined}
          onSubmit={handleFormSubmit}
          onCancel={() => setFormModalVisible(false)}
          loading={loading}
        />
      </Modal>
    </div>
  );
}

export default AdminCampaignManagement;
