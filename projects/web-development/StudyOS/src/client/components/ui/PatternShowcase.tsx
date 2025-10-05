import React, { useState } from 'react';
import { cn } from '../../lib/utils';
import Card from './Card';
import Button from './Button';

interface PatternShowcaseProps {
  className?: string;
}

const patterns = [
  {
    name: 'Aurora Waves',
    description: 'Dreamy aurora waves pattern',
    className: 'bg-aurora-waves',
    category: 'aurora'
  },
  {
    name: 'Aurora Dream',
    description: 'Soft aurora dream pattern',
    className: 'bg-aurora-dream',
    category: 'aurora'
  },
  {
    name: 'Aurora Silk',
    description: 'Silky aurora gradient',
    className: 'bg-aurora-silk',
    category: 'aurora'
  },
  {
    name: 'Cosmic Aurora',
    description: 'Cosmic aurora with multiple gradients',
    className: 'bg-cosmic-aurora',
    category: 'cosmic'
  },
  {
    name: 'Stellar Mist',
    description: 'Stellar mist with scattered glows',
    className: 'bg-stellar-mist',
    category: 'cosmic'
  },
  {
    name: 'Midnight Aurora',
    description: 'Dark midnight aurora',
    className: 'bg-midnight-aurora',
    category: 'dark'
  },
  {
    name: 'Grid Pattern',
    description: 'Subtle grid pattern',
    className: 'bg-grid-subtle bg-grid-md',
    category: 'grid'
  },
  {
    name: 'Paper Texture',
    description: 'Paper texture with noise',
    className: 'bg-paper-texture bg-noise-texture',
    category: 'texture'
  },
];

const categories = ['all', 'aurora', 'cosmic', 'dark', 'grid', 'texture'];

export const PatternShowcase: React.FC<PatternShowcaseProps> = ({ className }) => {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedPattern, setSelectedPattern] = useState(patterns[0]);

  const filteredPatterns = selectedCategory === 'all' 
    ? patterns 
    : patterns.filter(pattern => pattern.category === selectedCategory);

  return (
    <div className={cn('space-y-6', className)}>
      {/* Category Filter */}
      <div className="flex flex-wrap gap-2">
        {categories.map((category) => (
          <Button
            key={category}
            variant={selectedCategory === category ? 'primary' : 'ghost'}
            size="sm"
            onClick={() => setSelectedCategory(category)}
            className="capitalize"
          >
            {category}
          </Button>
        ))}
      </div>

      {/* Preview Card */}
      <Card variant="elevated" className="overflow-hidden">
        <div className={cn(
          'h-64 w-full relative rounded-lg overflow-hidden',
          selectedPattern.className
        )}>
          <div className="absolute inset-0 bg-black/10 flex items-center justify-center">
            <div className="text-center text-white">
              <h3 className="text-2xl font-bold mb-2 drop-shadow-lg">
                {selectedPattern.name}
              </h3>
              <p className="text-sm opacity-90 drop-shadow">
                {selectedPattern.description}
              </p>
            </div>
          </div>
        </div>
        
        <div className="p-4 bg-white">
          <h4 className="font-semibold text-neutral-900 mb-2">CSS Class</h4>
          <code className="text-sm bg-neutral-100 px-2 py-1 rounded text-neutral-800">
            {selectedPattern.className}
          </code>
        </div>
      </Card>

      {/* Pattern Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {filteredPatterns.map((pattern) => (
          <Card
            key={pattern.name}
            hover
            interactive
            onClick={() => setSelectedPattern(pattern)}
            className={cn(
              'cursor-pointer transition-all duration-200',
              selectedPattern.name === pattern.name && 'ring-2 ring-brand-500'
            )}
          >
            <div className={cn(
              'h-24 w-full rounded-lg mb-3',
              pattern.className
            )} />
            <div className="space-y-1">
              <h5 className="font-medium text-sm text-neutral-900">
                {pattern.name}
              </h5>
              <p className="text-xs text-neutral-600">
                {pattern.description}
              </p>
            </div>
          </Card>
        ))}
      </div>

      {/* Usage Example */}
      <Card variant="outlined" className="bg-neutral-50">
        <h4 className="font-semibold text-neutral-900 mb-3">Usage Example</h4>
        <div className="bg-neutral-900 rounded-lg p-4 overflow-x-auto">
          <pre className="text-green-400 text-sm">
{`// Using in PageLayout
<PageLayout background="aurora">
  {children}
</PageLayout>

// Using directly with Tailwind
<div className="${selectedPattern.className}">
  Your content here
</div>`}
          </pre>
        </div>
      </Card>
    </div>
  );
};

export default PatternShowcase;

