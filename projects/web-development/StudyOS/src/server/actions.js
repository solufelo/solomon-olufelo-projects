// Basic server actions for StudyOS
// This file will be expanded as we add more features

import { validateInput, ValidationSchemas } from './validation';
import { HttpError } from 'wasp/server';

export const uploadPdfAndGenerateCards = async (args, context) => {
  // TODO: Implement PDF upload and AI card generation
  throw new Error('Not implemented yet');
};

export const reviewCard = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.ReviewCard, args);

  if (!validatedData.cardId || !validatedData.status) {
    throw new Error('Card ID and review status are required');
  }

  const validStatuses = ['again', 'hard', 'good', 'easy'];
  if (!validStatuses.includes(validatedData.status)) {
    throw new Error('Invalid review status. Must be: again, hard, good, or easy');
  }

  try {
    // Verify the card belongs to the user
    const card = await context.entities.Card.findFirst({
      where: {
        id: validatedData.cardId,
        deck: {
          userId: context.user.id,
        },
      },
      include: {
        deck: true,
      },
    });

    if (!card) {
      throw new HttpError(404, 'Resource not found');
    }

    // Calculate new interval based on spaced repetition algorithm
    let newBox = card.box;
    let newIntervalDays = card.intervalDays;
    let newNextDue = new Date();

    switch (validatedData.status) {
      case 'again':
        // Reset to box 1, review again soon
        newBox = 1;
        newIntervalDays = 1;
        newNextDue = new Date(Date.now() + 1 * 24 * 60 * 60 * 1000); // 1 day
        break;
      
      case 'hard':
        // Stay in same box or move back one
        newBox = Math.max(1, card.box - 1);
        newIntervalDays = Math.max(1, Math.floor(card.intervalDays * 0.5));
        newNextDue = new Date(Date.now() + newIntervalDays * 24 * 60 * 60 * 1000);
        break;
      
      case 'good':
        // Move to next box
        newBox = Math.min(5, card.box + 1);
        newIntervalDays = card.intervalDays * 2;
        newNextDue = new Date(Date.now() + newIntervalDays * 24 * 60 * 60 * 1000);
        break;
      
      case 'easy':
        // Move to next box with bonus
        newBox = Math.min(5, card.box + 1);
        newIntervalDays = card.intervalDays * 2.5;
        newNextDue = new Date(Date.now() + newIntervalDays * 24 * 60 * 60 * 1000);
        break;
    }

    // Update the card with new spaced repetition data
    const updatedCard = await context.entities.Card.update({
      where: { id: validatedData.cardId },
      data: {
        box: newBox,
        intervalDays: newIntervalDays,
        nextDue: newNextDue,
      },
    });

    // Create review log entry
    await context.entities.ReviewLog.create({
      data: {
        cardId: validatedData.cardId,
        userId: context.user.id,
        status: validatedData.status,
        note: validatedData.note?.trim() || null,
      },
    });

    return {
      card: updatedCard,
      reviewLog: null, // reviewLog is not returned in the new structure
      nextReview: newNextDue,
    };
  } catch (error) {
    console.error('Error reviewing card:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to review card');
  }
};

export const getDueCards = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const now = new Date();
    
    const dueCards = await context.entities.Card.findMany({
      where: {
        deck: {
          userId: context.user.id,
        },
        nextDue: {
          lte: now,
        },
      },
      include: {
        deck: true,
        reviewLogs: {
          orderBy: {
            reviewedAt: 'desc',
          },
          take: 5, // Get last 5 reviews for context
        },
      },
      orderBy: {
        nextDue: 'asc', // Most overdue first
      },
    });

    return dueCards;
  } catch (error) {
    console.error('Error fetching due cards:', error);
    throw new HttpError(500, 'Failed to fetch due cards');
  }
};

export const createDeck = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.CreateDeck, args);
  
  if (!validatedData.name || validatedData.name.trim().length === 0) {
    throw new Error('Deck name is required');
  }

  try {
    const deck = await context.entities.Deck.create({
      data: {
        name: validatedData.name.trim(),
        userId: context.user.id,
      },
    });

    return deck;
  } catch (error) {
    console.error('Error creating deck:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to create deck');
  }
};

export const createCard = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.CreateCard, args);
  
  if (!validatedData.deckId || !validatedData.question || !validatedData.answer) {
    throw new Error('Deck ID, question, and answer are required');
  }

  // Verify the deck belongs to the user
  try {
    const deck = await context.entities.Deck.findFirst({
      where: {
        id: validatedData.deckId,
        userId: context.user.id,
      },
    });

    if (!deck) {
      throw new HttpError(404, 'Resource not found');
    }

    const card = await context.entities.Card.create({
      data: {
        question: validatedData.question.trim(),
        answer: validatedData.answer.trim(),
        deckId: validatedData.deckId,
      },
    });

    return card;
  } catch (error) {
    console.error('Error creating card:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to create card');
  }
};

