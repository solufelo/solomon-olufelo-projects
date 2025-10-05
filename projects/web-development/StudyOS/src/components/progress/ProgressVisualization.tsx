'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, Calendar, Target, Award, BarChart3, PieChart } from 'lucide-react';
import { StudyCard, GlassCard } from '../ui/enhanced-card';
import { useStudyProgress } from '../../lib/animation-hooks';

interface ProgressData {
  totalCards: number;
  studiedCards: number;
  studyStreak: number;
  weeklyGoal: number;
  weeklyProgress: number;
  accuracy: number;
  level: number;
  xp: number;
  nextLevelXp: number;
}

interface ProgressVisualizationProps {
  data: ProgressData;
  className?: string;
}

export default function ProgressVisualization({ 
  data, 
  className = '' 
}: ProgressVisualizationProps) {
  const studyProgress = useStudyProgress(data.studiedCards, data.totalCards);
  const weeklyProgress = useStudyProgress(data.weeklyProgress, data.weeklyGoal);
  const levelProgress = useStudyProgress(data.xp, data.nextLevelXp);

  const stats = [
    {
      label: 'Study Streak',
      value: data.studyStreak,
      icon: Calendar,
      color: 'from-orange-500 to-red-500',
      suffix: ' days'
    },
    {
      label: 'Accuracy',
      value: Math.round(data.accuracy),
      icon: Target,
      color: 'from-green-500 to-emerald-500',
      suffix: '%'
    },
    {
      label: 'Level',
      value: data.level,
      icon: Award,
      color: 'from-purple-500 to-pink-500',
      suffix: ''
    },
    {
      label: 'Cards Studied',
      value: data.studiedCards,
      icon: BarChart3,
      color: 'from-blue-500 to-cyan-500',
      suffix: `/${data.totalCards}`
    },
  ];

  return (
    <div className={`progress-visualization space-y-8 ${className}`}>
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="text-center"
      >
        <h2 className="text-3xl font-bold mb-2 gradient-text">
          Study Progress
        </h2>
        <p className="text-muted-foreground">
          Track your learning journey and achievements
        </p>
      </motion.div>

      {/* Stats Grid */}
      <motion.div
        className="grid grid-cols-2 md:grid-cols-4 gap-6"
        initial="hidden"
        animate="visible"
        variants={{
          hidden: { opacity: 0 },
          visible: {
            opacity: 1,
            transition: {
              staggerChildren: 0.1
            }
          }
        }}
      >
        {stats.map((stat, index) => (
          <motion.div
            key={stat.label}
            variants={{
              hidden: { opacity: 0, y: 30 },
              visible: { opacity: 1, y: 0 }
            }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <GlassCard className="text-center p-6 group cursor-pointer">
              <motion.div
                className={`w-12 h-12 mx-auto mb-4 rounded-xl bg-gradient-to-r ${stat.color} flex items-center justify-center`}
                whileHover={{ rotate: 360, scale: 1.1 }}
                transition={{ duration: 0.6 }}
              >
                <stat.icon className="w-6 h-6 text-white" />
              </motion.div>
              
              <motion.h3
                className="text-2xl font-bold mb-1"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ duration: 0.5, delay: 0.3 + index * 0.1 }}
              >
                {stat.value}{stat.suffix}
              </motion.h3>
              
              <p className="text-sm text-muted-foreground font-medium">
                {stat.label}
              </p>
            </GlassCard>
          </motion.div>
        ))}
      </motion.div>

      {/* Progress Charts */}
      <div className="grid md:grid-cols-2 gap-8">
        {/* Overall Progress */}
        <motion.div
          initial={{ opacity: 0, x: -30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <StudyCard className="p-8">
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-xl font-semibold flex items-center gap-2">
                <TrendingUp className="w-5 h-5" />
                Overall Progress
              </h3>
              <span className="text-sm text-muted-foreground">
                {Math.round(studyProgress)}% Complete
              </span>
            </div>
            
            <div className="relative h-4 bg-muted rounded-full overflow-hidden mb-4">
              <motion.div
                className="h-full bg-gradient-to-r from-green-500 to-blue-600 rounded-full"
                initial={{ width: 0 }}
                animate={{ width: `${studyProgress}%` }}
                transition={{ duration: 2, ease: "easeOut", delay: 0.6 }}
              />
              
              {/* Shine effect */}
              <motion.div
                className="absolute top-0 left-0 h-full w-8 bg-gradient-to-r from-transparent via-white/30 to-transparent"
                animate={{ x: ['-32px', '100%'] }}
                transition={{ duration: 2, repeat: Infinity, repeatDelay: 3 }}
              />
            </div>
            
            <p className="text-sm text-muted-foreground">
              {data.studiedCards} of {data.totalCards} cards studied
            </p>
          </StudyCard>
        </motion.div>

        {/* Weekly Goal */}
        <motion.div
          initial={{ opacity: 0, x: 30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.6, delay: 0.5 }}
        >
          <StudyCard className="p-8">
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-xl font-semibold flex items-center gap-2">
                <Target className="w-5 h-5" />
                Weekly Goal
              </h3>
              <span className="text-sm text-muted-foreground">
                {Math.round(weeklyProgress)}% Complete
              </span>
            </div>
            
            <div className="relative h-4 bg-muted rounded-full overflow-hidden mb-4">
              <motion.div
                className="h-full bg-gradient-to-r from-purple-500 to-pink-600 rounded-full"
                initial={{ width: 0 }}
                animate={{ width: `${weeklyProgress}%` }}
                transition={{ duration: 2, ease: "easeOut", delay: 0.7 }}
              />
            </div>
            
            <p className="text-sm text-muted-foreground">
              {data.weeklyProgress} of {data.weeklyGoal} cards this week
            </p>
          </StudyCard>
        </motion.div>
      </div>

      {/* Level Progress */}
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.6 }}
      >
        <GlassCard className="p-8">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-xl font-semibold flex items-center gap-2">
              <Award className="w-5 h-5" />
              Level Progress
            </h3>
            <div className="text-right">
              <p className="text-2xl font-bold gradient-text">Level {data.level}</p>
              <p className="text-sm text-muted-foreground">
                {data.xp} / {data.nextLevelXp} XP
              </p>
            </div>
          </div>
          
          <div className="relative h-6 bg-muted rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-gradient-to-r from-yellow-500 via-orange-500 to-red-500 rounded-full"
              initial={{ width: 0 }}
              animate={{ width: `${levelProgress}%` }}
              transition={{ duration: 2, ease: "easeOut", delay: 0.8 }}
            />
            
            {/* Shine effect */}
            <motion.div
              className="absolute top-0 left-0 h-full w-12 bg-gradient-to-r from-transparent via-white/40 to-transparent"
              animate={{ x: ['-48px', '100%'] }}
              transition={{ duration: 2, repeat: Infinity, repeatDelay: 4 }}
            />
          </div>
          
          <p className="text-sm text-muted-foreground mt-2">
            {data.nextLevelXp - data.xp} XP until next level
          </p>
        </GlassCard>
      </motion.div>

      {/* Achievement Badges */}
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.7 }}
      >
        <StudyCard className="p-8">
          <h3 className="text-xl font-semibold mb-6 flex items-center gap-2">
            <Award className="w-5 h-5" />
            Recent Achievements
          </h3>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { emoji: '🔥', label: '7 Day Streak', earned: data.studyStreak >= 7 },
              { emoji: '🎯', label: 'Perfect Week', earned: data.weeklyProgress >= data.weeklyGoal },
              { emoji: '🧠', label: '100 Cards', earned: data.studiedCards >= 100 },
              { emoji: '⭐', label: 'Level Up', earned: data.level > 1 },
            ].map((achievement, index) => (
              <motion.div
                key={achievement.label}
                className={`text-center p-4 rounded-lg border-2 transition-all ${
                  achievement.earned 
                    ? 'border-green-500 bg-green-50 dark:bg-green-950/20' 
                    : 'border-muted bg-muted/20'
                }`}
                initial={{ opacity: 0, scale: 0 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, delay: 0.8 + index * 0.1 }}
                whileHover={{ scale: 1.05 }}
              >
                <div className="text-3xl mb-2 opacity-60">
                  {achievement.emoji}
                </div>
                <p className={`text-sm font-medium ${
                  achievement.earned ? 'text-green-700 dark:text-green-300' : 'text-muted-foreground'
                }`}>
                  {achievement.label}
                </p>
              </motion.div>
            ))}
          </div>
        </StudyCard>
      </motion.div>
    </div>
  );
}
