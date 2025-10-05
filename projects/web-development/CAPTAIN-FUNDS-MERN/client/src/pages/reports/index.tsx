import {
  Typography,
  Card,
  Row,
  Col,
  Statistic,
  Button,
  DatePicker,
  Select,
  Table,
} from "antd";
import {
  BarChartOutlined,
  DownloadOutlined,
  FilterOutlined,
  CalendarOutlined,
} from "@ant-design/icons";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const { Title, Text } = Typography;
const { RangePicker } = DatePicker;
const { Option } = Select;

interface ReportData {
  key: string;
  campaign: string;
  donations: number;
  amount: number;
  successRate: number;
  avgDonation: number;
}

function ReportsPage() {
  // Sample report data
  const reportData: ReportData[] = [
    {
      key: "1",
      campaign: "Education Fund",
      donations: 45,
      amount: 12500,
      successRate: 95,
      avgDonation: 277.78,
    },
    {
      key: "2",
      campaign: "Medical Emergency",
      donations: 32,
      amount: 8900,
      successRate: 88,
      avgDonation: 278.13,
    },
    {
      key: "3",
      campaign: "Community Development",
      donations: 28,
      amount: 15600,
      successRate: 92,
      avgDonation: 557.14,
    },
    {
      key: "4",
      campaign: "Environmental Project",
      donations: 19,
      amount: 4200,
      successRate: 85,
      avgDonation: 221.05,
    },
  ];

  const columns = [
    {
      title: "Campaign",
      dataIndex: "campaign",
      key: "campaign",
    },
    {
      title: "Total Donations",
      dataIndex: "donations",
      key: "donations",
      render: (donations: number) => (
        <span className="font-medium">{donations}</span>
      ),
    },
    {
      title: "Total Amount",
      dataIndex: "amount",
      key: "amount",
      render: (amount: number) => (
        <span className="font-semibold text-green-600">
          ${amount.toLocaleString()}
        </span>
      ),
    },
    {
      title: "Success Rate",
      dataIndex: "successRate",
      key: "successRate",
      render: (rate: number) => (
        <span
          className={
            rate >= 90
              ? "text-green-600"
              : rate >= 80
              ? "text-orange-600"
              : "text-red-600"
          }
        >
          {rate}%
        </span>
      ),
    },
    {
      title: "Avg Donation",
      dataIndex: "avgDonation",
      key: "avgDonation",
      render: (avg: number) => <span>${avg.toFixed(2)}</span>,
    },
  ];

  const totalAmount = reportData.reduce((sum, item) => sum + item.amount, 0);
  const totalDonations = reportData.reduce(
    (sum, item) => sum + item.donations,
    0
  );
  const avgSuccessRate =
    reportData.reduce((sum, item) => sum + item.successRate, 0) /
    reportData.length;

  // Chart Components
  const DonationTrendsChart = () => {
    const trendData = [
      { month: "Jan", donations: 4500, campaigns: 8 },
      { month: "Feb", donations: 5200, campaigns: 12 },
      { month: "Mar", donations: 4800, campaigns: 10 },
      { month: "Apr", donations: 6100, campaigns: 15 },
      { month: "May", donations: 7300, campaigns: 18 },
      { month: "Jun", donations: 8500, campaigns: 22 },
    ];

    return (
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={trendData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="donations"
            stroke="#8884d8"
            strokeWidth={2}
          />
          <Line
            type="monotone"
            dataKey="campaigns"
            stroke="#82ca9d"
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    );
  };

  const CampaignComparisonChart = () => {
    return (
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={reportData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="campaign" angle={-45} textAnchor="end" height={80} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="amount" fill="#8884d8" />
          <Bar dataKey="donations" fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
    );
  };

  const CategoryPieChart = () => {
    const categoryData = [
      { name: "Education", value: 35, color: "#0088FE" },
      { name: "Healthcare", value: 25, color: "#00C49F" },
      { name: "Environment", value: 20, color: "#FFBB28" },
      { name: "Community", value: 20, color: "#FF8042" },
    ];

    return (
      <ResponsiveContainer width="100%" height={250}>
        <PieChart>
          <Pie
            data={categoryData}
            cx="50%"
            cy="50%"
            labelLine={false}
            label={({ name, percent }) =>
              `${name} ${(percent * 100).toFixed(0)}%`
            }
            outerRadius={80}
            fill="#8884d8"
            dataKey="value"
          >
            {categoryData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.color} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    );
  };

  const MonthlyPerformanceChart = () => {
    const performanceData = [
      { month: "Jan", target: 10000, raised: 8500, success: 85 },
      { month: "Feb", target: 12000, raised: 11200, success: 93 },
      { month: "Mar", target: 15000, raised: 12800, success: 85 },
      { month: "Apr", target: 18000, raised: 16200, success: 90 },
      { month: "May", target: 20000, raised: 17500, success: 88 },
      { month: "Jun", target: 22000, raised: 20100, success: 91 },
    ];

    return (
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={performanceData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="target" fill="#ffbb28" name="Target" />
          <Bar dataKey="raised" fill="#82ca9d" name="Raised" />
        </BarChart>
      </ResponsiveContainer>
    );
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <div>
          <Title level={1} className="flex items-center gap-3">
            <BarChartOutlined />
            Reports
          </Title>
          <Text type="secondary">
            Analytics and insights for your fundraising activities
          </Text>
        </div>
        <Button type="primary" icon={<DownloadOutlined />} size="large">
          Export Report
        </Button>
      </div>

      {/* Filters */}
      <Card className="mb-6">
        <Row gutter={[16, 16]} align="middle">
          <Col xs={24} sm={8}>
            <div>
              <Text strong>Date Range:</Text>
              <RangePicker className="w-full mt-1" />
            </div>
          </Col>
          <Col xs={24} sm={8}>
            <div>
              <Text strong>Campaign:</Text>
              <Select placeholder="All Campaigns" className="w-full mt-1">
                <Option value="all">All Campaigns</Option>
                <Option value="education">Education Fund</Option>
                <Option value="medical">Medical Emergency</Option>
                <Option value="community">Community Development</Option>
                <Option value="environmental">Environmental Project</Option>
              </Select>
            </div>
          </Col>
          <Col xs={24} sm={8}>
            <div>
              <Text strong>Report Type:</Text>
              <Select placeholder="Summary Report" className="w-full mt-1">
                <Option value="summary">Summary Report</Option>
                <Option value="detailed">Detailed Report</Option>
                <Option value="donor">Donor Analysis</Option>
              </Select>
            </div>
          </Col>
        </Row>
      </Card>

      {/* Summary Statistics */}
      <Row gutter={[16, 16]} className="mb-6">
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Total Raised"
              value={totalAmount}
              prefix="$"
              valueStyle={{ color: "#3f8600" }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic title="Total Donations" value={totalDonations} />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic
              title="Success Rate"
              value={avgSuccessRate}
              suffix="%"
              precision={1}
              valueStyle={{
                color: avgSuccessRate >= 90 ? "#3f8600" : "#cf1322",
              }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={6}>
          <Card>
            <Statistic title="Active Campaigns" value={reportData.length} />
          </Card>
        </Col>
      </Row>

      {/* Campaign Performance Table */}
      <Card
        title="Campaign Performance"
        extra={<Button icon={<FilterOutlined />}>Filter</Button>}
      >
        <Table
          columns={columns}
          dataSource={reportData}
          pagination={false}
          summary={(pageData) => {
            const totalAmount = pageData.reduce(
              (sum, item) => sum + item.amount,
              0
            );
            const totalDonations = pageData.reduce(
              (sum, item) => sum + item.donations,
              0
            );

            return (
              <Table.Summary.Row>
                <Table.Summary.Cell index={0}>
                  <strong>Total</strong>
                </Table.Summary.Cell>
                <Table.Summary.Cell index={1}>
                  <strong>{totalDonations}</strong>
                </Table.Summary.Cell>
                <Table.Summary.Cell index={2}>
                  <strong className="text-green-600">
                    ${totalAmount.toLocaleString()}
                  </strong>
                </Table.Summary.Cell>
                <Table.Summary.Cell index={3}>
                  <strong>{avgSuccessRate.toFixed(1)}%</strong>
                </Table.Summary.Cell>
                <Table.Summary.Cell index={4}>
                  <strong>${(totalAmount / totalDonations).toFixed(2)}</strong>
                </Table.Summary.Cell>
              </Table.Summary.Row>
            );
          }}
        />
      </Card>

      {/* Charts Section */}
      <Row gutter={[16, 16]} className="mt-6">
        <Col xs={24} lg={12}>
          <Card
            title="Donation Trends"
            extra={<Button icon={<CalendarOutlined />}>View Details</Button>}
          >
            <DonationTrendsChart />
          </Card>
        </Col>
        <Col xs={24} lg={12}>
          <Card
            title="Campaign Comparison"
            extra={<Button icon={<BarChartOutlined />}>View Details</Button>}
          >
            <CampaignComparisonChart />
          </Card>
        </Col>
      </Row>

      <Row gutter={[16, 16]} className="mt-6">
        <Col xs={24} lg={12}>
          <Card title="Category Distribution">
            <CategoryPieChart />
          </Card>
        </Col>
        <Col xs={24} lg={12}>
          <Card title="Monthly Performance">
            <MonthlyPerformanceChart />
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default ReportsPage;
