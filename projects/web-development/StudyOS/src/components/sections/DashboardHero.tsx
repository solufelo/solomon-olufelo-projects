'use client';

import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Brain, BookOpen, BarChart3, Trophy, Play, Target } from 'lucide-react';
import { EnhancedButton } from '../ui/enhanced-button';
import { useScrollAnimation, useStudyProgress } from '../../lib/animation-hooks';

interface DashboardHeroProps {
  className?: string;
  userStats?: {
    totalDecks: number;
    cardsStudied: number;
    studyStreak: number;
    level: number;
  };
}

export default function DashboardHero({ 
  className = '',
  userStats = {
    totalDecks: 12,
    cardsStudied: 247,
    studyStreak: 7,
    level: 3
  }
}: DashboardHeroProps) {
  const [hasScrolled, setHasScrolled] = useState(false);
  const studyProgress = useStudyProgress(userStats.cardsStudied, 1000); // Assuming 1000 cards for next level

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      setHasScrolled(scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const stats = [
    { 
      label: 'Decks', 
      value: userStats.totalDecks, 
      icon: BookOpen,
      color: 'from-blue-500 to-cyan-500'
    },
    { 
      label: 'Cards Studied', 
      value: userStats.cardsStudied, 
      icon: Brain,
      color: 'from-green-500 to-emerald-500'
    },
    { 
      label: 'Day Streak', 
      value: userStats.studyStreak, 
      icon: Trophy,
      color: 'from-yellow-500 to-orange-500'
    },
    { 
      label: 'Level', 
      value: userStats.level, 
      icon: Target,
      color: 'from-purple-500 to-pink-500'
    },
  ];

  return (
    <section className={`dashboard-hero relative w-full min-h-screen overflow-hidden ${className}`}>
      {/* Background with gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-background via-background to-primary/5" />
      
      {/* Animated background elements */}
      <div className="absolute inset-0">
        <motion.div
          className="absolute top-20 left-20 w-32 h-32 bg-gradient-to-r from-blue-500/20 to-purple-500/20 rounded-full blur-xl"
          animate={{
            x: [0, 50, 0],
            y: [0, -30, 0],
            scale: [1, 1.1, 1],
          }}
          transition={{
            duration: 8,
            repeat: Infinity,
            ease: "easeInOut"
          }}
        />
        <motion.div
          className="absolute bottom-20 right-20 w-40 h-40 bg-gradient-to-r from-green-500/20 to-cyan-500/20 rounded-full blur-xl"
          animate={{
            x: [0, -40, 0],
            y: [0, 40, 0],
            scale: [1, 0.9, 1],
          }}
          transition={{
            duration: 10,
            repeat: Infinity,
            ease: "easeInOut",
            delay: 2
          }}
        />
      </div>
      
      <div className="relative z-10 container mx-auto px-4 py-20">
        <div className="text-center mb-16">
          {/* Main Headline */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ 
              opacity: hasScrolled ? 0.6 : 1,
              y: hasScrolled ? -20 : 0,
              scale: hasScrolled ? 0.95 : 1
            }}
            transition={{ duration: 0.6, ease: "easeInOut" }}
            className="mb-8"
          >
            <motion.h1 
              className="text-5xl md:text-7xl lg:text-8xl font-bold mb-6 tracking-tight"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1 }}
            >
              <motion.span 
                className="gradient-text"
                animate={{ 
                  backgroundPosition: hasScrolled ? "0% 50%" : "100% 50%"
                }}
                transition={{ duration: 3, repeat: Infinity, repeatType: "reverse" }}
                style={{ backgroundSize: "200% 200%" }}
              >
                StudyOS
              </motion.span>
            </motion.h1>
            
            <motion.p 
              className="text-xl md:text-2xl text-muted-foreground font-light tracking-wide"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1, delay: 0.3 }}
            >
              Master Your Learning Journey
            </motion.p>
          </motion.div>
          
          {/* CTA Buttons */}
          <motion.div 
            className="flex flex-col sm:flex-row gap-4 justify-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            animate={{ 
              opacity: hasScrolled ? 0.5 : 1,
              y: hasScrolled ? 10 : 0,
              scale: hasScrolled ? 0.96 : 1
            }}
            transition={{ duration: 0.6, delay: 0.2, ease: "easeInOut" }}
          >
            <motion.div
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <EnhancedButton 
                variant="study"
                size="xl"
                className="min-w-[200px]"
              >
                <Play className="w-5 h-5 mr-2" />
                Start Studying
              </EnhancedButton>
            </motion.div>
            
            <motion.div
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <EnhancedButton 
                variant="outline"
                size="xl"
                className="min-w-[200px]"
              >
                <BookOpen className="w-5 h-5 mr-2" />
                Create Deck
              </EnhancedButton>
            </motion.div>
          </motion.div>
        </div>
        
        {/* Stats Grid */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto"
        >
          {stats.map((stat, index) => (
            <motion.div
              key={stat.label}
              className="glass rounded-2xl p-6 text-center group cursor-pointer"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.1 * index }}
              whileHover={{ 
                y: -8, 
                scale: 1.05,
                transition: { duration: 0.3 }
              }}
            >
              <motion.div
                className={`w-12 h-12 mx-auto mb-4 rounded-xl bg-gradient-to-r ${stat.color} flex items-center justify-center`}
                whileHover={{ rotate: 360 }}
                transition={{ duration: 0.6 }}
              >
                <stat.icon className="w-6 h-6 text-white" />
              </motion.div>
              
              <motion.h3 
                className="text-2xl md:text-3xl font-bold mb-2"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ duration: 0.5, delay: 0.3 + index * 0.1 }}
              >
                {stat.value}
              </motion.h3>
              
              <p className="text-sm text-muted-foreground font-medium">
                {stat.label}
              </p>
            </motion.div>
          ))}
        </motion.div>
        
        {/* Progress Section */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.8 }}
          className="mt-16 max-w-2xl mx-auto"
        >
          <div className="glass rounded-2xl p-8">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold">Study Progress</h3>
              <span className="text-sm text-muted-foreground">
                {Math.round(studyProgress)}% Complete
              </span>
            </div>
            
            <div className="relative h-3 bg-muted rounded-full overflow-hidden">
              <motion.div
                className="h-full bg-gradient-to-r from-green-500 to-blue-600 rounded-full"
                initial={{ width: 0 }}
                animate={{ width: `${studyProgress}%` }}
                transition={{ duration: 2, ease: "easeOut", delay: 1 }}
              />
              
              {/* Shine effect */}
              <motion.div
                className="absolute top-0 left-0 h-full w-8 bg-gradient-to-r from-transparent via-white/30 to-transparent"
                animate={{ x: ['-32px', '100%'] }}
                transition={{ duration: 2, repeat: Infinity, repeatDelay: 3 }}
              />
            </div>
            
            <p className="text-sm text-muted-foreground mt-2">
              Keep studying to reach the next level!
            </p>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
