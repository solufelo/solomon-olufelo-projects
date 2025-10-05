import { useState, useEffect } from 'react';

/**
 * Hook for scroll-based animations
 */
export const useScrollAnimation = (threshold = 50) => {
  const [hasScrolled, setHasScrolled] = useState(false);
  
  useEffect(() => {
    const handleScroll = () => {
      setHasScrolled(window.scrollY > threshold);
    };
    
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, [threshold]);
  
  return hasScrolled;
};

/**
 * Hook for study progress animations
 */
export const useStudyProgress = (current: number, total: number) => {
  const [progress, setProgress] = useState(0);
  
  useEffect(() => {
    const percentage = total > 0 ? (current / total) * 100 : 0;
    setProgress(percentage);
  }, [current, total]);
  
  return progress;
};

/**
 * Hook for element visibility
 */
export const useElementVisibility = (ref: React.RefObject<HTMLElement>, threshold = 0.1) => {
  const [isVisible, setIsVisible] = useState(false);
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsVisible(entry.isIntersecting);
      },
      { threshold }
    );
    
    if (ref.current) {
      observer.observe(ref.current);
    }
    
    return () => {
      if (ref.current) {
        observer.unobserve(ref.current);
      }
    };
  }, [ref, threshold]);
  
  return isVisible;
};

/**
 * Hook for staggered animations
 */
export const useStaggeredAnimation = (items: any[], delay = 100) => {
  const [visibleItems, setVisibleItems] = useState<Set<number>>(new Set());
  
  useEffect(() => {
    const timer = setTimeout(() => {
      items.forEach((_, index) => {
        setTimeout(() => {
          setVisibleItems(prev => new Set([...prev, index]));
        }, index * delay);
      });
    }, 100);
    
    return () => clearTimeout(timer);
  }, [items, delay]);
  
  return visibleItems;
};

/**
 * Hook for theme-aware animations
 */
export const useThemeAnimation = () => {
  const [isDark, setIsDark] = useState(false);
  
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    setIsDark(mediaQuery.matches);
    
    const handler = (e: MediaQueryListEvent) => setIsDark(e.matches);
    mediaQuery.addEventListener('change', handler);
    
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);
  
  return isDark;
};

/**
 * Hook for reduced motion preference
 */
export const useReducedMotion = () => {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);
  
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);
    
    const handler = (e: MediaQueryListEvent) => setPrefersReducedMotion(e.matches);
    mediaQuery.addEventListener('change', handler);
    
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);
  
  return prefersReducedMotion;
};

/**
 * Animation presets for StudyOS
 */
export const studyAnimations = {
  fadeInUp: {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
    transition: { duration: 0.5 }
  },
  staggerChildren: {
    animate: {
      transition: {
        staggerChildren: 0.1
      }
    }
  },
  scaleIn: {
    initial: { opacity: 0, scale: 0.9 },
    animate: { opacity: 1, scale: 1 },
    transition: { duration: 0.3 }
  },
  slideIn: {
    initial: { x: -20, opacity: 0 },
    animate: { x: 0, opacity: 1 },
    transition: { duration: 0.4 }
  },
  studyCard: {
    initial: { opacity: 0, y: 30 },
    animate: { opacity: 1, y: 0 },
    transition: { duration: 0.6, ease: "easeOut" }
  },
  progressBar: {
    initial: { width: 0 },
    animate: { width: "100%" },
    transition: { duration: 1, ease: "easeOut" }
  },
  hover: {
    hover: { 
      y: -8, 
      scale: 1.02,
      transition: { duration: 0.3 }
    }
  },
  tap: {
    tap: { 
      scale: 0.98,
      transition: { duration: 0.1 }
    }
  }
};

/**
 * Utility function for conditional animations
 */
export const getAnimationProps = (animation: keyof typeof studyAnimations, isReducedMotion = false) => {
  if (isReducedMotion) {
    return {
      initial: { opacity: 0 },
      animate: { opacity: 1 },
      transition: { duration: 0.1 }
    };
  }
  
  return studyAnimations[animation];
};
