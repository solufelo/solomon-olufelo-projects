import React from 'react';
import PageLayout from '../components/layout/PageLayout';
import Container from '../components/ui/Container';
import Card from '../components/ui/Card';
import Badge from '../components/ui/Badge';
import PatternShowcase from '../components/ui/PatternShowcase';

const PatternsPage: React.FC = () => {
  return (
    <PageLayout 
      title="Pattern Gallery" 
      background="cosmic"
      breadcrumbs={[
        { label: 'Dashboard', href: '/' },
        { label: 'Pattern Gallery' }
      ]}
    >
      {/* Header Section */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h1 className="text-3xl lg:text-4xl font-display font-bold text-neutral-900 mb-2">
              Pattern Gallery ✨
            </h1>
            <p className="text-lg text-neutral-600">
              Beautiful background patterns powered by{' '}
              <a 
                href="https://patterncraft.fun/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-brand-600 hover:text-brand-700 font-medium underline"
              >
                PatternCraft
              </a>
            </p>
          </div>
          <Badge variant="primary" size="lg">
            8+ Patterns
          </Badge>
        </div>
      </div>

      {/* Pattern Categories */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <Card hover className="text-center">
          <div className="w-16 h-16 bg-aurora-waves rounded-2xl mx-auto mb-4 border-4 border-white shadow-medium"></div>
          <h3 className="font-semibold text-neutral-900 mb-2">Aurora Patterns</h3>
          <p className="text-sm text-neutral-600">Dreamy aurora and cosmic effects</p>
        </Card>

        <Card hover className="text-center">
          <div className="w-16 h-16 bg-grid-subtle bg-grid-md rounded-2xl mx-auto mb-4 border-4 border-white shadow-medium"></div>
          <h3 className="font-semibold text-neutral-900 mb-2">Grid Patterns</h3>
          <p className="text-sm text-neutral-600">Subtle grids and geometric layouts</p>
        </Card>

        <Card hover className="text-center">
          <div className="w-16 h-16 bg-paper-texture bg-noise-texture rounded-2xl mx-auto mb-4 border-4 border-white shadow-medium"></div>
          <h3 className="font-semibold text-neutral-900 mb-2">Texture Patterns</h3>
          <p className="text-sm text-neutral-600">Paper textures and noise effects</p>
        </Card>
      </div>

      {/* Interactive Pattern Showcase */}
      <Card variant="elevated" className="mb-8">
        <div className="p-6">
          <h2 className="text-2xl font-display font-bold text-neutral-900 mb-4">
            Interactive Preview
          </h2>
          <p className="text-neutral-600 mb-6">
            Click on any pattern below to preview it and copy the CSS class.
          </p>
          <PatternShowcase />
        </div>
      </Card>

      {/* Implementation Examples */}
      <div className="grid lg:grid-cols-2 gap-6 mb-8">
        <Card variant="outlined">
          <h3 className="font-semibold text-neutral-900 mb-4">Landing Page Example</h3>
          <div className="bg-aurora-waves h-32 rounded-lg mb-4 flex items-center justify-center">
            <div className="text-center text-white drop-shadow-lg">
              <h4 className="font-bold">Welcome to StudyOS</h4>
              <p className="text-sm opacity-90">Beautiful aurora background</p>
            </div>
          </div>
          <code className="text-xs bg-neutral-100 px-2 py-1 rounded block">
            bg-aurora-waves
          </code>
        </Card>

        <Card variant="outlined">
          <h3 className="font-semibold text-neutral-900 mb-4">Dashboard Example</h3>
          <div className="bg-stellar-mist h-32 rounded-lg mb-4 flex items-center justify-center">
            <div className="text-center text-neutral-800">
              <h4 className="font-bold">Dashboard Content</h4>
              <p className="text-sm opacity-75">Stellar mist pattern</p>
            </div>
          </div>
          <code className="text-xs bg-neutral-100 px-2 py-1 rounded block">
            bg-stellar-mist
          </code>
        </Card>
      </div>

      {/* Technical Details */}
      <Card variant="glass" className="bg-white/80">
        <h3 className="font-semibold text-neutral-900 mb-4">Technical Implementation</h3>
        <div className="space-y-4">
          <div>
            <h4 className="font-medium text-neutral-800 mb-2">🎨 Pattern Source</h4>
            <p className="text-sm text-neutral-600">
              All patterns are sourced from{' '}
              <a 
                href="https://patterncraft.fun/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-brand-600 hover:text-brand-700 underline"
              >
                PatternCraft
              </a>
              {' '}and integrated into our Tailwind CSS configuration.
            </p>
          </div>
          
          <div>
            <h4 className="font-medium text-neutral-800 mb-2">⚡ Performance</h4>
            <p className="text-sm text-neutral-600">
              CSS-based patterns with no external dependencies. Optimized for performance with minimal impact on load times.
            </p>
          </div>
          
          <div>
            <h4 className="font-medium text-neutral-800 mb-2">🔧 Customization</h4>
            <p className="text-sm text-neutral-600">
              Patterns can be combined with opacity, overlays, and other Tailwind utilities for endless customization.
            </p>
          </div>
        </div>
      </Card>
    </PageLayout>
  );
};

export { PatternsPage };
export default PatternsPage;

