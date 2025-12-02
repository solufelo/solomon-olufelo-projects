# Java Development Basics - Core Concepts

## 🎯 The Big Picture

**Java is compiled AND interpreted:**
```
Your Code (.java) → Compiler (javac) → Bytecode (.class) → JVM → Runs on any OS
```

This is why Java is "Write Once, Run Anywhere" (WORA)

---

## 1. Java Program Structure

Every Java program needs these 3 things:

### **Minimum Working Program**
```java
public class ClassName {
    public static void main(String[] args) {
        // Your code here
    }
}
```

### **Key Rules**
1. **Filename MUST match class name**: `ClassName.java`
2. **One public class per file**
3. **`main` method is the entry point** (where program starts)
4. **Case sensitive**: `Main` ≠ `main`

---

## 2. The Compilation & Execution Process

### **Compilation** (Creating the .class file)
```bash
javac ClassName.java
```
- Checks for syntax errors
- Creates `ClassName.class` (bytecode)
- Bytecode runs on JVM (Java Virtual Machine)

### **Execution** (Running the program)
```bash
java ClassName
```
- **DO NOT include .class extension**
- JVM loads and runs the bytecode

### **Common Errors**

| Error | Cause | Fix |
|-------|-------|-----|
| `javac: command not found` | Java not installed | Install JDK |
| `error: class HelloWorld is public, should be declared in a file named HelloWorld.java` | Filename doesn't match class name | Rename file |
| `Error: Could not find or load main class` | Wrong command or no main method | Check spelling, add main method |

---

## 3. Documentation & Comments

### **Three Types of Comments**

```java
// 1. Single-line comment - for quick notes

/* 2. Multi-line comment
   Use for longer explanations
   spanning multiple lines */

/** 3. JavaDoc comment
 * Used to generate documentation
 * @param args command line arguments
 * @return nothing (void)
 */
```

### **When to Comment**

**DO Comment:**
- Why you're doing something
- Complex logic or algorithms
- Public methods (use JavaDoc)
- Non-obvious code

**DON'T Comment:**
- Obvious code (`i++; // increment i` ← BAD)
- Outdated information
- Instead of fixing bad code

### **JavaDoc Example**
```java
/**
 * Calculates the area of a circle
 * @param radius the circle's radius
 * @return the area of the circle
 */
public static double calculateArea(double radius) {
    return Math.PI * radius * radius;
}
```

Generate docs: `javadoc ClassName.java`

---

## 4. Java Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| **Class** | PascalCase (UpperCamelCase) | `StudentRecord`, `BankAccount` |
| **Method** | camelCase | `calculateTotal()`, `getName()` |
| **Variable** | camelCase | `studentName`, `totalScore` |
| **Constant** | UPPER_SNAKE_CASE | `MAX_SIZE`, `PI_VALUE` |
| **Package** | lowercase | `com.example.project` |

### **Constants**
```java
public static final double PI = 3.14159;
public static final int MAX_STUDENTS = 100;
```

---

## 5. Program Style Best Practices

### **Indentation & Spacing**
```java
// GOOD
public class Example {
    public static void main(String[] args) {
        int x = 5;
        if (x > 0) {
            System.out.println("Positive");
        }
    }
}

// BAD
public class Example{
public static void main(String[] args){
int x=5;
if(x>0){System.out.println("Positive");}}}
```

### **Consistent Brace Style**
```java
// K&R Style (most common in Java)
public void method() {
    if (condition) {
        // code
    } else {
        // code
    }
}
```

### **Meaningful Names**
```java
// GOOD
int studentAge;
double accountBalance;

// BAD
int a;        // What is 'a'?
double x123;  // Meaningless
```

---

## 6. Basic Debugging Strategies

### **Print Statement Debugging**
```java
System.out.println("Debug: x = " + x);
System.out.println("Reached this point");
```

### **Common Beginner Mistakes**

1. **Missing Semicolon**
```java
int x = 5  // ERROR: missing semicolon
```

2. **Case Sensitivity**
```java
System.out.println("Hello");  // ✅ Correct
system.out.println("Hello");  // ❌ 'system' not found
```

3. **String Concatenation**
```java
System.out.println("Age: " + 25);      // ✅ "Age: 25"
System.out.println("Sum: " + 5 + 10);  // ⚠️ "Sum: 510" (not 15!)
System.out.println("Sum: " + (5 + 10)); // ✅ "Sum: 15"
```

---

## 7. Basic Output

### **System.out Methods**
```java
System.out.print("No newline");
System.out.println("With newline");
System.out.printf("Formatted: %d\n", 42);
```

### **Escape Sequences**
| Sequence | Result |
|----------|--------|
| `\n` | Newline |
| `\t` | Tab |
| `\"` | Double quote |
| `\\` | Backslash |

```java
System.out.println("Line 1\nLine 2");
System.out.println("Name:\tJohn");
System.out.println("He said \"Hello\"");
```

---

## 🎯 Key Takeaways

1. **Java file = Java class**: Filename must match public class name
2. **Compile first, run second**: `javac` → `java`
3. **main method is required**: Program entry point
4. **Comment WHY, not WHAT**: Make code self-explanatory
5. **Follow conventions**: Makes code readable and professional
6. **Debug with prints**: Simple but effective
7. **Syntax matters**: Java is case-sensitive and strict

---

## 🔗 Quick Reference Commands

```bash
# Compile
javac MyProgram.java

# Run
java MyProgram

# Compile with all warnings
javac -Xlint MyProgram.java

# Generate JavaDoc
javadoc MyProgram.java

# Run with classpath
java -cp . MyProgram
```

---

## ✅ Self-Check

Before moving on, make sure you can:
- [ ] Write a complete Java program from scratch
- [ ] Compile and run a program without errors
- [ ] Explain what the compiler does vs. what the JVM does
- [ ] Add proper comments and JavaDoc
- [ ] Follow Java naming conventions
- [ ] Debug simple syntax errors

**Now try the examples in `02-examples/`!**

