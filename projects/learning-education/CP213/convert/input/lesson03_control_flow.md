# Lesson 03: Control Flow in Java

## **1. Introduction**

- Code executes **top to bottom**, unless modified by **control flow statements**.
- Control flow allows **branching** (decisions) and **looping** (repetition).

### **🔹 Types of Control Flow in Java**

- **Decision-making:** `if-then`, `if-then-else`, `switch`
- **Looping:** `for`, `while`, `do-while`
- **Branching:** `break`, `continue`, `return`

## **2. Boolean Expressions & Operators**

### **🔹 Comparison Operators**

| Operator | Meaning |
|----------|---------|
| `==`     | equal to |
| `!=`     | not equal to |
| `>`      | greater than |
| `>=`     | greater than or equal to |
| `<`      | less than |
| `<=`     | less than or equal to |

➡️ Remember: **`==` for equality**, **`=` for assignment**

**Example:**

```java
int x = 5, y = 8;
boolean z = x < y;
System.out.println(x < y); // true
```

### **2.2 Comparing Strings**

- `==` → compares memory addresses (not values).
- Use methods:
    - `str1.equals(str2)`
    - `str1.equalsIgnoreCase(str2)`

### **2.3 Lexicographic Ordering**

- Based on **ASCII** values:
    - Uppercase letters come before lowercase.
- Use `compareTo` methods:
    - `s1.compareTo(s2)` → `<0`, `=0`, or `>0`
    - `s1.compareToIgnoreCase(s2)` → ignores case differences.

### **2.4 Building Boolean Expressions**

- **AND (`&&`)** → true only if both are true.
- **OR (`||`)** → true if at least one is true.
- **NOT (`!`)** → negates a condition.

❌ Invalid:

```java
min < result < max
```

✅ Correct:

```java
(min < result) && (result < max)
```

### **2.5 Evaluating Boolean Expressions**

- Produce `true` or `false`.
- Can assign to variables:

```java
int x = 3, y = 5;
boolean z = x > y; // false
```

⚠️ **Common mistake:**

```java
boolean b = false;
if (b = true) {   // assignment, not comparison
    System.out.println("Hello"); // executes
}
```

### **2.6 Short-Circuit vs Complete Evaluation**

- **Short-circuit (lazy):**
    - `&&`: stops if first is `false`.
    - `||`: stops if first is `true`.

✅ Prevents runtime errors:

```java
int kids = 0, toys = 3;
if ((toys / 3) >= 2 && (toys / kids) >= 2) {
    // safe: second part never runs
}
```

- **Complete evaluation:**
    - Use `&` and `|` instead of `&&` and `||`.
    - Forces evaluation of both sides.

## **3. Branching with If-Else Statements**

### **3.0 If-Else Basics**

- **Definition**: Lets a program choose between two paths depending on a Boolean condition.
- **Syntax**:

```java
if (Boolean_Expression)
    Yes_Statement;
else
    No_Statement;
```

- **Example**:

```java
int mark = 0;
if (mark > 85)
    System.out.println("Your grade is A");
else
    System.out.println("Your grade is not A");
```

👉 **Java vs Python**:

- Java requires **parentheses** around conditions and **braces `{ }`** for multiple statements.
- Python uses `:` with indentation (`if ...:`, `elif ...:`, `else:`).

### **3.1 Compound Statements**

- If a branch has **multiple statements**, group them in `{ }`.

```java
if (myScore > yourScore) {
    System.out.println("I win!");
    wager += 100;
} else {
    System.out.println("I wish these were golf scores.");
    wager = 0;
}
```

### **3.2 Omitting Else**

- `else` is optional → creates a simple `if` statement.

```java
if (weight > ideal)
    calorieIntake -= 500;
```

- With multiple actions, braces are required:

```java
if (weight > ideal) {
    calorieIntake -= 500;
    System.out.println("Increase exercise rate!");
    exerciseRate *= 1.3;
}
```

### **3.3 Nested If-Else**

- If statements can be placed **inside each other**.

