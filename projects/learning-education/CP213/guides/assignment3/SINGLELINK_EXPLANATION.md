# SingleLink Class - Baby Steps Explanation

## What is SingleLink?
`SingleLink` is like a **blueprint** (abstract class) for creating different data structures (stacks, queues, lists) using linked nodes. Think of it as a foundation that child classes build upon.

---

## The Three Main Parts of a Linked Structure

Imagine a **chain of people holding hands**:

1. **`front`** - The first person in the chain (the front of the line)
2. **`rear`** - The last person in the chain (the end of the line)  
3. **`length`** - How many people are in the chain (the count)

```
front → [Person1] → [Person2] → [Person3] → null
                               ↑
                              rear
length = 3
```

---

## Attributes (The Data Storage)

### `protected SingleNode<T> front = null;`
- **What it is**: A pointer to the first node in your linked structure
- **Think of it as**: The person at the front of the line
- **Starts as**: `null` (empty line)

### `protected SingleNode<T> rear = null;`
- **What it is**: A pointer to the last node in your linked structure
- **Think of it as**: The person at the back of the line
- **Starts as**: `null` (empty line)

### `protected int length = 0;`
- **What it is**: Count of how many items are in the structure
- **Think of it as**: The number of people in line
- **Starts as**: `0` (empty)

---

## The Inner Class: SingleLinkIterator

### What is an Iterator?
An iterator is like a **tour guide** that walks through your linked structure, showing you each item one at a time.

### How it Works:
```java
private class SingleLinkIterator implements Iterator<T> {
    private SingleNode<T> current = SingleLink.this.front;  // Start at the front
```

1. **`current`** - Points to the node you're currently looking at
2. **Starts at**: `front` (beginning of the chain)

### `hasNext()` Method
```java
public boolean hasNext() {
    return this.current != null;
}
```
- **What it does**: Checks if there's another item to look at
- **Returns**: `true` if `current` is not `null`, `false` otherwise
- **Think of it as**: "Is there another person in line ahead of me?"

### `next()` Method
```java
public T next() {
    if (this.current == null) {
        throw new NoSuchElementException();  // Error: nothing left!
    } else {
        T result = this.current.getDatum();      // Get the data
        this.current = this.current.getNext();   // Move to next node
    }
    return result;
}
```
- **What it does**: 
  1. Gets the data from current node
  2. Moves `current` to the next node
  3. Returns the data
- **Think of it as**: "Show me this person, then point to the next person"

---

## Helper Methods (The Building Blocks)

### 1. `append(SingleLink<T> source)` - Attach One Chain to Another

**What it does**: Takes all nodes from `source` and attaches them to the end of `this`

**Step-by-step**:
```
Before:
this:  front → [A] → [B] → null
              rear
source: front → [X] → [Y] → [Z] → null
                rear

After:
this:  front → [A] → [B] → [X] → [Y] → [Z] → null
                                   rear
source: front → null (empty!)
      rear → null
```

**Code breakdown**:
```java
if (source.front != null) {  // Only if source has items
    
    if (this.front == null) {
        // If this is empty, just take source's nodes
        this.front = source.front;
    } else {
        // Connect source to the end of this
        this.rear.setNext(source.front);  // Link rear to source's front
    }
    
    this.rear = source.rear;        // Update rear pointer
    this.length += source.length;   // Update count
    
    // Empty source
    source.front = null;
    source.rear = null;
    source.length = 0;
}
```

**Real-world analogy**: Taking another line of people and making them join the back of your line.

---

### 2. `moveFrontToFront(SingleLink<T> source)` - Take First from Source, Add to Front of This

**What it does**: Removes the front node from `source` and adds it to the front of `this`

**Step-by-step**:
```
Before:
this:  front → [A] → [B] → null
              rear
source: front → [X] → [Y] → [Z] → null
                rear

After:
this:  front → [X] → [A] → [B] → null
              rear
source: front → [Y] → [Z] → null
                rear
```

**Code breakdown**:
```java
if (source.front != null) {  // Only if source has items
    
    final SingleNode<T> node = source.front;  // Save the node to move
    
    // Remove from source
    source.length--;
    source.front = source.front.getNext();  // Move source's front forward
    
    if (source.front == null) {
        source.rear = null;  // If source is now empty, clear rear
    }
    
    // Add to front of this
    node.setNext(this.front);  // Link node to current front
    
    if (this.rear == null) {
        this.rear = node;  // If this was empty, node is also rear
    }
    
    this.front = node;  // Make node the new front
    this.length++;
}
```

**Real-world analogy**: Taking the first person from another line and putting them at the front of your line.

---

### 3. `moveFrontToRear(SingleLink<T> source)` - Take First from Source, Add to End of This

**What it does**: Removes the front node from `source` and adds it to the end of `this`

