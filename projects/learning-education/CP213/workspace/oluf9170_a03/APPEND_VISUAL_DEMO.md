# Visual Demonstration: `append` Method (SingleList.java:16-40)

## Method Overview
The `append` method adds a new node containing the given datum to the **end** of the singly linked list.

## Code Reference
```16:40:workspace/oluf9170_a03/src/cp213/SingleList.java
public SingleList() {
    super();
}

/**
 * Appends an item to the end of the list.
 * 
 * @param datum the item to append
 */
public void append(final T datum) {
    // Create new node with the datum
    SingleNode<T> newNode = new SingleNode<T>(datum);
    
    // If list is empty, new node is front
    if (this.rear == null) {
        this.front = newNode;
    } else {
        // Link current rear to new node
        this.rear.setNext(newNode);
    }
    
    // Update rear and length
    this.rear = newNode;
    this.length++;
}
```

---

## Scenario 1: Appending to an EMPTY List

### Initial State
```
front ──> null
rear  ──> null
length = 0

[Empty List]
```

### Step 1: Create New Node
```java
SingleNode<T> newNode = new SingleNode<T>(datum);
```

```
newNode ──> [datum | null]

front ──> null
rear  ──> null
length = 0
```

### Step 2: Check if List is Empty
```java
if (this.rear == null) {  // TRUE - list is empty
    this.front = newNode;
}
```

```
newNode ──> [datum | null]
              ▲
              │
front ────────┘
rear  ──> null
length = 0
```

### Step 3: Update Rear and Length
```java
this.rear = newNode;
this.length++;
```

```
front ──> [datum | null] <── rear
             newNode
length = 1
```

### Final Result
```
front ──> [datum | null] <── rear
length = 1

List: front > datum > null
```

---

## Scenario 2: Appending to a NON-EMPTY List

### Initial State
```
front ──> [A | ──>] [B | ──>] [C | null] <── rear
          node1     node2     node3
length = 3

List: front > A > B > C > null
```

### Step 1: Create New Node
```java
SingleNode<T> newNode = new SingleNode<T>(datum);  // datum = "D"
```

```
front ──> [A | ──>] [B | ──>] [C | null] <── rear
          node1     node2     node3
length = 3

newNode ──> [D | null]
```

### Step 2: Check if List is Empty
```java
if (this.rear == null) {  // FALSE - list has nodes
    // Skip this branch
} else {
    this.rear.setNext(newNode);  // Execute this
}
```

**Before linking:**
```
front ──> [A | ──>] [B | ──>] [C | null] <── rear
          node1     node2     node3
length = 3

newNode ──> [D | null]
```

**After `this.rear.setNext(newNode)`:**
```
front ──> [A | ──>] [B | ──>] [C | ──>] [D | null]
          node1     node2     node3      newNode
                                  ▲
                                  │
rear ─────────────────────────────┘
length = 3  (not updated yet)
```

### Step 3: Update Rear and Length
```java
this.rear = newNode;
this.length++;
```

```
front ──> [A | ──>] [B | ──>] [C | ──>] [D | null] <── rear
          node1     node2     node3      newNode
length = 4
```

### Final Result
```
front ──> [A | ──>] [B | ──>] [C | ──>] [D | null] <── rear
length = 4

List: front > A > B > C > D > null
```

---

## Key Points

1. **Empty List Check**: If `rear == null`, the list is empty, so the new node becomes both `front` and `rear`.

2. **Non-Empty List**: If the list has nodes, we link the current `rear` node to the new node using `setNext()`.

3. **Always Update Rear**: After linking, `rear` always points to the new node (the last node).

4. **Always Increment Length**: The length counter is incremented regardless of whether the list was empty.

5. **Time Complexity**: O(1) - Constant time because we have direct access to the `rear` pointer.

---

## Step-by-Step Execution Trace

### Example: append("X") to list containing ["A", "B", "C"]

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
                           ▲
rear ──────────────────────┘
length = 3

STEP 1: Create newNode
newNode = [X | null]

STEP 2: Check rear == null? (FALSE)
Execute: this.rear.setNext(newNode)
front ──> [A]─> [B]─> [C]─> [X]─> null
                           ▲      ▲
rear ──────────────────────┘      │
                                  newNode

STEP 3: Update rear and length
this.rear = newNode;
this.length++;  // 3 → 4

AFTER:
front ──> [A]─> [B]─> [C]─> [X]─> null
                                  ▲
rear ─────────────────────────────┘
length = 4
```

---

## Visual Memory Aid

```
┌─────────────────────────────────────────┐
│  append(datum)                          │
│                                         │
│  1. Create newNode with datum          │
│     newNode = [datum | null]           │
│                                         │
│  2. Is list empty?                      │
│     ┌─────────┐                         │
│     │ YES     │  → front = newNode     │
│     │         │                         │
│     │ NO      │  → rear.setNext(newNode)│
│     └─────────┘                         │
│                                         │
│  3. rear = newNode                      │
│  4. length++                            │
│                                         │
│  Result: newNode is now at the end!    │
└─────────────────────────────────────────┘
```

