'use client';

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Menu, X, BookOpen, Brain, BarChart3, Settings, User } from 'lucide-react';
import { EnhancedButton } from '../ui/enhanced-button';
import { useScrollAnimation } from '../../lib/animation-hooks';

interface StudyNavigationProps {
  className?: string;
}

export default function StudyNavigation({ className = '' }: StudyNavigationProps) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isVisible, setIsVisible] = useState(true);
  const hasScrolled = useScrollAnimation(100);

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      const windowHeight = window.innerHeight;
      
      // Hide navbar after scrolling past the first section
      const shouldHide = scrollY > windowHeight * 0.8;
      setIsVisible(!shouldHide);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navigationItems = [
    { name: 'Decks', href: '/decks', icon: BookOpen },
    { name: 'Study', href: '/study', icon: Brain },
    { name: 'Progress', href: '/progress', icon: BarChart3 },
    { name: 'Settings', href: '/settings', icon: Settings },
  ];

  return (
    <AnimatePresence>
      {isVisible && (
        <motion.nav
          initial={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -100 }}
          transition={{ duration: 0.5, ease: "easeInOut" }}
          className={`fixed top-0 left-0 right-0 z-50 ${className}`}
        >
          <div className="flex justify-center mt-4">
            <motion.div 
              className="w-2/3 lg:w-1/2 glass rounded-2xl border border-white/20 shadow-2xl"
              animate={{
                scale: hasScrolled ? 0.95 : 1,
                opacity: hasScrolled ? 0.8 : 1,
              }}
              transition={{ duration: 0.3 }}
            >
              <div className="px-6 py-3">
                <div className="flex items-center justify-between">
                  {/* Logo */}
                  <motion.div
                    className="flex items-center gap-2"
                        whileHover={{ scale: 1.05 }}
                        transition={{ duration: 0.2 }}
                  >
                    <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                      <Brain className="w-5 h-5 text-white" />
                    </div>
                    <span className="text-xl font-bold gradient-text">StudyOS</span>
                  </motion.div>
                  
                  {/* Desktop Navigation */}
                  <div className="hidden lg:flex items-center gap-6">
                    {navigationItems.map((item) => (
                      <motion.a
                        key={item.name}
                        href={item.href}
                        className="flex items-center gap-2 text-foreground/80 hover:text-primary transition-colors text-sm font-medium tracking-wide group"
                        whileHover={{ y: -2 }}
                        transition={{ duration: 0.2 }}
                      >
                        <item.icon className="w-4 h-4 group-hover:scale-110 transition-transform" />
                        {item.name}
                      </motion.a>
                    ))}
                  </div>
                  
                  {/* User Menu */}
                  <div className="hidden lg:flex items-center gap-4">
                    <EnhancedButton variant="glass" size="sm">
                      <User className="w-4 h-4" />
                    </EnhancedButton>
                  </div>
                  
                  {/* Mobile Menu Button */}
                  <div className="lg:hidden">
                    <EnhancedButton
                      variant="ghost"
                      size="icon"
                      onClick={() => setIsMenuOpen(!isMenuOpen)}
                    >
                      {isMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
                    </EnhancedButton>
                  </div>
                </div>
              </div>
              
              {/* Mobile Menu */}
              <AnimatePresence>
                {isMenuOpen && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.3, ease: "easeInOut" }}
                    className="overflow-hidden border-t border-white/10"
                  >
                    <div className="px-6 py-4">
                      <div className="space-y-4">
                        {navigationItems.map((item, index) => (
                          <motion.a
                            key={item.name}
                            href={item.href}
                            className="flex items-center gap-3 text-foreground/80 hover:text-primary transition-colors py-2 group"
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.3, delay: index * 0.1 }}
                            onClick={() => setIsMenuOpen(false)}
                          >
                            <item.icon className="w-5 h-5 group-hover:scale-110 transition-transform" />
                            {item.name}
                          </motion.a>
                        ))}
                        
                        {/* Mobile User Actions */}
                        <motion.div
                          className="pt-4 border-t border-white/10"
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ duration: 0.3, delay: 0.4 }}
                        >
                          <EnhancedButton variant="study" className="w-full">
                            <User className="w-4 h-4 mr-2" />
                            Profile
                          </EnhancedButton>
                        </motion.div>
                      </div>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </div>
        </motion.nav>
      )}
    </AnimatePresence>
  );
}
