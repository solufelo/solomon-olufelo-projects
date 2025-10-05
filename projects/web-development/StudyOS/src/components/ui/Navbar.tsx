import React, { useState } from 'react';
import { theme, themeVariants, type ThemeVariant } from '../../theme';

interface NavItem {
  label: string;
  href?: string;
  icon?: React.ReactNode;
  onClick?: () => void;
  active?: boolean;
}

interface NavbarProps {
  /** Theme variant */
  variant?: ThemeVariant;
  /** Navigation items */
  items: NavItem[];
  /** Logo or brand element */
  logo?: React.ReactNode;
  /** User menu element */
  userMenu?: React.ReactNode;
  /** Whether navbar is sticky */
  sticky?: boolean;
  /** Custom className */
  className?: string;
  /** Mobile menu toggle */
  onMobileMenuToggle?: (isOpen: boolean) => void;
}

const Navbar: React.FC<NavbarProps> = ({
  variant = 'hybrid',
  items,
  logo,
  userMenu,
  sticky = true,
  className = '',
  onMobileMenuToggle,
}) => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const variantStyles = themeVariants[variant];

  const toggleMobileMenu = () => {
    const newState = !isMobileMenuOpen;
    setIsMobileMenuOpen(newState);
    onMobileMenuToggle?.(newState);
  };

  const baseStyles = `
    w-full border-b transition-all duration-200
    ${sticky ? 'sticky top-0 z-50' : ''}
    ${className}
  `;

  const containerStyles = `
    max-w-7xl mx-auto px-4 sm:px-6 lg:px-8
    ${variant === 'quizlet' ? 'py-3' : 'py-2'}
  `;

  const navStyles = {
    backgroundColor: variantStyles.background,
    borderColor: variantStyles.border,
    boxShadow: variant === 'quizlet' 
      ? variantStyles.shadow.base 
      : variantStyles.shadow.sm,
  };

  const linkBaseStyles = `
    transition-all duration-200 font-medium
    ${variant === 'quizlet' 
      ? 'px-4 py-2 rounded-full hover:scale-105 transform' 
      : 'px-3 py-2 rounded hover:bg-gray-50'
    }
  `;

  const getLinkStyles = (item: NavItem) => {
    if (item.active) {
      return variant === 'quizlet' 
        ? {
            backgroundColor: variantStyles.primary,
            color: 'white',
          }
        : {
            backgroundColor: variantStyles.primary + '10',
            color: variantStyles.primary,
          };
    }
    
    return {
      color: variantStyles.text,
    };
  };

  const renderNavItem = (item: NavItem, mobile = false) => {
    const Component = item.href ? 'a' : 'button';
    const itemStyles = getLinkStyles(item);
    
    const mobileStyles = mobile ? 'block w-full text-left' : '';
    
    return (
      <Component
        key={item.label}
        href={item.href}
        onClick={item.onClick}
        className={`${linkBaseStyles} ${mobileStyles}`}
        style={itemStyles}
        onMouseEnter={(e) => {
          if (!item.active) {
            e.currentTarget.style.backgroundColor = variant === 'quizlet' 
              ? variantStyles.primary + '15' 
              : theme.colors.neutral[100];
          }
        }}
        onMouseLeave={(e) => {
          if (!item.active) {
            e.currentTarget.style.backgroundColor = 'transparent';
          }
        }}
      >
        <div className="flex items-center space-x-2">
          {item.icon && (
            <span className={variant === 'quizlet' ? 'text-lg' : 'text-sm'}>
              {item.icon}
            </span>
          )}
          <span>{item.label}</span>
        </div>
      </Component>
    );
  };

  return (
    <nav className={baseStyles} style={navStyles}>
      <div className={containerStyles}>
        <div className="flex items-center justify-between">
          {/* Logo */}
          <div className="flex items-center">
            {logo && (
              <div className={variant === 'quizlet' ? 'mr-8' : 'mr-6'}>
                {logo}
              </div>
            )}
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-2">
            {items.map(item => renderNavItem(item))}
          </div>

          {/* Right side */}
          <div className="flex items-center space-x-4">
            {userMenu && (
              <div className="hidden md:block">
                {userMenu}
              </div>
            )}

            {/* Mobile menu button */}
            <button
              className="md:hidden p-2 rounded-md"
              onClick={toggleMobileMenu}
              style={{ color: variantStyles.text }}
            >
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                {isMobileMenuOpen ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M6 18L18 6M6 6l12 12"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMobileMenuOpen && (
          <div className="md:hidden mt-4 pb-4 border-t" style={{ borderColor: variantStyles.border }}>
            <div className="space-y-2 pt-4">
              {items.map(item => renderNavItem(item, true))}
              {userMenu && (
                <div className="pt-4 border-t" style={{ borderColor: variantStyles.border }}>
                  {userMenu}
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
