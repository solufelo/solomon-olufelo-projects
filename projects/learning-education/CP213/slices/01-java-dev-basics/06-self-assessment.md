# Self-Assessment - Java Development Basics

**Time Limit**: 30 minutes | **Passing Score**: 16/20 (80%)

Complete this without looking at notes. This simulates exam conditions.

---

## Part 1: Multiple Choice (10 questions × 2 points = 20 points)

### Question 1
What is the correct way to compile a Java file named `Student.java`?

A) `java Student.java`  
B) `javac Student`  
C) `javac Student.java`  
D) `compile Student.java`  

<details>
<summary>Answer</summary>
**C) javac Student.java**
</details>

---

### Question 2
Which of the following is the correct main method signature?

A) `public void main(String[] args)`  
B) `public static void main(String args)`  
C) `public static void main(String[] args)`  
D) `static void main(String[] args)`  

<details>
<summary>Answer</summary>
**C) public static void main(String[] args)**
</details>

---

### Question 3
What is the output of this code?
```java
System.out.print("Hello ");
System.out.println("World");
System.out.print("!");
```

A) `Hello World!`  
B) `Hello World` (newline) `!`  
C) `Hello` (newline) `World!`  
D) Compile error  

<details>
<summary>Answer</summary>
**B)** Output is:
```
Hello World
!
```
println adds newline after "World", then print adds "!" on next line.
</details>

---

### Question 4
Which naming convention is correct for a constant?

A) `maxValue`  
B) `MaxValue`  
C) `MAX_VALUE`  
D) `max_value`  

<details>
<summary>Answer</summary>
**C) MAX_VALUE** (UPPER_SNAKE_CASE for constants)
</details>

---

### Question 5
What type of comment is used for JavaDoc?

A) `// comment`  
B) `/* comment */`  
C) `/** comment */`  
D) `# comment`  

<details>
<summary>Answer</summary>
**C) /** comment */** (JavaDoc uses /** */)
</details>

---

### Question 6
What is the output of: `System.out.println("Result: " + 5 + 10);`

A) `Result: 15`  
B) `Result: 510`  
C) `Result: 5 10`  
D) Compile error  

<details>
<summary>Answer</summary>
**B) Result: 510** (String concatenation happens left to right, not arithmetic)
</details>

---

### Question 7
What is the result of `5 / 2` in Java?

A) `2.5`  
B) `2`  
C) `3`  
D) Compile error  

<details>
<summary>Answer</summary>
**B) 2** (Integer division truncates decimal part)
</details>

---

### Question 8
Which keyword makes a variable's value unchangeable?

A) `const`  
B) `final`  
C) `static`  
D) `immutable`  

<details>
<summary>Answer</summary>
**B) final**
</details>

---

### Question 9
If a class is named `HelloWorld`, what must the filename be?

A) `helloworld.java`  
B) `HelloWorld.java`  
C) `hello_world.java`  
D) Any name ending in `.java`  

<details>
<summary>Answer</summary>
**B) HelloWorld.java** (Must match class name exactly, including case)
</details>

---

### Question 10
What does `\n` do in a string?

A) Creates a tab  
B) Creates a space  
C) Creates a newline  
D) Creates a backslash  

<details>
<summary>Answer</summary>
**C) Creates a newline**
</details>

---

## Part 2: True/False (5 questions × 2 points = 10 points)

### Question 11
Java is case-sensitive (True/False)

<details>
<summary>Answer</summary>
**True** - `System` ≠ `system`, `Main` ≠ `main`
</details>

---

### Question 12
You can have multiple public classes in one `.java` file (True/False)

<details>
<summary>Answer</summary>
**False** - Only ONE public class per file
</details>

---

### Question 13
The `main` method must be `public static void` (True/False)

<details>
<summary>Answer</summary>
**True** - This is the required signature for the entry point
</details>

---

### Question 14
Variables should use PascalCase naming (True/False)

<details>
<summary>Answer</summary>
**False** - Variables use camelCase. Classes use PascalCase.
</details>

---

### Question 15
Comments are ignored by the compiler (True/False)

<details>
<summary>Answer</summary>
**True** - Comments are for humans, not the compiler
</details>

---

## Part 3: Code Analysis (3 questions × 5 points = 15 points)

### Question 16
Find and list ALL errors in this code:

```java
public class example {
    public static void main(string[] args) {
        int x = 10
        System.out.println("Value: " + x);
        
        double result = x / 3;
        system.out.println(result);
    }
}
```

<details>
<summary>Answer (5 points - 1 point each)</summary>

1. **Line 1**: Class name should be `Example` (PascalCase)
2. **Line 2**: `string` should be `String` (case-sensitive)
3. **Line 3**: Missing semicolon after `int x = 10`
4. **Line 6**: `system` should be `System` (case-sensitive)
5. **Line 6**: Integer division - `result` will be `3.0`, not `3.333...` (should use `x / 3.0`)
</details>

---

### Question 17
What is the output of this program?

