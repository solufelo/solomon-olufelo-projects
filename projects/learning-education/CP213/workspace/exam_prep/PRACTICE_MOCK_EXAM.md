# CP213 Practice Final Exam (Mock)

**Time Limit:** 2 Hours
**Total Marks:** 50
**Format:** Closed Book, Pen & Paper

---

## Section 1: Multiple Choice [20 Marks]
*(Select the best answer. 1 Mark each)*

1.  **Which of the following is TRUE about Abstract Classes?**
    a. They can be instantiated directly using `new`.
    b. They must contain at least one abstract method. TRUE
    c. They can contain both abstract and concrete methods.
    d. They cannot have constructors.

2.  **What happens if you try to catch `Exception` BEFORE catching `LabCapacityException`?**
    a. The code compiles and works fine.
    b. The code compiles but throws a RuntimeException.
    c. The compiler throws an error: "Unreachable code". TRUE
    d. The `LabCapacityException` block is executed first anyway.

3.  **Which keyword is used to access a hidden variable of a superclass?**
    a. `this`
    b. `super` TRUE
    c. `extends`
    d. `static`

4.  **What is the difference between `HashMap` and `ArrayList` lookup time?**
    a. HashMap is O(n), ArrayList is O(1).
    b. HashMap is O(1), ArrayList is O(n) (for searching). TRUE
    c. Both are O(n).
    d. Both are O(1).

5.  **If `Student` extends `UniversityMember`, which statement is VALID?**
    a. `Student s = new UniversityMember();`
    b. `UniversityMember m = new Student();` TRUE
    c. `LabAccess l = new UniversityMember();`
    d. `Student s = (Student) new UniversityMember();`

6.  **What does `transient` keyword do in Serialization?**
    a. It marks a variable as constant. 
    b. It prevents the variable from being saved to the file. TRUE
    c. It makes the variable thread-safe.
    d. It allows the variable to be accessed by inner classes. 

7.  **Which of the following is a Marker Interface?**
    a. `Comparable` 
    b. `Runnable`
    c. `Serializable` TRUE
    d. `ActionListener`

8.  **In an Inner Class, how do you access the Outer Class's `this`?**
    a. `super.this`
    b. `OuterClassName.this`
    c. `this.parent`
    d. You cannot access it. TRUE

*(... Assume 12 more questions covering Recursion, File I/O, Swing, Generics, etc. ...)*

---

## Section 2: Short Answer (Definitions, Errors, Outputs) [15 Marks]

**Q1. Code Error Finding [2 Marks]**
Identify the 2 errors in the following code snippet and explain why they are wrong.
```java
abstract class Shape {
    abstract void draw() {}  // Error 1?
}

class Circle extends Shape {
    // Error 2?
}
//abstarct styntax error no need for function brackets should be juist draw(); 
//circle error is that it never overrides draw and implements it correctly
```

**Q2. Output Tracing [3 Marks]**
What is the exact output of the following code?
```java
try {
    int[] arr = {1, 2};
    System.out.print(arr[2]);
} catch (NullPointerException e) {
    System.out.print("A");
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.print("B");
} finally {
    System.out.print("C");
}
```
the output is going to be arrayindexoutofbounds exception and  finally block being c so output : BC

**Q3. Definition [2 Marks]**
Explain the difference between **Static Binding** and **Dynamic Binding**. Give one example of each.

**Q4. Polymorphism Output [3 Marks]**
```java
class Parent { void say() { System.out.print("P"); } }
class Child extends Parent { void say() { System.out.print("C"); } }

Parent p = new Child();
p.say();
((Parent)p).say();
```

**Q5. Access Modifiers [2 Marks]**
What is the difference between `protected` and `package-private` (default) access?

**Q6. Recursion [3 Marks]**
What does the following recursive function return for `mystery(3)`?
```java
int mystery(int n) {
    if (n == 0) return 1;
    return n * mystery(n-1);
}
```

---

## Section 3: Programming Problems [15 Marks]

**Q1. The Interface Implementation (5 Marks)**
Write a class `VideoGame` that implements the `Rentable` interface.
*   `Rentable` has: `boolean isAvailable()` and `void rent()`.
*   `VideoGame` should have a `title` and an `isRented` status.
*   Implement the methods correctly.

**Q2. The Exception Handling (5 Marks)**
Write a method `readFile(String filename)` that:
1.  Uses a `Scanner` to read a file.
2.  Catches `FileNotFoundException`.
3.  Catches `InputMismatchException`.
4.  Closes the scanner in a `finally` block.

**Q3. The Algorithm (5 Marks)**
Write a recursive method `countFiles(FileNode folder)` that returns the total number of files in a folder and all its sub-folders.
*   `FileNode` has `boolean isFile()` and `ArrayList<FileNode> getChildren()`.
