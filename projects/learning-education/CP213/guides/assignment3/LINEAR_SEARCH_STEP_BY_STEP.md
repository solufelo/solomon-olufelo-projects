# linearSearch - Step by Step Walkthrough

## 🎯 What We're Trying to Do

Find a node containing `key` and return the **previous node**.

Example list: `front → [A] → [B] → [C] → null`

If we're looking for `C`:
- We want to return the node containing `B` (the previous node)
- Because `B` is the node before `C`

---

## 📊 Visual Representation

```
Initial state:
front → [A] → [B] → [C] → null
        ↑
     current (should start here!)
previous = null

After first iteration (A != key):
front → [A] → [B] → [C] → null
        ↑      ↑
    previous current

After second iteration (B != key):
front → [A] → [B] → [C] → null
              ↑      ↑
          previous current

Found! (C == key):
Return previous (which points to [B])
```

---

## 🔍 Your Current Code Analysis

```java
SingleNode<T> current = null;  // ← Problem 1: Starts as null

while(current != null){  // ← Problem 2: Loop never runs!
    if(current.getDatum().compareTo(key) == 0) {
        return previous;
    }
    // ← Problem 3: Nothing here to move forward!
}
return next;  // ← Problem 4: Wrong return value
```

---

## 🐛 Problem 1: Initialization

### What you have:
```java
SingleNode<T> current = null;
```

### Question:
If `current = null`, and your loop condition is `while(current != null)`, will the loop ever execute?

**Answer**: No! The condition is false immediately, so the loop never runs.

### What it should be:
```java
SingleNode<T> current = this.front;  // Start at the front of the list
```

**Why?**: You want to start examining nodes from the beginning of the list.

---

## 🐛 Problem 2: Loop Never Runs

### What you have:
```java
SingleNode<T> current = null;  // current is null
while(current != null){  // "while null is not null" = false
    // This code never executes!
}
```

### Fix:
```java
SingleNode<T> current = this.front;  // current points to first node
while(current != null){  // "while current is not null" = true (if list has nodes)
    // Now the loop can run!
}
```

---

## 🐛 Problem 3: Loop Doesn't Advance

### What you have:
```java
while(current != null){
    if(current.getDatum().compareTo(key) == 0) {
        return previous;
    }
    // ← Nothing here! current never changes!
}
```

### What happens:
- If `current` doesn't match the key, the loop checks the same node forever
- This creates an **infinite loop** (if current is not null)

### What you need:
After checking a node, you must move to the next one:

```java
while(current != null){
    if(current.getDatum().compareTo(key) == 0) {
        return previous;  // Found it! Return previous node
    }
    // Move forward:
    previous = current;              // Current node becomes previous
    current = current.getNext();    // Move to next node
}
```

### Why this works:
1. **`previous = current`**: The node we just checked becomes the "previous" node
2. **`current = current.getNext()`**: Move to the next node in the list
3. The loop continues with the next node

---

## 🐛 Problem 4: Wrong Return Value

### What you have:
```java
return next;  // What is "next"? Is this what we want to return?
```

### Questions:
1. What should we return if we **find** the key?
   - Answer: The `previous` node (which is done correctly inside the if statement)

2. What should we return if we **don't find** the key?
   - Answer: `null` (to indicate "not found")

3. Do we need the `next` variable at all?
   - Answer: No! We only need `previous` and `current`

### Fix:
```java
return null;  // Key not found
```

---

## ✅ Corrected Code Structure

```java
private SingleNode<T> linearSearch(final T key) {
    // Step 1: Initialize variables
    SingleNode<T> previous = null;        // No previous node at start
    SingleNode<T> current = this.front;   // Start at the front
    
    // Step 2: Loop through the list
    while (current != null) {
        // Step 3: Check if current node has the key
        if (current.getDatum().compareTo(key) == 0) {
            return previous;  // Found it! Return previous node
        }
        // Step 4: Move forward to next node
        previous = current;              // Current becomes previous
        current = current.getNext();    // Move to next node
    }
    
    // Step 5: Key not found
    return null;
}
```

---

## 🎓 Step-by-Step Execution Example

Let's trace through finding `C` in the list: `front → [A] → [B] → [C] → null`

### Initial:
```
previous = null
current = front (points to [A])
```

### Iteration 1:
```
Check: A.compareTo(C) != 0 (A < C)
Not found, so move forward:
previous = current (previous now points to [A])
current = current.getNext() (current now points to [B])
```

### Iteration 2:
```
Check: B.compareTo(C) != 0 (B < C)
Not found, so move forward:
previous = current (previous now points to [B])
current = current.getNext() (current now points to [C])
```

### Iteration 3:
```
Check: C.compareTo(C) == 0 (C == C)
Found it! Return previous (which points to [B])
```

---

## 🔑 Key Points to Remember

1. **Initialize `current = this.front`** - Start at the beginning
2. **Loop while `current != null`** - Continue until end of list
3. **Move forward inside the loop** - Update both `previous` and `current`
4. **Return `previous` when found** - That's what the method needs
5. **Return `null` when not found** - Indicate failure

---

## 💡 Common Mistakes to Avoid

1. ❌ `current = null` → Loop never runs
2. ❌ No update in loop → Infinite loop
3. ❌ Forgetting to update `previous` → Can't return correct node
4. ❌ Returning wrong value → Should return `previous` or `null`, not `next`

---

## 🎯 Your Turn!

Try rewriting the method with these fixes:
- Initialize `current = this.front` (not `null`)
- Update `previous` and `current` inside the loop
- Return `null` at the end (not `next`)
- Remove the `next` variable (you don't need it)

Good luck! 🚀

