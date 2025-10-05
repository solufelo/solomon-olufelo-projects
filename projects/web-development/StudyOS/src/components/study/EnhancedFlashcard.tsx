'use client';

import React, { useState, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { RotateCcw, CheckCircle, XCircle, Clock, Star } from 'lucide-react';
import { EnhancedButton } from '../ui/enhanced-button';
import { Card, CardContent } from '../ui/enhanced-card';

interface FlashcardData {
  id: string;
  question: string;
  answer: string;
  difficulty?: 'easy' | 'medium' | 'hard';
  category?: string;
  lastReviewed?: Date;
  reviewCount?: number;
}

interface EnhancedFlashcardProps {
  card: FlashcardData;
  onAnswer: (cardId: string, difficulty: 'again' | 'hard' | 'good' | 'easy') => void;
  className?: string;
}

export default function EnhancedFlashcard({ 
  card, 
  onAnswer, 
  className = '' 
}: EnhancedFlashcardProps) {
  const [isFlipped, setIsFlipped] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [selectedDifficulty, setSelectedDifficulty] = useState<string | null>(null);
  const cardRef = useRef<HTMLDivElement>(null);

  const handleFlip = () => {
    if (!isFlipped) {
      setIsFlipped(true);
      setShowAnswer(true);
    }
  };

  const handleAnswer = (difficulty: 'again' | 'hard' | 'good' | 'easy') => {
    setSelectedDifficulty(difficulty);
    onAnswer(card.id, difficulty);
    
    // Reset after a short delay
    setTimeout(() => {
      setIsFlipped(false);
      setShowAnswer(false);
      setSelectedDifficulty(null);
    }, 1500);
  };

  const getDifficultyColor = (difficulty?: string) => {
    switch (difficulty) {
      case 'easy': return 'from-green-500 to-emerald-600';
      case 'medium': return 'from-yellow-500 to-orange-600';
      case 'hard': return 'from-red-500 to-rose-600';
      default: return 'from-blue-500 to-purple-600';
    }
  };

  const getDifficultyIcon = (difficulty?: string) => {
    switch (difficulty) {
      case 'easy': return <CheckCircle className="w-4 h-4" />;
      case 'medium': return <Clock className="w-4 h-4" />;
      case 'hard': return <XCircle className="w-4 h-4" />;
      default: return <Star className="w-4 h-4" />;
    }
  };

  return (
    <div className={`enhanced-flashcard w-full max-w-2xl mx-auto ${className}`}>
      <motion.div
        ref={cardRef}
        className="relative w-full h-96 cursor-pointer"
        onClick={handleFlip}
        whileHover={{ scale: 1.02 }}
        transition={{ duration: 0.3 }}
        style={{ transformStyle: "preserve-3d" }}
      >
        {/* Card Container */}
        <AnimatePresence mode="wait">
          {!showAnswer ? (
            // Question Side
            <motion.div
              key="question"
              initial={{ rotateY: 0 }}
              exit={{ rotateY: 90 }}
              transition={{ duration: 0.6 }}
              className="absolute inset-0 w-full h-full"
            >
              <Card className="w-full h-full flex flex-col justify-center items-center p-8 bg-gradient-to-br from-card to-card/80 border-primary/20">
                {/* Difficulty Badge */}
                {card.difficulty && (
                  <motion.div
                    initial={{ opacity: 0, scale: 0 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.5, delay: 0.2 }}
                    className={`absolute top-4 right-4 px-3 py-1 rounded-full bg-gradient-to-r ${getDifficultyColor(card.difficulty)} text-white text-xs font-medium flex items-center gap-1`}
                  >
                    {getDifficultyIcon(card.difficulty)}
                    {card.difficulty}
                  </motion.div>
                )}

                {/* Category */}
                {card.category && (
                  <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.5, delay: 0.1 }}
                    className="absolute top-4 left-4 px-3 py-1 rounded-full bg-muted text-muted-foreground text-xs font-medium"
                  >
                    {card.category}
                  </motion.div>
                )}

                <CardContent className="text-center space-y-6">
                  <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                    className="text-6xl mb-4"
                  >
                    🤔
                  </motion.div>
                  
                  <motion.h2
                    className="text-2xl md:text-3xl font-semibold text-foreground leading-relaxed"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                  >
                    {card.question}
                  </motion.h2>
                  
                  <motion.p
                    className="text-muted-foreground text-sm"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                  >
                    Click to reveal answer
                  </motion.p>
                </CardContent>

                {/* Flip Hint */}
                <motion.div
                  className="absolute bottom-4 right-4 opacity-50"
                  animate={{ rotate: [0, 10, 0] }}
                  transition={{ duration: 2, repeat: Infinity }}
                >
                  <RotateCcw className="w-6 h-6 text-muted-foreground" />
                </motion.div>
              </Card>
            </motion.div>
          ) : (
            // Answer Side
            <motion.div
              key="answer"
              initial={{ rotateY: -90 }}
              animate={{ rotateY: 0 }}
              transition={{ duration: 0.6 }}
              className="absolute inset-0 w-full h-full"
            >
              <Card className="w-full h-full flex flex-col justify-center items-center p-8 bg-gradient-to-br from-primary/10 to-secondary/10 border-primary/40">
                <CardContent className="text-center space-y-8">
                  <motion.div
                    initial={{ opacity: 0, scale: 0 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.5, delay: 0.2 }}
                    className="text-6xl mb-4"
                  >
                    💡
                  </motion.div>
                  
                  <motion.h3
                    className="text-2xl md:text-3xl font-semibold text-foreground leading-relaxed"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                  >
                    {card.answer}
                  </motion.h3>
                </CardContent>

                {/* Answer Buttons */}
                <motion.div
                  className="absolute bottom-6 left-6 right-6"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.5 }}
                >
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                    {[
                      { difficulty: 'again' as const, label: 'Again', color: 'destructive', icon: '🔄' },
                      { difficulty: 'hard' as const, label: 'Hard', color: 'warning', icon: '😰' },
                      { difficulty: 'good' as const, label: 'Good', color: 'study', icon: '👍' },
                      { difficulty: 'easy' as const, label: 'Easy', color: 'correct', icon: '😎' },
                    ].map((option) => (
                      <motion.div
                        key={option.difficulty}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                      >
                        <EnhancedButton
                          variant={option.color as any}
                          size="sm"
                          className="w-full text-xs"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleAnswer(option.difficulty);
                          }}
                          disabled={selectedDifficulty !== null}
                        >
                          <span className="mr-1">{option.icon}</span>
                          {option.label}
                        </EnhancedButton>
                      </motion.div>
                    ))}
                  </div>
                </motion.div>
              </Card>
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>

      {/* Success Animation */}
      <AnimatePresence>
        {selectedDifficulty && (
          <motion.div
            initial={{ opacity: 0, scale: 0 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0 }}
            className="fixed inset-0 flex items-center justify-center z-50 pointer-events-none"
          >
            <motion.div
              className="text-8xl"
              animate={{ 
                scale: [1, 1.5, 1],
                rotate: [0, 360, 0]
              }}
              transition={{ duration: 1 }}
            >
              {selectedDifficulty === 'good' || selectedDifficulty === 'easy' ? '🎉' : '💪'}
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
