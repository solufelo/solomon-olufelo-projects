/**
 * Example03_Documentation.java
 * 
 * Purpose: Demonstrates proper code documentation using JavaDoc and comments
 * 
 * This example shows:
 * - JavaDoc comments for classes and methods
 * - Single-line comments for clarification
 * - Multi-line comments for explanations
 * - When and where to use each type
 * 
 * To generate JavaDoc documentation:
 * javadoc Example03_Documentation.java
 * 
 * @author Solomon Olufelo
 * @version 1.0
 * @since 2025-11-05
 */
public class Example03_Documentation {
    
    // Class constant for maximum score
    public static final int MAX_SCORE = 100;
    
    /**
     * Main method - demonstrates different comment styles
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        // Test data
        int score1 = 85;
        int score2 = 92;
        int score3 = 78;
        
        /* Calculate the average score
           This requires adding all scores and dividing by the count.
           We use double to preserve decimal precision. */
        double average = calculateAverage(score1, score2, score3);
        
        // Display results
        System.out.println("Scores: " + score1 + ", " + score2 + ", " + score3);
        System.out.println("Average: " + average);
        System.out.println("Grade: " + getLetterGrade(average));
    }
    
    /**
     * Calculates the average of three scores
     * 
     * This method takes three integer scores and returns their average
     * as a double to maintain decimal precision.
     * 
     * @param score1 the first score
     * @param score2 the second score
     * @param score3 the third score
     * @return the average of the three scores
     */
    public static double calculateAverage(int score1, int score2, int score3) {
        // Cast to double for decimal division
        return (score1 + score2 + score3) / 3.0;
    }
    
    /**
     * Converts a numeric average to a letter grade
     * 
     * Grading scale:
     * - 90-100: A
     * - 80-89: B
     * - 70-79: C
     * - 60-69: D
     * - Below 60: F
     * 
     * @param average the numeric average (0-100)
     * @return the letter grade as a String
     */
    public static String getLetterGrade(double average) {
        if (average >= 90) {
            return "A";
        } else if (average >= 80) {
            return "B";
        } else if (average >= 70) {
            return "C";
        } else if (average >= 60) {
            return "D";
        } else {
            return "F";
        }
    }
}

