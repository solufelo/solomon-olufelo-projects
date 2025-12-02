# Flashcards - Java Development Basics

Use these for active recall. Cover the answer and test yourself!

---

## Basic Program Structure

**Q: What are the three essential parts of every Java program?**
<details>
<summary>Answer</summary>

1. Class declaration: `public class ClassName`
2. Main method: `public static void main(String[] args)`
3. Code statements inside main method
</details>

---

**Q: What must the filename match in Java?**
<details>
<summary>Answer</summary>

The filename must EXACTLY match the public class name (including case).
Example: `public class HelloWorld` must be in `HelloWorld.java`
</details>

---

**Q: What is the purpose of the main method?**
<details>
<summary>Answer</summary>

The main method is the **entry point** of a Java program - it's where the JVM starts executing your code. Every executable Java program must have a main method.
</details>

---

## Compilation & Execution

**Q: What command compiles a Java program?**
<details>
<summary>Answer</summary>

`javac FileName.java`

This creates a `.class` file containing bytecode.
</details>

---

**Q: What command runs a compiled Java program?**
<details>
<summary>Answer</summary>

`java ClassName`

**Important**: Do NOT include the `.class` extension!
</details>

---

**Q: What is bytecode?**
<details>
<summary>Answer</summary>

Bytecode is the compiled form of Java code (stored in `.class` files) that runs on the Java Virtual Machine (JVM). It's platform-independent, allowing "Write Once, Run Anywhere."
</details>

---

**Q: What's the difference between JDK, JRE, and JVM?**
<details>
<summary>Answer</summary>

- **JDK** (Java Development Kit): Tools for developing Java programs (includes compiler, debugger)
- **JRE** (Java Runtime Environment): Environment for running Java programs (includes JVM)
- **JVM** (Java Virtual Machine): Executes bytecode
</details>

---

## Comments & Documentation

**Q: What are the three types of comments in Java?**
<details>
<summary>Answer</summary>

1. **Single-line**: `// comment`
2. **Multi-line**: `/* comment */`
3. **JavaDoc**: `/** comment */`
</details>

---

**Q: When should you use JavaDoc comments?**
<details>
<summary>Answer</summary>

Use JavaDoc for:
- Class descriptions
- Method descriptions
- Public API documentation
- When you want to generate HTML documentation

Example:
```java
/**
 * Calculates the area
 * @param radius the circle radius
 * @return the area
 */
```
</details>

---

**Q: What command generates documentation from JavaDoc comments?**
<details>
<summary>Answer</summary>

`javadoc FileName.java`

This creates HTML documentation files.
</details>

---

## Naming Conventions

**Q: What naming convention is used for classes?**
<details>
<summary>Answer</summary>

**PascalCase** (UpperCamelCase): Each word starts with capital letter, no spaces.

Examples: `StudentRecord`, `BankAccount`, `HelloWorld`
</details>

---

**Q: What naming convention is used for variables and methods?**
<details>
<summary>Answer</summary>

**camelCase**: First word lowercase, subsequent words capitalized.

Examples: `studentName`, `totalScore`, `calculateAverage()`
</details>

---

**Q: What naming convention is used for constants?**
<details>
<summary>Answer</summary>

**UPPER_SNAKE_CASE**: All uppercase with underscores between words.

Examples: `MAX_SIZE`, `PI_VALUE`, `TAX_RATE`
</details>

---

**Q: How do you declare a constant in Java?**
<details>
<summary>Answer</summary>

Use `final` keyword:
```java
public static final double PI = 3.14159;
public static final int MAX_STUDENTS = 100;
```

`final` means the value cannot be changed.
</details>

---

## Output

**Q: What's the difference between print() and println()?**
<details>
<summary>Answer</summary>

- **print()**: Prints without adding newline at the end
- **println()**: Prints and adds newline (moves to next line)

```java
System.out.print("Hello ");   // No newline
System.out.println("World!");  // Adds newline
// Output: Hello World!
```
</details>

---

**Q: What are common escape sequences?**
<details>
<summary>Answer</summary>

| Sequence | Result |
|----------|--------|
| `\n` | Newline |
| `\t` | Tab |
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |
</details>

---

**Q: How do you format output with printf()?**
<details>
<summary>Answer</summary>

```java
System.out.printf("format string", arguments);
```

Common format specifiers:
- `%d` - integer
- `%f` - floating point
- `%.2f` - floating point with 2 decimals
- `%s` - string

Example:
```java
System.out.printf("Price: $%.2f\n", 19.99);
// Output: Price: $19.99
```
</details>

---

## Common Errors

**Q: What does "cannot find symbol" error mean?**
<details>
<summary>Answer</summary>

