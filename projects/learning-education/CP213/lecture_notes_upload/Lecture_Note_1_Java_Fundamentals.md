# Lecture Note: Java Programming Fundamentals & OOP
**Course:** CP213 - Object Oriented Programming
**Topic:** Core Java Concepts, Variables, Control Flow, and Objects

---

## 1. Variables and Data Types

### 1.1 Variable Types
Java differentiates between several types of variables:
*   **Instance Variables (Fields):** Unique to each object instance. Declared inside a class but outside methods.
    *   Example: `private String studentName;`
*   **Static Variables (Class Variables):** Shared by all instances of a class.
    *   Example: `static String universityName;`
*   **Local Variables:** Temporary variables inside methods. Must be initialized before use.
    *   Example: `double average = 0.0;`
*   **Parameters:** Variables passed into methods.

### 1.2 Primitive Types
*   **Integers:** `byte` (8-bit), `short` (16-bit), `int` (32-bit), `long` (64-bit)
*   **Floating Point:** `float` (32-bit), `double` (64-bit)
*   **Other:** `char` (16-bit Unicode), `boolean` (true/false)

**Note on Type Casting:**
*   Implicit (Widening): `int` -> `double` (Automatic)
*   Explicit (Narrowing): `double` -> `int` (Requires cast: `(int) 3.14`)

---

## 2. Control Flow

### 2.1 Conditional Statements
*   **If-Else:** Standard branching.
    ```java
    if (score > 90) {
        System.out.println("A");
    } else {
        System.out.println("B");
    }
    ```
*   **Switch Statement:** Multi-way branching. Works with `int`, `char`, `String`, `enum`.
    ```java
    switch (day) {
        case 1: System.out.println("Monday"); break;
        default: System.out.println("Weekend"); break;
    }
    ```

### 2.2 Loops
*   **While Loop:** Pre-check condition. May never run.
*   **Do-While Loop:** Post-check condition. Runs at least once.
*   **For Loop:** Standard iteration.
    ```java
    for (int i = 0; i < 10; i++) { ... }
    ```
*   **Enhanced For-Each Loop:** For collections and arrays.
    ```java
    for (String name : namesList) { ... }
    ```

---

## 3. Object-Oriented Concepts

### 3.1 Classes and Objects
*   **Class:** A blueprint defining attributes (fields) and behaviors (methods).
*   **Object:** An instance of a class. Created using the `new` keyword.

### 3.2 Constructors
*   Special methods used to initialize objects.
*   Must have the same name as the class.
*   No return type (not even `void`).
*   Can be overloaded (multiple constructors with different parameters).

```java
public class Student {
    private String name;
    
    // Constructor
    public Student(String n) {
        this.name = n;
    }
}
```

### 3.3 Access Modifiers
*   **public:** Accessible from anywhere.
*   **private:** Accessible only within the class.
*   **protected:** Accessible within package and subclasses.
*   **default (no modifier):** Accessible within package.

### 3.4 Static vs Instance
*   **Static Methods:** Belong to the class, not an object. Called using ClassName.method().
*   **Instance Methods:** Belong to an object. Called using object.method().

---

## 4. Useful Java Classes

### 4.1 Scanner (Input)
Used for reading user input.
```java
Scanner input = new Scanner(System.in);
int number = input.nextInt();
input.nextLine(); // Clear buffer
String text = input.nextLine();
```

### 4.2 Random (Utility)
Generating pseudo-random numbers.
```java
Random rnd = new Random();
int randomInt = rnd.nextInt(100); // 0 to 99
```

---
*Notes prepared for CP213 Review.*