export const editCard = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.EditCard, args);
  
  if (!validatedData.cardId || !validatedData.question || !validatedData.answer) {
    throw new Error('Card ID, question, and answer are required');
  }

  try {
    // Verify the card belongs to the user through deck ownership
    const card = await context.entities.Card.findFirst({
      where: {
        id: validatedData.cardId,
        deck: {
          userId: context.user.id,
        },
      },
      include: {
        deck: true,
      },
    });

    if (!card) {
      throw new HttpError(404, 'Resource not found');
    }

    const updatedCard = await context.entities.Card.update({
      where: { id: validatedData.cardId },
      data: {
        question: validatedData.question.trim(),
        answer: validatedData.answer.trim(),
      },
    });

    return updatedCard;
  } catch (error) {
    console.error('Error updating card:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to update card');
  }
};

export const deleteCard = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.DeleteCard, args);
  
  if (!validatedData.cardId) {
    throw new Error('Card ID is required');
  }

  try {
    // Verify the card belongs to the user through deck ownership
    const card = await context.entities.Card.findFirst({
      where: {
        id: validatedData.cardId,
        deck: {
          userId: context.user.id,
        },
      },
      include: {
        deck: true,
      },
    });

    if (!card) {
      throw new HttpError(404, 'Resource not found');
    }

    await context.entities.Card.delete({
      where: { id: validatedData.cardId },
    });

    return { success: true, message: 'Card deleted successfully' };
  } catch (error) {
    console.error('Error deleting card:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to delete card');
  }
};

export const getDecks = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const decks = await context.entities.Deck.findMany({
      where: {
        userId: context.user.id,
      },
      include: {
        cards: true,
      },
      orderBy: {
        createdAt: 'desc',
      },
    });

    return decks;
  } catch (error) {
    console.error('Error fetching decks:', error);
    throw new HttpError(500, 'Failed to fetch decks');
  }
};

// Pomodoro actions
export const startPomodoro = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const session = await context.entities.PomodoroSession.create({
      data: {
        userId: context.user.id,
        startTime: new Date(),
        cyclesCompleted: 0,
      },
    });

    return session;
  } catch (error) {
    console.error('Error starting Pomodoro session:', error);
    throw new HttpError(500, 'Failed to start Pomodoro session');
  }
};

export const endPomodoro = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.EndPomodoro, args);

  if (!validatedData.sessionId) {
    throw new Error('Session ID is required');
  }

  try {
    const session = await context.entities.PomodoroSession.findFirst({
      where: {
        id: validatedData.sessionId,
        userId: context.user.id,
      },
    });

    if (!session) {
      throw new HttpError(404, 'Resource not found');
    }

    const updatedSession = await context.entities.PomodoroSession.update({
      where: { id: validatedData.sessionId },
      data: {
        endTime: new Date(),
        cyclesCompleted: validatedData.cyclesCompleted || 0,
      },
    });

    return updatedSession;
  } catch (error) {
    console.error('Error ending Pomodoro session:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to end Pomodoro session');
  }
};

export const getPomodoroStats = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const sessions = await context.entities.PomodoroSession.findMany({
      where: {
        userId: context.user.id,
        endTime: { not: null },
      },
      orderBy: {
        createdAt: 'desc',
      },
    });

    const totalSessions = sessions.length;
    const totalCycles = sessions.reduce((sum, session) => sum + session.cyclesCompleted, 0);
    const totalTime = sessions.reduce((sum, session) => {
      if (session.endTime) {
        return sum + (new Date(session.endTime) - new Date(session.startTime));
      }
      return sum;
    }, 0);

    const averageCycles = totalSessions > 0 ? totalCycles / totalSessions : 0;
    const averageTime = totalSessions > 0 ? totalTime / totalSessions : 0;

    return {
      totalSessions,
      totalCycles,
      totalTime: Math.round(totalTime / (1000 * 60)), // Convert to minutes
      averageCycles: Math.round(averageCycles * 100) / 100,
      averageTime: Math.round(averageTime / (1000 * 60)), // Convert to minutes
      recentSessions: sessions.slice(0, 10),
    };
  } catch (error) {
    console.error('Error fetching Pomodoro stats:', error);
    throw new HttpError(500, 'Failed to fetch Pomodoro statistics');
  }
};

// Task actions
export const createTask = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.CreateTask, args);

  if (!validatedData.title || !validatedData.dueDate) {
    throw new Error('Title and due date are required');
  }

  try {
    const task = await context.entities.Task.create({
      data: {
        title: validatedData.title.trim(),
        description: validatedData.description?.trim() || null,
        dueDate: new Date(validatedData.dueDate),
        userId: context.user.id,
        deckId: validatedData.deckId || null,
      },
    });

    return task;
  } catch (error) {
    console.error('Error creating task:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to create task');
  }
};

