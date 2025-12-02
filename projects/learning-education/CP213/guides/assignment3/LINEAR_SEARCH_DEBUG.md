# Debugging Your linearSearch Method - Step by Step

## 🐛 Issues to Fix

### Issue 1: Variable Declaration Location
```java
SingleNode<T> current;  // ← Outside the method (class variable)
```
**Question**: Should `current` be declared here, or inside the method?

**Think about**: Do other methods need to use `current`? Or is it only used in `linearSearch`?

**Hint**: If it's only used in one method, it should be a **local variable** inside that method.

---

### Issue 2: Variable Initialization Mismatch
```java
SingleNode<T> next = this.front;  // ← You initialized "next"
// ...
while(current != null){  // ← But checking "current"!
```
**Question**: What's the problem here?

**Think about**: 
- Which variable should track where you are in the list?
- What should that variable be initialized to?
- Should you use `next` or `current`?

**Hint**: You want to start at the front of the list. What points to the front?

---

### Issue 3: Infinite Loop Problem
```java
while(current != null){
    if(current.getDatum().compareTo(key) == 0) {
        return previous;
    }
    // ← Nothing happens here! Loop never advances!
}
```
**Question**: What will happen if `current` is not null but doesn't contain the key?

**Think about**:
- After checking a node, what should happen?
- How do you move to the next node?
- What should `previous` become?
- What should `current` become?

**Hint**: Look at the pattern from the explanation guide - you need to move forward!

---

### Issue 4: Unreachable Code
```java
return null;  // ← This returns and exits the method
}
return next;  // ← This code can NEVER execute!
```
**Question**: Can the second `return` ever be reached?

**Think about**: What happens when you execute `return null;`?

**Hint**: Once you `return`, the method exits immediately. Nothing after that line can execute.

---

### Issue 5: Variable Naming Confusion
```java
SingleNode<T> next = this.front;
```
**Question**: Is `next` a good name here?

**Think about**: 
- What does `next` represent? The current node you're looking at?
- What method gets the next node? (`getNext()`)
- Could this naming be confusing?

**Hint**: A better name might be `current` - it represents the current node you're examining.

---

## 🎯 The Correct Logic Flow

### Step 1: Initialize variables
```java
SingleNode<T> previous = null;      // No previous node at start
SingleNode<T> current = this.front; // Start at the front
```

### Step 2: Loop through the list
```java
while (current != null) {  // Continue while there are nodes
    // Check if this node has the key
    // If yes: return previous
    // If no: move forward
}
```

### Step 3: Move forward in the loop
```java
previous = current;              // Current becomes previous
current = current.getNext();    // Move to next node
```

### Step 4: Return null if not found
```java
return null;  // Only one return statement needed here
```

---

## 🔍 Complete Corrected Structure

```java
private SingleNode<T> linearSearch(final T key) {
    // Step 1: Initialize - where do we start?
    SingleNode<T> previous = ???;
    SingleNode<T> current = ???;
    
    // Step 2: Loop through nodes
    while (???) {
        // Step 3: Check if we found it
        if (???) {
            return ???;
        }
        // Step 4: Move forward
        ??? = ???;
        ??? = ???;
    }
    
    // Step 5: Not found
    return ???;
}
```

---

## 💡 Fill in the Blanks

Try to fill in the `???` above:

1. **`previous` should start as**: `???`
   - Hint: There's no previous node at the beginning

2. **`current` should start as**: `???`
   - Hint: Where does the list start?

3. **Loop condition should be**: `while (???)`
   - Hint: Continue while there are nodes to check

4. **Check condition should be**: `if (???)`
   - Hint: Compare the current node's data to the key

5. **If found, return**: `return ???`
   - Hint: What node do we want to return?

6. **Move forward**: 
   - `??? = ???;`  // Update previous
   - `??? = ???;`  // Update current
   - Hint: Current becomes previous, and current moves to the next node

7. **If not found, return**: `return ???`
   - Hint: What should we return if we never found it?

---

## ✅ Checklist

Before you write your code, make sure you understand:

- [ ] `current` should be a **local variable** (inside the method), not a class variable
- [ ] `current` should be initialized to `this.front` (start at the front)
- [ ] The loop should continue while `current != null`
- [ ] Inside the loop, you need to **move forward** after checking each node
- [ ] To move forward: `previous = current; current = current.getNext();`
- [ ] Only one `return null;` at the end (if not found)
- [ ] Return `previous` when you find a match

---

## 🎓 Key Insight

The most common mistake is **forgetting to move forward in the loop**. Without updating `current`, you'll either:
- Have an infinite loop (if current is not null)
- Only check the first node (if current stays the same)

Always remember: **After checking a node, move to the next one!**

