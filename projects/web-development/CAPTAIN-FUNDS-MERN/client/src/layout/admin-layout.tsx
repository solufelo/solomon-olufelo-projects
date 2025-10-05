import React from "react";
import { Typography } from "antd";
import userStore from "../store/users-store";

const { Title, Text } = Typography;

function AdminLayout({ children }: { children: React.ReactNode }) {
  const { currentUser } = userStore();

  // Redirect non-admin users
  if (!currentUser?.isAdmin) {
    return (
      <div className="container mx-auto px-4 py-8 text-center">
        <Title level={2}>Access Denied</Title>
        <Text type="secondary">
          You don't have permission to access this page. Admin access required.
        </Text>
      </div>
    );
  }

  return <>{children}</>;
}

export default AdminLayout;
