import React from 'react';
import { Link } from 'react-router-dom';
import { SignupForm } from 'wasp/client/auth';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import Button from '../components/ui/Button';
// Styles imported in App.tsx

const SignupPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-50 via-brand-50/30 to-neutral-100 flex items-center justify-center py-12 px-4">
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
          <div className="text-center">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-brand-500 to-brand-600 rounded-3xl shadow-glow mx-auto mb-4">
              <span className="text-white font-bold text-2xl">S</span>
            </div>
            <CardTitle className="text-3xl font-display">Create StudyOS Account</CardTitle>
            <p className="text-neutral-600 text-center">
              Join thousands of students mastering their studies.
            </p>
          </div>
        </CardHeader>
        <CardContent className="p-6 pt-0">
          <Link to="/login" className="block text-center text-sm text-brand-600 hover:text-brand-700 mb-6">
            Already have an account? Sign in
          </Link>
          <SignupForm />
        </CardContent>
      </Card>
    </div>
  );
};

export { SignupPage };
export default SignupPage;