```java
if (a > b) {
    if (c > d) {
        if (g < h) {
            // code
        }
    }
} else if (m == n) {
    if (z > y) {
        // code
    }
}
```

👉 Use indentation for clarity.

### **3.4 Multiway If-Else**

- Chains multiple conditions.

```java
if (number < 100 && number >= 1) {
    System.out.println("Two-digit number");
} else if (number < 1000 && number >= 100) {
    System.out.println("Three-digit number");
} else if (number < 10000 && number >= 1000) {
    System.out.println("Four-digit number");
} else {
    System.out.println("Number not in range 1–99999");
}
```

### **3.5 Ternary Operator (`?:`)**

- Shorthand for simple if-else assignments.

```java
int max = (n1 > n2) ? n1 : n2;
```

- Reads as:
    - If condition is **true**, take first value.
    - If **false**, take second value.

✅ Summary:

- **if-else** controls branching.
- **Compound** → multiple statements in `{ }`.
- **Omitting else** → runs only when condition is true.
- **Nested if** → allows deeper decisions.
- **Multiway if-else** → handles multiple conditions.
- **Ternary operator** → compact shorthand.

## **4. The Switch Statement**

### **📌 Purpose**

- Implements **multiway branching** in Java.

### **📝 Syntax**

```java
switch (Controlling_Expression) {
    case Case_Label_1:
        // code
        break;
    case Case_Label_2:
        // code
        break;
    default:
        // code if no case matches
        break;
}
```

### **⚖️ Key Rules**

- Controlling expression must be: `char`, `int`, `short`, `byte`, or (Java 7+) `String`.
- Each **case label** must be the same type as the controlling expression.
- Labels can be in any order but must be **unique**.
- `break;` ends execution of a case.
- If `break` is omitted → execution **falls through** to the next case.

### **4.1 Default Section**

- Handles all values **not explicitly matched** by any case.
- **Optional**, but good practice to include.
- Usually placed **last**.

### **✅ Example**

```java
int numberOfIceCreamFlavors = 15;

switch (numberOfIceCreamFlavors) {
    case 15:
        System.out.println("Nice selection.");
        break;
    case 1:
        System.out.println("I bet it's vanilla.");
        break;
    default:
        System.out.println("Unknown number of flavors.");
        break;
}
```

### **4.1.1 Non-Graded Activity**

```java
import java.util.Scanner;

public class SwitchClass {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Type a number that represents your lucky day");
        int luckyDay = keyboard.nextInt();

        switch (luckyDay) {
            case 1:
                System.out.println("Your lucky day is Monday");
                break;
            case 2:
                System.out.println("Your lucky day is Tuesday");
                break;
            case 3:
            case 4:
            case 5:
                System.out.println("Your lucky day is Wednesday, Thursday or Friday");
                System.out.println("is acceptable.");
                break;
            default:
                System.out.println("Your lucky day is either Saturday or Sunday");
                break;
        }
    }
}
```

## **5. Loops in Java**

Loops allow you to **repeat a block of code** multiple times. Each repetition is called an **iteration**, and the code inside the loop is called the **loop body**.

Java has **three types of loops**:

1. `while` loop
2. `do-while` loop
3. `for` loop

### **5.1 while Statement**

- Executes the loop **only if** the Boolean expression is true.
- **Condition is checked before** each iteration.
- Loop body can be **a single statement** or **multiple statements enclosed in braces `{}`**.

**Syntax:**

```java
while (Boolean_Expression)
    Statement;
```

Or with a compound body:

```java
while (Boolean_Expression) {
    Statement_1;
    Statement_2;
    ...
    Statement_Last;
}
```

### **5.2 do-while Statement**

- Executes the loop body **at least once**.
- Boolean expression is **checked after** the loop body executes.
- Acts like a `while` loop after the first iteration.
- Loop body can also be **single or compound statements**.
- **Important:** there is a **semicolon after the Boolean expression**.

**Syntax:**

```java
do
    Statement;
while (Boolean_Expression);
```