**Step-by-step**:
```
Before:
this:  front → [A] → [B] → null
              rear
source: front → [X] → [Y] → [Z] → null
                rear

After:
this:  front → [A] → [B] → [X] → null
                           rear
source: front → [Y] → [Z] → null
                rear
```

**Code breakdown**:
```java
if (source.front != null) {  // Only if source has items
    
    final SingleNode<T> node = source.front;  // Save the node to move
    
    // Remove from source (same as moveFrontToFront)
    source.length--;
    source.front = source.front.getNext();
    
    if (source.front == null) {
        source.rear = null;
    }
    
    node.setNext(null);  // This node becomes the new end
    
    // Add to rear of this
    if (this.rear == null) {
        this.front = node;  // If this was empty, node is front
    } else {
        this.rear.setNext(node);  // Link current rear to node
    }
    
    this.rear = node;  // Make node the new rear
    this.length++;
}
```

**Real-world analogy**: Taking the first person from another line and putting them at the back of your line.

---

## Simple Methods (Easy Ones!)

### `getLength()`
```java
public final int getLength() {
    return this.length;
}
```
- **What it does**: Returns how many items are in the structure
- **Think of it as**: "How many people are in line?"

### `isEmpty()`
```java
public final boolean isEmpty() {
    return this.front == null;
}
```
- **What it does**: Checks if the structure is empty
- **Returns**: `true` if `front` is `null`, `false` otherwise
- **Think of it as**: "Is the line empty?"

### `peek()`
```java
public final T peek() {
    if (this.front != null) {
        return this.front.getDatum();  // Return data without removing
    }
    return null;
}
```
- **What it does**: Looks at the front item WITHOUT removing it
- **Think of it as**: "Who's at the front of the line?" (just looking, not moving them)

### `iterator()`
```java
public final Iterator<T> iterator() {
    return new SingleLinkIterator();
}
```
- **What it does**: Creates a new iterator to walk through the structure
- **Used by**: Enhanced for-loops like `for (T item : myStructure)`

### `toString()`
```java
public String toString() {
    String string = "front > ";
    SingleNode<T> curr = this.front;
    
    while (curr != null) {
        string += curr.getDatum() + " > ";
        curr = curr.getNext();
    }
    string += "null";
    return string;
}
```
- **What it does**: Creates a string showing all items in the structure
- **Output format**: `"front > A > B > C > null"`
- **How it works**: Walks through each node, adding its data to the string

---

## Key Concepts to Remember

### 1. **Null Checks**
Always check if `front` is `null` before trying to access nodes - this means the structure is empty!

### 2. **Updating Pointers**
When you add/remove nodes, you MUST update:
- `front` (if adding/removing at front)
- `rear` (if adding/removing at rear)
- `length` (always update the count)

### 3. **Linking Nodes**
- To add a node: Set its `next` pointer, then update `front`/`rear`
- To remove a node: Update `front`/`rear` to skip the node

### 4. **O(1) Operations**
The helper methods (`append`, `moveFrontToFront`, `moveFrontToRear`) are O(1) because they:
- Don't use loops
- Just move pointers around
- Work in constant time

---

## Common Patterns

### Pattern 1: Adding to Front
```java
newNode.setNext(this.front);
this.front = newNode;
if (this.rear == null) {
    this.rear = newNode;
}
this.length++;
```

### Pattern 2: Adding to Rear
```java
if (this.rear == null) {
    this.front = newNode;
} else {
    this.rear.setNext(newNode);
}
this.rear = newNode;
this.length++;
```

### Pattern 3: Removing from Front
```java
if (this.front != null) {
    this.front = this.front.getNext();
    if (this.front == null) {
        this.rear = null;  // Now empty!
    }
    this.length--;
}
```

---

## Visual Summary

```
Empty Structure:
front → null
rear → null
length = 0

One Item:
front → [Data] → null
        ↑
       rear
length = 1

Multiple Items:
front → [A] → [B] → [C] → null
        ↑              ↑
      front          rear
length = 3
```

---

## Why This Class is Abstract

This class is `abstract` because:
- It provides the **foundation** (attributes and helper methods)
- Child classes (Stack, Queue, List) define the **specific behavior** (push, pop, enqueue, dequeue, etc.)
- You can't create a `SingleLink` object directly - you create `SingleStack`, `SingleQueue`, etc.

---

## Tips for Using This Class

1. **Always update `length`** when adding/removing nodes
2. **Always check for empty** (`front == null`) before accessing nodes
3. **Update both `front` and `rear`** when the structure becomes empty or gets its first item
4. **Use the helper methods** (`moveFrontToFront`, `moveFrontToRear`, `append`) - they're O(1) and make your life easier!
5. **Test with simple cases first**: empty structure, one item, two items

