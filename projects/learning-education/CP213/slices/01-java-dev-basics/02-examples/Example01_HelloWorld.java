/**
 * Example01_HelloWorld.java
 * 
 * Purpose: Demonstrates the most basic Java program structure
 * 
 * Key Concepts:
 * - Class declaration
 * - main method syntax
 * - Basic output
 * 
 * How to run:
 * 1. javac Example01_HelloWorld.java
 * 2. java Example01_HelloWorld
 * 
 * @author CP213 Course
 * @version 1.0
 */
public class Example01_HelloWorld {
    
    /**
     * Main method - program entry point
     * @param args command line arguments (not used here)
     */
    public static void main(String[] args) {
        // Print a message to the console
        System.out.println("Hello, Java World!");
        
        // Print without newline
        System.out.print("This is ");
        System.out.print("on the same line.\n");
        
        // Print with escape sequences
        System.out.println("Tab:\tSpaced\tOut");
        System.out.println("Quote: \"Hello\"");
        System.out.println("Backslash: \\");
    }
}

