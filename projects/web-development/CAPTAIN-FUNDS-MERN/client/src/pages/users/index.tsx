import {
  Typography,
  Card,
  Table,
  Button,
  Tag,
  Space,
  Avatar,
  Modal,
  Form,
  Input,
  Switch,
  message,
  Popconfirm,
  Statistic,
  Row,
  Col,
  Select,
  DatePicker,
  Tooltip,
} from "antd";
import {
  TeamOutlined,
  EditOutlined,
  DeleteOutlined,
  UserAddOutlined,
  UserOutlined,
  MailOutlined,
  LockOutlined,
  EyeOutlined,
  SearchOutlined,
  FilterOutlined,
} from "@ant-design/icons";
import { useState, useEffect } from "react";
import axios from "axios";
import userStore from "../../store/users-store";

const { Title, Text } = Typography;
const { Option } = Select;

interface User {
  _id: string;
  name: string;
  email: string;
  isAdmin: boolean;
  isActive: boolean;
  timeStamp: string;
  phone?: string;
  location?: string;
  bio?: string;
  profileImage?: string;
  lastLogin?: string;
  totalDonations?: number;
  totalCampaigns?: number;
}

interface UserStats {
  totalUsers: number;
  activeUsers: number;
  adminUsers: number;
  newUsersThisMonth: number;
}