Or with a compound body:

```java
do {
    Statement_1;
    Statement_2;
    ...
    Statement_Last;
} while (Boolean_Expression);
```

### **5.3 Example: while vs do-while**

```java
package lesson03;

public class WhileExample {

    public static void main(String[] args) {
        int countDown;

        System.out.println("First while loop:");
        countDown = 5;
        while (countDown > 0) {
            System.out.println("Hello");
            countDown -= 1;
        }

        System.out.println("Second while loop:");
        countDown = 0;
        while (countDown > 0) { // Won't run
            System.out.println("Hello");
            countDown -= 1;
        }

        System.out.println("First do-while loop:");
        countDown = 5;
        do {
            System.out.println("Hello");
            countDown -= 1;
        } while (countDown > 0);

        System.out.println("Second do-while loop:");
        countDown = 0;
        do { // Executes at least once
            System.out.println("Hello");
            countDown -= 1;
        } while (countDown > 0);
    }
}
```

**Key takeaway:**

- `while` may not execute if the condition is false at the start.
- `do-while` **always executes at least once**.

## **5.4 The `for` Statement**

The `for` loop is commonly used to iterate over a range of values with a control variable.

**Syntax:**

```java
for (Initializing; Boolean_Expression; Update) {
    Statement_1;
    Statement_2;
    ...
    Statement_Last;
}
```

- **Initializing:** Set up control variable(s). Can declare multiple variables separated by commas.
- **Boolean_Expression:** Condition checked before each iteration.
- **Update:** Changes control variable(s) after each iteration. Can contain multiple updates separated by commas.
- **Body:** Single or compound statements.

**Examples:**

```java
// Single statement
for (int i = 0; i < 3; i++)
    System.out.println("i is " + i);

// Multiple statements
int j = 0;
for (int i = 0; i < 3; i++) {
    j += 1;
    System.out.println("hello " + j);
    System.out.println("j is " + j);
}
```

**Multiple Initialization Example:**

```java
int j = 0;
for (int i = 0; (i + j) < 6; i++) {
    j++;
    System.out.println("i and j: " + i + " " + j);
}
```

**Multiple Updates Example:**

```java
for (int i = 0, j = 0; (i + j) < 6; i++, j++, System.out.println("i and j: " + i + " " + j));
```

### **5.4.1 Infinite Loops**

- Loops must modify the condition to eventually terminate.
- Equality (`==`) and inequality (`!=`) checks with `double` or `float` may cause **infinite loops** due to precision errors.
- Example of risky loop:

```java
double x = 1.0 / 3;
for (int i = 0, j = 0; x != 0.33333; i++) {
    j++;
    System.out.println("i and j: " + i + " " + j);
}
```

- A `for(;;)` statement is a valid infinite loop.

### **5.4.2 Nested Loops**

- Loops can be **nested** like other control structures.
- Inner loop executes **completely** for every iteration of the outer loop.

**Example:**

```java
for (int rowNum = 1; rowNum <= 3; rowNum++) {
    for (int columnNum = 1; columnNum <= 2; columnNum++) {
        System.out.print("row " + rowNum + " column " + columnNum + " ");
    }
    System.out.println();
}
```

## **5.5 For-each Loop (Enhanced for loop)**

- Introduced in **Java 5** for **arrays** and **collections**.
- Iterates through elements **without using indices**.

**Syntax:**

```java
for (type var : arrayOrCollection) {
    body-of-loop;
}
```

**Array Example:**

```java
double sum = 0;
double[] price = {1.5, 2.5, 3.5, 4, 0.5};

// Basic for loop
for (int i = 0; i < price.length; i++)
    sum += price[i];
System.out.println(sum);

// For-each loop
sum = 0;
for (double p : price)
    sum += p;
System.out.println(sum);
```

**Collection Example:**

