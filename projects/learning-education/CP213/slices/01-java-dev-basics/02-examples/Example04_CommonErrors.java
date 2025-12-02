/**
 * Example04_CommonErrors.java
 * 
 * Purpose: Demonstrates common beginner errors and how to fix them
 * 
 * This file contains COMMENTED OUT code showing common mistakes.
 * Uncomment each error one at a time to see the error message,
 * then fix it based on the instructions.
 * 
 * @author CP213 Course
 * @version 1.0
 */
public class Example04_CommonErrors {
    
    public static void main(String[] args) {
        System.out.println("=== Common Java Errors Demo ===\n");
        
        // ========================================
        // ERROR 1: Missing Semicolon
        // ========================================
        // Uncomment to see error:
        // int x = 5
        
        // Fix:
        int x = 5;
        System.out.println("1. Semicolon fixed: x = " + x);
        
        // ========================================
        // ERROR 2: Case Sensitivity
        // ========================================
        // Uncomment to see error:
        // system.out.println("Wrong case");
        
        // Fix: Java is case-sensitive - use System with capital S
        System.out.println("2. Case sensitivity fixed");
        
        // ========================================
        // ERROR 3: String Concatenation Order
        // ========================================
        System.out.println("\n3. Concatenation order:");
        
        // Wrong: Addition happens left to right as string concat
        System.out.println("Sum: " + 5 + 10);  // Outputs "Sum: 510"
        
        // Correct: Use parentheses to force arithmetic first
        System.out.println("Sum: " + (5 + 10)); // Outputs "Sum: 15"
        
        // ========================================
        // ERROR 4: Integer Division
        // ========================================
        System.out.println("\n4. Integer division:");
        
        // Wrong: Integer division truncates
        int result1 = 5 / 2;
        System.out.println("5 / 2 = " + result1);  // Outputs 2, not 2.5
        
        // Correct: Use double for decimal results
        double result2 = 5.0 / 2.0;
        System.out.println("5.0 / 2.0 = " + result2);  // Outputs 2.5
        
        // ========================================
        // ERROR 5: Uninitialized Variable
        // ========================================
        // Uncomment to see error:
        // int count;
        // System.out.println("Count: " + count);
        
        // Fix: Initialize before use
        int count = 0;
        System.out.println("\n5. Initialized variable: count = " + count);
        
        // ========================================
        // ERROR 6: Using = instead of ==
        // ========================================
        System.out.println("\n6. Assignment vs comparison:");
        
        int age = 20;
        
        // Wrong (will cause compilation error in if statement):
        // if (age = 20) { ... }
        
        // Correct: Use == for comparison
        if (age == 20) {
            System.out.println("Age is 20 (using ==)");
        }
        
        // ========================================
        // ERROR 7: Off-by-One in String Indexing
        // ========================================
        System.out.println("\n7. String indexing:");
        
        String word = "Java";
        System.out.println("Word: " + word);
        System.out.println("Length: " + word.length());  // 4
        System.out.println("First char: " + word.charAt(0));  // 'J'
        System.out.println("Last char: " + word.charAt(3));   // 'a'
        
        // Wrong: index out of bounds
        // System.out.println(word.charAt(4));  // ERROR!
        
        // Correct: last index is length - 1
        System.out.println("Last char (correct): " + word.charAt(word.length() - 1));
        
        // ========================================
        // Tips for Debugging
        // ========================================
        System.out.println("\n=== Debugging Tips ===");
        System.out.println("1. Read error messages carefully");
        System.out.println("2. Check line numbers in errors");
        System.out.println("3. Use System.out.println to trace values");
        System.out.println("4. Compile often to catch errors early");
        System.out.println("5. Check for missing semicolons, braces, parentheses");
    }
}

