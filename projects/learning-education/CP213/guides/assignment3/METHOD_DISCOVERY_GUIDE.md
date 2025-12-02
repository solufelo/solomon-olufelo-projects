# Where Do These Methods Come From? - Discovery Guide

## 🔍 Finding `getDatum()`

### The Question:
How do we get the data out of a `SingleNode<T>`?

### The Answer:
The `SingleNode` class has a method to retrieve the data it stores. Based on the `SingleLink` code you saw earlier, it uses `getDatum()`.

### How to Discover This:

1. **Look at the SingleNode class definition** - The assignment says `SingleNode` is complete and must be left unchanged. This class should have methods like:
   - `getDatum()` - returns the data (of type `T`) stored in the node
   - `getNext()` - returns the next node
   - `setNext(SingleNode<T> next)` - sets the next node

2. **Check the SingleLink code** - Look at how `SingleLink` uses `SingleNode`:
   ```java
   // From SingleLink's iterator:
   result = this.current.getDatum();  // Gets data from node
   this.current = this.current.getNext();  // Gets next node
   ```

3. **The Pattern**: In Java, when you have an object, you call methods on it:
   - `node.getDatum()` - "Hey node, give me your data"
   - `node.getNext()` - "Hey node, give me the next node"

### So `getDatum()` comes from:
- **The `SingleNode` class** - it's a method defined in that class
- You call it on a `SingleNode<T>` object
- It returns the data of type `T` stored in that node

---

## 🔍 Finding `compareTo()`

### The Question:
How do we compare two objects of type `T`?

### The Answer:
Since `SingleList<T extends Comparable<T>>`, the type `T` must implement the `Comparable<T>` interface, which provides the `compareTo()` method.

### Understanding the Generic Constraint:

```java
public class SingleList<T extends Comparable<T>> extends SingleLink<T>
```

This means:
- `T` is a generic type (could be Integer, String, Food, etc.)
- BUT `T` must extend/implement `Comparable<T>`
- So any object of type `T` has a `compareTo()` method

### What is `Comparable<T>`?

`Comparable` is a Java interface that defines one method:
```java
public interface Comparable<T> {
    int compareTo(T other);
}
```

### How `compareTo()` Works:

```java
int result = object1.compareTo(object2);
```

Returns:
- **`0`** if `object1 == object2` (they are equal)
- **Negative number** if `object1 < object2` (object1 comes before object2)
- **Positive number** if `object1 > object2` (object1 comes after object2)

### Examples:

```java
// For Integers:
Integer a = 5;
Integer b = 3;
a.compareTo(b);  // Returns positive (5 > 3)
b.compareTo(a);  // Returns negative (3 < 5)
a.compareTo(a);  // Returns 0 (5 == 5)

// For Strings:
String s1 = "apple";
String s2 = "banana";
s1.compareTo(s2);  // Returns negative ("apple" < "banana" alphabetically)

// For your Food/Movie class:
Food food1 = new Food(...);
Food food2 = new Food(...);
food1.compareTo(food2);  // Uses your compareTo implementation
```

### So `compareTo()` comes from:
- **The `Comparable<T>` interface** - it's a method defined in that interface
- Since `T extends Comparable<T>`, any object of type `T` has this method
- You call it on the data: `data.compareTo(key)`
- It returns an `int` that tells you the relationship between the objects

---

## 🎯 Putting It Together

### In Your Code:

```java
if (current.getDatum().compareTo(key) == 0) {
    return previous;
}
```

Let's break this down step by step:

1. `current` is a `SingleNode<T>` - a node in your linked list
2. `current.getDatum()` - gets the data (of type `T`) stored in that node
3. `.compareTo(key)` - calls compareTo on that data, comparing it to `key`
4. `== 0` - checks if they are equal (compareTo returns 0 when equal)

### The Flow:

```
current (SingleNode<T>)
  ↓ getDatum()
data (type T, which implements Comparable<T>)
  ↓ compareTo(key)
int (0 if equal, negative/positive if not)
  ↓ == 0
boolean (true if equal, false if not)
```

---

## 📚 How to Discover Methods in General

### 1. **Check the Class Definition**
   - Look at the class file (SingleNode.java)
   - See what methods are defined
   - Read the documentation (JavaDoc comments)

### 2. **Check Interfaces**
   - If a class implements an interface, it has those interface methods
   - `Comparable<T>` interface → `compareTo()` method
   - `Iterable<T>` interface → `iterator()` method

### 3. **Check the Parent Class**
   - Look at what `SingleLink` provides (protected methods, attributes)
   - Check how methods are used in the parent class

### 4. **Use Your IDE**
   - Type the variable name and a dot: `current.`
   - Your IDE will show available methods
   - This is called "autocomplete" or "IntelliSense"

### 5. **Read Documentation**
   - Java API documentation
   - Assignment documentation
   - Comments in the code

---

## 🔑 Key Takeaways

1. **`getDatum()`** - Method from `SingleNode` class
   - Gets the data stored in a node
   - Returns type `T`

2. **`compareTo()`** - Method from `Comparable<T>` interface
   - Available because `T extends Comparable<T>`
   - Compares two objects
   - Returns `int`: 0 if equal, negative/positive if not

3. **How to use them together**:
   ```java
   current.getDatum().compareTo(key) == 0
   ```
   This checks if the data in the current node equals the key.

---

## 💡 Practice Questions

1. **What does `node.getDatum()` return?**
   - Answer: The data of type `T` stored in that node

2. **Why can we call `compareTo()` on the data?**
   - Answer: Because `T extends Comparable<T>`, so objects of type `T` implement the `Comparable` interface

3. **What does `compareTo()` return when two objects are equal?**
   - Answer: `0`

4. **How would you check if node's data is greater than key?**
   - Answer: `node.getDatum().compareTo(key) > 0`

5. **How would you check if node's data is less than key?**
   - Answer: `node.getDatum().compareTo(key) < 0`

