/**
 * StudyOS Design System
 * Inspired by Quizlet's playful design and Anki's minimal efficiency
 */

export const theme = {
  // Color Palettes
  colors: {
    // Quizlet-inspired brand colors
    quizlet: {
      primary: '#4255FF',     // Quizlet blue
      secondary: '#FFCD1F',   // Quizlet yellow
      accent: '#3CCFCF',      // Quizlet teal
      success: '#23D160',     // Green
      warning: '#FF9F43',     // Orange
      danger: '#FF3860',      // Red
      purple: '#B86BFF',      // Purple accent
    },
    
    // Anki-inspired neutrals
    anki: {
      primary: '#2B2D42',     // Dark blue-gray
      secondary: '#8D99AE',   // Medium gray
      light: '#EDF2F4',       // Light gray
      lighter: '#FAFAFA',     // Very light gray
      white: '#FFFFFF',       // Pure white
      border: '#E5E7EB',      // Border gray
    },
    
    // Semantic colors
    semantic: {
      success: '#10B981',
      warning: '#F59E0B', 
      error: '#EF4444',
      info: '#3B82F6',
    },
    
    // Neutral scale (combining both approaches)
    neutral: {
      50: '#FAFAFA',   // Anki lighter
      100: '#F5F5F5',
      200: '#E5E7EB',  // Anki border
      300: '#D1D5DB',
      400: '#9CA3AF',
      500: '#6B7280',
      600: '#4B5563',
      700: '#374151',
      800: '#2B2D42',  // Anki primary
      900: '#1F2937',
      950: '#0F172A',
    }
  },
  
  // Typography
  typography: {
    fonts: {
      primary: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      secondary: ['Open Sans', 'system-ui', 'sans-serif'],
      mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
    },
    
    sizes: {
      xs: '0.75rem',     // 12px
      sm: '0.875rem',    // 14px
      base: '1rem',      // 16px
      lg: '1.125rem',    // 18px
      xl: '1.25rem',     // 20px
      '2xl': '1.5rem',   // 24px
      '3xl': '1.875rem', // 30px
      '4xl': '2.25rem',  // 36px
      '5xl': '3rem',     // 48px
    },
    
    weights: {
      light: '300',
      normal: '400',
      medium: '500',
      semibold: '600',
      bold: '700',
      extrabold: '800',
    },
    
    lineHeights: {
      tight: '1.25',
      normal: '1.5',
      relaxed: '1.625',
      loose: '2',
    }
  },
  
  // Spacing (8px base unit)
  spacing: {
    px: '1px',
    0: '0',
    1: '0.25rem',   // 4px
    2: '0.5rem',    // 8px
    3: '0.75rem',   // 12px
    4: '1rem',      // 16px
    5: '1.25rem',   // 20px
    6: '1.5rem',    // 24px
    8: '2rem',      // 32px
    10: '2.5rem',   // 40px
    12: '3rem',     // 48px
    16: '4rem',     // 64px
    20: '5rem',     // 80px
    24: '6rem',     // 96px
  },
  
  // Border radius
  borderRadius: {
    none: '0',
    sm: '0.125rem',    // 2px
    base: '0.25rem',   // 4px - Anki style
    md: '0.375rem',    // 6px
    lg: '0.5rem',      // 8px
    xl: '0.75rem',     // 12px - Quizlet cards
    '2xl': '1rem',     // 16px
    '3xl': '1.5rem',   // 24px - Quizlet buttons
    full: '9999px',    // Pills
  },
  
  // Shadows
  shadows: {
    // Anki-style minimal shadows
    anki: {
      sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
      base: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
      md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    },
    
    // Quizlet-style playful shadows
    quizlet: {
      sm: '0 2px 4px 0 rgba(66, 85, 255, 0.1)',
      base: '0 4px 8px 0 rgba(66, 85, 255, 0.15)',
      md: '0 8px 16px 0 rgba(66, 85, 255, 0.2)',
      lg: '0 12px 24px 0 rgba(66, 85, 255, 0.25)',
      glow: '0 0 20px rgba(66, 85, 255, 0.3)',
    },
    
    // Neutral shadows
    neutral: {
      sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
      base: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
      md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
    }
  },
  
  // Animation
  animation: {
    durations: {
      fast: '150ms',
      normal: '250ms',
      slow: '350ms',
    },
    
    easings: {
      linear: 'linear',
      easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
      easeOut: 'cubic-bezier(0, 0, 0.2, 1)',
      easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
      bounce: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
    }
  },
  
  // Breakpoints
  breakpoints: {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
    '2xl': '1536px',
  }
} as const;

