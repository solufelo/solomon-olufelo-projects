import React, { useState } from 'react';
import { theme, themeVariants, componentTokens, type ThemeVariant } from '../../theme';

interface FlashcardProps {
  /** Front content of the card */
  front: React.ReactNode;
  /** Back content of the card */
  back: React.ReactNode;
  /** Theme variant to apply */
  variant?: ThemeVariant;
  /** Whether the card starts flipped */
  initialFlipped?: boolean;
  /** Custom className */
  className?: string;
  /** Click handler */
  onClick?: () => void;
  /** Whether the card is interactive (clickable to flip) */
  interactive?: boolean;
  /** Size variant */
  size?: 'sm' | 'md' | 'lg';
  /** Whether to show flip indicator */
  showFlipIndicator?: boolean;
}

const Flashcard: React.FC<FlashcardProps> = ({
  front,
  back,
  variant = 'hybrid',
  initialFlipped = false,
  className = '',
  onClick,
  interactive = true,
  size = 'md',
  showFlipIndicator = true,
}) => {
  const [isFlipped, setIsFlipped] = useState(initialFlipped);
  
  const handleClick = () => {
    if (interactive) {
      setIsFlipped(!isFlipped);
    }
    onClick?.();
  };

  const variantStyles = themeVariants[variant];
  const cardTokens = variant === 'quizlet' 
    ? componentTokens.flashcard.quizlet 
    : componentTokens.flashcard.anki;

  const sizeStyles = {
    sm: 'min-h-[120px] text-sm',
    md: 'min-h-[180px] text-base',
    lg: 'min-h-[240px] text-lg',
  };

  const baseStyles = `
    relative w-full ${sizeStyles[size]}
    cursor-pointer select-none
    transition-all duration-300 ease-in-out
    transform-gpu perspective-1000
    ${interactive ? 'hover:scale-105' : ''}
    ${className}
  `;

  const cardFaceStyles = `
    absolute inset-0 w-full h-full
    flex items-center justify-center
    p-6 rounded-xl
    backface-hidden
    transition-transform duration-500 ease-in-out
    border shadow-lg
  `;

  const frontStyles = `
    ${cardFaceStyles}
    ${isFlipped ? 'rotate-y-180' : 'rotate-y-0'}
  `;

  const backStyles = `
    ${cardFaceStyles}
    ${isFlipped ? 'rotate-y-0' : 'rotate-y-180'}
  `;

  // Dynamic styles based on variant
  const dynamicStyles = {
    backgroundColor: variantStyles.surface,
    borderColor: variant === 'quizlet' ? variantStyles.primary : variantStyles.border,
    borderWidth: variant === 'quizlet' ? '2px' : '1px',
    borderRadius: cardTokens.borderRadius,
    boxShadow: variant === 'quizlet' ? variantStyles.shadow.md : variantStyles.shadow.base,
  };

  return (
    <div className={baseStyles} onClick={handleClick}>
      {/* Front of card */}
      <div 
        className={frontStyles}
        style={dynamicStyles}
      >
        <div className="text-center w-full">
          {front}
          {showFlipIndicator && (
            <div className="absolute bottom-3 right-3 text-xs opacity-60">
              {variant === 'quizlet' ? '🔄' : 'Click to flip'}
            </div>
          )}
        </div>
      </div>

      {/* Back of card */}
      <div 
        className={backStyles}
        style={{
          ...dynamicStyles,
          backgroundColor: variant === 'quizlet' 
            ? themeVariants.quizlet.accent + '20' 
            : variantStyles.surface,
        }}
      >
        <div className="text-center w-full">
          {back}
          {showFlipIndicator && (
            <div className="absolute bottom-3 right-3 text-xs opacity-60">
              {variant === 'quizlet' ? '🔄' : 'Click to flip'}
            </div>
          )}
        </div>
      </div>

      {/* Flip indicator for Quizlet style */}
      {variant === 'quizlet' && showFlipIndicator && (
        <div className="absolute top-3 right-3 w-6 h-6 bg-white rounded-full flex items-center justify-center shadow-sm text-xs">
          ↻
        </div>
      )}
    </div>
  );
};

export default Flashcard;

// CSS for 3D flip animation (add to global styles)
export const flashcardStyles = `
  .perspective-1000 {
    perspective: 1000px;
  }
  
  .backface-hidden {
    backface-visibility: hidden;
  }
  
  .rotate-y-0 {
    transform: rotateY(0deg);
  }
  
  .rotate-y-180 {
    transform: rotateY(180deg);
  }
  
  .transform-gpu {
    transform: translate3d(0, 0, 0);
  }
`;
