import { Button, App, Dropdown, Avatar } from "antd";
import {
  UserOutlined,
  LogoutOutlined,
  ProfileOutlined,
  DollarOutlined,
  BarChartOutlined,
  TeamOutlined,
  SettingOutlined,
  FundOutlined,
} from "@ant-design/icons";
import type { MenuProps } from "antd";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";
import userStore from "../store/users-store";

function Header() {
  const navigate = useNavigate();
  const { currentUser, clearUser } = userStore();
  const { message } = App.useApp();

  const handleLogout = () => {
    Cookies.remove("token");
    Cookies.remove("user");
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    clearUser();
    message.success("Logged out successfully");
    navigate("/login");
  };

  const handleNavigation = (path: string) => {
    navigate(path);
  };

  const getMenuItems = (): MenuProps["items"] => {
    const baseItems: MenuProps["items"] = [
      {
        key: "profile",
        label: "Profile",
        icon: <ProfileOutlined />,
        onClick: () => handleNavigation("/profile"),
      },
      {
        key: "donations",
        label: "Donations",
        icon: <DollarOutlined />,
        onClick: () => handleNavigation("/donations"),
      },
      {
        key: "campaigns",
        label: "Campaigns",
        icon: <FundOutlined />,
        onClick: () => handleNavigation("/campaigns"),
      },
      {
        key: "reports",
        label: "Reports",
        icon: <BarChartOutlined />,
        onClick: () => handleNavigation("/reports"),
      },
    ];

    // Admin-only items
    if (currentUser?.isAdmin) {
      baseItems.push({
        type: "divider",
      });
      baseItems.push({
        key: "admin-panel",
        label: "Admin Panel",
        icon: <SettingOutlined />,
        children: [
          {
            key: "user-management",
            label: "User Management",
            icon: <TeamOutlined />,
            onClick: () => handleNavigation("/users"),
          },
          {
            key: "campaign-management",
            label: "Campaign Management",
            icon: <DollarOutlined />,
            onClick: () => handleNavigation("/admin/campaigns"),
          },
          {
            key: "system-settings",
            label: "System Settings",
            icon: <SettingOutlined />,
            onClick: () => handleNavigation("/admin/settings"),
          },
        ],
      });
    }

    // Add logout
    baseItems.push(
      {
        type: "divider",
      },
      {
        key: "logout",
        label: "Logout",
        icon: <LogoutOutlined />,
        danger: true,
        onClick: handleLogout,
      }
    );

    return baseItems;
  };

  const userMenuProps: MenuProps = {
    items: getMenuItems(),
  };

  return (
    <div className="bg-primary flex justify-between items-center p-4">
      <h1
        className="text-white text-2xl font-bold cursor-pointer"
        onClick={() => navigate("/")}
      >
        CAPTAIN-FUNDS
      </h1>

      <Dropdown menu={userMenuProps} placement="bottomRight">
        <Button
          type="text"
          className="flex items-center gap-2 hover:bg-white/10 px-3 py-2 rounded-md"
          style={{
            backgroundColor: "white",
            color: "#1890ff",
            border: "1px solid #d9d9d9",
          }}
        >
          <Avatar size="small" icon={<UserOutlined />} />
          <span className="font-medium" style={{ color: "#1890ff" }}>
            {currentUser?.name || "User"}
          </span>
        </Button>
      </Dropdown>
    </div>
  );
}

export default Header;
