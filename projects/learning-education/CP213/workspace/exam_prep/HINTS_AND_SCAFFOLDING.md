# Hints and Scaffolding: The "Why" and "How"

This guide bridges the gap between theory and implementation. Use this when you understand the *goal* but aren't sure about the *syntax* or *design pattern*.

---

## Phase 1: Class Hierarchy (Inheritance & Abstraction)

### **The Concept: Abstract Classes vs. Interfaces**
*   **What:** An `abstract class` is a blueprint that can contain both implemented methods and abstract (empty) methods.
*   **Why:** We use `UniversityMember` as an abstract class because it has shared state (`name`, `id`) that every subclass needs. We don't want anyone to say `new UniversityMember()` because that's too vague.
*   **Where:** `src/exam_prep/UniversityMember.java`

### **Implementation Guide**
**1. Validation in Constructor:**
Don't just set variables; protect them!
```java
public UniversityMember(String id, String name) {
    // Validate BEFORE assignment
    if (id == null || id.length() != 9) {
        throw new IllegalArgumentException("ID must be 9 digits");
    }
    this.id = id;
    this.name = name;
}
```

**2. The `equals` Method:**
Always override `equals` so Java knows how to compare two objects of your custom type.
```java
@Override
public boolean equals(Object obj) {
    // 1. Identity check (are they the same memory address?)
    if (this == obj) return true;
    
    // 2. Null and Type check
    if (obj == null || !(obj instanceof UniversityMember)) return false;
    
    // 3. Cast and Compare specific fields
    UniversityMember other = (UniversityMember) obj;
    return this.id.equals(other.id);
}
```

---

## Phase 2: Interfaces, Polymorphism & Covariant Returns

### **The Concept: Covariant Return Types**
*   **What:** When overriding a method, you can return a *subclass* of the original return type.
*   **Why:** If `Student.getDetails()` returns a `Student`, then `TA.getDetails()` should be allowed to return a `TA` (since a TA *is* a Student). It's more specific and useful.

### **Implementation Guide**
**The Parent:**
```java
public class Student {
    public Student getSelf() { return this; }
}
```
**The Child (Covariant Override):**
```java
public class TeachingAssistant extends Student {
    @Override
    // Valid! TeachingAssistant IS-A Student, so this is allowed.
    public TeachingAssistant getSelf() { return this; }
}
```

---

## Phase 3: Exceptions & Collections

### **The Concept: Custom Exceptions**
*   **What:** A specific error type for your domain logic.
*   **Why:** Throwing a generic `Exception` is bad practice because it's hard to catch specifically. `LabCapacityException` tells the caller *exactly* what went wrong.
*   **How:** Extend `Exception` (for checked exceptions - must be caught) or `RuntimeException` (unchecked).

### **Implementation Guide**
**The Exception:**
```java
public class LabCapacityException extends Exception {
    public LabCapacityException(String message) {
        super(message); // Pass the message up to the parent Exception class
    }
}
```

**The List (Polymorphism in Action):**
Use the **Interface** as the list type. This allows you to store `Student`, `Professor`, and `TA` in the same list.
```java
// Good: Stores anything that has LabAccess
private ArrayList<LabAccess> activeUsers = new ArrayList<>();

// Bad: Can only store Students
private ArrayList<Student> activeUsers = new ArrayList<>(); 
```

---

## Phase 4: Generics & Inner Classes

### **The Concept: Inner Classes**
*   **What:** A class defined *inside* another class.
*   **Why:** Perfect for helper objects like `Node` that shouldn't exist outside the `WaitQueue`. It keeps your code organized and encapsulated.
*   **How:** `private class Node<T> { ... }` inside the `WaitQueue` class.

### **The Concept: Cloning**
*   **What:** Creating an exact copy of an object.
*   **Shallow Copy:** Copies references (both objects point to the same data).
*   **Deep Copy:** Copies the *actual data* (new object, new data).
*   **How:** Implement `Cloneable` interface and override `clone()`.

### **Implementation Guide**
**The Inner Node Class:**
```java
public class WaitQueue<T> {
    
    // Inner class - only WaitQueue can see this!
    private class Node {
        T data;
        Node next;
        
        Node(T data) { this.data = data; }
    }

    private Node head;
    private Node tail;
    // ... methods use Node here ...
}
```

**The Clone Method:**
```java
@Override
public Object clone() throws CloneNotSupportedException {
    // 1. Call super.clone() (Shallow copy)
    UniversityMember copy = (UniversityMember) super.clone();
    
    // 2. Fix Mutable Fields (Deep Copy steps)
    // If 'name' was a Mutable StringBuilder, we'd need:
    // copy.name = new StringBuilder(this.name);
    
    return copy;
}
```

---

## Phase 5: The GUI & Anonymous Classes

### **The Concept: Anonymous Inner Classes**
*   **What:** A class with no name, defined right where you use it.
*   **Why:** Often you need a class (like an `ActionListener`) only ONCE. Creating a whole new file `MyButtonListener.java` is overkill.
*   **Syntax:** `new ParentClassOrInterface() { ... implementation ... };`

### **Implementation Guide**
**The Event Listener:**
```java
JButton btn = new JButton("Enter Lab");

// Defining the class AND creating an instance in one step!
btn.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Button clicked!");
    }
});
```

---

## Phase 6: HashMaps (The "Backend")

### **The Concept: Static Methods**
*   **What:** Methods that belong to the *class*, not an *instance*.
*   **Why:** Use `static` for utility functions or global rules that don't depend on a specific object's state (e.g., "Is 5.0 a passing grade?" is a global rule).

### **Implementation Guide**
```java
public class AcademicRegistrar {
    
    // Static because the rules don't change based on WHICH registrar we ask
    public static boolean canGraduate(Student s) {
        if (s.getGpa() < 5.0) return false;
        
        // Check other systems...
        return true;
    }
}
```

---

## Phase 8: Persistence & Serialization

### **The Concept: Serialization**
*   **What:** Converting a Java Object into a stream of bytes (to save to a file).
*   **Why:** Writing `name,id,gpa` to a text file is tedious. Serialization lets you save the *entire* `ArrayList` or `HashMap` in one line of code.
*   **The Badge:** You MUST implement `Serializable` (it has no methods, it's just a stamp of approval).

### **Implementation Guide**
**Saving Objects:**
```java
// 1. Make sure UniversityMember implements Serializable!
public abstract class UniversityMember implements Serializable { ... }

// 2. Write to file
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("data.ser"))) {
    oos.writeObject(allMembersMap); // Saves the WHOLE map at once!
}
```

**Loading Objects:**
```java
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("data.ser"))) {
    HashMap<String, UniversityMember> data = (HashMap) ois.readObject();
}
```

---

## Phase 9: Recursion

### **The Concept: Solving by Self-Reference**
*   **What:** A function calling itself with a smaller version of the problem.
*   **Why:** Essential for navigating trees (like file systems or HTML DOMs) where you don't know how deep the structure goes.

### **Implementation Guide**
**File Search:**
```java
public String searchFile(FileNode currentFolder, String targetName) {
    // 1. Base Case: Did we find it here?
    if (currentFolder.getName().equals(targetName)) {
        return currentFolder.getPath();
    }

    // 2. Recursive Step: Check all children
    for (FileNode child : currentFolder.getChildren()) {
        String result = searchFile(child, targetName);
        if (result != null) return result; // Found it deep down!
    }

    // 3. Not found in this branch
    return null; 
}
```
