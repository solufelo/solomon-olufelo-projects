import React from 'react';
import { cn } from '../../lib/utils';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
  variant?: 'default' | 'elevated' | 'outlined' | 'glass';
  size?: 'sm' | 'md' | 'lg';
  padding?: 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
  hover?: boolean;
  interactive?: boolean;
}

const cardVariants = {
  default: 'bg-white border border-neutral-200 shadow-soft',
  elevated: 'bg-white border border-neutral-200 shadow-medium',
  outlined: 'bg-white border-2 border-neutral-300',
  glass: 'bg-white/80 backdrop-blur-sm border border-white/20 shadow-soft',
};

const cardSizes = {
  sm: 'rounded-lg',
  md: 'rounded-xl', 
  lg: 'rounded-2xl',
};

const cardPadding = {
  sm: 'p-4',
  md: 'p-6',
  lg: 'p-8',
  xl: 'p-10',
};

export const Card: React.FC<CardProps> = ({
  children,
  variant = 'default',
  size = 'md',
  padding = 'md',
  className,
  hover = false,
  interactive = false,
  onClick,
  ...props
}) => {
  const isClickable = interactive || onClick;

  return (
    <div
      className={cn(
        cardVariants[variant],
        cardSizes[size],
        cardPadding[padding],
        'transition-all duration-200',
        hover && 'hover:shadow-strong hover:-translate-y-1',
        isClickable && 'cursor-pointer hover:shadow-medium',
        className
      )}
      onClick={onClick}
      {...props}
    >
      {children}
    </div>
  );
};

export default Card;
