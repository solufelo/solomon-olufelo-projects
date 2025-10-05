/**
 * Input Validation Schemas for StudyOS
 * 
 * This file contains Zod schemas for validating user input across all operations.
 * Using Zod provides runtime type safety and clear error messages.
 */

import { z } from 'zod';

// ===== Deck Validation =====

/**
 * Schema for creating a new deck
 * Ensures deck names are reasonable length and not empty
 */
export const CreateDeckSchema = z.object({
  name: z.string()
    .min(1, 'Deck name is required')
    .max(100, 'Deck name must be less than 100 characters')
    .trim()
    .refine((val) => val.length > 0, {
      message: 'Deck name cannot be only whitespace',
    }),
});

export type CreateDeckInput = z.infer<typeof CreateDeckSchema>;

// ===== Card Validation =====

/**
 * Schema for creating a new flashcard
 * Validates question and answer content with reasonable limits
 */
export const CreateCardSchema = z.object({
  deckId: z.number().int().positive('Deck ID must be a positive integer'),
  question: z.string()
    .min(1, 'Question is required')
    .max(1000, 'Question must be less than 1000 characters')
    .trim()
    .refine((val) => val.length > 0, {
      message: 'Question cannot be only whitespace',
    }),
  answer: z.string()
    .min(1, 'Answer is required')
    .max(2000, 'Answer must be less than 2000 characters')
    .trim()
    .refine((val) => val.length > 0, {
      message: 'Answer cannot be only whitespace',
    }),
});

export type CreateCardInput = z.infer<typeof CreateCardSchema>;

/**
 * Schema for editing an existing card
 * All fields required for update
 */
export const EditCardSchema = z.object({
  cardId: z.number().int().positive('Card ID must be a positive integer'),
  question: z.string()
    .min(1, 'Question is required')
    .max(1000, 'Question must be less than 1000 characters')
    .trim(),
  answer: z.string()
    .min(1, 'Answer is required')
    .max(2000, 'Answer must be less than 2000 characters')
    .trim(),
});

export type EditCardInput = z.infer<typeof EditCardSchema>;

/**
 * Schema for deleting a card
 */
export const DeleteCardSchema = z.object({
  cardId: z.number().int().positive('Card ID must be a positive integer'),
});

export type DeleteCardInput = z.infer<typeof DeleteCardSchema>;

// ===== Review Validation =====

/**
 * Valid review statuses based on spaced repetition algorithm
 */
export const ReviewStatus = z.enum(['again', 'hard', 'good', 'easy'], {
  errorMap: () => ({ message: 'Status must be: again, hard, good, or easy' }),
});

/**
 * Schema for reviewing a flashcard
 * Validates the review status and optional note
 */
export const ReviewCardSchema = z.object({
  cardId: z.number().int().positive('Card ID must be a positive integer'),
  status: ReviewStatus,
  note: z.string()
    .max(500, 'Note must be less than 500 characters')
    .trim()
    .optional()
    .nullable(),
});

export type ReviewCardInput = z.infer<typeof ReviewCardSchema>;

// ===== Task Validation =====

/**
 * Schema for creating a task
 * Validates title, description, and due date
 */
export const CreateTaskSchema = z.object({
  title: z.string()
    .min(1, 'Title is required')
    .max(200, 'Title must be less than 200 characters')
    .trim(),
  description: z.string()
    .max(1000, 'Description must be less than 1000 characters')
    .trim()
    .optional()
    .nullable(),
  dueDate: z.string()
    .or(z.date())
    .refine((val) => {
      const date = new Date(val);
      return !isNaN(date.getTime());
    }, {
      message: 'Invalid date format',
    }),
  deckId: z.number().int().positive().optional().nullable(),
});

export type CreateTaskInput = z.infer<typeof CreateTaskSchema>;

/**
 * Schema for editing a task
 * All fields optional except taskId
 */
