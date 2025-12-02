# Practice Problems - Java Development Basics

Complete these 10 problems in order. Solutions are in the `solutions/` folder, but **try them yourself first!**

---

## Problem 1: First Program ⭐
**Difficulty**: Easy | **Time**: 5 minutes

Write a Java program named `FirstProgram.java` that prints your name, student ID, and course name on separate lines.

**Expected Output:**
```
Name: Solomon Olufelo
Student ID: 210729170
Course: CP213 - Java Programming
```

**Concepts**: Basic program structure, println

---

## Problem 2: Math Calculator ⭐
**Difficulty**: Easy | **Time**: 10 minutes

Write a program `MathCalc.java` that:
1. Declares two integer variables (a = 15, b = 4)
2. Calculates and prints: sum, difference, product, quotient, and remainder
3. Uses proper labels for output

**Expected Output:**
```
a = 15, b = 4
Sum: 19
Difference: 11
Product: 60
Quotient: 3
Remainder: 3
```

**Concepts**: Variables, arithmetic operators, output

---

## Problem 3: Circle Calculator ⭐⭐
**Difficulty**: Medium | **Time**: 15 minutes

Write `CircleCalc.java` that:
1. Declares a constant `PI = 3.14159`
2. Declares a variable `radius = 5.0`
3. Calculates area (πr²) and circumference (2πr)
4. Prints results with 2 decimal places using `printf`

**Expected Output:**
```
Radius: 5.00
Area: 78.54
Circumference: 31.42
```

**Hint**: Use `System.out.printf("%.2f", value)` for 2 decimal places

**Concepts**: Constants, floating-point math, printf

---

## Problem 4: Temperature Converter ⭐⭐
**Difficulty**: Medium | **Time**: 15 minutes

Write `TempConverter.java` that converts Celsius to Fahrenheit.

**Formula**: F = (C × 9/5) + 32

Test with these values:
- 0°C → 32°F
- 100°C → 212°F
- -40°C → -40°F

**Expected Output:**
```
0°C = 32.0°F
100°C = 212.0°F
-40°C = -40.0°F
```

**Hint**: Use `double` to avoid integer division!

**Concepts**: Floating-point arithmetic, type casting

---

## Problem 5: Documentation Practice ⭐⭐
**Difficulty**: Medium | **Time**: 20 minutes

Create `Student.java` with:
1. A class constant `MAX_CREDITS = 6` (per semester)
2. A method `calculateGPA()` that takes 3 grades (doubles) and returns average
3. A main method that tests with grades: 85.5, 92.0, 78.5
4. **Full JavaDoc documentation** for class and method

**Expected Output:**
```
Grade 1: 85.5
Grade 2: 92.0
Grade 3: 78.5
GPA: 85.33
Maximum Credits: 6
```

**Concepts**: Constants, methods, JavaDoc, formatting

---

## Problem 6: Error Hunt 🐛⭐⭐
**Difficulty**: Medium | **Time**: 15 minutes

Fix all errors in this code (save as `ErrorHunt.java`):

```java
public class errorhunt {
    public static void main(string[] args) {
        int x = 5
        int y = 10;
        
        System.out.println("Sum: " + x + y);
        
        double result = x / 2;
        system.out.println("Half of x: " + result);
        
        String name = "Java
        System.out.println(name);
    }
}
```

**Errors to find**: 7 errors total

**Concepts**: Syntax rules, case sensitivity, semicolons, strings

---

## Problem 7: Receipt Generator ⭐⭐⭐
**Difficulty**: Hard | **Time**: 25 minutes

Create `Receipt.java` that prints a formatted store receipt:

**Requirements:**
- Item 1: $12.99
- Item 2: $8.50
- Item 3: $24.99
- Tax rate: 13%
- Calculate subtotal, tax, and total
- Format all prices to 2 decimal places
- Align numbers properly

**Expected Output:**
```
========== RECEIPT ==========
Item 1:              $12.99
Item 2:               $8.50
Item 3:              $24.99
----------------------------
Subtotal:            $46.48
Tax (13%):            $6.04
----------------------------
Total:               $52.52
============================
```

**Hint**: Use `System.out.printf("%-20s $%6.2f\n", label, price)`

**Concepts**: Constants, arithmetic, printf formatting

---

## Problem 8: Name Formatter ⭐⭐⭐
**Difficulty**: Hard | **Time**: 20 minutes

Write `NameFormatter.java` that:
1. Takes a full name as a String: "Solomon James Olufelo"
2. Prints: first name, middle name, last name (each on separate line)
3. Prints initials: "SJO"
4. Counts total characters (excluding spaces)

**Expected Output:**
```
Full Name: Solomon James Olufelo
First Name: Solomon
Middle Name: James
Last Name: Olufelo
Initials: SJO
Total Characters: 20
```

**Hint**: Use `indexOf()`, `substring()`, `length()`, `charAt()`

**Concepts**: String methods, character manipulation

---

## Problem 9: Debug Challenge 🐛⭐⭐⭐
**Difficulty**: Hard | **Time**: 20 minutes

This program should calculate average test scores but has **logic errors** (not syntax errors). Find and fix them:

```java
public class DebugChallenge {
    public static void main(String[] args) {
        int test1 = 85;
        int test2 = 90;
        int test3 = 78;
        
        // Calculate average
        int average = test1 + test2 + test3 / 3;
        
        // Check if passing (60 or higher)
        boolean passing = average >= 60;
        
        System.out.println("Test 1: " + test1);
        System.out.println("Test 2: " + test2);
        System.out.println("Test 3: " + test3);
        System.out.println("Average: " + average);
        System.out.println("Passing: " + passing);
    }
}
```

**Hint**: The average calculation is wrong!

**Concepts**: Order of operations, type casting

---

## Problem 10: Style Checker ⭐⭐⭐
**Difficulty**: Hard | **Time**: 25 minutes

Write `StyleExample.java` following ALL these style rules:
1. Proper class naming (PascalCase)
2. Proper variable naming (camelCase)
3. At least one constant (UPPER_SNAKE_CASE)
4. JavaDoc for class and all methods
5. Proper indentation (4 spaces)
6. Blank lines between methods
7. Meaningful variable names
8. Comments explaining non-obvious logic

**Program requirements:**
- Calculate BMI (Body Mass Index)
- Formula: BMI = weight(kg) / (height(m))²
- Test with: weight = 70kg, height = 1.75m
- Expected BMI: 22.86

**This problem tests**: All style and documentation skills

---

## 🎯 Completion Checklist

- [ ] Problem 1: First Program
- [ ] Problem 2: Math Calculator
- [ ] Problem 3: Circle Calculator
- [ ] Problem 4: Temperature Converter
- [ ] Problem 5: Documentation Practice
- [ ] Problem 6: Error Hunt
- [ ] Problem 7: Receipt Generator
- [ ] Problem 8: Name Formatter
- [ ] Problem 9: Debug Challenge
- [ ] Problem 10: Style Checker

**Goal**: Complete at least 7/10 before moving to the mini-project.

---

## 💡 Tips

1. **Test your code** after every small change
2. **Read error messages** - they tell you exactly what's wrong
3. **Compare output** with expected output carefully
4. **Use printf** for formatted output (numbers with decimals)
5. **Don't copy-paste** - type the code to build muscle memory

**Ready? Start with Problem 1!**

