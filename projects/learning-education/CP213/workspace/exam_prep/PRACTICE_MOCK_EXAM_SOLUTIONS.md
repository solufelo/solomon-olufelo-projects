# CP213 Practice Final Exam (Mock) - SOLUTIONS

## Section 1: Multiple Choice

1.  **C** - Abstract classes can have both. They don't *need* abstract methods, but they *can* have them.
2.  **C** - Unreachable code. `Exception` catches everything, so the specific `LabCapacityException` below it would never be reached.
3.  **B** - `super.variableName` accesses the parent's version.
4.  **B** - HashMap is O(1) (instant) by key. ArrayList is O(n) (linear) if you have to search for an item.
5.  **B** - Polymorphism! A Parent reference can hold a Child object.
6.  **B** - `transient` tells Java "skip this variable" during serialization.
7.  **C** - `Serializable` has no methods, making it a Marker Interface.
8.  **B** - `OuterClass.this` is the syntax.

## Section 2: Short Answer

**Q1. Errors**
1.  Abstract methods cannot have a body `{}`. It should end with a semicolon `;`.
2.  `Circle` must either implement `draw()` OR be declared `abstract` itself.

**Q2. Output**
`BC` - Index 2 is out of bounds (0, 1 exist), so `ArrayIndexOutOfBoundsException` is caught (prints B). `Finally` always runs (prints C).

**Q3. Binding**
*   **Static:** Resolved at compile time (e.g., Overloading).
*   **Dynamic:** Resolved at runtime based on object type (e.g., Overriding).

**Q4. Output**
`CC` - Even with casting `(Parent)p`, the object is a `Child`, so the overridden method runs.

**Q5. Access Modifiers**
*   **Protected:** Accessible in same package + subclasses in DIFFERENT packages.
*   **Default:** Accessible ONLY in same package.

**Q6. Recursion**
`6` (It calculates 3 factorial: 3 * 2 * 1 * 1).

## Section 3: Coding

**Q1. VideoGame**
```java
public class VideoGame implements Rentable {
    private String title;
    private boolean isRented = false;

    public VideoGame(String title) { this.title = title; }

    public boolean isAvailable() { return !isRented; }
    public void rent() { isRented = true; }
}
```

**Q2. File Reading**
```java
public void readFile(String filename) {
    Scanner s = null;
    try {
        s = new Scanner(new File(filename));
        while(s.hasNext()) {
            System.out.println(s.next());
        }
    } catch (FileNotFoundException e) {
        System.out.println("File not found");
    } catch (InputMismatchException e) {
        System.out.println("Bad data");
    } finally {
        if (s != null) s.close();
    }
}
```

**Q3. Recursion**
```java
public int countFiles(FileNode folder) {
    if (folder.isFile()) return 1; // Base Case
    
    int total = 0;
    for (FileNode child : folder.getChildren()) {
        total += countFiles(child); // Recursive Step
    }
    return total;
}
```