export const EditTaskSchema = z.object({
  taskId: z.number().int().positive('Task ID must be a positive integer'),
  title: z.string()
    .min(1, 'Title is required')
    .max(200, 'Title must be less than 200 characters')
    .trim()
    .optional(),
  description: z.string()
    .max(1000, 'Description must be less than 1000 characters')
    .trim()
    .optional()
    .nullable(),
  dueDate: z.string()
    .or(z.date())
    .refine((val) => {
      const date = new Date(val);
      return !isNaN(date.getTime());
    }, {
      message: 'Invalid date format',
    })
    .optional(),
  completed: z.boolean().optional(),
  deckId: z.number().int().positive().optional().nullable(),
});

export type EditTaskInput = z.infer<typeof EditTaskSchema>;

/**
 * Schema for deleting a task
 */
export const DeleteTaskSchema = z.object({
  taskId: z.number().int().positive('Task ID must be a positive integer'),
});

export type DeleteTaskInput = z.infer<typeof DeleteTaskSchema>;

// ===== Pomodoro Validation =====

/**
 * Schema for ending a pomodoro session
 */
export const EndPomodoroSchema = z.object({
  sessionId: z.number().int().positive('Session ID must be a positive integer'),
  cyclesCompleted: z.number()
    .int()
    .min(0, 'Cycles completed must be non-negative')
    .max(20, 'Cycles completed seems unreasonably high')
    .optional()
    .default(0),
});

export type EndPomodoroInput = z.infer<typeof EndPomodoroSchema>;

// ===== Game Validation =====

/**
 * Schema for recording a game score
 */
export const RecordGameScoreSchema = z.object({
  score: z.number()
    .int()
    .min(0, 'Score must be non-negative')
    .max(10000, 'Score seems unreasonably high'),
  reactionTime: z.number()
    .min(0, 'Reaction time must be non-negative')
    .max(60000, 'Reaction time must be less than 60 seconds'),
});

export type RecordGameScoreInput = z.infer<typeof RecordGameScoreSchema>;

// ===== Utility Functions =====

/**
 * Sanitizes user input by removing potentially dangerous characters
 * Note: This is a basic implementation. Consider using a library like DOMPurify for HTML content.
 * 
 * @param input - The string to sanitize
 * @returns Sanitized string
 */
export function sanitizeInput(input: string): string {
  return input
    .trim()
    .replace(/[<>]/g, '') // Remove < and > to prevent basic XSS
    .slice(0, 10000); // Absolute max length as safety measure
}

/**
 * Validates and parses input using a Zod schema
 * Returns validated data or throws user-friendly error
 * 
 * @param schema - Zod schema to validate against
 * @param data - Data to validate
 * @returns Validated and typed data
 * @throws Error with user-friendly message
 */
export function validateInput<T extends z.ZodTypeAny>(
  schema: T,
  data: unknown
): z.infer<T> {
  try {
    return schema.parse(data);
  } catch (error) {
    if (error instanceof z.ZodError) {
      const firstError = error.errors[0];
      throw new Error(firstError.message);
    }
    throw new Error('Invalid input data');
  }
}

/**
 * Checks if a string contains potentially malicious patterns
 * This is a basic check and should not be relied upon as sole protection
 * 
 * @param input - String to check
 * @returns true if suspicious patterns found
 */
export function containsSuspiciousPatterns(input: string): boolean {
  const suspiciousPatterns = [
    /<script/i,
    /javascript:/i,
    /on\w+\s*=/i, // Event handlers like onclick=
    /data:text\/html/i,
    /<iframe/i,
  ];
  
  return suspiciousPatterns.some(pattern => pattern.test(input));
}

/**
 * Truncates a string to a maximum length, adding ellipsis if truncated
 * 
 * @param str - String to truncate
 * @param maxLength - Maximum length
 * @returns Truncated string
 */
export function truncateString(str: string, maxLength: number): string {
  if (str.length <= maxLength) return str;
  return str.slice(0, maxLength - 3) + '...';
}

// ===== Export all schemas for easy import =====
export const ValidationSchemas = {
  CreateDeck: CreateDeckSchema,
  CreateCard: CreateCardSchema,
  EditCard: EditCardSchema,
  DeleteCard: DeleteCardSchema,
  ReviewCard: ReviewCardSchema,
  CreateTask: CreateTaskSchema,
  EditTask: EditTaskSchema,
  DeleteTask: DeleteTaskSchema,
  EndPomodoro: EndPomodoroSchema,
  RecordGameScore: RecordGameScoreSchema,
} as const;

