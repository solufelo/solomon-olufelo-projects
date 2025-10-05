# StudyOS - Multi-Purpose Study Application

A comprehensive study platform built with Wasp that combines multiple learning methodologies and productivity tools for academic success.

## 🎯 Core Features

### 1. Flashcard System (Spaced Repetition)
- **Deck Management** - Create, organize, and manage flashcard decks
- **Smart Review Algorithm** - Implements spaced repetition using the Leitner system
- **PDF to Cards** - AI-powered conversion of PDF documents to flashcards using OpenAI
- **Review Statistics** - Track learning progress and retention rates

### 2. Task Management System
- **Due Date Tracking** - Tasks with deadlines and completion status
- **Deck Integration** - Link tasks to specific flashcard decks
- **Today's Tasks** - Quick view of tasks due today
- **Progress Tracking** - Visual progress indicators

### 3. Pomodoro Timer
- **Study Sessions** - Timed study periods with break intervals
- **Cycle Tracking** - Monitor completed pomodoro cycles
- **Statistics** - Track total study time and productivity metrics
- **Integration** - Connect pomodoro sessions with specific study materials

### 4. Gamification System
- **Reaction Time Games** - Quick cognitive exercises
- **Score Tracking** - Personal best scores and improvement over time
- **Study Motivation** - Game elements to encourage consistent studying

## 🛠️ Technical Architecture

### Frontend
- **Wasp Framework** - Full-stack React framework
- **React** - Component-based UI development
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework

### Backend
- **Wasp Server** - Built-in server with Express.js
- **Prisma** - Database ORM and migrations
- **Authentication** - Built-in user authentication
- **API Operations** - Queries and actions for data management

### Database Schema
```prisma
User (id, email, password, name, createdAt)
├── Deck (id, name, userId, createdAt)
│   └── Card (id, question, answer, deckId, box, intervalDays, nextDue)
├── Task (id, title, description, dueDate, completed, userId, deckId?)
├── PomodoroSession (id, userId, startTime, endTime, cyclesCompleted)
├── ReviewLog (id, cardId, userId, status, reviewedAt, note?)
└── GameScore (id, userId, score, reactionTime, playedAt)
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+ recommended)
- Wasp CLI (latest version)
- VSCode with recommended extensions

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd StudyOS

# Install dependencies
wasp start                    # First time setup
wasp db migrate-dev          # Apply database migrations
```

### Development
```bash
# Start development server
wasp start

# Database operations
wasp db migrate-dev          # Apply migrations
wasp db studio              # Open database admin UI
wasp db seed               # Seed with test data
```

## 📱 User Interface

### Dashboard
- **Today's Tasks** - Quick overview of due tasks
- **Recent Decks** - Access to recently used flashcard decks
- **Study Statistics** - Progress tracking and analytics
- **Quick Actions** - Fast access to common features

### Flashcard System
- **Deck Creation** - Easy deck setup with custom categories
- **Card Management** - Add, edit, and organize flashcards
- **Review Interface** - Clean, distraction-free study environment
- **Progress Tracking** - Visual indicators of learning progress

### Task Management
- **Task Creation** - Simple task setup with due dates
- **Deck Integration** - Link tasks to specific study materials
- **Completion Tracking** - Mark tasks as complete
- **Priority System** - Organize tasks by importance

## 🎮 Gamification Features

### Reaction Time Games
- **Quick Cognitive Exercises** - Improve focus and reaction time
- **Score Tracking** - Personal best scores and improvement
- **Leaderboards** - Compare performance with friends
- **Achievements** - Unlock badges for consistent studying

### Study Motivation
- **Streak Tracking** - Daily study streaks
- **Progress Visualization** - Charts and graphs of improvement
- **Reward System** - Unlock features through consistent use
- **Social Features** - Share progress with study groups

## 🔧 Development Guidelines

### Code Standards
- **TypeScript Strict Mode** - All files use strict type checking
- **Interface Definitions** - Define interfaces for all data structures
- **Error Handling** - Comprehensive error handling and user feedback
- **Accessibility** - WCAG 2.1 AA compliance

### Component Patterns
```typescript
// Component template
interface ComponentProps {
  data: SomeData;
  onAction: (id: number) => void;
}

const Component: React.FC<ComponentProps> = ({ data, onAction }) => {
  const [loading, setLoading] = useState(false);
  
  // Component logic here
  
  return (
    <div className="component-container">
      {/* Component JSX */}
    </div>
  );
};
```

### State Management
- **Wasp Operations** - Use queries for data fetching, actions for mutations
- **Local State** - React hooks for component-specific state
- **Error Boundaries** - Consistent error handling across the app

## 📊 Performance Optimization

### Frontend
- **Lazy Loading** - Route-based code splitting
- **Memoization** - React.memo for expensive components
- **Debouncing** - Search inputs and API calls
- **Image Optimization** - Optimized images and formats

### Backend
- **Database Queries** - Efficient Prisma queries
- **Pagination** - Large dataset handling
- **Caching** - Frequently accessed data
- **Error Responses** - Appropriate HTTP codes

## 🚀 Deployment

### Production Build
```bash
# Build for production
wasp build

# Deploy to production
wasp deploy
```

### Environment Setup
- Configure environment variables
- Set up database connections
- Configure authentication providers
- Set up file storage for uploads

## 🔮 Future Enhancements

### Planned Features
1. **Advanced Analytics** - Detailed study metrics and insights
2. **Social Features** - Study groups and shared decks
3. **Mobile App** - React Native companion app
4. **AI Tutor** - Personalized study recommendations
5. **Export/Import** - Anki-compatible deck exchange
6. **Calendar Integration** - Study schedule planning
7. **Collaborative Study** - Real-time study sessions

### Technical Improvements
1. **Real-time Features** - WebSocket integration
2. **Offline Support** - Progressive Web App features
3. **Advanced Search** - Full-text search across all content
4. **API Integration** - Third-party service integrations
5. **Performance Monitoring** - Application performance tracking

## 📞 Support

For support or questions:
- **Email:** oluf9170@mylaurier.ca
- **Phone:** 289-233-8317

## 📄 License

This project is part of my academic portfolio. Please respect the intellectual property and use responsibly.

---

*"Transforming study habits through technology and gamification."* 📚