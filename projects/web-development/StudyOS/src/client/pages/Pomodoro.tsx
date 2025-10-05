import React, { useState, useEffect } from 'react';
import { useAuth } from 'wasp/client/auth';
import { getPomodoroStats, startPomodoro, endPomodoro } from 'wasp/client/operations';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, StatsCard } from '../components/UIComponents';
import { Clock, Play, Pause, RotateCcw, Coffee } from 'lucide-react';

const Pomodoro: React.FC = () => {
  const { data: user } = useAuth();
  const [timer, setTimer] = useState(25 * 60);
  const [isRunning, setIsRunning] = useState(false);
  const [isBreak, setIsBreak] = useState(false);
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [stats, setStats] = useState({ totalSessions: 0, totalMinutes: 0 });

  useEffect(() => {
    loadStats();
  }, []);

  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    
    if (isRunning && timer > 0) {
      interval = setInterval(() => {
        setTimer((prev) => prev - 1);
      }, 1000);
    } else if (timer === 0) {
      handleTimerComplete();
    }

    return () => {
      if (interval) clearInterval(interval);
    };
  }, [isRunning, timer]);

  const loadStats = async () => {
    try {
      const data = await getPomodoroStats();
      setStats({
        totalSessions: data.totalSessions || 0,
        totalMinutes: Math.round((data.totalTime || 0) / 60)
      });
    } catch (error) {
      console.error('Error loading stats:', error);
    }
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleStart = async () => {
    try {
      if (!sessionId) {
        const session = await startPomodoro({});
        setSessionId(session.id);
      }
      setIsRunning(true);
    } catch (error) {
      console.error('Error starting pomodoro:', error);
    }
  };

  const handlePause = () => {
    setIsRunning(false);
  };

  const handleReset = () => {
    setIsRunning(false);
    setTimer(isBreak ? 5 * 60 : 25 * 60);
  };

  const handleTimerComplete = async () => {
    setIsRunning(false);
    if (!isBreak && sessionId) {
      try {
        await endPomodoro({ sessionId, cyclesCompleted: 1 });
        setSessionId(null);
        loadStats();
      } catch (error) {
        console.error('Error ending pomodoro:', error);
      }
    }
    setIsBreak(!isBreak);
    setTimer(isBreak ? 25 * 60 : 5 * 60);
  };

  return (
    <DashboardLayout>
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Header */}
        <div className="text-center animate-fade-in">
          <h1 className="text-3xl font-bold text-foreground mb-2">Pomodoro Timer</h1>
          <p className="text-muted-foreground">
            Stay focused with the Pomodoro technique
          </p>
        </div>

        {/* Timer Card */}
        <Card className="text-center animate-card-rise">
          <div className="mb-6">
            {isBreak ? (
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-success/10 text-success">
                <Coffee className="w-5 h-5" />
                <span className="font-medium">Break Time</span>
              </div>
            ) : (
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary">
                <Clock className="w-5 h-5" />
                <span className="font-medium">Focus Time</span>
              </div>
            )}
          </div>

          <div className="text-7xl font-mono font-bold text-foreground mb-8">
            {formatTime(timer)}
          </div>

          <div className="flex justify-center gap-3">
            {!isRunning ? (
              <Button onClick={handleStart} size="lg">
                <Play className="w-5 h-5" />
                Start
              </Button>
            ) : (
              <Button onClick={handlePause} size="lg" variant="outline">
                <Pause className="w-5 h-5" />
                Pause
              </Button>
            )}
            <Button onClick={handleReset} size="lg" variant="ghost">
              <RotateCcw className="w-5 h-5" />
              Reset
            </Button>
          </div>
        </Card>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <StatsCard
            icon={<Clock className="w-6 h-6" />}
            label="Total Sessions"
            value={stats.totalSessions}
          />
          <StatsCard
            icon={<Clock className="w-6 h-6" />}
            label="Total Minutes"
            value={stats.totalMinutes}
          />
        </div>

        {/* Instructions */}
        <Card className="bg-muted/30">
          <h3 className="text-lg font-semibold text-foreground mb-3">How it works</h3>
          <ul className="space-y-2 text-sm text-muted-foreground">
            <li>• Work for 25 minutes with full focus</li>
            <li>• Take a 5 minute break</li>
            <li>• After 4 sessions, take a longer break</li>
            <li>• Track your productivity over time</li>
          </ul>
        </Card>
      </div>
    </DashboardLayout>
  );
};

export default Pomodoro;
export { Pomodoro };
