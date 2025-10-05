import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from 'wasp/client/auth';
import { cn } from '../../lib/utils';
import Container from './Container';
import Button from './Button';

interface HeaderProps {
  title?: string;
  breadcrumbs?: Array<{ label: string; href?: string }>;
  actions?: React.ReactNode;
  className?: string;
  variant?: 'default' | 'glass' | 'solid';
}

const headerVariants = {
  default: 'bg-white/95 backdrop-blur-sm border-b border-neutral-200/80',
  glass: 'bg-white/80 backdrop-blur-md border-b border-white/20',
  solid: 'bg-white border-b border-neutral-200',
};

export const Header: React.FC<HeaderProps> = ({
  title,
  breadcrumbs,
  actions,
  className,
  variant = 'default',
}) => {
  const { data: user } = useAuth();

  return (
    <header className={cn(
      'sticky top-0 z-40 transition-all duration-200',
      headerVariants[variant],
      className
    )}>
      <Container className="py-4 lg:py-6">
        <div className="flex items-center justify-between">
          {/* Left side - Logo and breadcrumbs */}
          <div className="flex items-center space-x-4">
            <Link 
              to="/" 
              className="flex items-center space-x-2 group"
            >
              <div className="w-8 h-8 bg-gradient-to-br from-brand-500 to-brand-600 rounded-xl flex items-center justify-center group-hover:shadow-glow transition-all duration-200">
                <span className="text-white font-bold text-lg">S</span>
              </div>
              <span className="text-xl font-display font-bold text-neutral-900 group-hover:text-brand-600 transition-colors">
                StudyOS
              </span>
            </Link>

            {breadcrumbs && breadcrumbs.length > 0 && (
              <nav className="flex items-center space-x-2 text-sm">
                <span className="text-neutral-400">/</span>
                {breadcrumbs.map((crumb, index) => (
                  <React.Fragment key={index}>
                    {crumb.href ? (
                      <Link
                        to={crumb.href}
                        className="text-neutral-600 hover:text-brand-600 transition-colors"
                      >
                        {crumb.label}
                      </Link>
                    ) : (
                      <span className="text-neutral-900 font-medium">
                        {crumb.label}
                      </span>
                    )}
                    {index < breadcrumbs.length - 1 && (
                      <span className="text-neutral-400">/</span>
                    )}
                  </React.Fragment>
                ))}
              </nav>
            )}

            {title && !breadcrumbs && (
              <div className="flex items-center space-x-2">
                <span className="text-neutral-400">/</span>
                <h1 className="text-lg font-semibold text-neutral-900">{title}</h1>
              </div>
            )}
          </div>

          {/* Right side - Actions and user info */}
          <div className="flex items-center space-x-4">
            {actions}
            
            {user ? (
              <div className="flex items-center space-x-3">
                <span className="hidden sm:inline text-sm text-neutral-600">
                  Welcome back!
                </span>
                <div className="w-8 h-8 bg-gradient-to-br from-brand-400 to-brand-500 rounded-full flex items-center justify-center">
                  <span className="text-white text-sm font-medium">
                    {user.id.toString().slice(-1)}
                  </span>
                </div>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Link to="/login">
                  <Button variant="ghost" size="sm">
                    Sign In
                  </Button>
                </Link>
                <Link to="/signup">
                  <Button size="sm">
                    Get Started
                  </Button>
                </Link>
              </div>
            )}
          </div>
        </div>
      </Container>
    </header>
  );
};

export default Header;
