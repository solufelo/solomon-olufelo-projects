# StudyOS UI Components

A modern, flexible component library inspired by Quizlet's playful design and Anki's minimal efficiency. Built with React, TypeScript, and Tailwind CSS.

## 🎨 Design Philosophy

Our components support three theme variants:
- **Quizlet**: Playful, colorful, with rounded corners and hover animations
- **Anki**: Minimal, efficient, with clean lines and subtle shadows  
- **Hybrid**: Best of both worlds - modern aesthetics with professional functionality

## 📦 Components

### Flashcard

Interactive flashcard component with 3D flip animation.

```tsx
import Flashcard from './ui/Flashcard';

<Flashcard
  variant="quizlet" // "quizlet" | "anki" | "hybrid"
  size="md" // "sm" | "md" | "lg"
  front={<div>Question: What is React?</div>}
  back={<div>Answer: A JavaScript library for building UIs</div>}
  interactive={true}
  showFlipIndicator={true}
/>
```

**Props:**
- `front` - Content for the front of the card
- `back` - Content for the back of the card  
- `variant` - Theme variant ("quizlet" | "anki" | "hybrid")
- `size` - Size variant ("sm" | "md" | "lg")
- `interactive` - Whether card can be flipped by clicking
- `showFlipIndicator` - Show flip hint/icon
- `initialFlipped` - Start with back side showing
- `onClick` - Custom click handler

### Button

Versatile button component with multiple styles and variants.

```tsx
import Button from './ui/Button';

<Button
  variant="quizlet"
  styleType="primary" // "primary" | "secondary" | "outline" | "ghost" | "danger"
  size="md"
  leftIcon="🚀"
  loading={false}
  fullWidth={false}
>
  Get Started
</Button>
```

**Props:**
- `variant` - Theme variant
- `styleType` - Visual style type
- `size` - Button size ("sm" | "md" | "lg")
- `loading` - Show loading spinner
- `leftIcon` / `rightIcon` - Icons before/after text
- `fullWidth` - Take full container width
- `disabled` - Disable the button

### Navbar

Responsive navigation bar with mobile menu support.

```tsx
import Navbar from './ui/Navbar';

const navItems = [
  { label: 'Home', icon: '🏠', active: true },
  { label: 'Library', icon: '📚', href: '/library' },
  { label: 'Settings', icon: '⚙️', onClick: () => openSettings() },
];

<Navbar
  variant="hybrid"
  items={navItems}
  logo={<YourLogo />}
  userMenu={<UserDropdown />}
  sticky={true}
/>
```

**Props:**
- `variant` - Theme variant
- `items` - Array of navigation items
- `logo` - Logo/brand element
- `userMenu` - User menu component
- `sticky` - Whether navbar sticks to top
- `onMobileMenuToggle` - Mobile menu state callback

### Input & TextArea

Form input components with validation states.

```tsx
import Input, { TextArea } from './ui/Input';

<Input
  variant="hybrid"
  size="md"
  label="Email Address"
  placeholder="Enter your email..."
  leftIcon="📧"
  error="Please enter a valid email"
  fullWidth={true}
/>

<TextArea
  variant="anki"
  label="Description"
  rows={4}
  helperText="Provide a brief description"
  success="Looks good!"
/>
```

**Props:**
- `variant` - Theme variant
- `size` - Input size ("sm" | "md" | "lg")
- `label` - Input label text
- `helperText` - Helper text below input
- `error` - Error message (shows red styling)
- `success` - Success message (shows green styling)
- `leftIcon` / `rightIcon` - Icons inside input
- `fullWidth` - Take full container width

### StudySetCard

Display study sets in grid, list, or compact layouts.

```tsx
import StudySetCard from './ui/StudySetCard';

<StudySetCard
  variant="quizlet"
  layout="grid" // "grid" | "list" | "compact"
  title="Spanish Vocabulary"
  cardCount={47}
  description="Essential words for travel"
  author="Maria Rodriguez"
  progress={78}
  lastStudied={new Date()}
  tags={['Spanish', 'Travel']}
  difficulty="medium"
  onStudy={() => startStudying()}
  onEdit={() => editSet()}
  onDelete={() => deleteSet()}
/>
```

**Props:**
- `variant` - Theme variant
- `layout` - Display layout style
- `title` - Study set title
- `cardCount` - Number of cards in set
- `description` - Set description
- `author` - Creator name
- `progress` - Study progress (0-100)
- `lastStudied` - Last study date
- `tags` - Array of tag strings
- `difficulty` - Difficulty level ("easy" | "medium" | "hard")
- `onStudy` / `onEdit` / `onDelete` - Action handlers

## 🎨 Theme System

### Using Variants

All components accept a `variant` prop:

```tsx
// Quizlet style - playful and colorful
<Button variant="quizlet">Fun Button</Button>

// Anki style - minimal and efficient  
<Button variant="anki">Clean Button</Button>

// Hybrid style - modern and balanced
<Button variant="hybrid">Balanced Button</Button>
```

### Theme Configuration

The theme system is defined in `src/theme.ts`:

```tsx
import { theme, themeVariants } from '../theme';

// Access theme values
const primaryColor = themeVariants.quizlet.primary; // #4255FF
const spacing = theme.spacing[4]; // 1rem
const borderRadius = theme.borderRadius.xl; // 0.75rem
```

### Custom Styling

Components use inline styles for theme-specific properties and Tailwind classes for layout:

```tsx
// Theme-aware styling
const buttonStyle = {
  backgroundColor: variantStyles.primary,
  borderRadius: variant === 'quizlet' ? '9999px' : '0.5rem',
};

// Tailwind for layout
const buttonClass = "flex items-center justify-center px-4 py-2 font-medium";
```

## 📱 Responsive Design

All components are built mobile-first with Tailwind responsive utilities:

```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  {/* Responsive grid */}
</div>
```

## 🎯 Best Practices

### Component Usage

1. **Choose the right variant** for your use case:
   - `quizlet` for consumer-facing, fun interfaces
   - `anki` for professional, data-heavy interfaces  
   - `hybrid` for balanced, modern applications

2. **Use semantic props** for better accessibility:
   ```tsx
   <Button leftIcon="🚀" aria-label="Start studying">
     Study Now
   </Button>
   ```

3. **Handle loading and error states**:
   ```tsx
   <Button loading={isSubmitting} disabled={!isValid}>
     {isSubmitting ? 'Saving...' : 'Save Changes'}
   </Button>
   ```

### Styling Guidelines

1. **Prefer theme variants** over custom styling
2. **Use Tailwind utilities** for layout and spacing
3. **Maintain consistency** within your chosen variant
4. **Test responsive behavior** on different screen sizes

## 🔧 Development

### Adding New Components

1. Create component in `src/components/ui/`
2. Follow the existing pattern for theme variants
3. Add TypeScript interfaces for props
4. Include responsive design considerations
5. Update this README with usage examples

### Extending Themes

Add new theme variants in `src/theme.ts`:

```tsx
export const themeVariants = {
  // ... existing variants
  custom: {
    primary: '#your-color',
    // ... other theme properties
  }
} as const;
```

## 📚 Examples

See the demo pages for complete examples:
- `src/pages/demo/DemoQuizlet.tsx` - Quizlet-style interface
- `src/pages/demo/DemoAnki.tsx` - Anki-style interface  
- `src/pages/demo/DemoHybrid.tsx` - Hybrid approach

## 🤝 Contributing

1. Follow the existing code style and patterns
2. Add TypeScript types for all props
3. Include responsive design considerations
4. Test with all three theme variants
5. Update documentation for new features
