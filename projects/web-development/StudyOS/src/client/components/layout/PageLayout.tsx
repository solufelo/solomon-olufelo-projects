import React from 'react';
import { cn } from '../../lib/utils';
import Header from '../ui/Header';
import Container from '../ui/Container';

interface PageLayoutProps {
  children: React.ReactNode;
  title?: string;
  breadcrumbs?: Array<{ label: string; href?: string }>;
  actions?: React.ReactNode;
  headerVariant?: 'default' | 'glass' | 'solid';
  containerSize?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  className?: string;
  background?: 'default' | 'gradient' | 'pattern' | 'aurora' | 'cosmic' | 'grid' | 'stellar' | 'midnight' | 'paper';
}

const backgroundVariants = {
  default: 'bg-neutral-50',
  gradient: 'bg-gradient-to-br from-neutral-50 via-blue-50/30 to-neutral-100',
  pattern: 'bg-neutral-50 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-blue-100/20 via-neutral-50 to-neutral-100',
  // PatternCraft Aurora Patterns
  aurora: 'bg-neutral-50 bg-aurora-waves',
  cosmic: 'bg-neutral-50 bg-cosmic-aurora',
  stellar: 'bg-neutral-50 bg-stellar-mist',
  midnight: 'bg-neutral-900 bg-midnight-aurora',
  // Grid and Texture Patterns
  grid: 'bg-neutral-50 bg-grid-subtle bg-grid-md',
  paper: 'bg-neutral-50 bg-paper-texture bg-noise-texture',
};

export const PageLayout: React.FC<PageLayoutProps> = ({
  children,
  title,
  breadcrumbs,
  actions,
  headerVariant = 'default',
  containerSize = 'lg',
  className,
  background = 'gradient',
}) => {
  return (
    <div className={cn(
      'min-h-screen',
      backgroundVariants[background],
      className
    )}>
      <Header
        title={title}
        breadcrumbs={breadcrumbs}
        actions={actions}
        variant={headerVariant}
      />
      
      <main className="pb-12">
        <Container size={containerSize} className="py-6 lg:py-8">
          <div className="animate-fade-in-up">
            {children}
          </div>
        </Container>
      </main>
    </div>
  );
};

export default PageLayout;