```java
Collection<String> myCollectionItem = new ArrayList<>();
myCollectionItem.add("1 - H - Hydrogen");
myCollectionItem.add("2 - He - Helium");
myCollectionItem.add("3 - Li - Lithium");

System.out.println("Using iterator:");
Iterator<String> iter = myCollectionItem.iterator();
while (iter.hasNext()) {
    System.out.println(iter.next());
}

System.out.println("Using for-each:");
for (String item : myCollectionItem)
    System.out.println(item);
```

**Rules for For-each Loop:**

- Loop variable **cannot be assigned** inside the loop.
- Can **only iterate one collection** at a time.
- Iterates **forward by single steps**.

## **5.6 The `break` and `continue` Statements**

### **`break`**

- Syntax: `break;`
- Immediately **terminates the nearest enclosing loop or switch statement**.
- Control moves to the statement immediately after the loop or switch.
- Does **not** terminate the program.

**Example – break in inner loop:**

```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println(i + " , " + j);
        break;  // exits inner loop only
    }
}
```

**Output:**

```
0 , 0
1 , 0
2 , 0
```

### **`continue`**

- Syntax: `continue;`
- Ends the **current iteration** of the nearest enclosing loop.
- Control moves to the **next iteration** of the loop.
- In a `for` loop, it transfers control to the **update expression**.

**Example – continue in nested loop:**

```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i >= 1)
            continue;
        System.out.println(i + " , " + j);
    }
}
```

**Output:**

```
0 , 0
0 , 1
0 , 2
```

## **5.7 Labeled Break Statement**

- Used to **break out of an outer loop** from an inner loop.
- Syntax:

```java
labelName: for(...) {
    for(...) {
        break labelName;  // exits the labeled loop
    }
}
```

**Example:**

```java
endBothLoops:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println(i + " , " + j);
        break endBothLoops;
    }
}
```

**Output:**

```
0 , 0
```

- Similarly, `continue` can be used with labels in Java 8+.

### **5.7.1 Program Termination**

- `System.exit(0);` immediately terminates the **entire program**.
- The argument `0` indicates a normal termination.

## **5.8 Common Loop Errors**

1. **Infinite loops:** Condition never becomes false.
2. **Off-by-one errors:** Loop executes **one extra or one fewer iteration** than intended.
3. **Floating-point comparisons:** Avoid `==` or `!=` in Boolean expressions for `float`/`double`.

## **5.9 Java Iterator Interface**

The **Iterator** interface in Java provides a standard way to traverse elements in any collection (like `ArrayList`, `HashSet`, etc.).

### **Using a `for` loop with ArrayList:**

```java
ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.add("Cherry");

for (int i = 0; i < list.size(); i++) {
    String s = list.get(i);
    System.out.println(s);
}
```

### **Using an `Iterator`:**

```java
Iterator<String> itr = list.iterator();
while (itr.hasNext()) {
    String s = itr.next();
    System.out.println(s);
}
```

**Key Points:**

- `iterator()` returns an `Iterator` object for the collection.
- `hasNext()` checks if there are more elements to traverse.
- `next()` returns the next element in the collection.
- Using `Iterator` is preferred when you want to remove elements safely during iteration.

## **5.10 Assertion Checks**

An **assertion** is a statement that tests a condition which should always be true if the program is running correctly.

### **Syntax:**

```java
assert Boolean_Expression;   // Example: assert database_version == 1.2;
```

- If the expression evaluates to **true**, the program continues normally.
- If **false**, the program throws an `AssertionError` and stops execution.
- Assertions are mainly used for **debugging and testing**, not for production logic.

### **Enabling Assertions**

By default, assertions are **disabled**. To enable them:

**Command line:**

```bash
java -enableassertions ProgramName
```

Or using **Eclipse configuration**, enable assertions in the runtime settings.

### **Example Use Case:**

```java
double database_version = 1.0;
assert database_version == 1.2;  // Throws AssertionError if false
```

- Helps ensure assumptions in your code are valid.
- Useful in team environments to catch version mismatches or logic errors early.

**Summary Table**

