# Lecture Note: Exception Handling in Java
**Course:** CP213 - Object Oriented Programming
**Topic:** Error Handling, Try-Catch, and Custom Exceptions

---

## 1. Overview of Exceptions
Exceptions are events that disrupt the normal flow of program execution. Java uses exceptions to handle errors gracefully rather than crashing or using obscure error codes.

### Key Benefits
*   **Separation of Concerns:** Error handling code is separated from "regular" business logic.
*   **Propagation:** Errors can bubble up the call stack to where they can be handled.
*   **Grouping:** Error types can be grouped by hierarchy (e.g., `IOException`).

---

## 2. The Try-Catch Block
The fundamental structure for handling exceptions.

```java
try {
    // Code that might throw an exception
    int result = 10 / 0; 
} catch (ArithmeticException e) {
    // Handle specific exception
    System.out.println("Cannot divide by zero.");
} catch (Exception e) {
    // Handle general exceptions
    System.out.println("Something went wrong: " + e.getMessage());
} finally {
    // Optional: Code that runs regardless of success or failure
    // Useful for closing resources (files, scanners)
    System.out.println("Cleanup complete.");
}
```

---

## 3. Exception Hierarchy

### 3.1 Checked Exceptions
*   Must be handled (try-catch) or declared (`throws`).
*   Represent external errors (e.g., `FileNotFoundException`, `IOException`).
*   Compiler enforces handling.

### 3.2 Unchecked Exceptions (RuntimeExceptions)
*   Do not typically need to be explicitly handled (though good practice).
*   Represent programming errors (e.g., `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`).

---

## 4. Creating Custom Exceptions
You can define your own exception types by extending `Exception` (checked) or `RuntimeException` (unchecked).

```java
public class BadNumberException extends Exception {
    private int badNumber;
    
    public BadNumberException(int number) {
        super("Invalid number provided: " + number);
        this.badNumber = number;
    }
    
    public int getBadNumber() {
        return badNumber;
    }
}
```

### Usage:
```java
public void checkNumber(int num) throws BadNumberException {
    if (num < 0) {
        throw new BadNumberException(num);
    }
}
```

---

## 5. Input Validation Pattern
A common pattern in CP213 for robust user input.

```java
Scanner keyboard = new Scanner(System.in);
boolean done = false;
int value = 0;

while (!done) {
    try {
        System.out.print("Enter a whole number: ");
        value = keyboard.nextInt();
        done = true; // Success!
    } catch (InputMismatchException e) {
        keyboard.nextLine(); // Important: Clear invalid input from buffer
        System.out.println("That's not a number. Try again.");
    }
}
```

---

## 6. Key Methods
*   `e.getMessage()`: Get the error message string.
*   `e.printStackTrace()`: Print the full stack trace (useful for debugging).
*   `e.toString()`: String representation of the exception.

---
*Notes derived from Lesson 09 - Exception Handling.*

