import React from 'react';

/**
 * Button Component
 * Follows the StudyOS design system with multiple variants and sizes
 */

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'destructive';
  size?: 'sm' | 'md' | 'lg' | 'icon';
  fullWidth?: boolean;
  children: React.ReactNode;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', fullWidth = false, className = '', children, ...props }, ref) => {
    // Base button class
    let buttonClass = 'btn';

    // Add variant class
    switch (variant) {
      case 'primary':
        buttonClass += ' btn-primary';
        break;
      case 'secondary':
        buttonClass += ' btn-secondary';
        break;
      case 'outline':
        buttonClass += ' btn-outline';
        break;
      case 'ghost':
        buttonClass += ' btn-ghost';
        break;
      case 'destructive':
        buttonClass += ' btn-destructive';
        break;
    }

    // Add size class
    switch (size) {
      case 'sm':
        buttonClass += ' btn-sm';
        break;
      case 'lg':
        buttonClass += ' btn-lg';
        break;
      case 'icon':
        buttonClass += ' btn-icon';
        break;
      // 'md' is default, no extra class needed
    }

    // Add full width class
    if (fullWidth) {
      buttonClass += ' w-full';
    }

    // Append custom className
    if (className) {
      buttonClass += ' ' + className;
    }

    return (
      <button ref={ref} className={buttonClass} {...props}>
        {children}
      </button>
    );
  }
);

Button.displayName = 'Button';

export default Button;
