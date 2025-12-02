# How to Use linearSearch - Helper Method Guide

## 🎯 What is a Helper Method?

A **helper method** is a private method that:
- Is used by other methods in the same class
- Makes code more readable and reusable
- Is not meant to be called directly from outside the class

## 📋 Methods That Should Use `linearSearch`

### 1. `remove(T key)` - Remove a node containing key
**Logic**:
- Use `linearSearch(key)` to find the previous node
- If found, remove the node after previous
- Return the removed node's data

**How `linearSearch` helps**:
- Finds the previous node
- Returns `null` if key not found

### 2. `contains(T key)` - Check if key exists
**Logic**:
- Use `linearSearch(key)` to search for the key
- If it returns a node (or we can check differently), key exists
- Return `true` or `false`

**How `linearSearch` helps**:
- Does the searching work
- We just need to check if key was found

### 3. `find(T key)` - Find and return the data
**Logic**:
- Use `linearSearch(key)` to find the previous node
- If found, get the next node's data
- Return the data or `null`

**How `linearSearch` helps**:
- Finds where the key is
- We can access the node containing the key

### 4. `removeMany(T key)` - Remove all occurrences
**Logic**:
- Use `linearSearch(key)` repeatedly
- Remove each occurrence found
- Continue until none found

**How `linearSearch` helps**:
- Finds each occurrence
- We remove it and search again

## 🔍 Understanding the Return Value

### `linearSearch` returns:
- **`SingleNode<T> previous`** - The node before the one containing key
- **`null`** - If key not found OR key is at the front

### How to Use This:

#### Case 1: Previous is `null`
```java
SingleNode<T> previous = linearSearch(key);
if (previous == null) {
    // Key might be at front, or not found
    // Need to check if front contains the key
}
```

#### Case 2: Previous is not `null`
```java
SingleNode<T> previous = linearSearch(key);
if (previous != null) {
    // Key is found!
    // The node containing key is: previous.getNext()
    SingleNode<T> target = previous.getNext();
}
```

## 💡 Example: Implementing `contains(T key)`

### Think About It:
1. What does `contains` need to do?
   - Check if `key` exists in the list
   - Return `true` if found, `false` if not

2. How can `linearSearch` help?
   - It finds where the key is (or returns `null` if not found)
   - But there's a problem: if key is at front, `linearSearch` returns `null`
   - So we need to check the front separately!

### Step-by-Step Logic:

```java
public boolean contains(final T key) {
    // Check if list is empty
    if (this.front == null) {
        return false;
    }
    
    // Check if key is at the front
    if (this.front.getDatum().compareTo(key) == 0) {
        return true;  // Found at front!
    }
    
    // Use linearSearch to find key in rest of list
    SingleNode<T> previous = linearSearch(key);
    
    // If previous is not null, key was found (after front)
    // If previous is null, key might be at front (already checked) or not found
    // Wait... if we already checked front, and linearSearch returns null,
    // that means key is not in the list
    
    // Actually, let's think differently:
    // linearSearch returns null if:
    // 1. Key is at front
    // 2. Key is not found
    
    // So we need to check front separately first!
    
    // Better approach: check front first, then use linearSearch
    if (this.front.getDatum().compareTo(key) == 0) {
        return true;
    }
    
    SingleNode<T> previous = linearSearch(key);
    return previous != null;  // If previous is not null, key was found
}
```

### Wait, But There's a Problem!

If `linearSearch` returns `null`, it could mean:
1. Key is at front (but we checked that already)
2. Key is not found

So after checking front, if `linearSearch` returns `null`, it means key is not found.

### Simpler Approach:

```java
public boolean contains(final T key) {
    // Check if key is at front
    if (this.front != null && this.front.getDatum().compareTo(key) == 0) {
        return true;
    }
    
    // Search rest of list
    SingleNode<T> previous = linearSearch(key);
    return previous != null;  // Found if previous is not null
}
```

## 🎓 Key Insight

`linearSearch` is designed to help with operations that need to **modify** the list (like `remove`), because it returns the previous node. For simple checks like `contains`, you might:

1. Check the front separately (since `linearSearch` can't distinguish "at front" from "not found")
2. Use `linearSearch` for the rest of the list
3. Or implement `contains` differently (using iterator or direct traversal)

## ✅ Summary

- **The warning is normal** - `linearSearch` will be used by other methods
- **You can ignore it for now** - It will go away when you implement other methods
- **`linearSearch` is useful for**: `remove()`, `find()`, `removeMany()`
- **For `contains()`**: You might want to check front separately first

## 🚀 Next Steps

When you implement methods like `remove()` or `find()`, you'll use `linearSearch` like this:

```java
public T remove(final T key) {
    // Check if key is at front
    if (this.front != null && this.front.getDatum().compareTo(key) == 0) {
        // Remove from front
        T data = this.front.getDatum();
        this.front = this.front.getNext();
        this.length--;
        if (this.front == null) {
            this.rear = null;  // List is now empty
        }
        return data;
    }
    
    // Use linearSearch to find key in rest of list
    SingleNode<T> previous = linearSearch(key);
    if (previous != null) {
        // Remove the node after previous
        SingleNode<T> target = previous.getNext();
        T data = target.getDatum();
        previous.setNext(target.getNext());
        this.length--;
        if (target == this.rear) {
            this.rear = previous;  // Update rear if removing last node
        }
        return data;
    }
    
    return null;  // Key not found
}
```

But that's for later! For now, the warning is fine - you can ignore it. 🎉

