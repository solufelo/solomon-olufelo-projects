# Lesson 09: Exception Handling - Learning Notes

## Overview
Lesson 09 covers exception handling in Java, including creating custom exceptions, using try-catch blocks, and handling input validation errors.

## Key Concepts

### 1. What are Exceptions?
Exceptions are events that disrupt the normal flow of program execution. They represent error conditions or unexpected situations that need to be handled.

**Why use exceptions?**
- Better error handling than returning error codes
- Forces explicit handling of error conditions
- Separates error handling from normal code flow
- Makes code more readable and maintainable

### 2. Try-Catch Blocks

**Basic Syntax:**
```java
try {
    // Code that might throw an exception
} catch (ExceptionType e) {
    // Handle the exception
}
```

**Example from `ReadInteger.java`:**
- Uses a while loop with try-catch to repeatedly prompt until valid input
- Catches `InputMismatchException` when user enters non-integer input
- Uses `keyboard.nextLine()` to clear the invalid input from the buffer

**Key Points:**
- The try block contains code that might throw an exception
- The catch block handles specific exception types
- Multiple catch blocks can handle different exception types
- Execution continues after the catch block (unless program exits)

### 3. Creating Custom Exceptions

**Custom Exception Class Structure:**
```java
public class BadNumberException extends Exception {
    private int badNumber;
    
    public BadNumberException(int number) {
        super("BadNumberException");
        badNumber = number;
    }
    
    public int getBadNumber() {
        return badNumber;
    }
}
```

**Examples in lesson09:**
- `BadNumberException.java`: Custom exception with additional data (badNumber)
- `ARException.java`: Simple custom exception for division by zero
- `HighScoreException.ScoreNotSetException`: Inner class exception

**Key Points:**
- Custom exceptions extend `Exception` (checked) or `RuntimeException` (unchecked)
- Can add custom fields to store additional error information
- Use `super()` to pass messages to parent Exception class
- Can provide getter methods to access exception data

### 4. Throwing Exceptions

**Syntax:**
```java
throw new ExceptionClassName("Optional message");
```

**Example from `BadNumberExceptionDemo.java`:**
```java
if ((inputNumber != 23) && (inputNumber != 33))
    throw new BadNumberException(inputNumber);
```

**Example from `DivisionDemoFirstVersion.java`:**
```java
if (denominator == 0)
    throw new ARException("division by zero");
```

**Key Points:**
- Use `throw` to explicitly throw an exception
- Must be inside a try-catch block or method with `throws` clause
- Can throw built-in or custom exceptions
- Often used for input validation and business logic errors

### 5. Exception Methods

**Common Exception Methods (from `ExceptionUseGetMessage.java`):**

1. **`getMessage()`**: Returns the error message string
   ```java
   System.out.println(e.getMessage());
   // Output: "my personal error message"
   ```

2. **`toString()`**: Returns string representation of exception
   ```java
   System.out.println(e.toString());
   // Output: "ExceptionUseGetMessage: my personal error message"
   ```

3. **`getClass()`**: Returns the Class object of the exception
   ```java
   System.out.println(e.getClass());
   // Output: class lesson09.ExceptionUseGetMessage
   ```

4. **`printStackTrace()`**: Prints the call stack trace
   ```java
   e.printStackTrace();
   // Shows full stack trace to console
   ```

### 6. Input Validation with Exceptions

**Pattern from `ReadInteger.java` and `ExceptionOnNumberFormat.java`:**
```java
boolean done = false;
while (!done) {
    try {
        System.out.println("Enter a whole number:");
        number = keyboard.nextInt();
        done = true;  // Success - exit loop
    } catch (InputMismatchException e) {
        keyboard.nextLine();  // Clear invalid input
        System.out.println("Not a correctly written whole number.");
        System.out.println("Try again.");
    }
}
```

**Key Points:**
- Loop until valid input is received
- Clear invalid input with `keyboard.nextLine()`
- Provide clear error messages
- This pattern is reusable (see `getIntDemo.java`)

### 7. Exception vs. No Exception Approach

**Comparison: `HighScoreException` vs `HighScoreNoException`**

**Without Exceptions (`HighScoreNoException`):**
```java
public int getScore() {
    if (!scoreSet)
        return -1;  // Magic number indicates error
    else
        return score;
}
```
- Problem: Caller must check for magic number (-1)
- Problem: -1 might be a valid score
- Problem: Easy to forget error checking

