import React from 'react';
import { theme, themeVariants, type ThemeVariant } from '../../theme';

interface StudySetCardProps {
  /** Study set title */
  title: string;
  /** Number of cards in the set */
  cardCount: number;
  /** Study set description */
  description?: string;
  /** Author/creator name */
  author?: string;
  /** Author avatar */
  authorAvatar?: string;
  /** Study progress (0-100) */
  progress?: number;
  /** Last studied date */
  lastStudied?: Date;
  /** Theme variant */
  variant?: ThemeVariant;
  /** Layout style */
  layout?: 'grid' | 'list' | 'compact';
  /** Click handler */
  onClick?: () => void;
  /** Study button click handler */
  onStudy?: () => void;
  /** Edit button click handler */
  onEdit?: () => void;
  /** Delete button click handler */
  onDelete?: () => void;
  /** Custom className */
  className?: string;
  /** Whether card is interactive */
  interactive?: boolean;
  /** Tags/categories */
  tags?: string[];
  /** Difficulty level */
  difficulty?: 'easy' | 'medium' | 'hard';
}

const StudySetCard: React.FC<StudySetCardProps> = ({
  title,
  cardCount,
  description,
  author,
  authorAvatar,
  progress,
  lastStudied,
  variant = 'hybrid',
  layout = 'grid',
  onClick,
  onStudy,
  onEdit,
  onDelete,
  className = '',
  interactive = true,
  tags = [],
  difficulty,
}) => {
  const variantStyles = themeVariants[variant];

  const baseStyles = `
    transition-all duration-200 ease-in-out
    ${interactive ? 'cursor-pointer hover:shadow-lg' : ''}
    ${variant === 'quizlet' ? 'transform hover:scale-105' : ''}
    ${className}
  `;

  const cardStyles = {
    backgroundColor: variantStyles.surface,
    borderColor: variantStyles.border,
    borderWidth: variant === 'quizlet' ? '2px' : '1px',
    borderRadius: variant === 'quizlet' ? theme.borderRadius['2xl'] : theme.borderRadius.lg,
    boxShadow: variantStyles.shadow.base,
  };

  const getDifficultyColor = () => {
    switch (difficulty) {
      case 'easy': return theme.colors.semantic.success;
      case 'medium': return theme.colors.semantic.warning;
      case 'hard': return theme.colors.semantic.error;
      default: return variantStyles.textSecondary;
    }
  };

  const formatLastStudied = (date: Date) => {
    const now = new Date();
    const diffTime = Math.abs(now.getTime() - date.getTime());
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`;
    return `${Math.ceil(diffDays / 30)} months ago`;
  };

  // Grid layout (Quizlet-style)
  if (layout === 'grid') {
    return (
      <div 
        className={`${baseStyles} border rounded-xl p-6`}
        style={cardStyles}
        onClick={onClick}
      >
        {/* Header */}
        <div className="flex items-start justify-between mb-4">
          <div className="flex-1">
            <h3 
              className="text-lg font-semibold mb-2 line-clamp-2"
              style={{ color: variantStyles.text }}
            >
              {title}
            </h3>
            <div className="flex items-center space-x-4 text-sm">
              <span style={{ color: variantStyles.textSecondary }}>
                {cardCount} {cardCount === 1 ? 'card' : 'cards'}
              </span>
              {difficulty && (
                <span 
                  className="px-2 py-1 rounded-full text-xs font-medium"
                  style={{ 
                    backgroundColor: getDifficultyColor() + '20',
                    color: getDifficultyColor()
                  }}
                >
                  {difficulty}
                </span>
              )}
            </div>
          </div>
          
          {/* Actions */}
          <div className="flex items-center space-x-2">
            {onEdit && (
              <button
                onClick={(e) => { e.stopPropagation(); onEdit(); }}
                className="p-2 rounded-full hover:bg-gray-100 transition-colors"
                style={{ color: variantStyles.textSecondary }}
              >
                ✏️
              </button>
            )}
            {onDelete && (
              <button
                onClick={(e) => { e.stopPropagation(); onDelete(); }}
                className="p-2 rounded-full hover:bg-red-50 transition-colors text-red-500"
              >
                🗑️
              </button>
            )}
          </div>
        </div>

        {/* Description */}
        {description && (
          <p 
            className="text-sm mb-4 line-clamp-2"
            style={{ color: variantStyles.textSecondary }}
          >
            {description}
          </p>
        )}

        {/* Tags */}
        {tags.length > 0 && (
          <div className="flex flex-wrap gap-2 mb-4">
            {tags.slice(0, 3).map((tag, index) => (
              <span
                key={index}
                className="px-2 py-1 rounded-full text-xs"
                style={{
                  backgroundColor: variantStyles.primary + '15',
                  color: variantStyles.primary,
                }}
              >
                {tag}
              </span>
            ))}
            {tags.length > 3 && (
              <span 
                className="text-xs"
                style={{ color: variantStyles.textSecondary }}
              >
                +{tags.length - 3} more
              </span>
            )}
          </div>
        )}

        {/* Progress */}
        {progress !== undefined && (
          <div className="mb-4">
            <div className="flex justify-between text-sm mb-1">
              <span style={{ color: variantStyles.textSecondary }}>Progress</span>
              <span style={{ color: variantStyles.text }}>{progress}%</span>
            </div>
            <div 
              className="w-full bg-gray-200 rounded-full h-2"
              style={{ backgroundColor: variantStyles.border }}
            >
              <div
                className="h-2 rounded-full transition-all duration-300"
                style={{
                  width: `${progress}%`,
                  backgroundColor: variantStyles.primary,
                }}
              />
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            {author && (
              <>
                {authorAvatar ? (
                  <img
                    src={authorAvatar}
                    alt={author}
                    className="w-6 h-6 rounded-full"
                  />
                ) : (
                  <div 
                    className="w-6 h-6 rounded-full flex items-center justify-center text-xs font-medium"
                    style={{
                      backgroundColor: variantStyles.primary,
                      color: 'white',
                    }}
                  >
                    {author.charAt(0).toUpperCase()}
                  </div>
                )}
                <span 
                  className="text-sm"
                  style={{ color: variantStyles.textSecondary }}
                >
                  {author}
                </span>
              </>
            )}
          </div>
          
          {lastStudied && (
            <span 
              className="text-xs"
              style={{ color: variantStyles.textSecondary }}
            >
              {formatLastStudied(lastStudied)}
            </span>
          )}
        </div>

        {/* Study Button */}
        {onStudy && (
          <button
            onClick={(e) => { e.stopPropagation(); onStudy(); }}
            className="w-full mt-4 py-2 px-4 rounded-lg font-medium transition-all duration-200"
            style={{
              backgroundColor: variantStyles.primary,
              color: 'white',
              borderRadius: variant === 'quizlet' ? theme.borderRadius.full : theme.borderRadius.lg,
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor = variantStyles.primary + 'DD';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = variantStyles.primary;
            }}
          >
            Study Now
          </button>
        )}
      </div>
    );
  }

  // List layout (Anki-style)
  if (layout === 'list') {
    return (
      <div 
        className={`${baseStyles} border rounded-lg p-4 flex items-center space-x-4`}
        style={cardStyles}
        onClick={onClick}
      >
        <div className="flex-1">
          <div className="flex items-center space-x-4">
            <h3 
              className="font-semibold"
              style={{ color: variantStyles.text }}
            >
              {title}
            </h3>
            <span 
              className="text-sm"
              style={{ color: variantStyles.textSecondary }}
            >
              {cardCount} cards
            </span>
            {difficulty && (
              <span 
                className="px-2 py-1 rounded text-xs font-medium"
                style={{ 
                  backgroundColor: getDifficultyColor() + '20',
                  color: getDifficultyColor()
                }}
              >
                {difficulty}
              </span>
            )}
          </div>
          {description && (
            <p 
              className="text-sm mt-1 line-clamp-1"
              style={{ color: variantStyles.textSecondary }}
            >
              {description}
            </p>
          )}
        </div>

        <div className="flex items-center space-x-4">
          {progress !== undefined && (
            <div className="flex items-center space-x-2">
              <div 
                className="w-16 bg-gray-200 rounded-full h-2"
                style={{ backgroundColor: variantStyles.border }}
              >
                <div
                  className="h-2 rounded-full"
                  style={{
                    width: `${progress}%`,
                    backgroundColor: variantStyles.primary,
                  }}
                />
              </div>
              <span 
                className="text-xs w-8 text-right"
                style={{ color: variantStyles.textSecondary }}
              >
                {progress}%
              </span>
            </div>
          )}

          {lastStudied && (
            <span 
              className="text-xs whitespace-nowrap"
              style={{ color: variantStyles.textSecondary }}
            >
              {formatLastStudied(lastStudied)}
            </span>
          )}

          <div className="flex items-center space-x-2">
            {onStudy && (
              <button
                onClick={(e) => { e.stopPropagation(); onStudy(); }}
                className="px-3 py-1 rounded text-sm font-medium transition-colors"
                style={{
                  backgroundColor: variantStyles.primary,
                  color: 'white',
                }}
              >
                Study
              </button>
            )}
            {onEdit && (
              <button
                onClick={(e) => { e.stopPropagation(); onEdit(); }}
                className="p-1 rounded hover:bg-gray-100 transition-colors"
                style={{ color: variantStyles.textSecondary }}
              >
                ✏️
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  // Compact layout
  return (
    <div 
      className={`${baseStyles} border rounded p-3 flex items-center justify-between`}
      style={cardStyles}
      onClick={onClick}
    >
      <div>
        <h4 
          className="font-medium"
          style={{ color: variantStyles.text }}
        >
          {title}
        </h4>
        <span 
          className="text-sm"
          style={{ color: variantStyles.textSecondary }}
        >
          {cardCount} cards
        </span>
      </div>
      
      {onStudy && (
        <button
          onClick={(e) => { e.stopPropagation(); onStudy(); }}
          className="px-2 py-1 rounded text-sm transition-colors"
          style={{
            backgroundColor: variantStyles.primary + '20',
            color: variantStyles.primary,
          }}
        >
          Study
        </button>
      )}
    </div>
  );
};

export default StudySetCard;
