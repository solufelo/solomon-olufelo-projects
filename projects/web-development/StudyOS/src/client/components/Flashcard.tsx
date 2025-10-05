import React, { useState } from 'react';

/**
 * Flashcard Component with 3D flip animation
 * Supports click-to-flip interaction with smooth transitions
 */

interface FlashcardProps {
  question: string;
  answer: string;
  onFlip?: (isFlipped: boolean) => void;
  className?: string;
}

export const Flashcard: React.FC<FlashcardProps> = ({ 
  question, 
  answer, 
  onFlip,
  className = '' 
}) => {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleFlip = () => {
    const newFlippedState = !isFlipped;
    setIsFlipped(newFlippedState);
    onFlip?.(newFlippedState);
  };

  return (
    <div 
      className={`flashcard-container ${className}`} 
      style={{ perspective: '1000px' }}
    >
      <div
        className={`flashcard cursor-pointer transition-transform duration-600 ease-in-out ${
          isFlipped ? 'is-flipped' : ''
        }`}
        onClick={handleFlip}
        style={{
          transformStyle: 'preserve-3d',
          transform: isFlipped ? 'rotateY(180deg)' : 'rotateY(0deg)',
        }}
      >
        {/* Front Face */}
        <div
          className="flashcard-face front absolute w-full h-full bg-[var(--card)] rounded-xl p-8 
                     border border-[var(--border)] flex items-center justify-center shadow-lg"
          style={{
            backfaceVisibility: 'hidden',
            WebkitBackfaceVisibility: 'hidden',
          }}
        >
          <div className="text-center">
            <div className="text-sm text-[var(--muted-foreground)] mb-2 uppercase tracking-wide">
              Question
            </div>
            <h3 className="text-2xl font-semibold text-[var(--card-foreground)]">
              {question}
            </h3>
            <div className="mt-6 text-xs text-[var(--muted-foreground)] opacity-60">
              Click to reveal answer
            </div>
          </div>
        </div>

        {/* Back Face */}
        <div
          className="flashcard-face back absolute w-full h-full bg-[var(--card)] rounded-xl p-8 
                     border border-[var(--border)] flex items-center justify-center shadow-lg"
          style={{
            backfaceVisibility: 'hidden',
            WebkitBackfaceVisibility: 'hidden',
            transform: 'rotateY(180deg)',
          }}
        >
          <div className="text-center">
            <div className="text-sm text-[var(--primary)] mb-2 uppercase tracking-wide font-medium">
              Answer
            </div>
            <h3 className="text-2xl font-semibold text-[var(--primary)]">
              {answer}
            </h3>
            <div className="mt-6 text-xs text-[var(--muted-foreground)] opacity-60">
              Click to flip back
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

/**
 * Flashcard Review Component
 * Enhanced flashcard with review difficulty buttons
 */

interface ReviewFlashcardProps extends FlashcardProps {
  onReview?: (difficulty: 'again' | 'hard' | 'good' | 'easy') => void;
  showReviewButtons?: boolean;
}

export const ReviewFlashcard: React.FC<ReviewFlashcardProps> = ({
  question,
  answer,
  onReview,
  showReviewButtons = true,
  className = '',
}) => {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleReview = (difficulty: 'again' | 'hard' | 'good' | 'easy') => {
    onReview?.(difficulty);
    // Reset flip state after review
    setTimeout(() => setIsFlipped(false), 300);
  };

  return (
    <div className={`space-y-4 ${className}`}>
      <Flashcard
        question={question}
        answer={answer}
        onFlip={setIsFlipped}
        className="min-h-[300px]"
      />

      {/* Review Buttons - Only show when card is flipped and enabled */}
      {showReviewButtons && isFlipped && (
        <div className="flex gap-3 justify-center animate-fade-in">
          <button
            onClick={() => handleReview('again')}
            className="btn btn-sm btn-destructive"
            title="I didn't know this"
          >
            Again
          </button>
          <button
            onClick={() => handleReview('hard')}
            className="btn btn-sm btn-outline"
            title="I knew this, but it was difficult"
          >
            Hard
          </button>
          <button
            onClick={() => handleReview('good')}
            className="btn btn-sm btn-primary"
            title="I knew this"
          >
            Good
          </button>
          <button
            onClick={() => handleReview('easy')}
            className="btn btn-sm bg-[var(--success)] text-white hover:opacity-90"
            title="This was very easy"
          >
            Easy
          </button>
        </div>
      )}
    </div>
  );
};

export default Flashcard;