```java
public class Test {
    public static void main(String[] args) {
        int a = 5;
        int b = 2;
        double c = a / b;
        System.out.println(c);
    }
}
```

<details>
<summary>Answer (5 points)</summary>

**Output**: `2.0`

**Explanation**: Even though `c` is a double, the division `a / b` is integer division (5/2=2), then the result (2) is converted to double (2.0). To get 2.5, you'd need `double c = (double)a / b;` or `double c = 5.0 / 2;`
</details>

---

### Question 18
Add proper JavaDoc comments to this method:

```java
public static double calculateArea(double radius) {
    return 3.14159 * radius * radius;
}
```

<details>
<summary>Answer (5 points)</summary>

```java
/**
 * Calculates the area of a circle given its radius
 * @param radius the radius of the circle (must be positive)
 * @return the area of the circle (πr²)
 */
public static double calculateArea(double radius) {
    return 3.14159 * radius * radius;
}
```

**Points breakdown**:
- Description of what method does (2 pts)
- @param tag with description (2 pts)
- @return tag with description (1 pt)
</details>

---

## Part 4: Short Answer (3 questions × 5 points = 15 points)

### Question 19
Explain the difference between compiling and running a Java program. Include the commands used and what each produces.

<details>
<summary>Answer (5 points)</summary>

**Compiling** (`javac FileName.java`):
- Converts human-readable source code (.java) into bytecode (.class)
- Checks for syntax errors
- Produces a .class file if successful

**Running** (`java ClassName`):
- Loads the bytecode (.class file) into the JVM
- Executes the program starting from the main method
- Produces program output

**Key difference**: Compiling is translation (code → bytecode), running is execution (bytecode → results).

**Scoring**:
- Mentions compilation creates bytecode (2 pts)
- Mentions running executes bytecode (1 pt)
- Includes correct commands (1 pt)
- Clear explanation (1 pt)
</details>

---

### Question 20
List 3 Java naming conventions and give an example of each.

<details>
<summary>Answer (5 points)</summary>

1. **Classes**: PascalCase (UpperCamelCase)
   - Example: `StudentRecord`, `BankAccount`

2. **Variables/Methods**: camelCase
   - Example: `studentName`, `calculateTotal()`

3. **Constants**: UPPER_SNAKE_CASE
   - Example: `MAX_SIZE`, `PI_VALUE`

**Scoring**: 
- Convention 1 with example (2 pts)
- Convention 2 with example (2 pts)
- Convention 3 with example (1 pt)
</details>

---

### Question 21
What are three ways to debug a Java program when it's not working correctly?

<details>
<summary>Answer (5 points)</summary>

1. **Print statements**: Add `System.out.println()` to track variable values and program flow

2. **Compiler warnings**: Use `javac -Xlint` to see all warnings and potential issues

3. **IDE debugger**: Set breakpoints and step through code line by line to find logic errors

**Other acceptable answers**:
- Read error messages carefully
- Test with simple inputs
- Check for common errors (semicolons, braces, case)
- Rubber duck debugging (explain code to someone/something)

**Scoring**: 
- Any 3 valid debugging techniques (3 pts)
- Clear explanation of each (2 pts)
</details>

---

## Scoring Summary

| Section | Points | Your Score |
|---------|--------|------------|
| Multiple Choice (Q1-10) | 20 | ____ |
| True/False (Q11-15) | 10 | ____ |
| Code Analysis (Q16-18) | 15 | ____ |
| Short Answer (Q19-21) | 15 | ____ |
| **Total** | **60** | ____ |

---

## Grade Scale

| Score | Percentage | Grade | Status |
|-------|------------|-------|--------|
| 54-60 | 90-100% | A | Excellent! Move to next slice |
| 48-53 | 80-89% | B | Good! Move to next slice |
| 42-47 | 70-79% | C | Review weak areas first |
| 36-41 | 60-69% | D | Re-study concepts before continuing |
| 0-35 | <60% | F | Re-do entire slice |

---

## Next Steps Based on Score

### 🎉 Score 48+ (80%+)
**Congratulations!** You've mastered Slice 1!
- ✅ Mark Slice 1 as COMPLETE
- ➡️ Move to **Slice 2: Input/Output & Formatting**
- 📝 Update your progress tracker

### ⚠️ Score 42-47 (70-79%)
**Almost there!** Review these topics:
- Revisit `01-concepts.md` for weak areas
- Redo practice problems you struggled with
- Retake this assessment tomorrow

### 🔄 Score below 42 (<70%)
**Need more practice!**
- Re-read `01-concepts.md` carefully
- Work through ALL examples again
- Complete ALL practice problems
- Watch Java tutorial videos
- Retake assessment after 2 days of practice

---

## Reflection Questions

1. What concept was easiest for you? _________________
2. What concept needs more practice? _________________
3. How long did this assessment take? _________________
4. Did you need to look anything up? _________________
5. Confidence level (1-10)? _________________

---

**Remember**: The goal isn't perfection, it's **progress**. If you scored lower than expected, that's okay! Use this as a learning tool, not a judgment. 

**Ready to dominate this course!** 💪

