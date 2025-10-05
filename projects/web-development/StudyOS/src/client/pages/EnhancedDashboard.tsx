'use client';

import React from 'react';
import { motion } from 'framer-motion';
import MainLayout from '../../components/layout/MainLayout';
import DashboardHero from '../../components/sections/DashboardHero';
import DeckGrid from '../../components/decks/DeckGrid';
import ProgressVisualization from '../../components/progress/ProgressVisualization';
import { EnhancedButton } from '../../components/ui/enhanced-button';
import { Plus, BookOpen, Brain, BarChart3 } from 'lucide-react';

// Mock data for demonstration
const mockUserStats = {
  totalDecks: 12,
  cardsStudied: 247,
  studyStreak: 7,
  level: 3
};

const mockDecks = [
  {
    id: '1',
    name: 'JavaScript Fundamentals',
    description: 'Core JavaScript concepts, ES6+ features, and modern development patterns',
    cardCount: 45,
    studiedCount: 32,
    difficulty: 'medium' as const,
    category: 'Programming',
    lastStudied: new Date('2024-01-15'),
    isFavorite: true,
    color: 'from-blue-500 to-cyan-500'
  },
  {
    id: '2',
    name: 'React Hooks',
    description: 'useState, useEffect, useContext, and custom hooks',
    cardCount: 28,
    studiedCount: 28,
    difficulty: 'easy' as const,
    category: 'React',
    lastStudied: new Date('2024-01-14'),
    isFavorite: false,
    color: 'from-green-500 to-emerald-500'
  },
  {
    id: '3',
    name: 'TypeScript Advanced',
    description: 'Advanced TypeScript features, generics, and type manipulation',
    cardCount: 67,
    studiedCount: 23,
    difficulty: 'hard' as const,
    category: 'Programming',
    lastStudied: new Date('2024-01-12'),
    isFavorite: true,
    color: 'from-purple-500 to-pink-500'
  },
  {
    id: '4',
    name: 'CSS Grid & Flexbox',
    description: 'Modern CSS layout techniques and responsive design',
    cardCount: 34,
    studiedCount: 34,
    difficulty: 'medium' as const,
    category: 'CSS',
    lastStudied: new Date('2024-01-13'),
    isFavorite: false,
    color: 'from-orange-500 to-red-500'
  },
  {
    id: '5',
    name: 'Node.js Backend',
    description: 'Server-side JavaScript, Express.js, and API development',
    cardCount: 52,
    studiedCount: 18,
    difficulty: 'hard' as const,
    category: 'Backend',
    lastStudied: new Date('2024-01-10'),
    isFavorite: false,
    color: 'from-teal-500 to-green-500'
  },
  {
    id: '6',
    name: 'Database Design',
    description: 'SQL, NoSQL, database optimization, and data modeling',
    cardCount: 41,
    studiedCount: 41,
    difficulty: 'medium' as const,
    category: 'Database',
    lastStudied: new Date('2024-01-11'),
    isFavorite: true,
    color: 'from-indigo-500 to-purple-500'
  },
];

const mockProgressData = {
  totalCards: 267,
  studiedCards: 176,
  studyStreak: 7,
  weeklyGoal: 50,
  weeklyProgress: 32,
  accuracy: 87.5,
  level: 3,
  xp: 2450,
  nextLevelXp: 3000
};

export default function EnhancedDashboard() {
  const handleStudy = (deckId: string) => {
    console.log('Starting study session for deck:', deckId);
    // Navigate to study page
  };

  const handleEdit = (deckId: string) => {
    console.log('Editing deck:', deckId);
    // Open edit modal
  };

  const handleDelete = (deckId: string) => {
    console.log('Deleting deck:', deckId);
    // Show confirmation modal
  };

  const handleToggleFavorite = (deckId: string) => {
    console.log('Toggling favorite for deck:', deckId);
    // Update favorite status
  };

  return (
    <MainLayout>
      <div className="space-y-0">
        {/* Hero Section */}
        <DashboardHero userStats={mockUserStats} />
        
        {/* Main Content */}
        <div className="container mx-auto px-4 py-16">
          {/* Quick Actions */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
            className="mb-12"
          >
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <EnhancedButton variant="study" size="lg" className="min-w-[200px]">
                <Brain className="w-5 h-5 mr-2" />
                Continue Studying
              </EnhancedButton>
              
              <EnhancedButton variant="outline" size="lg" className="min-w-[200px]">
                <Plus className="w-5 h-5 mr-2" />
                Create New Deck
              </EnhancedButton>
              
              <EnhancedButton variant="glass" size="lg" className="min-w-[200px]">
                <BarChart3 className="w-5 h-5 mr-2" />
                View Progress
              </EnhancedButton>
            </div>
          </motion.div>

          {/* Recent Decks Section */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            viewport={{ once: true }}
            className="mb-16"
          >
            <div className="flex items-center justify-between mb-8">
              <div>
                <h2 className="text-3xl font-bold mb-2 gradient-text">
                  Your Decks
                </h2>
                <p className="text-muted-foreground">
                  Continue your learning journey
                </p>
              </div>
              
              <EnhancedButton variant="outline">
                <BookOpen className="w-4 h-4 mr-2" />
                View All
              </EnhancedButton>
            </div>
            
            <DeckGrid
              decks={mockDecks}
              onStudy={handleStudy}
              onEdit={handleEdit}
              onDelete={handleDelete}
              onToggleFavorite={handleToggleFavorite}
            />
          </motion.div>

          {/* Progress Section */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            viewport={{ once: true }}
          >
            <ProgressVisualization data={mockProgressData} />
          </motion.div>
        </div>
      </div>
    </MainLayout>
  );
}

export { EnhancedDashboard };
