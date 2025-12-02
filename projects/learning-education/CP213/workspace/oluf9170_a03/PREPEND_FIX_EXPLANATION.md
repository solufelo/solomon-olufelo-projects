# Why Your prepend() Method is Wrong

## The Problem

Your code tries to call:
```java
SingleNode<T> newNode = new SingleNode<T>(datum, front);
```

But `SingleNode` only has **one constructor** that takes a single parameter:
```java
public SingleNode(final T datum) {
    this.datum = datum;
    this.next = null;  // Always initialized to null
}
```

## Why This Causes an Error

When you try to pass two parameters (`datum` and `front`), Java looks for a constructor that matches:
- `SingleNode(T datum, SingleNode<T> next)` - **This doesn't exist!**

Result: **Compilation Error**

```
error: constructor SingleNode in class SingleNode cannot be applied to given types;
  required: T
  found: T,SingleNode<T>
  reason: actual and formal argument lists differ in length
```

## Correct Implementation

```java
public void prepend(final T datum) {
    // Step 1: Create new node with ONLY datum
    SingleNode<T> newNode = new SingleNode<T>(datum);
    // newNode now: [datum | null]
    
    // Step 2: Set newNode's next pointer to current front
    newNode.setNext(this.front);
    // newNode now: [datum | ──>] [oldFront | ──>] ...
    
    // Step 3: Make newNode the new front
    this.front = newNode;
    
    // Step 4: If list was empty, newNode is also the rear
    if (this.rear == null) {
        this.rear = newNode;
    }
    
    // Step 5: Update length
    this.length++;
}
```

## Visual Comparison

### ❌ Your Version (WRONG - Won't Compile)

```
BEFORE:
front ──> [A]─> [B]─> null

STEP 1: Try to create node
newNode = new SingleNode<T>(datum, front)  // ❌ ERROR! Constructor doesn't exist
```

### ✅ Correct Version

```
BEFORE:
front ──> [A]─> [B]─> null
rear  ──> [B]─> null
length = 2

STEP 1: Create new node
newNode = new SingleNode<T>(datum)
newNode: [X | null]

STEP 2: Link newNode to current front
newNode.setNext(this.front)
newNode: [X]─> [A]─> [B]─> null
          ▲
          newNode

STEP 3: Update front pointer
this.front = newNode
front ──> [X]─> [A]─> [B]─> null
          ▲
          newNode (now front)

STEP 4: Check if list was empty (it wasn't, so skip)
rear stays: [B]─> null

STEP 5: Update length
length = 3

AFTER:
front ──> [X]─> [A]─> [B]─> null
rear  ──> [B]─> null
length = 3
```

## Step-by-Step Execution (Correct Version)

### Scenario: Prepending to Non-Empty List

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3
prepend("X")

STEP 1: Create newNode
newNode = new SingleNode<T>("X")
State: newNode = [X | null]

STEP 2: Link newNode to front
newNode.setNext(this.front)
State:
  newNode: [X]─> [A]─> [B]─> [C]─> null
  front:   [A]─> [B]─> [C]─> null

STEP 3: Update front
this.front = newNode
State:
  front:   [X]─> [A]─> [B]─> [C]─> null
  rear:    [C]─> null  (unchanged)

STEP 4: Check rear
this.rear != null  ✓ (skip if block)

STEP 5: Increment length
length = 4

AFTER:
front ──> [X]─> [A]─> [B]─> [C]─> null
rear  ──> [C]─> null
length = 4
```

### Scenario: Prepending to Empty List

```
BEFORE:
front ──> null
rear  ──> null
length = 0
prepend("X")

STEP 1: Create newNode
newNode = new SingleNode<T>("X")
State: newNode = [X | null]

STEP 2: Link newNode to front
newNode.setNext(this.front)  // this.front is null
State: newNode = [X | null]

STEP 3: Update front
this.front = newNode
State:
  front:   [X]─> null
  rear:    null

STEP 4: Check rear
this.rear == null  ✓
this.rear = newNode
State:
  front:   [X]─> null
  rear:    [X]─> null  (same node!)

STEP 5: Increment length
length = 1

AFTER:
front ──> [X]─> null
rear  ──> [X]─> null
length = 1
```

## Key Points

1. **Constructor takes only one parameter**: `SingleNode(T datum)`
2. **Next pointer is always initialized to null** in the constructor
3. **You must manually set the next pointer** using `setNext()`
4. **Order matters**: Set next pointer BEFORE updating front
5. **Empty list check**: If rear is null, the new node becomes both front and rear

## Why the Constructor is Designed This Way

The `SingleNode` constructor only takes the datum because:
- It keeps the constructor simple
- It gives you explicit control over pointer manipulation
- It follows the single responsibility principle
- It's the standard pattern for linked list nodes

You always create a node first, then link it to the list structure.

## Common Mistake Pattern

Many students think they can do:
```java
new SingleNode<T>(datum, nextNode)  // ❌ Doesn't exist
```

But you must do:
```java
SingleNode<T> newNode = new SingleNode<T>(datum);  // ✅ Create node
newNode.setNext(nextNode);  // ✅ Then set the link
```

## Summary

| Your Code | Issue | Fix |
|-----------|-------|-----|
| `new SingleNode<T>(datum, front)` | ❌ Constructor doesn't exist | ✅ `new SingleNode<T>(datum)` |
| - | - | ✅ Then `newNode.setNext(this.front)` |

**The correct pattern is:**
1. Create node with datum only
2. Set next pointer explicitly
3. Update list pointers (front/rear)
4. Update length

