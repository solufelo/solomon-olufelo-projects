/**
 * Example02_Variables.java
 * 
 * Purpose: Demonstrates variable declaration, initialization, and constants
 * 
 * Key Concepts:
 * - Primitive data types
 * - Variable naming conventions
 * - Constants (final keyword)
 * - Basic arithmetic
 * 
 * @author CP213 Course
 * @version 1.0
 */
public class Example02_Variables {
    
    // Class constant - available to all methods
    public static final double TAX_RATE = 0.13;
    
    public static void main(String[] args) {
        // Integer variables
        int age = 20;
        int year = 2025;
        
        // Floating point variables
        double price = 19.99;
        double total = price * (1 + TAX_RATE);
        
        // Character and String
        char grade = 'A';
        String studentName = "Solomon";
        
        // Boolean
        boolean isPassing = true;
        
        // Display all variables
        System.out.println("=== Student Information ===");
        System.out.println("Name: " + studentName);
        System.out.println("Age: " + age);
        System.out.println("Grade: " + grade);
        System.out.println("Passing: " + isPassing);
        
        System.out.println("\n=== Purchase Calculation ===");
        System.out.println("Price: $" + price);
        System.out.println("Tax Rate: " + (TAX_RATE * 100) + "%");
        System.out.println("Total: $" + total);
        
        // Arithmetic operations
        int sum = age + year;
        int difference = year - age;
        int product = age * 2;
        int quotient = year / age;
        int remainder = year % age;
        
        System.out.println("\n=== Arithmetic Examples ===");
        System.out.println(age + " + " + year + " = " + sum);
        System.out.println(year + " - " + age + " = " + difference);
        System.out.println(age + " * 2 = " + product);
        System.out.println(year + " / " + age + " = " + quotient);
        System.out.println(year + " % " + age + " = " + remainder);
    }
}