export const editTask = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.EditTask, args);

  if (!validatedData.taskId) {
    throw new Error('Task ID is required');
  }

  try {
    // Verify the task belongs to the user
    const task = await context.entities.Task.findFirst({
      where: {
        id: validatedData.taskId,
        userId: context.user.id,
      },
    });

    if (!task) {
      throw new HttpError(404, 'Resource not found');
    }

    const updateData = {};
    if (validatedData.title !== undefined) updateData.title = validatedData.title.trim();
    if (validatedData.description !== undefined) updateData.description = validatedData.description?.trim() || null;
    if (validatedData.dueDate !== undefined) updateData.dueDate = new Date(validatedData.dueDate);
    if (validatedData.completed !== undefined) updateData.completed = validatedData.completed;
    if (validatedData.deckId !== undefined) updateData.deckId = validatedData.deckId || null;

    const updatedTask = await context.entities.Task.update({
      where: { id: validatedData.taskId },
      data: updateData,
    });

    return updatedTask;
  } catch (error) {
    console.error('Error updating task:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to update task');
  }
};

export const deleteTask = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.DeleteTask, args);

  if (!validatedData.taskId) {
    throw new Error('Task ID is required');
  }

  try {
    // Verify the task belongs to the user
    const task = await context.entities.Task.findFirst({
      where: {
        id: validatedData.taskId,
        userId: context.user.id,
      },
    });

    if (!task) {
      throw new HttpError(404, 'Resource not found');
    }

    await context.entities.Task.delete({
      where: { id: validatedData.taskId },
    });

    return { success: true, message: 'Task deleted successfully' };
  } catch (error) {
    console.error('Error deleting task:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to delete task');
  }
};

export const getTasks = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const tasks = await context.entities.Task.findMany({
      where: {
        userId: context.user.id,
      },
      include: {
        deck: true,
      },
      orderBy: {
        dueDate: 'asc',
      },
    });

    return tasks;
  } catch (error) {
    console.error('Error fetching tasks:', error);
    throw new HttpError(500, 'Failed to fetch tasks');
  }
};

export const getTasksDueToday = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const today = new Date();
    const startOfDay = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    const endOfDay = new Date(today.getFullYear(), today.getMonth(), today.getDate() + 1);

    const tasks = await context.entities.Task.findMany({
      where: {
        userId: context.user.id,
        dueDate: {
          gte: startOfDay,
          lt: endOfDay,
        },
        completed: false,
      },
      include: {
        deck: true,
      },
      orderBy: {
        dueDate: 'asc',
      },
    });

    return tasks;
  } catch (error) {
    console.error('Error fetching tasks due today:', error);
    throw new HttpError(500, 'Failed to fetch tasks due today');
  }
};

// Game actions
export const recordGameScore = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  const validatedData = validateInput(ValidationSchemas.RecordGameScore, args);

  if (validatedData.score === undefined || validatedData.reactionTime === undefined) {
    throw new Error('Score and reaction time are required');
  }

  try {
    const gameScore = await context.entities.GameScore.create({
      data: {
        userId: context.user.id,
        score: validatedData.score,
        reactionTime: validatedData.reactionTime,
      },
    });

    return gameScore;
  } catch (error) {
    console.error('Error recording game score:', error);
    if (error instanceof HttpError) throw error;
    throw new HttpError(500, 'Failed to record game score');
  }
};

export const getGameScores = async (args, context) => {
  if (!context.user) {
    throw new HttpError(401, 'Not authorized');
  }

  try {
    const scores = await context.entities.GameScore.findMany({
      where: {
        userId: context.user.id,
      },
      orderBy: {
        playedAt: 'desc',
      },
    });

    // Calculate statistics
    const totalGames = scores.length;
    const averageScore = totalGames > 0 ? scores.reduce((sum, score) => sum + score.score, 0) / totalGames : 0;
    const averageReactionTime = totalGames > 0 ? scores.reduce((sum, score) => sum + score.reactionTime, 0) / totalGames : 0;
    const bestScore = totalGames > 0 ? Math.max(...scores.map(score => score.score)) : 0;
    const bestReactionTime = totalGames > 0 ? Math.min(...scores.map(score => score.reactionTime)) : 0;

    return {
      scores,
      statistics: {
        totalGames,
        averageScore: Math.round(averageScore * 100) / 100,
        averageReactionTime: Math.round(averageReactionTime * 100) / 100,
        bestScore,
        bestReactionTime: Math.round(bestReactionTime * 100) / 100,
      },
    };
  } catch (error) {
    console.error('Error fetching game scores:', error);
    throw new HttpError(500, 'Failed to fetch game scores');
  }
};