The compiler can't find the variable, method, or class you're trying to use. Common causes:
- Typo in the name
- Variable not declared
- Wrong scope
- Case sensitivity issue (Java is case-sensitive!)
</details>

---

**Q: What causes "class X is public, should be declared in a file named X.java"?**
<details>
<summary>Answer</summary>

The filename doesn't match the public class name. 

Fix: Rename the file to match the class name exactly (including case).
</details>

---

**Q: Why does "5 + 10" print as "510" instead of "15"?**
<details>
<summary>Answer</summary>

String concatenation is happening instead of addition:
```java
System.out.println("Sum: " + 5 + 10);  // "Sum: 510"
```

Fix: Use parentheses to force arithmetic first:
```java
System.out.println("Sum: " + (5 + 10));  // "Sum: 15"
```
</details>

---

**Q: Why does 5/2 equal 2 instead of 2.5?**
<details>
<summary>Answer</summary>

Integer division truncates the decimal part.

```java
int result = 5 / 2;     // result = 2 (integer division)
double result = 5.0 / 2.0;  // result = 2.5 (floating-point division)
```

Fix: Use at least one double value in the division.
</details>

---

## Style & Best Practices

**Q: What is proper Java indentation?**
<details>
<summary>Answer</summary>

Use **4 spaces** (or 1 tab) for each indentation level:

```java
public class Example {
    public static void main(String[] args) {
        if (condition) {
            // code here
        }
    }
}
```
</details>

---

**Q: What makes a good variable name?**
<details>
<summary>Answer</summary>

Good variable names are:
- **Descriptive**: `studentAge` not `a`
- **CamelCase**: `totalScore` not `total_score`
- **Not too long**: `avgScore` not `averageScoreForTheStudent`
- **Meaningful**: `count` not `x123`
</details>

---

**Q: When should you add comments?**
<details>
<summary>Answer</summary>

**DO comment:**
- WHY you're doing something (not WHAT)
- Complex algorithms or logic
- Non-obvious code
- Public methods (use JavaDoc)

**DON'T comment:**
- Obvious code (`i++; // increment i`)
- Instead of fixing bad code
- Outdated information
</details>

---

## Debugging

**Q: What are three ways to debug a Java program?**
<details>
<summary>Answer</summary>

1. **Print statements**: `System.out.println("Debug: x = " + x);`
2. **IDE debugger**: Set breakpoints and step through code
3. **Compiler warnings**: Use `javac -Xlint` to see all warnings
</details>

---

**Q: What should you check first when your program won't compile?**
<details>
<summary>Answer</summary>

1. **Semicolons**: Every statement needs one
2. **Braces**: All `{` need matching `}`
3. **Parentheses**: All `(` need matching `)`
4. **Quotes**: All strings need closing quotes
5. **Case**: Java is case-sensitive
</details>

---

**Q: How can you find logic errors (not syntax errors)?**
<details>
<summary>Answer</summary>

1. **Add print statements** to track variable values
2. **Test edge cases** (zero, negative, max values)
3. **Verify calculations** by hand
4. **Check operator precedence**: `5 + 3 * 2 = 11` not `16`
5. **Use a debugger** to step through code line by line
</details>

---

## Quizlet Import Format

Copy-paste this into Quizlet (tab-separated):

```
What are the three essential parts of every Java program?	1. Class declaration: public class ClassName, 2. Main method: public static void main(String[] args), 3. Code statements inside main method
What must the filename match in Java?	The filename must EXACTLY match the public class name (including case)
What command compiles a Java program?	javac FileName.java
What command runs a compiled Java program?	java ClassName (without .class extension)
What are the three types of comments in Java?	Single-line: //, Multi-line: /* */, JavaDoc: /** */
What naming convention is used for classes?	PascalCase (UpperCamelCase): StudentRecord, BankAccount
What naming convention is used for variables?	camelCase: studentName, totalScore
What naming convention is used for constants?	UPPER_SNAKE_CASE: MAX_SIZE, PI_VALUE
What's the difference between print() and println()?	print() - no newline, println() - adds newline
How do you declare a constant in Java?	public static final double PI = 3.14159;
What does \n do in a string?	Creates a newline
What does \t do in a string?	Creates a tab
Why does 5/2 equal 2 instead of 2.5?	Integer division truncates decimals. Use 5.0/2.0 for correct result
What is bytecode?	Compiled Java code (.class files) that runs on the JVM
What is the purpose of the main method?	Entry point where JVM starts executing the program
```

---

**Study Method**: 
1. Go through all cards once
2. Mark difficult ones
3. Review difficult cards 3 times
4. Test yourself the next day
5. Repeat until you get 100% correct

**Goal**: Answer all questions correctly in under 60 seconds each.

