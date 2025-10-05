import React, { useState, useEffect } from 'react';
import { useAuth } from 'wasp/client/auth';
import { getGameScores, recordGameScore } from 'wasp/client/operations';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, StatsCard, Alert } from '../components/UIComponents';
import { Zap, Trophy, Target, Clock } from 'lucide-react';

const Game: React.FC = () => {
  const { data: user } = useAuth();
  const [gameState, setGameState] = useState<'idle' | 'ready' | 'playing' | 'result'>('idle');
  const [startTime, setStartTime] = useState<number>(0);
  const [reactionTime, setReactionTime] = useState<number>(0);
  const [bestScore, setBestScore] = useState<number>(0);
  const [scores, setScores] = useState<number[]>([]);

  useEffect(() => {
    loadScores();
  }, []);

  const loadScores = async () => {
    try {
      const data = await getGameScores();
      if (data.scores && data.scores.length > 0) {
        const times = data.scores.map((s: any) => s.reactionTime);
        setBestScore(Math.min(...times));
        setScores(times.slice(0, 5));
      }
    } catch (error) {
      console.error('Error loading scores:', error);
    }
  };

  const startGame = () => {
    setGameState('ready');
    const delay = Math.random() * 3000 + 1000;
    setTimeout(() => {
      setStartTime(Date.now());
      setGameState('playing');
    }, delay);
  };

  const handleClick = async () => {
    if (gameState === 'playing') {
      const time = Date.now() - startTime;
      setReactionTime(time);
      setGameState('result');
      
      try {
        await recordGameScore({ score: 100, reactionTime: time });
        loadScores();
      } catch (error) {
        console.error('Error saving score:', error);
      }
    } else if (gameState === 'ready') {
      setGameState('idle');
      alert('Too early! Wait for the screen to turn green.');
    }
  };

  const resetGame = () => {
    setGameState('idle');
    setReactionTime(0);
  };

  return (
    <DashboardLayout>
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Header */}
        <div className="text-center animate-fade-in">
          <h1 className="text-3xl font-bold text-foreground mb-2">Reaction Game</h1>
          <p className="text-muted-foreground">Test your reflexes and improve your reaction time</p>
        </div>

        {/* Game Area */}
        <Card 
          className={`h-96 flex items-center justify-center cursor-pointer transition-all duration-300 ${
            gameState === 'playing' ? 'bg-success/20 hover:bg-success/30' :
            gameState === 'ready' ? 'bg-warning/20' :
            'hover:bg-muted/50'
          }`}
          onClick={handleClick}
        >
          <div className="text-center">
            {gameState === 'idle' && (
              <div className="space-y-4">
                <Zap className="w-16 h-16 mx-auto text-primary" />
                <h2 className="text-2xl font-bold text-foreground">Ready to Test Your Reflexes?</h2>
                <Button onClick={(e) => { e.stopPropagation(); startGame(); }} size="lg">
                  Start Game
                </Button>
              </div>
            )}
            
            {gameState === 'ready' && (
              <div className="space-y-4">
                <Clock className="w-16 h-16 mx-auto text-warning animate-pulse" />
                <h2 className="text-2xl font-bold text-foreground">Wait for green...</h2>
              </div>
            )}
            
            {gameState === 'playing' && (
              <div className="space-y-4">
                <Target className="w-16 h-16 mx-auto text-success" />
                <h2 className="text-2xl font-bold text-success">Click Now!</h2>
              </div>
            )}
            
            {gameState === 'result' && (
              <div className="space-y-4">
                <Trophy className="w-16 h-16 mx-auto text-primary" />
                <h2 className="text-3xl font-bold text-foreground">{reactionTime}ms</h2>
                <p className="text-muted-foreground">
                  {reactionTime < 200 ? 'Lightning fast! ⚡' :
                   reactionTime < 300 ? 'Great reflexes! 🎯' :
                   reactionTime < 400 ? 'Good job! 👍' :
                   'Keep practicing! 💪'}
                </p>
                <Button onClick={(e) => { e.stopPropagation(); resetGame(); }}>
                  Play Again
                </Button>
              </div>
            )}
          </div>
        </Card>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <StatsCard
            icon={<Trophy className="w-6 h-6" />}
            label="Best Time"
            value={bestScore > 0 ? `${bestScore}ms` : 'N/A'}
          />
          <StatsCard
            icon={<Target className="w-6 h-6" />}
            label="Games Played"
            value={scores.length}
          />
        </div>

        {/* Recent Scores */}
        {scores.length > 0 && (
          <Card>
            <h3 className="text-lg font-semibold text-foreground mb-4">Recent Scores</h3>
            <div className="space-y-2">
              {scores.map((score, index) => (
                <div key={index} className="flex justify-between items-center p-2 rounded bg-muted/30">
                  <span className="text-sm text-muted-foreground">Attempt {index + 1}</span>
                  <span className="font-semibold text-foreground">{score}ms</span>
                </div>
              ))}
            </div>
          </Card>
        )}
      </div>
    </DashboardLayout>
  );
};

export default Game;
export { Game };
