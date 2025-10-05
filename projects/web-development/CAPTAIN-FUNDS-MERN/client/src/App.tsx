"use client";

import "./index.css";
import RegisterPage from "./pages/auth/register";
import ThemeProvider from "./providers/theme-provider";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/auth/login/index";
import Homepage from "./pages/auth/private/index";
import CampaignsPage from "./pages/campaigns/index";
import AdminCampaignManagement from "./pages/admin/campaign-management/index";
import SettingsPage from "./pages/settings/index";
import UsersPage from "./pages/users/index";
import ProfilePage from "./pages/profile/index";
import DonationsPage from "./pages/donations/index";
import ReportsPage from "./pages/reports/index";
import PublicLayout from "./layout/public-layout";
import PrivateLayout from "./layout/private-layout";
import AdminLayout from "./layout/admin-layout";
import RealtimeDashboard from "./pages/dashboard/realtime-dashboard";

function App() {
  return (
    <ThemeProvider>
      <BrowserRouter>
        <Routes>
          {/* Public Routes */}
          <Route
            path="/login"
            element={
              <PublicLayout>
                <LoginPage />
              </PublicLayout>
            }
          />
          <Route
            path="/register"
            element={
              <PublicLayout>
                <RegisterPage />
              </PublicLayout>
            }
          />

          {/* Private Routes */}
          <Route
            path="/"
            element={
              <PrivateLayout>
                <Homepage />
              </PrivateLayout>
            }
          />
          <Route
            path="/profile"
            element={
              <PrivateLayout>
                <ProfilePage />
              </PrivateLayout>
            }
          />
          <Route
            path="/donations"
            element={
              <PrivateLayout>
                <DonationsPage />
              </PrivateLayout>
            }
          />
          <Route
            path="/reports"
            element={
              <PrivateLayout>
                <ReportsPage />
              </PrivateLayout>
            }
          />
          <Route
            path="/settings"
            element={
              <PrivateLayout>
                <SettingsPage />
              </PrivateLayout>
            }
          />

          <Route
            path="/campaigns"
            element={
              <PrivateLayout>
                <CampaignsPage />
              </PrivateLayout>
            }
          />
          <Route
            path="/dashboard/realtime"
            element={
              <PrivateLayout>
                <RealtimeDashboard />
              </PrivateLayout>
            }
          />

          {/* Admin Routes */}
          <Route
            path="/admin/campaigns"
            element={
              <PrivateLayout>
                <AdminLayout>
                  <AdminCampaignManagement />
                </AdminLayout>
              </PrivateLayout>
            }
          />
          <Route
            path="/users"
            element={
              <PrivateLayout>
                <AdminLayout>
                  <UsersPage />
                </AdminLayout>
              </PrivateLayout>
            }
          />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
