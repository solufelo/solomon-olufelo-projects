# SingleList Visual Guide - Complete Method Diagrams

This guide provides visual demonstrations for all methods in the `SingleList` class.

---

## Table of Contents

1. [Basic Operations](#basic-operations)
   - append()
   - prepend()
   - insert(int i, T datum)
   - remove(T key)
   - removeFront()

2. [Search Operations](#search-operations)
   - contains(T key)
   - find(T key)
   - count(T key)
   - index(T key)
   - get(int n)

3. [Comparison Operations](#comparison-operations)
   - equals(SingleList<T> source)
   - min()
   - max()

4. [List Manipulation](#list-manipulation)
   - clean()
   - reverse()
   - removeMany(T key)

5. [Node Movement Operations](#node-movement-operations)
   - combine(SingleList<T> left, SingleList<T> right)
   - split(SingleList<T> left, SingleList<T> right)
   - splitAlternate(SingleList<T> left, SingleList<T> right)

6. [Set Operations](#set-operations)
   - intersection(SingleList<T> left, SingleList<T> right)
   - union(SingleList<T> left, SingleList<T> right)

7. [Helper Methods](#helper-methods)
   - linearSearch(T key)

---

## Basic Operations

### 1. append(T datum)

**Purpose**: Adds a new node to the end of the list.

#### Scenario: Appending to Empty List

```
BEFORE:
front ──> null
rear  ──> null
length = 0

STEP 1: Create newNode
newNode = [X | null]

STEP 2: List is empty, set front
front ──> [X | null]
rear  ──> null
length = 0

STEP 3: Update rear and length
front ──> [X | null] <── rear
length = 1

AFTER:
front ──> [X | null] <── rear
length = 1
```

#### Scenario: Appending to Non-Empty List

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
                           ▲
rear ──────────────────────┘
length = 3

STEP 1: Create newNode
newNode = [X | null]

STEP 2: Link rear to newNode
front ──> [A]─> [B]─> [C]─> [X]─> null
                           ▲      ▲
rear ──────────────────────┘      │
                                  newNode
length = 3

STEP 3: Update rear and length
front ──> [A]─> [B]─> [C]─> [X]─> null
                                  ▲
rear ─────────────────────────────┘
length = 4

AFTER:
front ──> [A]─> [B]─> [C]─> [X]─> null
length = 4
```

---

### 2. prepend(T datum)

**Purpose**: Adds a new node to the front of the list.

#### Scenario: Prepending to Empty List

```
BEFORE:
front ──> null
rear  ──> null
length = 0

STEP 1: Create newNode
newNode = [X | null]

STEP 2: Set newNode as front
front ──> [X | null]
rear  ──> null
length = 0

STEP 3: If list was empty, set rear too
front ──> [X | null] <── rear
length = 1

AFTER:
front ──> [X | null] <── rear
length = 1
```

#### Scenario: Prepending to Non-Empty List

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
                           ▲
rear ──────────────────────┘
length = 3

STEP 1: Create newNode
newNode = [X | ──>] (will point to A)
          [A]─> [B]─> [C]─> null

STEP 2: Link newNode to front
newNode.setNext(this.front)
          [X]─> [A]─> [B]─> [C]─> null
          ▲
front ────┘
rear ──────────────────────┘
length = 3

STEP 3: Update front and length
front ──> [X]─> [A]─> [B]─> [C]─> null
                           ▲
rear ──────────────────────┘
length = 4

AFTER:
front ──> [X]─> [A]─> [B]─> [C]─> null
length = 4
```

---

### 3. insert(int i, T datum)

**Purpose**: Inserts a node at a specific index. If index is beyond length, appends.

#### Scenario: Insert at Front (i = 0)

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3

STEP 1: Create newNode
newNode = [X | null]

STEP 2: i <= 0, insert at front
newNode.setNext(this.front)
          [X]─> [A]─> [B]─> [C]─> null
          ▲
front ────┘

STEP 3: Update front and length
front ──> [X]─> [A]─> [B]─> [C]─> null
length = 4

AFTER:
front ──> [X]─> [A]─> [B]─> [C]─> null
length = 4
```

#### Scenario: Insert in Middle (i = 2)

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
index:    0     1     2
length = 3

STEP 1: Create newNode
newNode = [X | null]

STEP 2: Find node at position i-1 (index 1)
previous = [B] (at index 1)

STEP 3: Insert after previous
newNode.setNext(previous.getNext())  // X points to C
previous.setNext(newNode)            // B points to X

front ──> [A]─> [B]─> [X]─> [C]─> null
                  ▲     ▲
           previous  newNode
length = 3

STEP 4: Update length
front ──> [A]─> [B]─> [X]─> [C]─> null
length = 4

AFTER:
front ──> [A]─> [B]─> [X]─> [C]─> null
length = 4
```

#### Scenario: Insert Beyond Length (i >= length)

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3
Insert at i = 5 (beyond length)

RESULT: Calls append()
front ──> [A]─> [B]─> [C]─> [X]─> null
length = 4
```

---

### 4. remove(T key)

**Purpose**: Removes the first occurrence of key and returns it.

#### Scenario: Remove from Front

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3
remove("A")

STEP 1: linearSearch("A") returns null (key is at front)
STEP 2: Check if front contains key
front.getDatum().compareTo("A") == 0  ✓

STEP 3: Remove from front
result = "A"
front ──> [B]─> [C]─> null
          ▲
front ────┘
length = 2

AFTER:
front ──> [B]─> [C]─> null
length = 2
Returns: "A"
```

#### Scenario: Remove from Middle

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3
remove("B")

STEP 1: linearSearch("B")
  current = [A], compareTo("B") != 0
  previous = [A], current = [B]
  current.getDatum().compareTo("B") == 0  ✓
  return previous = [A]

STEP 2: Remove node after previous
nodeToRemove = previous.getNext() = [B]
result = "B"
previous.setNext(nodeToRemove.getNext())
  [A]─> [C]─> null

STEP 3: Update length
front ──> [A]─> [C]─> null
length = 2

AFTER:
front ──> [A]─> [C]─> null
length = 2
Returns: "B"
```

#### Scenario: Remove from End

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3
remove("C")

STEP 1: linearSearch("C")
  Returns previous = [B]

STEP 2: Remove last node
nodeToRemove = [C]
previous.setNext(null)  // B now points to null
this.rear = previous    // Update rear to B

STEP 3: Update length
front ──> [A]─> [B]─> null
                  ▲
rear ─────────────┘
length = 2

AFTER:
front ──> [A]─> [B]─> null
length = 2
Returns: "C"
```

---

### 5. removeFront()

**Purpose**: Removes and returns the front element.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
length = 3

STEP 1: Check if empty
front != null  ✓

STEP 2: Save result and remove front
result = "A"
front ──> [B]─> [C]─> null
          ▲
front ────┘
length = 2

STEP 3: Check if list is now empty
front != null  ✓ (no need to update rear)

AFTER:
front ──> [B]─> [C]─> null
length = 2
Returns: "A"
```

#### Scenario: Remove from Single-Node List

```
BEFORE:
front ──> [A]─> null
rear  ──> [A]─> null
length = 1

STEP 1: Remove front
result = "A"
front = null
length = 0

STEP 2: List is empty, clear rear
rear = null

AFTER:
front ──> null
rear  ──> null
length = 0
Returns: "A"
```

---

## Search Operations

### 6. contains(T key)

**Purpose**: Checks if key exists in the list.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
contains("B")

STEP 1: Start at front
current = [A]
current.getDatum().compareTo("B") != 0

STEP 2: Move to next
current = [B]
current.getDatum().compareTo("B") == 0  ✓

RESULT: return true

---

contains("X")

STEP 1: Check [A] - not "X"
STEP 2: Check [B] - not "X"
STEP 3: Check [C] - not "X"
STEP 4: current = null

RESULT: return false
```

---

### 7. find(T key)

**Purpose**: Finds and returns the matching object.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
find("B")

STEP 1: Start at front
current = [A]
current.getDatum().compareTo("B") != 0

STEP 2: Move to next
current = [B]
current.getDatum().compareTo("B") == 0  ✓

RESULT: return "B"

---

find("X")

Traverse entire list, no match found
RESULT: return null
```

---

### 8. count(T key)

**Purpose**: Counts occurrences of key.

```
BEFORE:
front ──> [A]─> [B]─> [B]─> [C]─> [B]─> null
count("B")

STEP 1: Initialize
count = 0
current = [A]
current.getDatum() != "B"  → count = 0

STEP 2: current = [B]
current.getDatum() == "B"  → count = 1

STEP 3: current = [B]
current.getDatum() == "B"  → count = 2

STEP 4: current = [C]
current.getDatum() != "B"  → count = 2

STEP 5: current = [B]
current.getDatum() == "B"  → count = 3

STEP 6: current = null

RESULT: return 3
```

---

### 9. index(T key)

**Purpose**: Finds the first index of key.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> [B]─> null
index:    0     1     2     3
index("B")

STEP 1: index = 0, current = [A]
current.getDatum() != "B"

STEP 2: index = 1, current = [B]
current.getDatum() == "B"  ✓

RESULT: return 1

---

index("X")

Traverse entire list, no match
RESULT: return -1
```

---

### 10. get(int n)

**Purpose**: Gets the nth object by index.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
index:    0     1     2
get(1)

STEP 1: Check bounds
n = 1, length = 3
0 <= 1 < 3  ✓ (valid)

STEP 2: Traverse to index n
current = [A]  (i = 0)
current = [B]  (i = 1)  ← Found!

RESULT: return "B"

---

get(5)

STEP 1: Check bounds
n = 5, length = 3
5 >= 3  ✓ (invalid)

RESULT: return null
```

---

## Comparison Operations

### 11. equals(SingleList<T> source)

**Purpose**: Compares two lists for equality.

```
BEFORE:
this:   front ──> [A]─> [B]─> [C]─> null
        length = 3

source: front ──> [A]─> [B]─> [C]─> null
        length = 3

equals(source)

STEP 1: Check lengths
this.length (3) == source.length (3)  ✓

STEP 2: Compare elements
current1 = [A], current2 = [A]
"A".compareTo("A") == 0  ✓

current1 = [B], current2 = [B]
"B".compareTo("B") == 0  ✓

current1 = [C], current2 = [C]
"C".compareTo("C") == 0  ✓

STEP 3: Both lists exhausted
current1 = null, current2 = null

RESULT: return true

---

NOT EQUAL EXAMPLE:

this:   front ──> [A]─> [B]─> [C]─> null
source: front ──> [A]─> [X]─> [C]─> null

STEP 2: Compare elements
current1 = [A], current2 = [A]  ✓
current1 = [B], current2 = [X]
"B".compareTo("X") != 0  ✗

RESULT: return false
```

---

### 12. min()

**Purpose**: Finds the minimum value.

```
BEFORE:
front ──> [5]─> [2]─> [8]─> [1]─> null

min()

STEP 1: Initialize
min = 5 (front.getDatum())
current = [2]

STEP 2: Compare
2 < 5  ✓  → min = 2
current = [8]

STEP 3: Compare
8 < 2  ✗  → min = 2
current = [1]

STEP 4: Compare
1 < 2  ✓  → min = 1
current = null

RESULT: return 1
```

---

### 13. max()

**Purpose**: Finds the maximum value.

```
BEFORE:
front ──> [5]─> [2]─> [8]─> [1]─> null

max()

STEP 1: Initialize
max = 5 (front.getDatum())
current = [2]

STEP 2: Compare
2 > 5  ✗  → max = 5
current = [8]

STEP 3: Compare
8 > 5  ✓  → max = 8
current = [1]

STEP 4: Compare
1 > 8  ✗  → max = 8
current = null

RESULT: return 8
```

---

## List Manipulation

### 14. clean()

**Purpose**: Removes duplicates, keeping first occurrence.

```
BEFORE:
front ──> [A]─> [B]─> [A]─> [C]─> [B]─> [A]─> null
length = 6

clean()

ITERATION 1: current = [A]
  Check remaining: [B]─> [A]─> [C]─> [B]─> [A]
  Remove all "A" duplicates:
    Remove second [A]
    Remove third [A]
  After: [A]─> [B]─> [C]─> [B]─> null
  length = 4

ITERATION 2: current = [B]
  Check remaining: [C]─> [B]
  Remove "B" duplicate:
    Remove second [B]
  After: [A]─> [B]─> [C]─> null
  length = 3

ITERATION 3: current = [C]
  Check remaining: (none)
  No duplicates

AFTER:
front ──> [A]─> [B]─> [C]─> null
length = 3
```

**Detailed Step-by-Step for First Iteration:**

```
current = [A]
datum = "A"
previous = [A]
check = [B]

STEP 1: check = [B]
"B" != "A"  → previous = [B], check = [A]

STEP 2: check = [A]
"A" == "A"  ✓
  Remove: previous.setNext([A].getNext())
  [B]─> [C]─> [B]─> [A]
  check = [C]

STEP 3: check = [C]
"C" != "A"  → previous = [C], check = [B]

STEP 4: check = [B]
"B" != "A"  → previous = [B], check = [A]

STEP 5: check = [A]
"A" == "A"  ✓
  Remove: [B]─> null
  check = null

Result after first iteration:
[A]─> [B]─> [C]─> null
```

---

### 15. reverse()

**Purpose**: Reverses the order of nodes.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> [D]─> null
                              ▲
rear ─────────────────────────┘
length = 4

reverse()

STEP 1: Initialize pointers
previous = null
current = [A]
next = null
oldFront = [A]

STEP 2: Reverse link [A]
next = [B]
current.setNext(null)  // [A]─> null
previous = [A]
current = [B]

State: null <── [A]     [B]─> [C]─> [D]─> null
                ▲
             previous

STEP 3: Reverse link [B]
next = [C]
current.setNext([A])   // [B]─> [A]─> null
previous = [B]
current = [C]

State: null <── [A] <── [B]     [C]─> [D]─> null
                      previous

STEP 4: Reverse link [C]
next = [D]
current.setNext([B])   // [C]─> [B]─> [A]─> null
previous = [C]
current = [D]

State: null <── [A] <── [B] <── [C]     [D]─> null
                            previous

STEP 5: Reverse link [D]
next = null
current.setNext([C])   // [D]─> [C]─> [B]─> [A]─> null
previous = [D]
current = null

State: null <── [A] <── [B] <── [C] <── [D]
                                    previous

STEP 6: Swap front and rear
front = previous = [D]
rear = oldFront = [A]

AFTER:
front ──> [D]─> [C]─> [B]─> [A]─> null
                              ▲
rear ─────────────────────────┘
length = 4
```

---

### 16. removeMany(T key)

**Purpose**: Removes all occurrences of key.

```
BEFORE:
front ──> [B]─> [A]─> [B]─> [C]─> [B]─> null
length = 5
removeMany("B")

PHASE 1: Remove from front
  [B] at front?  ✓
  front = [A]
  length = 4

  [B] at front?  ✗ (now [A])
  Stop

State: [A]─> [B]─> [C]─> [B]─> null

PHASE 2: Remove from middle and end
  previous = [A]
  current = [B]

  Iteration 1: current = [B]
    "B" == "B"  ✓
    Remove: [A]─> [C]─> [B]─> null
    current = [C]
    length = 3

  Iteration 2: current = [C]
    "C" != "B"  ✗
    previous = [C]
    current = [B]

  Iteration 3: current = [B]
    "B" == "B"  ✓
    Remove: [A]─> [C]─> null
    current = null
    length = 2
    Update rear: rear = [C]

AFTER:
front ──> [A]─> [C]─> null
                  ▲
rear ─────────────┘
length = 2
```

---

## Node Movement Operations

### 17. combine(SingleList<T> left, SingleList<T> right)

**Purpose**: Alternately moves nodes from left and right into this.

```
BEFORE:
this:   front ──> null
        length = 0

left:   front ──> [A]─> [B]─> [C]─> null
        length = 3

right:  front ──> [X]─> [Y]─> null
        length = 2

combine(left, right)

ITERATION 1:
  Move from left: moveFrontToRear(left)
    this:   [A]─> null
    left:   [B]─> [C]─> null
    right:  [X]─> [Y]─> null

  Move from right: moveFrontToRear(right)
    this:   [A]─> [X]─> null
    left:   [B]─> [C]─> null
    right:  [Y]─> null

ITERATION 2:
  Move from left: moveFrontToRear(left)
    this:   [A]─> [X]─> [B]─> null
    left:   [C]─> null
    right:  [Y]─> null

  Move from right: moveFrontToRear(right)
    this:   [A]─> [X]─> [B]─> [Y]─> null
    left:   [C]─> null
    right:  null

ITERATION 3:
  Move from left: moveFrontToRear(left)
    this:   [A]─> [X]─> [B]─> [Y]─> [C]─> null
    left:   null
    right:  null

  Move from right: (skipped, right is empty)

AFTER:
this:   front ──> [A]─> [X]─> [B]─> [Y]─> [C]─> null
        length = 5

left:   front ──> null
        length = 0

right:  front ──> null
        length = 0
```

---

### 18. split(SingleList<T> left, SingleList<T> right)

**Purpose**: Splits this list in half. Left gets one more if odd length.

```
BEFORE:
this:   front ──> [A]─> [B]─> [C]─> [D]─> [E]─> null
        length = 5

left:   front ──> null
        length = 0

right:  front ──> null
        length = 0

split(left, right)

STEP 1: Calculate split point
splitPoint = (5 + 1) / 2 = 3
Move 3 nodes to left, 2 to right

STEP 2: Move first 3 nodes to left
  Move [A]: left = [A]─> null, this = [B]─> [C]─> [D]─> [E]─> null
  Move [B]: left = [A]─> [B]─> null, this = [C]─> [D]─> [E]─> null
  Move [C]: left = [A]─> [B]─> [C]─> null, this = [D]─> [E]─> null

STEP 3: Move remaining to right
  Move [D]: right = [D]─> null, this = [E]─> null
  Move [E]: right = [D]─> [E]─> null, this = null

AFTER:
this:   front ──> null
        length = 0

left:   front ──> [A]─> [B]─> [C]─> null
        length = 3

right:  front ──> [D]─> [E]─> null
        length = 2
```

#### Example: Even Length

```
BEFORE:
this:   front ──> [A]─> [B]─> [C]─> [D]─> null
        length = 4

splitPoint = (4 + 1) / 2 = 2

AFTER:
left:   [A]─> [B]─> null  (2 nodes)
right:  [C]─> [D]─> null  (2 nodes)
```

---

### 19. splitAlternate(SingleList<T> left, SingleList<T> right)

**Purpose**: Splits nodes alternately (opposite of combine).

```
BEFORE:
this:   front ──> [A]─> [B]─> [C]─> [D]─> [E]─> null
        length = 5

left:   front ──> null
        length = 0

right:  front ──> null
        length = 0

splitAlternate(left, right)

ITERATION 1: toLeft = true
  Move [A] to left
    left:  [A]─> null
    this:  [B]─> [C]─> [D]─> [E]─> null
  toLeft = false

ITERATION 2: toLeft = false
  Move [B] to right
    right: [B]─> null
    this:  [C]─> [D]─> [E]─> null
  toLeft = true

ITERATION 3: toLeft = true
  Move [C] to left
    left:  [A]─> [C]─> null
    this:  [D]─> [E]─> null
  toLeft = false

ITERATION 4: toLeft = false
  Move [D] to right
    right: [B]─> [D]─> null
    this:  [E]─> null
  toLeft = true

ITERATION 5: toLeft = true
  Move [E] to left
    left:  [A]─> [C]─> [E]─> null
    this:  null
  toLeft = false

AFTER:
this:   front ──> null
        length = 0

left:   front ──> [A]─> [C]─> [E]─> null
        length = 3

right:  front ──> [B]─> [D]─> null
        length = 2
```

---

## Set Operations

### 20. intersection(SingleList<T> left, SingleList<T> right)

**Purpose**: Creates intersection (elements in both lists).

```
BEFORE:
this:   front ──> [X]─> [Y]─> null
        length = 2

left:   front ──> [A]─> [B]─> [C]─> null
        length = 3

right:  front ──> [B]─> [C]─> [D]─> null
        length = 3

intersection(left, right)

STEP 1: Clear this
this:   front ──> null
        length = 0

STEP 2: Check each element in left
  Check [A]:
    right.contains("A")?  ✗
    Skip

  Check [B]:
    right.contains("B")?  ✓
    this.contains("B")?   ✗ (empty)
    Append "B"
    this: [B]─> null

  Check [C]:
    right.contains("C")?  ✓
    this.contains("C")?   ✗
    Append "C"
    this: [B]─> [C]─> null

AFTER:
this:   front ──> [B]─> [C]─> null
        length = 2

left:   front ──> [A]─> [B]─> [C]─> null  (unchanged)
        length = 3

right:  front ──> [B]─> [C]─> [D]─> null  (unchanged)
        length = 3
```

---

### 21. union(SingleList<T> left, SingleList<T> right)

**Purpose**: Creates union (elements in either list).

```
BEFORE:
this:   front ──> [X]─> [Y]─> null
        length = 2

left:   front ──> [A]─> [B]─> [C]─> null
        length = 3

right:  front ──> [B]─> [C]─> [D]─> null
        length = 3

union(left, right)

STEP 1: Clear this
this:   front ──> null
        length = 0

STEP 2: Copy unique elements from left
  [A]: this.contains("A")?  ✗  → Append "A"
    this: [A]─> null

  [B]: this.contains("B")?  ✗  → Append "B"
    this: [A]─> [B]─> null

  [C]: this.contains("C")?  ✗  → Append "C"
    this: [A]─> [B]─> [C]─> null

STEP 3: Copy unique elements from right
  [B]: this.contains("B")?  ✓  → Skip (already added)

  [C]: this.contains("C")?  ✓  → Skip (already added)

  [D]: this.contains("D")?  ✗  → Append "D"
    this: [A]─> [B]─> [C]─> [D]─> null

AFTER:
this:   front ──> [A]─> [B]─> [C]─> [D]─> null
        length = 4

left:   front ──> [A]─> [B]─> [C]─> null  (unchanged)
        length = 3

right:  front ──> [B]─> [C]─> [D]─> null  (unchanged)
        length = 3
```

---

## Helper Methods

### 22. linearSearch(T key)

**Purpose**: Private helper that finds the previous node of the node containing key.

```
BEFORE:
front ──> [A]─> [B]─> [C]─> null
linearSearch("B")

STEP 1: Initialize
previous = null
current = [A]

STEP 2: Check [A]
current.getDatum().compareTo("B") != 0
previous = [A]
current = [B]

STEP 3: Check [B]
current.getDatum().compareTo("B") == 0  ✓

RESULT: return previous = [A]

---

linearSearch("A")

STEP 1: Initialize
previous = null
current = [A]

STEP 2: Check [A]
current.getDatum().compareTo("A") == 0  ✓

RESULT: return previous = null
(Returns null when key is at front)

---

linearSearch("X")

STEP 1: Check [A] - not "X"
STEP 2: Check [B] - not "X"
STEP 3: Check [C] - not "X"
STEP 4: current = null

RESULT: return null
(Returns null when key not found)
```

---

## Summary of Time Complexities

| Method | Time Complexity | Notes |
|--------|----------------|-------|
| `append()` | O(1) | Direct access to rear |
| `prepend()` | O(1) | Direct access to front |
| `insert(int i, T)` | O(n) | May need to traverse to index |
| `remove(T)` | O(n) | Must search for key |
| `removeFront()` | O(1) | Direct access to front |
| `contains()` | O(n) | Linear search |
| `find()` | O(n) | Linear search |
| `count()` | O(n) | Traverse entire list |
| `index()` | O(n) | Linear search |
| `get(int n)` | O(n) | Traverse to index |
| `equals()` | O(n) | Compare all elements |
| `min()` / `max()` | O(n) | Traverse entire list |
| `clean()` | O(n²) | Nested loops |
| `reverse()` | O(n) | Traverse once |
| `removeMany()` | O(n) | Single pass |
| `combine()` | O(n+m) | Process all nodes |
| `split()` | O(n) | Process all nodes |
| `splitAlternate()` | O(n) | Process all nodes |
| `intersection()` | O(n*m) | Nested loops |
| `union()` | O(n*m) | Nested loops |
| `linearSearch()` | O(n) | Linear search |

---

## Key Patterns

### Pattern 1: Traversing the List
```java
SingleNode<T> current = this.front;
while (current != null) {
    // Process current node
    current = current.getNext();
}
```

### Pattern 2: Finding Previous Node
```java
SingleNode<T> previous = null;
SingleNode<T> current = this.front;
while (current != null) {
    if (/* condition */) {
        return previous;
    }
    previous = current;
    current = current.getNext();
}
```

### Pattern 3: Inserting After a Node
```java
newNode.setNext(previous.getNext());
previous.setNext(newNode);
```

### Pattern 4: Removing a Node
```java
previous.setNext(nodeToRemove.getNext());
// Update rear if necessary
if (previous.getNext() == null) {
    this.rear = previous;
}
```

### Pattern 5: Reversing Links
```java
SingleNode<T> previous = null;
SingleNode<T> current = this.front;
while (current != null) {
    SingleNode<T> next = current.getNext();
    current.setNext(previous);
    previous = current;
    current = next;
}
```

---

## Visual Notation Guide

- `[A]` = Node containing data "A"
- `─>` = Pointer to next node
- `null` = End of list / no next node
- `front` = Pointer to first node
- `rear` = Pointer to last node
- `current` = Current pointer during traversal
- `previous` = Pointer to previous node
- `newNode` = New node being added

---

*End of Visual Guide*

