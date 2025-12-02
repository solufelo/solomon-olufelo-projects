# Loop Condition Guide - Understanding Types

## 🚨 The Problem in Your Code

```java
SingleNode<T> current = null;
while(current != key){  // ← TYPE MISMATCH!
```

### Why This Doesn't Work:

1. **`current`** is of type `SingleNode<T>` (a node object)
2. **`key`** is of type `T` (the data value)
3. **You can't compare a node to data directly!**

This is like comparing:
- A **box** (the node) to what's **inside the box** (the data)
- They're different types!

---

## ✅ What the Loop Condition Should Check

### The Purpose:
The loop condition should answer: **"Are there more nodes to check?"**

### The Answer:
- **Yes** - if `current != null` (there's a node to examine)
- **No** - if `current == null` (we've reached the end)

### Correct Condition:
```java
while (current != null)  // "While there are nodes to check"
```

---

## 🎯 The Two Different Checks

### 1. Loop Condition (Outside the loop)
**Purpose**: Decide if we should continue looping
**Checks**: Have we reached the end of the list?
**Uses**: `current != null`

```java
while (current != null) {  // Continue while there are nodes
    // ...
}
```

### 2. Key Check (Inside the loop)
**Purpose**: Decide if we found what we're looking for
**Checks**: Does this node's data match the key?
**Uses**: `current.getDatum().compareTo(key) == 0`

```java
while (current != null) {
    if (current.getDatum().compareTo(key) == 0) {  // Check if data matches
        return previous;  // Found it!
    }
    // ...
}
```

---

## 📊 Visual Explanation

```
List: front → [A] → [B] → [C] → null

Loop condition checks: "Is current pointing to a node?"
- current points to [A] → YES, continue
- current points to [B] → YES, continue
- current points to [C] → YES, continue
- current points to null → NO, stop!

Key check (inside loop): "Does this node's data equal key?"
- [A].getDatum().compareTo(key) → Check if A == key
- [B].getDatum().compareTo(key) → Check if B == key
- [C].getDatum().compareTo(key) → Check if C == key
```

---

## 🔍 Understanding Types

### Node vs Data:

```java
SingleNode<T> node = ...;     // The container (node)
T data = node.getDatum();     // What's inside (data)
```

### Comparison:

```java
// ❌ WRONG: Compare node to data
if (node == key) { ... }

// ✅ CORRECT: Compare data to data
if (node.getDatum().compareTo(key) == 0) { ... }
```

---

## ✅ Correct Structure

```java
private SingleNode<T> linearSearch(final T key) {
    SingleNode<T> previous = null;
    SingleNode<T> current = this.front;  // Start at front
    
    // Loop condition: Check if we've reached the end
    while (current != null) {
        // Key check: Check if this node's data matches key
        if (current.getDatum().compareTo(key) == 0) {
            return previous;  // Found it!
        }
        // Move forward
        previous = current;
        current = current.getNext();
    }
    
    return null;  // Not found
}
```

---

## 🎓 Key Takeaways

1. **Loop condition** = `current != null` (check if we've reached the end)
2. **Key check** = `current.getDatum().compareTo(key) == 0` (check if data matches)
3. **Don't mix them up!** The loop condition doesn't check for the key
4. **Types matter**: `current` is a node, `key` is data - they can't be compared directly

---

## 💡 Common Mistakes

### Mistake 1: Comparing node to key
```java
while(current != key)  // ❌ Wrong types!
```

### Mistake 2: Using key in loop condition
```java
while(current.getDatum() != key)  // ❌ Should use compareTo, not !=
```

### Mistake 3: Wrong initialization
```java
SingleNode<T> current = null;  // ❌ Loop won't run
while(current != null) { ... }
```

### ✅ Correct Approach:
```java
SingleNode<T> current = this.front;  // ✅ Start at front
while(current != null) {  // ✅ Check if we've reached end
    if(current.getDatum().compareTo(key) == 0) {  // ✅ Check if data matches
        return previous;
    }
    // Move forward...
}
```

---

## 🔑 Remember:

- **Loop condition**: "Are there more nodes?" → `current != null`
- **Key check**: "Does this node contain the key?" → `current.getDatum().compareTo(key) == 0`
- **These are two separate checks!**

