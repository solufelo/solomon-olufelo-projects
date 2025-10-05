import React, { useState, useEffect } from 'react';
import { useAuth } from 'wasp/client/auth';
import { Link } from 'react-router-dom';
import { getDecks, getTasks, getPomodoroStats } from 'wasp/client/operations';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, StatsCard, ProgressBar, Spinner } from '../components/UIComponents';
import { BookOpen, CheckSquare, Clock, Trophy, TrendingUp, Target, Zap } from 'lucide-react';

const MainPage: React.FC = () => {
  const { data: user, isLoading } = useAuth();
  const [stats, setStats] = useState({
    totalDecks: 0,
    cardsDue: 0,
    tasks: 0,
    sessions: 0
  });
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (user) {
      loadUserStats();
    }
  }, [user]);

  const loadUserStats = async () => {
    try {
      setLoading(true);
      const [decks, tasks, pomodoroStats] = await Promise.all([
        getDecks().catch(() => []),
        getTasks().catch(() => []),
        getPomodoroStats().catch(() => ({ totalSessions: 0 }))
      ]);

      const cardsDue = decks.reduce((total: number, deck: any) => total + (deck.cards?.length || 0), 0);
      const pendingTasks = tasks.filter((task: any) => !task.completed).length;

      setStats({
        totalDecks: decks.length,
        cardsDue: cardsDue,
        tasks: pendingTasks,
        sessions: pomodoroStats.totalSessions || 0
      });
    } catch (error) {
      console.error('Error loading user stats:', error);
    } finally {
      setLoading(false);
    }
  };

  // Loading state
  if (isLoading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <Spinner size="lg" className="mx-auto mb-4" />
          <p className="text-muted-foreground">Loading your dashboard...</p>
        </div>
      </div>
    );
  }

  // Landing page for non-authenticated users
  if (!user) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-background via-muted/30 to-background flex items-center justify-center p-4">
        <div className="max-w-4xl mx-auto">
          <div className="text-center space-y-8 animate-fade-in">
            {/* Hero Section */}
            <div className="space-y-4">
              <div className="inline-flex items-center justify-center w-20 h-20 bg-primary rounded-2xl shadow-lg mb-4">
                <BookOpen className="w-10 h-10 text-primary-foreground" />
              </div>
              <h1 className="text-5xl lg:text-6xl font-bold text-foreground">
                Study<span className="text-primary">OS</span>
              </h1>
              <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
                Your comprehensive study companion powered by spaced repetition, task management, and gamified learning
              </p>
            </div>

            {/* Features Grid */}
            <div className="grid md:grid-cols-3 gap-6 my-12">
              <Card className="text-center hover-lift">
                <div className="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center mx-auto mb-4">
                  <BookOpen className="w-7 h-7 text-primary" />
                </div>
                <h3 className="font-semibold text-lg mb-2 text-foreground">Smart Flashcards</h3>
                <p className="text-sm text-muted-foreground">AI-powered spaced repetition for optimal learning</p>
              </Card>
              
              <Card className="text-center hover-lift">
                <div className="w-14 h-14 bg-success/10 rounded-xl flex items-center justify-center mx-auto mb-4">
                  <CheckSquare className="w-7 h-7 text-success" />
                </div>
                <h3 className="font-semibold text-lg mb-2 text-foreground">Task Management</h3>
                <p className="text-sm text-muted-foreground">Organize your study schedule efficiently</p>
              </Card>
              
              <Card className="text-center hover-lift">
                <div className="w-14 h-14 bg-accent/10 rounded-xl flex items-center justify-center mx-auto mb-4">
                  <Trophy className="w-7 h-7 text-accent" />
                </div>
                <h3 className="font-semibold text-lg mb-2 text-foreground">Gamification</h3>
                <p className="text-sm text-muted-foreground">Make learning fun and engaging with rewards</p>
              </Card>
            </div>

            {/* CTA Buttons */}
            <Card className="p-8 max-w-md mx-auto">
              <div className="space-y-4">
                <Link to="/signup" className="block">
                  <Button size="lg" fullWidth>
                    <Zap className="w-5 h-5" />
                    Get Started Free
                  </Button>
                </Link>
                <Link to="/login" className="block">
                  <Button variant="outline" size="lg" fullWidth>
                    Sign In
                  </Button>
                </Link>
              </div>
            </Card>
          </div>
        </div>
      </div>
    );
  }

  // Dashboard for authenticated users
  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Welcome Section */}
        <div className="animate-fade-in">
          <h1 className="text-3xl font-bold mb-2" style={{color: '#111827'}}>
            Welcome back! 👋
          </h1>
          <p style={{color: '#6b7280'}}>
            Here's your study overview for today
          </p>
        </div>

        {/* Stats Grid */}
        {loading ? (
          <div className="flex justify-center py-12">
            <Spinner size="lg" />
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 animate-card-rise">
            <StatsCard
              icon={<BookOpen className="w-6 h-6" />}
              label="Total Decks"
              value={stats.totalDecks}
            />
            <StatsCard
              icon={<Target className="w-6 h-6" />}
              label="Cards Due"
              value={stats.cardsDue}
            />
            <StatsCard
              icon={<CheckSquare className="w-6 h-6" />}
              label="Pending Tasks"
              value={stats.tasks}
            />
            <StatsCard
              icon={<Clock className="w-6 h-6" />}
              label="Study Sessions"
              value={stats.sessions}
            />
          </div>
        )}

        {/* Quick Actions */}
        <div className="animate-card-rise">
          <h2 className="text-xl font-semibold mb-4" style={{color: '#111827'}}>Quick Actions</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <Link to="/decks">
              <Card hover className="cursor-pointer">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center">
                    <BookOpen className="w-6 h-6 text-primary" />
                  </div>
                  <div>
                    <div className="font-medium text-foreground">Study Flashcards</div>
                    <div className="text-sm text-muted-foreground">{stats.cardsDue} cards due</div>
                  </div>
                </div>
              </Card>
            </Link>

            <Link to="/tasks">
              <Card hover className="cursor-pointer">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-full bg-success/10 flex items-center justify-center">
                    <CheckSquare className="w-6 h-6 text-success" />
                  </div>
                  <div>
                    <div className="font-medium text-foreground">Review Tasks</div>
                    <div className="text-sm text-muted-foreground">{stats.tasks} pending</div>
                  </div>
                </div>
              </Card>
            </Link>

            <Link to="/pomodoro">
              <Card hover className="cursor-pointer">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center">
                    <Clock className="w-6 h-6 text-accent" />
                  </div>
                  <div>
                    <div className="font-medium text-foreground">Start Focus Session</div>
                    <div className="text-sm text-muted-foreground">Pomodoro timer</div>
                  </div>
                </div>
              </Card>
            </Link>
          </div>
        </div>

        {/* Study Progress */}
        <Card className="animate-fade-in">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-foreground">Today's Progress</h3>
            <TrendingUp className="w-5 h-5 text-success" />
          </div>
          <ProgressBar value={65} showLabel />
          <p className="text-sm text-muted-foreground mt-2">
            You've completed 65% of your daily study goal. Keep it up!
          </p>
        </Card>

        {/* Getting Started */}
        <Card className="bg-gradient-to-br from-primary/10 to-accent/10 border-primary/20">
          <h3 className="text-lg font-semibold mb-2 text-foreground">Get Started</h3>
          <p className="text-muted-foreground mb-4">
            Ready to begin your study journey? Create your first deck or add a task.
          </p>
          <div className="flex gap-3">
            <Link to="/decks">
              <Button>
                <BookOpen className="w-4 h-4" />
                Create Deck
              </Button>
            </Link>
            <Link to="/tasks">
              <Button variant="outline">
                <CheckSquare className="w-4 h-4" />
                Add Task
              </Button>
            </Link>
          </div>
        </Card>
      </div>
    </DashboardLayout>
  );
};

export default MainPage;
export { MainPage };