**With Exceptions (`HighScoreException`):**
```java
public int getScore() throws ScoreNotSetException {
    if (!scoreSet)
        throw new ScoreNotSetException();
    else
        return score;
}
```
- Advantage: Forces caller to handle the error
- Advantage: No ambiguity about valid vs invalid values
- Advantage: Clear error message
- Advantage: Compiler enforces exception handling

### 8. Inner Class Exceptions

**Example from `HighScoreException.java`:**
```java
public class HighScoreException {
    public class ScoreNotSetException extends Exception {
        // Inner exception class
    }
    
    public int getScore() throws ScoreNotSetException {
        // Uses inner exception
    }
}
```

**Key Points:**
- Exceptions can be defined as inner classes
- Useful when exception is only relevant to one class
- Can access outer class members if needed

## Code Examples Summary

| File | Concept Demonstrated |
|------|---------------------|
| `BadNumberException.java` | Custom exception with data fields |
| `BadNumberExceptionDemo.java` | Throwing and catching custom exception |
| `ARException.java` | Simple custom exception |
| `DivisionDemoFirstVersion.java` | Throwing exception, recovery method |
| `ReadInteger.java` | Input validation loop with exceptions |
| `ExceptionOnNumberFormat.java` | Input validation pattern |
| `ExceptionUseGetMessage.java` | Exception methods (getMessage, toString, etc.) |
| `getIntDemo.java` | Reusable input validation method |
| `HighScoreException.java` | Exception-based error handling |
| `HighScoreNoException.java` | Error code approach (for comparison) |
| `ExceptionHandlingClass.java` | Template/skeleton for exception handling |

## Common Patterns

### Pattern 1: Input Validation Loop
```java
boolean done = false;
while (!done) {
    try {
        // Get input
        done = true;
    } catch (InputMismatchException e) {
        keyboard.nextLine();
        // Error message
    }
}
```

### Pattern 2: Custom Exception with Data
```java
public class CustomException extends Exception {
    private int errorData;
    
    public CustomException(int data) {
        super("Error message");
        errorData = data;
    }
    
    public int getErrorData() {
        return errorData;
    }
}
```

### Pattern 3: Throwing for Validation
```java
if (invalidCondition) {
    throw new CustomException(errorData);
}
```

## What I Tried
- Reviewed all exception handling examples in lesson09
- Analyzed the difference between exception-based and error-code approaches
- Examined input validation patterns with try-catch loops
- Studied custom exception creation and usage

## What Confused Me
- **Checked vs Unchecked Exceptions**: Need to understand when to use `Exception` vs `RuntimeException`
- **Exception Propagation**: How exceptions bubble up through method calls
- **When to Create Custom Exceptions**: Guidelines for creating custom exceptions vs using built-in ones
- **Finally Blocks**: Not covered in these examples, but important for cleanup code

## Next Actions
1. **Practice**: Write a program that validates user input for multiple data types (int, double, String)
2. **Experiment**: Create a custom exception hierarchy (base exception with specific subclasses)
3. **Study**: Learn about `finally` blocks and when to use them
4. **Review**: Understand checked vs unchecked exceptions in Java
5. **Apply**: Use exception handling in upcoming assignments/labs
6. **Compare**: Practice converting error-code approaches to exception-based approaches

## Key Takeaways
1. ✅ Exceptions provide better error handling than magic numbers or error codes
2. ✅ Try-catch blocks allow graceful error recovery
3. ✅ Custom exceptions can carry additional error information
4. ✅ Input validation loops with exceptions create robust user input handling
5. ✅ Exception methods (getMessage, printStackTrace) help with debugging
6. ✅ Exceptions force explicit error handling, making code more reliable

## Study Questions
1. What's the difference between `throw` and `throws`?
2. When should you create a custom exception vs use a built-in one?
3. Why is `keyboard.nextLine()` needed in the catch block for input validation?
4. What happens if an exception is thrown but not caught?
5. How do you handle multiple different exception types in one method?

## Related Topics
- **Lab 6**: Exception Handling (due Nov 13) - Apply these concepts
- **Week 10**: Focus on exception handling in course schedule
- **Java Documentation**: `java.lang.Exception`, `java.util.InputMismatchException`

---
*Generated from lesson09 workspace examples*
*Last updated: [Current Date]*

