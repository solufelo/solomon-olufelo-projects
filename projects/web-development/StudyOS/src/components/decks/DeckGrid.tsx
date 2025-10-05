'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Play, Edit, Trash2, MoreHorizontal, Star, Clock, Target } from 'lucide-react';
import { EnhancedButton } from '../ui/enhanced-button';
import { StudyCard, ProgressCard, GlassCard } from '../ui/enhanced-card';
import { useStaggeredAnimation } from '../../lib/animation-hooks';

interface DeckData {
  id: string;
  name: string;
  description: string;
  cardCount: number;
  studiedCount: number;
  difficulty: 'easy' | 'medium' | 'hard';
  category: string;
  lastStudied?: Date;
  isFavorite?: boolean;
  color?: string;
}

interface DeckGridProps {
  decks: DeckData[];
  onStudy?: (deckId: string) => void;
  onEdit?: (deckId: string) => void;
  onDelete?: (deckId: string) => void;
  onToggleFavorite?: (deckId: string) => void;
  className?: string;
}

export default function DeckGrid({ 
  decks, 
  onStudy, 
  onEdit, 
  onDelete, 
  onToggleFavorite,
  className = '' 
}: DeckGridProps) {
  const visibleItems = useStaggeredAnimation(decks, 100);

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy': return 'from-green-500 to-emerald-600';
      case 'medium': return 'from-yellow-500 to-orange-600';
      case 'hard': return 'from-red-500 to-rose-600';
      default: return 'from-blue-500 to-purple-600';
    }
  };

  const getProgressPercentage = (studied: number, total: number) => {
    return total > 0 ? (studied / total) * 100 : 0;
  };

  return (
    <div className={`deck-grid ${className}`}>
      <motion.div
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
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
        {decks.map((deck, index) => (
          <motion.div
            key={deck.id}
            variants={{
              hidden: { opacity: 0, y: 30 },
              visible: { opacity: 1, y: 0 }
            }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <ProgressCard
              progress={getProgressPercentage(deck.studiedCount, deck.cardCount)}
              className="group h-full"
            >
              {/* Header */}
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  <motion.div
                    className={`w-12 h-12 rounded-xl bg-gradient-to-r ${getDifficultyColor(deck.difficulty)} flex items-center justify-center`}
                    whileHover={{ rotate: 360, scale: 1.1 }}
                    transition={{ duration: 0.6 }}
                  >
                    <BookOpen className="w-6 h-6 text-white" />
                  </motion.div>
                  
                  <div className="flex-1">
                    <h3 className="font-semibold text-lg leading-tight mb-1">
                      {deck.name}
                    </h3>
                    <p className="text-sm text-muted-foreground">
                      {deck.category}
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-1">
                  {/* Favorite Button */}
                  <motion.button
                    onClick={() => onToggleFavorite?.(deck.id)}
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.9 }}
                    className="p-1 rounded-lg hover:bg-muted transition-colors"
                  >
                    <Star 
                      className={`w-4 h-4 ${
                        deck.isFavorite 
                          ? 'fill-yellow-400 text-yellow-400' 
                          : 'text-muted-foreground hover:text-yellow-400'
                      }`} 
                    />
                  </motion.button>

                  {/* More Options */}
                  <EnhancedButton variant="ghost" size="icon" className="opacity-0 group-hover:opacity-100 transition-opacity">
                    <MoreHorizontal className="w-4 h-4" />
                  </EnhancedButton>
                </div>
              </div>

              {/* Description */}
              <p className="text-sm text-muted-foreground mb-4 line-clamp-2">
                {deck.description}
              </p>

              {/* Stats */}
              <div className="grid grid-cols-2 gap-4 mb-6">
                <div className="text-center">
                  <div className="flex items-center justify-center gap-1 mb-1">
                    <Target className="w-4 h-4 text-muted-foreground" />
                    <span className="text-sm text-muted-foreground">Cards</span>
                  </div>
                  <p className="text-lg font-semibold">
                    {deck.studiedCount}/{deck.cardCount}
                  </p>
                </div>
                
                <div className="text-center">
                  <div className="flex items-center justify-center gap-1 mb-1">
                    <Clock className="w-4 h-4 text-muted-foreground" />
                    <span className="text-sm text-muted-foreground">Last Study</span>
                  </div>
                  <p className="text-sm font-medium">
                    {deck.lastStudied 
                      ? new Date(deck.lastStudied).toLocaleDateString()
                      : 'Never'
                    }
                  </p>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex gap-2">
                <EnhancedButton
                  variant="study"
                  size="sm"
                  className="flex-1"
                  onClick={() => onStudy?.(deck.id)}
                >
                  <Play className="w-4 h-4 mr-2" />
                  Study
                </EnhancedButton>
                
                <EnhancedButton
                  variant="outline"
                  size="icon"
                  onClick={() => onEdit?.(deck.id)}
                >
                  <Edit className="w-4 h-4" />
                </EnhancedButton>
                
                <EnhancedButton
                  variant="destructive"
                  size="icon"
                  onClick={() => onDelete?.(deck.id)}
                >
                  <Trash2 className="w-4 h-4" />
                </EnhancedButton>
              </div>
            </ProgressCard>
          </motion.div>
        ))}
      </motion.div>

      {/* Empty State */}
      {decks.length === 0 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center py-16"
        >
          <div className="w-24 h-24 mx-auto mb-6 bg-muted rounded-full flex items-center justify-center">
            <BookOpen className="w-12 h-12 text-muted-foreground" />
          </div>
          <h3 className="text-xl font-semibold mb-2">No decks yet</h3>
          <p className="text-muted-foreground mb-6">
            Create your first deck to start studying
          </p>
          <EnhancedButton variant="study">
            Create New Deck
          </EnhancedButton>
        </motion.div>
      )}
    </div>
  );
}
