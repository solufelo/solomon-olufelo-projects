import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useAuth } from 'wasp/client/auth';
import { getDecks, createCard, editCard, deleteCard } from 'wasp/client/operations';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, Input, EmptyState, Spinner, Alert } from '../components/UIComponents';
import { BookOpen, Plus, Edit, Trash2, ArrowLeft, Play } from 'lucide-react';

interface Deck {
  id: number;
  name: string;
  createdAt: string;
  cards: FlashCard[];
}

interface FlashCard {
  id: number;
  question: string;
  answer: string;
  deckId: number;
  box: number;
  intervalDays: number;
  nextDue: string;
  createdAt: string;
  updatedAt: string;
}

const DeckCardsPage: React.FC = () => {
  const { data: user } = useAuth();
  const { deckId } = useParams<{ deckId: string }>();
  const [deck, setDeck] = useState<Deck | null>(null);
  const [loading, setLoading] = useState(true);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingCard, setEditingCard] = useState<FlashCard | null>(null);
  const [formData, setFormData] = useState({ question: '', answer: '' });
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    loadDeck();
  }, [deckId]);

  const loadDeck = async () => {
    try {
      setLoading(true);
      const decks = await getDecks();
      const foundDeck = decks.find(d => d.id === parseInt(deckId || '0'));
      if (foundDeck) {
        setDeck(foundDeck);
      }
    } catch (error) {
      console.error('Error loading deck:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateCard = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.question.trim() || !formData.answer.trim() || submitting) return;

    try {
      setSubmitting(true);
      await createCard({
        question: formData.question,
        answer: formData.answer,
        deckId: parseInt(deckId || '0'),
      });
      setFormData({ question: '', answer: '' });
      setShowCreateForm(false);
      loadDeck();
    } catch (error) {
      console.error('Error creating card:', error);
    } finally {
      setSubmitting(false);
    }
  };

  const handleEditCard = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingCard || !formData.question.trim() || !formData.answer.trim() || submitting) return;

    try {
      setSubmitting(true);
      await editCard({
        id: editingCard.id,
        data: {
          question: formData.question,
          answer: formData.answer,
        },
      });
      setFormData({ question: '', answer: '' });
      setEditingCard(null);
      loadDeck();
    } catch (error) {
      console.error('Error editing card:', error);
    } finally {
      setSubmitting(false);
    }
  };

  const handleDeleteCard = async (cardId: number) => {
    if (!confirm('Are you sure you want to delete this card?')) return;

    try {
      await deleteCard({ id: cardId });
      loadDeck();
    } catch (error) {
      console.error('Error deleting card:', error);
    }
  };

  const startEdit = (card: FlashCard) => {
    setEditingCard(card);
    setFormData({ question: card.question, answer: card.answer });
    setShowCreateForm(false);
  };

  const cancelEdit = () => {
    setEditingCard(null);
    setFormData({ question: '', answer: '' });
  };

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex justify-center py-12">
          <Spinner size="lg" />
        </div>
      </DashboardLayout>
    );
  }

  if (!deck) {
    return (
      <DashboardLayout>
        <EmptyState
          icon={<BookOpen className="w-12 h-12" />}
          title="Deck not found"
          description="The deck you're looking for doesn't exist."
          action={{
            label: 'Back to Decks',
            onClick: () => window.location.href = '/decks'
          }}
        />
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="animate-fade-in">
          <Link to="/decks" className="inline-flex items-center gap-2 text-muted-foreground hover:text-foreground mb-4">
            <ArrowLeft className="w-4 h-4" />
            Back to Decks
          </Link>
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-foreground mb-2">{deck.name}</h1>
              <p className="text-muted-foreground">{deck.cards?.length || 0} cards in this deck</p>
            </div>
            <div className="flex gap-3">
              {deck.cards && deck.cards.length > 0 && (
                <Button size="lg">
                  <Play className="w-5 h-5" />
                  Study Now
                </Button>
              )}
              <Button 
                onClick={() => {
                  setShowCreateForm(!showCreateForm);
                  setEditingCard(null);
                  setFormData({ question: '', answer: '' });
                }}
                size="lg"
                variant="outline"
              >
                <Plus className="w-5 h-5" />
                Add Card
              </Button>
            </div>
          </div>
        </div>

        {/* Create/Edit Form */}
        {(showCreateForm || editingCard) && (
          <Card className="animate-card-rise">
            <h3 className="text-lg font-semibold text-foreground mb-4">
              {editingCard ? 'Edit Card' : 'Create New Card'}
            </h3>
            <form onSubmit={editingCard ? handleEditCard : handleCreateCard} className="space-y-4">
              <div>
                <label className="text-sm font-medium text-foreground block mb-2">Question</label>
                <textarea
                  className="form-input min-h-[100px]"
                  placeholder="Enter the question..."
                  value={formData.question}
                  onChange={(e) => setFormData({ ...formData, question: e.target.value })}
                  required
                  autoFocus
                />
              </div>
              <div>
                <label className="text-sm font-medium text-foreground block mb-2">Answer</label>
                <textarea
                  className="form-input min-h-[100px]"
                  placeholder="Enter the answer..."
                  value={formData.answer}
                  onChange={(e) => setFormData({ ...formData, answer: e.target.value })}
                  required
                />
              </div>
              <div className="flex gap-3">
                <Button type="submit" disabled={submitting}>
                  {submitting ? 'Saving...' : (editingCard ? 'Update Card' : 'Create Card')}
                </Button>
                <Button 
                  type="button" 
                  variant="outline"
                  onClick={() => {
                    if (editingCard) {
                      cancelEdit();
                    } else {
                      setShowCreateForm(false);
                      setFormData({ question: '', answer: '' });
                    }
                  }}
                >
                  Cancel
                </Button>
              </div>
            </form>
          </Card>
        )}

        {/* Cards List */}
        {!deck.cards || deck.cards.length === 0 ? (
          <EmptyState
            icon={<BookOpen className="w-12 h-12" />}
            title="No cards yet"
            description="Add your first flashcard to start studying."
            action={{
              label: 'Add Your First Card',
              onClick: () => setShowCreateForm(true)
            }}
          />
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 animate-card-rise">
            {deck.cards.map((card) => (
              <Card key={card.id} className={editingCard?.id === card.id ? 'ring-2 ring-primary' : ''}>
                <div className="space-y-3">
                  <div>
                    <div className="text-xs text-muted-foreground mb-1 font-medium">Question</div>
                    <p className="text-sm text-foreground font-medium">{card.question}</p>
                  </div>
                  <div>
                    <div className="text-xs text-muted-foreground mb-1 font-medium">Answer</div>
                    <p className="text-sm text-muted-foreground">{card.answer}</p>
                  </div>
                  <div className="flex gap-2 pt-2">
                    <Button 
                      size="sm" 
                      variant="outline"
                      onClick={() => startEdit(card)}
                    >
                      <Edit className="w-3 h-3" />
                      Edit
                    </Button>
                    <Button 
                      size="sm" 
                      variant="ghost"
                      onClick={() => handleDeleteCard(card.id)}
                    >
                      <Trash2 className="w-3 h-3" />
                      Delete
                    </Button>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        )}
      </div>
    </DashboardLayout>
  );
};

export default DeckCardsPage;
export { DeckCardsPage };
