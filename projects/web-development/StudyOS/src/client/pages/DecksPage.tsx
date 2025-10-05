import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from 'wasp/client/auth';
import { getDecks, createDeck } from 'wasp/client/operations';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, Input, EmptyState, Spinner, Alert } from '../components/UIComponents';
import { BookOpen, Plus, X, ArrowRight } from 'lucide-react';

interface CardType {
  id: number;
  question: string;
  answer: string;
  deckId: number;
}

interface Deck {
  id: number;
  name: string;
  createdAt: string;
  cards: CardType[];
}

const DecksPage: React.FC = () => {
  const { data: user } = useAuth();
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [newDeckName, setNewDeckName] = useState('');
  const [decks, setDecks] = useState<Deck[]>([]);
  const [loading, setLoading] = useState(true);
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadDecks();
  }, []);

  const loadDecks = async () => {
    try {
      setLoading(true);
      setError(null);
      const fetchedDecks = await getDecks();
      setDecks(fetchedDecks);
    } catch (err) {
      console.error('Error loading decks:', err);
      setError('Failed to load decks. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateDeck = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!newDeckName.trim()) {
      setError('Deck name cannot be empty');
      return;
    }

    try {
      setCreating(true);
      setError(null);
      const newDeck = await createDeck({ name: newDeckName.trim() });
      setDecks([...decks, newDeck]);
      setNewDeckName('');
      setShowCreateForm(false);
    } catch (err) {
      console.error('Error creating deck:', err);
      setError('Failed to create deck. Please try again.');
    } finally {
      setCreating(false);
    }
  };

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between animate-fade-in">
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">
              Flashcard Decks
            </h1>
            <p className="text-muted-foreground">
              Create and manage your study decks
            </p>
          </div>
          <Button 
            onClick={() => setShowCreateForm(!showCreateForm)}
            size="lg"
          >
            {showCreateForm ? (
              <>
                <X className="w-5 h-5" />
                Cancel
              </>
            ) : (
              <>
                <Plus className="w-5 h-5" />
                New Deck
              </>
            )}
          </Button>
        </div>

        {/* Error Alert */}
        {error && (
          <Alert variant="error" className="animate-fade-in">
            {error}
          </Alert>
        )}

        {/* Create Deck Form */}
        {showCreateForm && (
          <Card className="animate-card-rise">
            <form onSubmit={handleCreateDeck} className="space-y-4">
              <Input
                label="Deck Name"
                placeholder="e.g., Spanish Vocabulary"
                value={newDeckName}
                onChange={(e) => setNewDeckName(e.target.value)}
                autoFocus
              />
              <div className="flex gap-3">
                <Button 
                  type="submit" 
                  disabled={creating || !newDeckName.trim()}
                >
                  {creating ? 'Creating...' : 'Create Deck'}
                </Button>
                <Button 
                  type="button" 
                  variant="outline"
                  onClick={() => {
                    setShowCreateForm(false);
                    setNewDeckName('');
                    setError(null);
                  }}
                >
                  Cancel
                </Button>
              </div>
            </form>
          </Card>
        )}

        {/* Decks List */}
        {loading ? (
          <div className="flex justify-center py-12">
            <Spinner size="lg" />
          </div>
        ) : decks.length === 0 ? (
          <EmptyState
            icon={<BookOpen className="w-12 h-12" />}
            title="No decks yet"
            description="Create your first flashcard deck to start studying with spaced repetition."
            action={{
              label: 'Create Your First Deck',
              onClick: () => setShowCreateForm(true)
            }}
          />
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 animate-card-rise">
            {decks.map((deck) => (
              <Link key={deck.id} to={`/decks/${deck.id}/cards`}>
                <Card hover className="cursor-pointer h-full">
                  <div className="flex items-start justify-between mb-4">
                    <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center">
                      <BookOpen className="w-6 h-6 text-primary" />
                    </div>
                    <ArrowRight className="w-5 h-5 text-muted-foreground" />
                  </div>
                  
                  <h3 className="text-lg font-semibold text-foreground mb-2">
                    {deck.name}
                  </h3>
                  
                  <div className="flex items-center gap-4 text-sm text-muted-foreground">
                    <span>{deck.cards?.length || 0} cards</span>
                    <span>•</span>
                    <span>
                      {new Date(deck.createdAt).toLocaleDateString()}
                    </span>
                  </div>
                </Card>
              </Link>
            ))}
          </div>
        )}
      </div>
    </DashboardLayout>
  );
};

export default DecksPage;
export { DecksPage };