// Theme variants
export const themeVariants = {
  quizlet: {
    primary: theme.colors.quizlet.primary,
    secondary: theme.colors.quizlet.secondary,
    accent: theme.colors.quizlet.accent,
    background: theme.colors.neutral[50],
    surface: theme.colors.neutral[100],
    text: theme.colors.neutral[800],
    textSecondary: theme.colors.neutral[600],
    border: theme.colors.neutral[200],
    shadow: theme.shadows.quizlet,
    borderRadius: theme.borderRadius['3xl'], // Playful rounded
  },
  
  anki: {
    primary: theme.colors.anki.primary,
    secondary: theme.colors.anki.secondary,
    accent: theme.colors.semantic.info,
    background: theme.colors.anki.white,
    surface: theme.colors.anki.lighter,
    text: theme.colors.anki.primary,
    textSecondary: theme.colors.anki.secondary,
    border: theme.colors.anki.border,
    shadow: theme.shadows.anki,
    borderRadius: theme.borderRadius.base, // Minimal rounded
  },
  
  hybrid: {
    primary: theme.colors.quizlet.primary,
    secondary: theme.colors.anki.secondary,
    accent: theme.colors.quizlet.accent,
    background: theme.colors.anki.white,
    surface: theme.colors.neutral[50],
    text: theme.colors.anki.primary,
    textSecondary: theme.colors.anki.secondary,
    border: theme.colors.anki.border,
    shadow: theme.shadows.neutral,
    borderRadius: theme.borderRadius.lg, // Balanced rounded
  }
} as const;

// Component-specific design tokens
export const componentTokens = {
  // Flashcard tokens
  flashcard: {
    quizlet: {
      borderRadius: theme.borderRadius['2xl'],
      shadow: theme.shadows.quizlet.md,
      padding: theme.spacing[6],
      minHeight: '200px',
      background: theme.colors.neutral[50],
      border: `2px solid ${theme.colors.quizlet.primary}`,
    },
    anki: {
      borderRadius: theme.borderRadius.base,
      shadow: theme.shadows.anki.base,
      padding: theme.spacing[4],
      minHeight: '150px',
      background: theme.colors.anki.white,
      border: `1px solid ${theme.colors.anki.border}`,
    }
  },
  
  // Button tokens
  button: {
    quizlet: {
      borderRadius: theme.borderRadius.full, // Pill shape
      padding: `${theme.spacing[3]} ${theme.spacing[6]}`,
      fontSize: theme.typography.sizes.base,
      fontWeight: theme.typography.weights.semibold,
      shadow: theme.shadows.quizlet.sm,
    },
    anki: {
      borderRadius: theme.borderRadius.base, // Rectangular
      padding: `${theme.spacing[2]} ${theme.spacing[4]}`,
      fontSize: theme.typography.sizes.sm,
      fontWeight: theme.typography.weights.medium,
      shadow: theme.shadows.anki.sm,
    }
  },
  
  // Input tokens
  input: {
    borderRadius: theme.borderRadius.lg,
    padding: `${theme.spacing[3]} ${theme.spacing[4]}`,
    fontSize: theme.typography.sizes.base,
    border: `1px solid ${theme.colors.neutral[300]}`,
    focusBorder: `2px solid ${theme.colors.quizlet.primary}`,
    shadow: theme.shadows.neutral.sm,
  }
} as const;

export type ThemeVariant = keyof typeof themeVariants;
export type Theme = typeof theme;
export type ComponentTokens = typeof componentTokens;
