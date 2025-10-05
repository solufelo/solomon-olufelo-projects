import React, { useState, useEffect } from 'react';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, StatsCard, ProgressBar } from '../components/UIComponents';
import { BookOpen, CheckSquare, Clock, Trophy, Calendar, Inbox } from 'lucide-react';

/**
 * Enhanced Dashboard Page with Modern Design System
 * Features focus session timer, progress widgets, and quick access cards
 */

export const EnhancedDashboardNew: React.FC = () => {
  // Pomodoro timer state
  const [pomodoroTime, setPomodoroTime] = useState(25 * 60); // 25 minutes in seconds
  const [isPomodoroRunning, setIsPomodoroRunning] = useState(false);

  // Format time as MM:SS
  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Pomodoro countdown effect
  useEffect(() => {
    let interval: NodeJS.Timeout;
    
    if (isPomodoroRunning && pomodoroTime > 0) {
      interval = setInterval(() => {
        setPomodoroTime((prev) => prev - 1);
      }, 1000);
    } else if (pomodoroTime === 0) {
      setIsPomodoroRunning(false);
      // Could add notification here
    }

    return () => clearInterval(interval);
  }, [isPomodoroRunning, pomodoroTime]);

  const handlePomodoroStart = () => {
    if (pomodoroTime === 0) {
      setPomodoroTime(25 * 60);
    }
    setIsPomodoroRunning(true);
  };

  const handlePomodoroStop = () => {
    setIsPomodoroRunning(false);
  };

  const handlePomodoroReset = () => {
    setIsPomodoroRunning(false);
    setPomodoroTime(25 * 60);
  };

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Welcome Section */}
        <div className="animate-fade-in">
          <h1 className="text-3xl font-bold text-[var(--foreground)] mb-2">
            Welcome back! 👋
          </h1>
          <p className="text-[var(--muted-foreground)]">
            Ready to level up your studying? Let's make today count.
          </p>
        </div>

        {/* Main Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Pomodoro Timer Card */}
          <Card className="animate-card-rise">
            <h3 className="text-lg font-semibold mb-6 text-[var(--foreground)]">
              Focus Session
            </h3>
            <div
              className={`text-6xl font-mono text-center mb-6 text-[var(--primary)] font-bold ${
                isPomodoroRunning ? 'animate-pomodoro' : ''
              }`}
            >
              {formatTime(pomodoroTime)}
            </div>
            <div className="flex justify-center gap-3">
              {!isPomodoroRunning ? (
                <Button onClick={handlePomodoroStart} size="lg">
                  <Clock className="w-5 h-5" />
                  Start
                </Button>
              ) : (
                <>
                  <Button onClick={handlePomodoroStop} variant="outline" size="lg">
                    Pause
                  </Button>
                  <Button onClick={handlePomodoroReset} variant="ghost" size="lg">
                    Reset
                  </Button>
                </>
              )}
            </div>
          </Card>

          {/* Today's Progress Card */}
          <Card className="animate-card-rise">
            <h3 className="text-lg font-semibold mb-6 text-[var(--foreground)]">
              Today's Progress
            </h3>
            <div className="space-y-4">
              <ProgressBar value={65} showLabel className="mb-4" />
              
              <div className="grid grid-cols-2 gap-4 mt-6">
                <div className="text-center p-3 rounded-lg bg-[var(--muted)]">
                  <div className="text-2xl font-bold text-[var(--foreground)]">12</div>
                  <div className="text-xs text-[var(--muted-foreground)]">Cards Reviewed</div>
                </div>
                <div className="text-center p-3 rounded-lg bg-[var(--muted)]">
                  <div className="text-2xl font-bold text-[var(--foreground)]">3</div>
                  <div className="text-xs text-[var(--muted-foreground)]">Tasks Done</div>
                </div>
              </div>
            </div>
          </Card>
        </div>

        {/* Stats Row */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 animate-card-rise">
          <StatsCard
            icon={<Inbox className="w-6 h-6" />}
            label="Pending Tasks"
            value={5}
          />
          <StatsCard
            icon={<Calendar className="w-6 h-6" />}
            label="Upcoming Deadlines"
            value={2}
          />
          <StatsCard
            icon={<Trophy className="w-6 h-6" />}
            label="Achievements"
            value={3}
          />
        </div>

        {/* Quick Actions */}
        <div className="animate-card-rise">
          <h3 className="text-lg font-semibold mb-4 text-[var(--foreground)]">
            Quick Actions
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <Card hover className="cursor-pointer">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-[var(--primary)]/10 flex items-center justify-center">
                  <BookOpen className="w-6 h-6 text-[var(--primary)]" />
                </div>
                <div>
                  <div className="font-medium text-[var(--foreground)]">Study Flashcards</div>
                  <div className="text-sm text-[var(--muted-foreground)]">15 cards due</div>
                </div>
              </div>
            </Card>

            <Card hover className="cursor-pointer">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-[var(--secondary)]/10 flex items-center justify-center">
                  <CheckSquare className="w-6 h-6 text-[var(--secondary)]" />
                </div>
                <div>
                  <div className="font-medium text-[var(--foreground)]">Review Tasks</div>
                  <div className="text-sm text-[var(--muted-foreground)]">5 pending</div>
                </div>
              </div>
            </Card>

            <Card hover className="cursor-pointer">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-[var(--accent)]/10 flex items-center justify-center">
                  <Trophy className="w-6 h-6 text-[var(--accent)]" />
                </div>
                <div>
                  <div className="font-medium text-[var(--foreground)]">View Achievements</div>
                  <div className="text-sm text-[var(--muted-foreground)]">3 unlocked</div>
                </div>
              </div>
            </Card>
          </div>
        </div>

        {/* Recent Activity */}
        <Card className="animate-fade-in">
          <h3 className="text-lg font-semibold mb-4 text-[var(--foreground)]">
            Recent Activity
          </h3>
          <div className="space-y-3">
            <div className="flex items-center gap-3 p-3 rounded-lg hover:bg-[var(--muted)] transition-colors">
              <div className="w-2 h-2 rounded-full bg-[var(--success)]" />
              <div className="flex-1">
                <div className="text-sm font-medium text-[var(--foreground)]">
                  Completed "Introduction to React" deck
                </div>
                <div className="text-xs text-[var(--muted-foreground)]">2 hours ago</div>
              </div>
            </div>
            <div className="flex items-center gap-3 p-3 rounded-lg hover:bg-[var(--muted)] transition-colors">
              <div className="w-2 h-2 rounded-full bg-[var(--primary)]" />
              <div className="flex-1">
                <div className="text-sm font-medium text-[var(--foreground)]">
                  Started focus session
                </div>
                <div className="text-xs text-[var(--muted-foreground)]">4 hours ago</div>
              </div>
            </div>
            <div className="flex items-center gap-3 p-3 rounded-lg hover:bg-[var(--muted)] transition-colors">
              <div className="w-2 h-2 rounded-full bg-[var(--accent)]" />
              <div className="flex-1">
                <div className="text-sm font-medium text-[var(--foreground)]">
                  Unlocked "Early Bird" achievement
                </div>
                <div className="text-xs text-[var(--muted-foreground)]">1 day ago</div>
              </div>
            </div>
          </div>
        </Card>
      </div>
    </DashboardLayout>
  );
};

export default EnhancedDashboardNew;

