import React from 'react';
import { Link } from 'react-router-dom';
import { LoginForm } from 'wasp/client/auth';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
// Styles imported in App.tsx

const LoginPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-50 via-brand-50/30 to-neutral-100 flex items-center justify-center py-12 px-4">
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
          <div className="text-center">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-brand-500 to-brand-600 rounded-3xl shadow-glow mx-auto mb-4">
              <span className="text-white font-bold text-2xl">S</span>
            </div>
            <CardTitle className="text-3xl font-display">Sign in to StudyOS</CardTitle>
            <p className="text-neutral-600 text-center">
              Welcome back! Please sign in to your account.
            </p>
          </div>
        </CardHeader>
        <CardContent className="p-6 pt-0">
          <Link to="/signup" className="block text-center text-sm text-brand-600 hover:text-brand-700 mb-6">
            Don't have an account? Sign up
          </Link>
          <LoginForm />
        </CardContent>
      </Card>
    </div>
  );
};

export { LoginPage };
export default LoginPage;