function UsersPage() {
  const { currentUser } = userStore();
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [editingUser, setEditingUser] = useState<User | null>(null);
  const [userStats, setUserStats] = useState<UserStats>({
    totalUsers: 0,
    activeUsers: 0,
    adminUsers: 0,
    newUsersThisMonth: 0,
  });
  const [searchTerm, setSearchTerm] = useState("");
  const [filterRole, setFilterRole] = useState<string>("all");
  const [filterStatus, setFilterStatus] = useState<string>("all");

  const [form] = Form.useForm();

  const fetchUsers = async () => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");
      const response = await axios.get("/api/users", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Mock enhanced user data with additional fields
      const enhancedUsers =
        response.data.users?.map((user: User, index: number) => ({
          ...user,
          phone: user.phone || `+1-555-${1000 + index}`,
          location:
            user.location ||
            ["New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX"][
              index % 4
            ],
          lastLogin:
            user.lastLogin ||
            new Date(
              Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000
            ).toISOString(),
          totalDonations: Math.floor(Math.random() * 20),
          totalCampaigns: Math.floor(Math.random() * 5),
        })) || [];

      setUsers(enhancedUsers);

      // Calculate stats
      const stats = {
        totalUsers: enhancedUsers.length,
        activeUsers: enhancedUsers.filter((u: User) => u.isActive).length,
        adminUsers: enhancedUsers.filter((u: User) => u.isAdmin).length,
        newUsersThisMonth: enhancedUsers.filter((u: User) => {
          const userDate = new Date(u.timeStamp);
          const currentDate = new Date();
          return (
            userDate.getMonth() === currentDate.getMonth() &&
            userDate.getFullYear() === currentDate.getFullYear()
          );
        }).length,
      };
      setUserStats(stats);
    } catch (error) {
      console.error("Failed to fetch users:", error);
      message.error("Failed to fetch users");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (currentUser?.isAdmin) {
      fetchUsers();
    }
  }, [currentUser]);

  const handleCreateUser = () => {
    setEditingUser(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEditUser = (user: User) => {
    setEditingUser(user);
    form.setFieldsValue({
      name: user.name,
      email: user.email,
      phone: user.phone,
      location: user.location,
      bio: user.bio,
      isAdmin: user.isAdmin,
      isActive: user.isActive,
    });
    setModalVisible(true);
  };

  const handleDeleteUser = async (userId: string) => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");
      await axios.delete(`/api/users/${userId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setUsers(users.filter((u) => u._id !== userId));
      message.success("User deleted successfully");
    } catch (error: any) {
      message.error(error?.response?.data?.message || "Failed to delete user");
    } finally {
      setLoading(false);
    }
  };

  const handleToggleUserStatus = async (userId: string, isActive: boolean) => {
    try {
      const token = localStorage.getItem("token");
      await axios.patch(
        `/api/users/${userId}/status`,
        { isActive },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setUsers(users.map((u) => (u._id === userId ? { ...u, isActive } : u)));

      message.success(
        `User ${isActive ? "activated" : "deactivated"} successfully`
      );
    } catch (error: any) {
      message.error(
        error?.response?.data?.message || "Failed to update user status"
      );
    }
  };

  const handleSubmit = async (values: any) => {
    try {
      setLoading(true);
      const token = localStorage.getItem("token");

      if (editingUser) {
        // Update existing user
        const response = await axios.put(
          `/api/users/${editingUser._id}`,
          values,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        setUsers(
          users.map((u) =>
            u._id === editingUser._id ? { ...u, ...response.data.user } : u
          )
        );

        message.success("User updated successfully");
      } else {
        // Create new user
        const response = await axios.post("/api/users/create", values, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setUsers([response.data.user, ...users]);
        message.success("User created successfully");
      }

      setModalVisible(false);
      form.resetFields();
    } catch (error: any) {
      message.error(
        error?.response?.data?.message ||
          `Failed to ${editingUser ? "update" : "create"} user`
      );
    } finally {
      setLoading(false);
    }
  };

  // Filter users based on search and filters
  const filteredUsers = users.filter((user) => {
    const matchesSearch =
      user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.email.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesRole =
      filterRole === "all" ||
      (filterRole === "admin" && user.isAdmin) ||
      (filterRole === "user" && !user.isAdmin);
    const matchesStatus =
      filterStatus === "all" ||
      (filterStatus === "active" && user.isActive) ||
      (filterStatus === "inactive" && !user.isActive);

    return matchesSearch && matchesRole && matchesStatus;
  });

  const columns = [
    {
      title: "User",
      dataIndex: "name",
      key: "name",
      width: 250,
      render: (name: string, record: User) => (
        <div className="flex items-center gap-3">
          <Avatar size={40} src={record.profileImage} icon={<UserOutlined />} />
          <div>
            <div className="font-medium">{name}</div>
            <div className="text-sm text-gray-500">{record.email}</div>
            {record.phone && (
              <div className="text-xs text-gray-400">{record.phone}</div>
            )}
          </div>
        </div>
      ),
    },
    {
      title: "Role & Status",
      key: "roleStatus",
      width: 150,
      render: (record: User) => (
        <div className="space-y-1">
          <Tag color={record.isAdmin ? "red" : "blue"}>
            {record.isAdmin ? "Admin" : "User"}
          </Tag>
          <br />
          <Tag color={record.isActive ? "green" : "red"}>
            {record.isActive ? "Active" : "Inactive"}
          </Tag>
        </div>
      ),
    },
    {
      title: "Location",
      dataIndex: "location",
      key: "location",
      width: 150,
      render: (location: string) => (
        <Text type="secondary">{location || "Not specified"}</Text>
      ),
    },
    {
      title: "Activity",
      key: "activity",
      width: 120,
      render: (record: User) => (
        <div className="text-center">
          <div className="text-sm font-medium">
            {record.totalDonations || 0}
          </div>
          <div className="text-xs text-gray-500">Donations</div>
          <div className="text-sm font-medium">
            {record.totalCampaigns || 0}
          </div>
          <div className="text-xs text-gray-500">Campaigns</div>
        </div>
      ),
    },
    {
      title: "Last Login",
      dataIndex: "lastLogin",
      key: "lastLogin",
      width: 120,
      render: (lastLogin: string) => (
        <Text type="secondary">
          {lastLogin ? new Date(lastLogin).toLocaleDateString() : "Never"}
        </Text>
      ),
    },
    {
      title: "Joined",
      dataIndex: "timeStamp",
      key: "timeStamp",
      width: 120,
      render: (timeStamp: string) => (
        <Text type="secondary">{new Date(timeStamp).toLocaleDateString()}</Text>
      ),
    },
    {
      title: "Actions",
      key: "actions",
      width: 200,
      fixed: "right" as const,
      render: (record: User) => (
        <Space>
          <Tooltip title="View Details">
            <Button size="small" icon={<EyeOutlined />} />
          </Tooltip>
          <Tooltip title="Edit User">
            <Button
              size="small"
              icon={<EditOutlined />}
              onClick={() => handleEditUser(record)}
            />
          </Tooltip>
          <Tooltip title={record.isActive ? "Deactivate" : "Activate"}>
            <Button
              size="small"
              type={record.isActive ? "default" : "primary"}
              onClick={() =>
                handleToggleUserStatus(record._id, !record.isActive)
              }
            >
              {record.isActive ? "Deactivate" : "Activate"}
            </Button>
          </Tooltip>
          {record._id !== currentUser?._id && (
            <Popconfirm
              title="Are you sure you want to delete this user?"
              description="This action cannot be undone."
              onConfirm={() => handleDeleteUser(record._id)}
              okText="Yes, Delete"
              cancelText="Cancel"
            >
              <Tooltip title="Delete User">
                <Button size="small" danger icon={<DeleteOutlined />} />
              </Tooltip>
            </Popconfirm>
          )}
        </Space>
      ),
    },
  ];

  // Redirect non-admin users
  if (!currentUser?.isAdmin) {
    return (
      <div className="container mx-auto px-4 py-8 text-center">
        <Title level={2}>Access Denied</Title>
        <Text type="secondary">
          You don't have permission to access this page.
        </Text>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <div>
          <Title level={1} className="flex items-center gap-3">
            <TeamOutlined />
            User Management
          </Title>
          <Text type="secondary">Manage system users and permissions</Text>
        </div>
        <Button
          type="primary"
          icon={<UserAddOutlined />}
          size="large"
          onClick={handleCreateUser}
        >
          Add User
        </Button>
      </div>

      {/* Statistics Cards */}
      <Row gutter={[16, 16]} className="mb-6">
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Total Users"
              value={userStats.totalUsers}
              prefix={<TeamOutlined />}
              valueStyle={{ color: "#1890ff" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Active Users"
              value={userStats.activeUsers}
              valueStyle={{ color: "#52c41a" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Administrators"
              value={userStats.adminUsers}
              valueStyle={{ color: "#f5222d" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="New This Month"
              value={userStats.newUsersThisMonth}
              valueStyle={{ color: "#722ed1" }}
            />
          </Card>
        </Col>
      </Row>

      {/* Filters */}
      <Card className="mb-6">
        <Row gutter={[16, 16]} align="middle">
          <Col xs={24} sm={8}>
            <Input
              placeholder="Search users..."
              prefix={<SearchOutlined />}
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              allowClear
            />
          </Col>
          <Col xs={24} sm={4}>
            <Select
              placeholder="Role"
              value={filterRole}
              onChange={setFilterRole}
              className="w-full"
            >
              <Option value="all">All Roles</Option>
              <Option value="admin">Admins</Option>
              <Option value="user">Users</Option>
            </Select>
          </Col>
          <Col xs={24} sm={4}>
            <Select
              placeholder="Status"
              value={filterStatus}
              onChange={setFilterStatus}
              className="w-full"
            >
              <Option value="all">All Status</Option>
              <Option value="active">Active</Option>
              <Option value="inactive">Inactive</Option>
            </Select>
          </Col>
          <Col xs={24} sm={8}>
            <Text type="secondary">
              Showing {filteredUsers.length} of {users.length} users
            </Text>
          </Col>
        </Row>
      </Card>

      {/* Users Table */}
      <Card>
        <Table
          columns={columns}
          dataSource={filteredUsers}
          loading={loading}
          rowKey="_id"
          scroll={{ x: 1200 }}
          pagination={{
            pageSize: 10,
            showSizeChanger: true,
            showQuickJumper: true,
            showTotal: (total, range) =>
              `${range[0]}-${range[1]} of ${total} users`,
          }}
        />
      </Card>

      {/* User Form Modal */}
      <Modal
        title={editingUser ? "Edit User" : "Create New User"}
        open={modalVisible}
        onCancel={() => setModalVisible(false)}
        footer={null}
        width={600}
      >
        <Form form={form} layout="vertical" onFinish={handleSubmit}>
          <Row gutter={16}>
            <Col span={12}>
              <Form.Item
                name="name"
                label="Full Name"
                rules={[{ required: true, message: "Please enter full name" }]}
              >
                <Input
                  prefix={<UserOutlined />}
                  placeholder="Enter full name"
                />
              </Form.Item>
            </Col>
            <Col span={12}>
              <Form.Item
                name="email"
                label="Email Address"
                rules={[
                  { required: true, message: "Please enter email" },
                  { type: "email", message: "Please enter valid email" },
                ]}
              >
                <Input prefix={<MailOutlined />} placeholder="Enter email" />
              </Form.Item>
            </Col>
          </Row>

          <Row gutter={16}>
            <Col span={12}>
              <Form.Item name="phone" label="Phone Number">
                <Input placeholder="Enter phone number" />
              </Form.Item>
            </Col>
            <Col span={12}>
              <Form.Item name="location" label="Location">
                <Input placeholder="Enter location" />
              </Form.Item>
            </Col>
          </Row>

          {!editingUser && (
            <Form.Item
              name="password"
              label="Password"
              rules={[
                { required: true, message: "Please enter password" },
                { min: 6, message: "Password must be at least 6 characters" },
              ]}
            >
              <Input.Password
                prefix={<LockOutlined />}
                placeholder="Enter password"
              />
            </Form.Item>
          )}

          <Form.Item name="bio" label="Bio">
            <Input.TextArea
              rows={3}
              placeholder="Enter user bio..."
              maxLength={500}
              showCount
            />
          </Form.Item>

          <Row gutter={16}>
            <Col span={12}>
              <Form.Item name="isAdmin" valuePropName="checked">
                <div className="flex items-center gap-2">
                  <Switch />
                  <span>Administrator privileges</span>
                </div>
              </Form.Item>
            </Col>
            <Col span={12}>
              <Form.Item
                name="isActive"
                valuePropName="checked"
                initialValue={true}
              >
                <div className="flex items-center gap-2">
                  <Switch defaultChecked />
                  <span>Account active</span>
                </div>
              </Form.Item>
            </Col>
          </Row>

          <Form.Item>
            <Space>
              <Button type="primary" htmlType="submit" loading={loading}>
                {editingUser ? "Update User" : "Create User"}
              </Button>
              <Button onClick={() => setModalVisible(false)}>Cancel</Button>
            </Space>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
}

export default UsersPage;
