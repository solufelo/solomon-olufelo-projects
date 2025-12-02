# Lesson 09: Exception Handling - Quick Reference

This lesson covers exception handling in Java. For comprehensive learning notes, see:
**`/home/solom/Projects/CP213/notes/lesson09-exception-handling-notes.md`**

## Files in This Lesson

### Core Concepts

1. **`BadNumberException.java`** - Custom exception class
   - Shows how to create a custom exception
   - Includes additional data field (badNumber)
   - Multiple constructors for flexibility

2. **`BadNumberExceptionDemo.java`** - Using custom exceptions
   - Demonstrates throwing and catching custom exceptions
   - Shows how to access exception data

3. **`ARException.java`** - Simple custom exception
   - Basic custom exception structure
   - Used for division by zero errors

4. **`DivisionDemoFirstVersion.java`** - Exception with recovery
   - Throws exception for division by zero
   - Shows recovery method (`secondChance()`)
   - Demonstrates program flow after exception

### Input Validation

5. **`ReadInteger.java`** - Input validation loop
   - Catches `InputMismatchException`
   - Uses while loop to retry until valid input
   - Clears invalid input with `keyboard.nextLine()`

6. **`ExceptionOnNumberFormat.java`** - Input validation pattern
   - Similar pattern to ReadInteger
   - Shows reusable input validation approach

7. **`getIntDemo.java`** - Reusable input method
   - Encapsulates input validation in a method
   - Returns validated integer
   - Can be reused across programs

### Exception Methods

8. **`ExceptionUseGetMessage.java`** - Exception methods demo
   - `getMessage()` - error message
   - `toString()` - string representation
   - `getClass()` - exception class
   - `printStackTrace()` - call stack trace

### Design Patterns

9. **`HighScoreException.java`** - Exception-based design
   - Uses exceptions for error handling
   - Inner class exception (`ScoreNotSetException`)
   - Method with `throws` clause

10. **`HighScoreNoException.java`** - Error code approach
    - Uses magic number (-1) for errors
    - Compare with HighScoreException to see benefits of exceptions

### Templates

11. **`ExceptionHandlingClass.java`** - Template/skeleton
    - Basic structure for exception handling
    - Commented template code

## Quick Study Guide

1. **Start Here**: Read `BadNumberException.java` and `BadNumberExceptionDemo.java`
2. **Input Validation**: Study `ReadInteger.java` and `getIntDemo.java`
3. **Exception Methods**: Review `ExceptionUseGetMessage.java`
4. **Design Comparison**: Compare `HighScoreException.java` vs `HighScoreNoException.java`
5. **Practice**: Try modifying examples to handle different error cases

## Key Patterns to Learn

- ✅ Creating custom exceptions
- ✅ Try-catch blocks
- ✅ Throwing exceptions
- ✅ Input validation loops
- ✅ Exception methods
- ✅ Exception vs error code design

## Full Notes

For detailed explanations, examples, and study questions, see:
**`../../notes/lesson09-exception-handling-notes.md`**