| Feature | Description | Example |
|---------|-------------|---------|
| Iterator | Traverses elements in collections | `itr.next()` |
| hasNext() | Checks if more elements exist | `itr.hasNext()` |
| Assertions | Verifies conditions during runtime | `assert x > 0;` |
| Enabling assertions | Must be enabled explicitly | `java -enableassertions ProgramName` |

## **6 Generating Random Numbers**

Java provides the **`Random`** class in the `java.util` package to generate pseudo-random numbers. These are **not truly random**, but are sufficiently unpredictable for most applications.

### **Importing the Random Class**

```java
import java.util.Random;
```

### **Creating a Random Object**

```java
Random rnd = new Random();
```

### **Generating Random Numbers**

| Method | Description | Example |
|--------|-------------|---------|
| `nextInt(n)` | Random integer from `0` to `n-1` | `int i = rnd.nextInt(10); // 0-9` |
| `nextDouble()` | Random double between `0.0` (inclusive) and `1.0` (exclusive) | `double d = rnd.nextDouble();` |
| `nextBoolean()` | Random boolean value (`true` or `false`) | `boolean b = rnd.nextBoolean();` |
| `nextLong()` | Random long value | `long l = rnd.nextLong();` |
| `nextFloat()` | Random float between `0.0` and `1.0` | `float f = rnd.nextFloat();` |

### **Example: Simulating a Coin Flip**

```java
package lesson03;

import java.util.Random;

public class CoinFlipDemo {

    public static void main(String[] args) {
        Random randomGenerator = new Random();
        int counter = 1;

        while (counter <= 5) {
            System.out.print("Flip number " + counter + ": ");
            int coinFlip = randomGenerator.nextInt(2); // 0 or 1

            if (coinFlip == 1)
                System.out.println("Heads");
            else
                System.out.println("Tails");

            counter++;
        }
    }
}
```

**Explanation:**

- `nextInt(2)` generates either `0` or `1`.
- The `if` statement checks the value to print "Heads" or "Tails".
- The loop runs 5 times, simulating 5 coin flips.

### **Tips:**

- You can experiment with other `Random` methods like `nextDouble()`, `nextLong()`, `nextBoolean()`, or even generate numbers in a custom range.
- Random numbers are **pseudo-random**, meaning if you use the same seed (optional in `new Random(seed)`), the sequence of numbers is repeatable.

## **Key Terms Glossary**

| Keyword | Description & Notes |
|---------|-------------------|
| **assert** | Checks a Boolean condition; throws `AssertionError` if false; mainly used for debugging. |
| **break** | Exits the nearest enclosing loop or `switch`; can be labeled to exit outer loops in nested loops. |
| **continue** | Skips the rest of the current loop iteration; in a `for` loop, moves to the update expression. |
| **do-while** | Executes the loop body **at least once**, then checks the condition; ends if false. |
| **for-each** | Enhanced loop to iterate arrays or collections; cannot modify loop variable; one element at a time. |
| **if-else** | Executes one branch if condition is true, another if false; can be nested or multiway (`else if`). |
| **iterator** | Interface to traverse collections; `hasNext()` checks for next element, `next()` retrieves it. |
| **java short-circuits** | Logical operators `&&` and `\|\|` evaluate left-to-right and stop early if result is determined. |
| **labeled break** | Break with a label to exit a specific outer loop in nested loops. |
| **switch** | Multiway branching; executes the case that matches the controlling expression; use `break` to stop. |
| **ternary operator** | Compact `if-else` expression: `(condition) ? valueIfTrue : valueIfFalse`. |
| **while** | Executes the loop body **only if** the condition is true; condition checked before each iteration. |

### **Notes & Tips:**

- **Break & continue** are best used sparingly; overuse can make loops hard to read.
- **For-each** simplifies loops over arrays/collections, but can't modify the elements directly.
- **Assertions** are mostly for development/testing, not production.
- **Ternary operator** is ideal for short, conditional assignments.
- **Infinite loops** often happen with `while(true)` or incorrect Boolean conditions; watch `==` with floating-point numbers.



