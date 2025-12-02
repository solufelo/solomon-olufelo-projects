# What Exactly Is `datum`?

## Simple Answer

**`datum` is a VARIABLE that HOLDS the VALUE you pass into the `append()` method.**

Think of it like a box with a label "datum" - you put a value into the box, and the method uses whatever is inside.

---

## Breaking It Down

### Method Definition
```java
public void append(final T datum) {
    //                  ^^^^^
    //                  This is a PARAMETER (a variable that receives a value)
}
```

### Method Call
```java
list.append("D");
//          ^^^
//          This is the VALUE being passed in
```

### What Happens
1. You call `append("D")`
2. The value `"D"` gets stored in the variable `datum`
3. Inside the method, `datum` now contains `"D"`
4. The method uses `datum` to create a new node

---

## Visual Explanation

### Step 1: You Call the Method
```java
SingleList<String> list = new SingleList<String>();
list.append("D");
```

### Step 2: Value Goes Into the Parameter
```
Method Call:           append("D")
                            │
                            │ (value "D" is passed)
                            ▼
Method Definition:     append(final T datum)
                                      │
                                      │ (datum now contains "D")
                                      ▼
Inside Method:         datum = "D"
```

### Step 3: Method Uses `datum`
```java
public void append(final T datum) {
    // At this point: datum = "D"
    
    SingleNode<T> newNode = new SingleNode<T>(datum);
    //                                        ^^^^^
    //                                        Uses the value in datum (which is "D")
    //                                        So it creates: new SingleNode<T>("D")
}
```

---

## Concrete Examples

### Example 1: Adding "D"
```java
list.append("D");
```

**What happens:**
- `datum` = `"D"` (the string "D")
- A new node is created with `datum` as its value
- The node stores "D"

**Visual:**
```
Call: append("D")
           │
           ▼
datum ──> [ "D" ]
           │
           ▼
Creates: [Node with "D" inside]
```

### Example 2: Adding "Alice"
```java
list.append("Alice");
```

**What happens:**
- `datum` = `"Alice"` (the string "Alice")
- A new node is created with `datum` as its value
- The node stores "Alice"

**Visual:**
```
Call: append("Alice")
           │
           ▼
datum ──> [ "Alice" ]
           │
           ▼
Creates: [Node with "Alice" inside]
```

### Example 3: Adding the Number 42
```java
SingleList<Integer> numbers = new SingleList<Integer>();
numbers.append(42);
```

**What happens:**
- `datum` = `42` (the integer 42)
- A new node is created with `datum` as its value
- The node stores 42

**Visual:**
```
Call: append(42)
           │
           ▼
datum ──> [ 42 ]
           │
           ▼
Creates: [Node with 42 inside]
```

---

## ⚠️ IMPORTANT: Understanding Generics and Type Safety

### Your Questions Answered

#### Question 1: "Wouldn't the value be 42? Either key be datum or is datum the object class?"

**Answer:**
- **`datum`** is the **variable name** (the parameter)
- **`42`** is the **value** stored in `datum`
- **`Integer`** is the **type** of `datum` (because `T = Integer` for this list)

**Breakdown:**
```java
SingleList<Integer> numbers = new SingleList<Integer>();
//        ^^^^^^^^
//        This tells Java: T = Integer

// So when you call:
numbers.append(42);

// Inside the method:
public void append(final T datum) {
    //                    ^
    //                    T is Integer here!
    //                    So datum is of type Integer
    //                    datum = 42 (an Integer object)
}
```

#### Question 2: "Is datum the wrapper class? Or unboxing the item inside?"

**Answer:**
- **`datum` is of type `Integer`** (the wrapper class), not `int` (primitive)
- **Auto-boxing happens automatically** when you write `append(42)`
- Java automatically converts `42` (primitive `int`) → `Integer(42)` (wrapper object)

**What happens:**
```java
numbers.append(42);  // You write: primitive int

// Java automatically does:
numbers.append(new Integer(42));  // Converts to Integer object

// Inside method:
public void append(final T datum) {
    // datum is of type Integer (wrapper class)
    // No unboxing needed - we work with Integer objects
}
```

**Visual:**
```
You write:    append(42)           ← primitive int
                    │
                    │ (auto-boxing)
                    ▼
Java converts: append(Integer(42)) ← Integer object
                    │
                    ▼
datum receives: Integer(42)        ← datum is type Integer
```

#### Question 3: "Does Java handle everything as one generic type regardless of what's inside?"

**Answer:**
- **NO!** Each list instance has **ONE specific type**
- When you create `SingleList<String>`, `T = String` for that list
- When you create `SingleList<Integer>`, `T = Integer` for that list
- **You cannot mix types in the same list!**

**Example:**
```java
// List 1: T = String
SingleList<String> stringList = new SingleList<String>();
stringList.append("Alice");  // ✅ OK - String
stringList.append("Bob");    // ✅ OK - String
stringList.append(42);       // ❌ ERROR! Can't add Integer to String list

// List 2: T = Integer
SingleList<Integer> numberList = new SingleList<Integer>();
numberList.append(42);       // ✅ OK - Integer
numberList.append(100);      // ✅ OK - Integer
numberList.append("Alice");  // ❌ ERROR! Can't add String to Integer list
```

#### Question 4: "If we tried to compare 42 with Alice's value, would we get an error?"

**Answer:**
- **YES, you would get a COMPILE ERROR!**
- They are in **different list instances** with **different types**
- You **cannot compare** values from different list types
- Java's **type system prevents this** at compile time

**Why it fails:**
```java
SingleList<String> stringList = new SingleList<String>();
stringList.append("Alice");

SingleList<Integer> numberList = new SingleList<Integer>();
numberList.append(42);

// ❌ CANNOT COMPARE - Different types!
// stringList.get(0).compareTo(numberList.get(0));  // ERROR!

// ✅ CAN COMPARE - Same type!
stringList.append("Bob");
stringList.get(0).compareTo(stringList.get(1));  // OK - both Strings
```

---

## Detailed Explanation: How Generics Work

### Step 1: You Declare the Type When Creating the List

```java
SingleList<String> list1 = new SingleList<String>();
//        ^^^^^^
//        This is where you tell Java: T = String
```

**What Java does internally:**
- Java sees: `SingleList<String>`
- Java says: "Okay, for this list, `T = String`"
- Every time you use `T` in methods for this list, Java replaces it with `String`

### Step 2: The Type is "Baked In" to Each List Instance

```java
// List 1: T = String
SingleList<String> stringList = new SingleList<String>();
// For this list:
// - append(String datum)  ← T becomes String
// - datum is always type String
// - Can only store Strings

// List 2: T = Integer  
SingleList<Integer> numberList = new SingleList<Integer>();
// For this list:
// - append(Integer datum)  ← T becomes Integer
// - datum is always type Integer
// - Can only store Integers
```

**Visual:**
```
┌─────────────────────────────────────────┐
│ stringList (T = String)                 │
│                                         │
│ append(final String datum) {            │
│     // datum is always String           │
│     // Can only store "Alice", "Bob"    │
│ }                                       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ numberList (T = Integer)                │
│                                         │
│ append(final Integer datum) {           │
│     // datum is always Integer          │
│     // Can only store 42, 100, etc.     │
│ }                                       │
└─────────────────────────────────────────┘
```

### Step 3: Type Safety at Compile Time

Java checks types **before** your program runs:

```java
SingleList<String> list = new SingleList<String>();
list.append("Alice");  // ✅ Compiles - String matches T (String)
list.append(42);       // ❌ COMPILE ERROR - Integer doesn't match T (String)
```

**Error message you'd see:**
```
error: incompatible types: int cannot be converted to String
list.append(42);
            ^
```

---

## Boxing and Unboxing Explained

### Primitives vs Wrapper Classes

**Primitives** (lowercase): `int`, `double`, `char`, `boolean`
- Stored directly in memory
- Faster, use less memory
- Cannot be `null`

**Wrapper Classes** (capitalized): `Integer`, `Double`, `Character`, `Boolean`
- Objects that wrap primitives
- Can be `null`
- Required for generics (generics need objects, not primitives)

### Auto-Boxing (Primitive → Wrapper)

```java
SingleList<Integer> numbers = new SingleList<Integer>();

// You write:
numbers.append(42);  // primitive int

// Java automatically converts to:
numbers.append(new Integer(42));  // Integer object

// This is called "auto-boxing"
// Java "boxes" the primitive in a wrapper object
```

### Auto-Unboxing (Wrapper → Primitive)

```java
Integer number = new Integer(42);

// Auto-unboxing: Integer → int
int value = number;  // Java automatically extracts the int value

// Equivalent to:
int value = number.intValue();
```

### In Our Linked List

```java
SingleList<Integer> numbers = new SingleList<Integer>();
numbers.append(42);  // Auto-boxing: 42 (int) → Integer(42)

// Inside append method:
public void append(final T datum) {
    // datum is type Integer (wrapper class)
    // We store Integer objects in nodes, not int primitives
    SingleNode<T> newNode = new SingleNode<T>(datum);
    // newNode stores Integer(42), not int 42
}

// When you retrieve it:
Integer value = numbers.get(0);  // Gets Integer object
int primitive = value;  // Auto-unboxing: Integer → int
```

---

## Can You Compare 42 with "Alice"?

### ❌ NO - Different List Types

```java
SingleList<String> stringList = new SingleList<String>();
stringList.append("Alice");

SingleList<Integer> numberList = new SingleList<Integer>();
numberList.append(42);

// ❌ IMPOSSIBLE - They're in different lists with different types!
// You can't even try to compare them because:
// 1. They're in different list instances
// 2. One is String, one is Integer
// 3. Java's type system prevents mixing types
```

### ✅ YES - Same List Type

```java
SingleList<String> list = new SingleList<String>();
list.append("Alice");
list.append("Bob");

// ✅ OK - Both are Strings in the same list
String alice = list.get(0);
String bob = list.get(1);
int result = alice.compareTo(bob);  // Compares two Strings
```

### What About Comparing Within the List?

The `SingleList` class uses `compareTo()` for sorting:

```java
public class SingleList<T extends Comparable<T>> {
    //                          ^^^^^^^^^^^^^^^^
    //                          T must be a type that can be compared
    
    public void insert(final T datum) {
        // Uses datum.compareTo(other) to find insertion point
        // This only works because T extends Comparable<T>
    }
}
```

**This means:**
- `String` implements `Comparable<String>` ✅
- `Integer` implements `Comparable<Integer>` ✅
- You can compare Strings with Strings
- You can compare Integers with Integers
- **You CANNOT compare String with Integer** ❌

---

## Summary: Your Questions Answered

### Q1: "Wouldn't the value be 42?"
**A:** Yes! The **value** is `42`. `datum` is the **variable** that holds `42`.

### Q2: "Is datum the wrapper class or unboxing?"
**A:** `datum` is of type `Integer` (wrapper class). Auto-boxing converts `42` (int) → `Integer(42)` automatically.

### Q3: "Does Java handle everything as one generic type?"
**A:** No! Each list has **one specific type**. `SingleList<String>` can only hold Strings. `SingleList<Integer>` can only hold Integers.

### Q4: "Can we compare 42 with Alice?"
**A:** No! They're in **different list types**. Java prevents this with compile-time type checking. You can only compare values of the same type in the same list.

---

## Key Takeaways for Your Whiteboard

```
GENERICS AND TYPE SAFETY:
─────────────────────────

1. T is determined when you create the list:
   SingleList<String>  → T = String
   SingleList<Integer> → T = Integer

2. Each list instance has ONE type:
   - String list can only store Strings
   - Integer list can only store Integers
   - Cannot mix types!

3. datum is the variable, its TYPE is T:
   - In String list: datum is type String
   - In Integer list: datum is type Integer

4. Boxing happens automatically:
   append(42) → Java converts to Integer(42)

5. Type safety prevents errors:
   - Can't add Integer to String list
   - Can't compare String with Integer
   - Java checks at compile time
```

---

## Whiteboard Diagram: Complete Visual Explanation

```
┌─────────────────────────────────────────────────────────────────┐
│ UNDERSTANDING DATUM, TYPES, AND GENERICS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ 1. CREATING A LIST WITH A TYPE:                                │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ SingleList<String> list = new SingleList<String>();       │  │
│ │         ^^^^^^                                             │  │
│ │         This tells Java: T = String                        │  │
│ └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│ 2. WHAT IS DATUM?                                              │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ datum = VARIABLE NAME (parameter)                         │  │
│ │ "Alice" = VALUE (what you pass in)                        │  │
│ │ String = TYPE (determined by T)                           │  │
│ │                                                           │  │
│ │ list.append("Alice");                                     │  │
│ │            ^^^^^^^                                        │  │
│ │            Value "Alice" goes into variable datum         │  │
│ │                                                           │  │
│ │ Inside method:                                            │  │
│ │ datum = "Alice"  (variable contains value)                │  │
│ │ datum is type String  (because T = String)                │  │
│ └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│ 3. DIFFERENT LIST TYPES:                                       │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ List 1: SingleList<String>                                │  │
│ │   - T = String                                            │  │
│ │   - datum is type String                                  │  │
│ │   - Can only store: "Alice", "Bob", etc.                 │  │
│ │   - append("Alice") ✅                                    │  │
│ │   - append(42) ❌ ERROR!                                  │  │
│ │                                                           │  │
│ │ List 2: SingleList<Integer>                               │  │
│ │   - T = Integer                                           │  │
│ │   - datum is type Integer                                 │  │
│ │   - Can only store: 42, 100, etc.                        │  │
│ │   - append(42) ✅ (auto-boxed to Integer(42))            │  │
│ │   - append("Alice") ❌ ERROR!                             │  │
│ └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│ 4. BOXING AND UNBOXING:                                        │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ You write: append(42)  ← primitive int                    │  │
│ │                    │                                       │  │
│ │                    │ (auto-boxing)                        │  │
│ │                    ▼                                       │  │
│ │ Java converts: Integer(42)  ← Integer object              │  │
│ │                    │                                       │  │
│ │                    ▼                                       │  │
│ │ datum receives: Integer(42)                               │  │
│ │ datum is type Integer (wrapper class)                     │  │
│ │                                                           │  │
│ │ Note: Generics need objects, not primitives!             │  │
│ │ So Java automatically boxes primitives                    │  │
│ └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│ 5. CAN YOU COMPARE 42 WITH "Alice"?                            │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ ❌ NO! They're in DIFFERENT lists with DIFFERENT types:   │  │
│ │                                                           │  │
│ │ stringList (T = String)                                   │  │
│ │   - Contains: "Alice"                                     │  │
│ │                                                           │  │
│ │ numberList (T = Integer)                                  │  │
│ │   - Contains: 42                                          │  │
│ │                                                           │  │
│ │ ❌ Cannot compare - different types!                      │  │
│ │ ✅ Can only compare same type in same list                │  │
│ └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│ 6. KEY POINTS:                                                 │
│ ┌───────────────────────────────────────────────────────────┐  │
│ │ • datum = variable name (the "box")                       │  │
│ │ • Value = what you put in the box ("Alice", 42, etc.)    │  │
│ │ • Type = determined by T (String, Integer, etc.)          │  │
│ │ • Each list has ONE type (cannot mix!)                    │  │
│ │ • Auto-boxing: primitive → wrapper (automatic)            │  │
│ │ • Type safety: Java prevents mixing types (compile time)  │  │
│ └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│ DATUM QUICK REFERENCE                               │
├─────────────────────────────────────────────────────┤
│                                                     │
│ datum = VARIABLE (parameter name)                  │
│        ↓                                           │
│ Contains a VALUE (what you pass in)                │
│        ↓                                           │
│ Has a TYPE (determined by T when creating list)    │
│                                                     │
│ Example:                                            │
│   SingleList<String> list;                          │
│   list.append("Alice");                             │
│                                                     │
│   Inside method:                                    │
│   - datum = "Alice"  (value)                       │
│   - datum type = String  (because T = String)      │
│                                                     │
│ Example with numbers:                               │
│   SingleList<Integer> numbers;                      │
│   numbers.append(42);                               │
│                                                     │
│   Inside method:                                    │
│   - You write: 42 (primitive int)                  │
│   - Java auto-boxes: Integer(42)                   │
│   - datum = Integer(42)  (value)                   │
│   - datum type = Integer  (because T = Integer)    │
│                                                     │
│ Type Safety:                                        │
│   - String list → can only add Strings             │
│   - Integer list → can only add Integers           │
│   - Cannot mix types!                              │
│   - Cannot compare different types!                │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Understanding `datum` as a Variable

```
┌─────────────────────────────────────────────────────┐
│ METHOD CALL                                          │
│ list.append("D");                                    │
│           ^^^                                        │
│           This VALUE gets passed in                  │
└─────────────────────────────────────────────────────┘
                    │
                    │ (value travels)
                    ▼
┌─────────────────────────────────────────────────────┐
│ METHOD DEFINITION                                    │
│ public void append(final T datum) {                  │
│                      ^^^^^                           │
│                      This is a VARIABLE              │
│                      (like a box with a label)       │
│                                                      │
│  Inside the method:                                  │
│  datum = "D"  ← The value is now stored here        │
│                                                      │
│  SingleNode<T> newNode = new SingleNode<T>(datum);  │
│                                         ^^^^^        │
│                                         Uses the     │
│                                         value in     │
│                                         datum        │
└─────────────────────────────────────────────────────┘
```

---

## Key Points for Your Whiteboard

### 1. `datum` is a Parameter (Variable)
```
datum is like a mailbox or box labeled "datum"
- It HOLDS a value
- The value comes from the method call
- You can put different values in it
```

### 2. `datum` Gets Its Value from the Method Call
```
When you call:    append("D")
                  append("Alice")
                  append(42)

datum becomes:    "D"
                  "Alice"
                  42
```

### 3. `datum` is Used to Create the Node
```java
new SingleNode<T>(datum)
//                 ^^^^^
//                 Takes the value from datum
//                 and puts it in the node
```

---

## Detailed Whiteboard Layout

### Left Side: Method Call
```
┌──────────────────────┐
│  list.append("D");   │
│         ┌─────┐      │
│         │ "D" │      │  ← This is the VALUE
│         └─────┘      │
└──────────────────────┘
```

### Middle: The Parameter
```
┌──────────────────────┐
│  append(T datum)     │
│         ┌─────┐      │
│  datum: │ "D" │      │  ← datum is a VARIABLE
│         │     │      │     that HOLDS the value
│         └─────┘      │
└──────────────────────┘
```

### Right Side: Using datum
```
┌──────────────────────────────┐
│  new SingleNode<T>(datum)    │
│                   ┌─────┐    │
│                   │ "D" │    │  ← Uses value from datum
│                   └─────┘    │
│                              │
│  Creates:                    │
│  ┌─────────────┐             │
│  │ Node        │             │
│  │ datum: "D"  │             │
│  │ next: null  │             │
│  └─────────────┘             │
└──────────────────────────────┘
```

---

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: You write the method call                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  list.append("D");                                           │
│           ^^^                                                │
│           This is the VALUE you want to add                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ (Java passes the value)
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Method receives the value in the parameter           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  public void append(final T datum) {                         │
│                      ^^^^^                                   │
│                      PARAMETER: a variable that receives     │
│                                 the value                    │
│                                                              │
│  At this moment:                                             │
│  datum = "D"  ← The variable now contains "D"               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ (datum is used)
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Method uses datum to create a node                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  SingleNode<T> newNode = new SingleNode<T>(datum);          │
│                                         ^^^^^                │
│                                         Takes "D" from datum │
│                                                              │
│  Result: A new node is created with "D" stored inside        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Analogy: Function Parameter

Think of `datum` like a function in math:

### Math Function
```
f(x) = x + 5

When you call: f(3)
- x = 3 (x is the parameter, 3 is the value)
- Result: 3 + 5 = 8
```

### Java Method
```java
append(datum) {
    create node with datum
}

When you call: append("D")
- datum = "D" (datum is the parameter, "D" is the value)
- Result: node created with "D"
```

---

## Summary for Whiteboard

### `datum` Explained Simply

1. **What is it?**
   - `datum` is a **variable** (parameter)
   - It's like a box labeled "datum"

2. **What goes in it?**
   - The **value** you pass when calling `append()`
   - Example: `append("D")` → `datum = "D"`

3. **What is it used for?**
   - To create a new node with that value
   - `new SingleNode<T>(datum)` uses the value from `datum`

4. **Key Point:**
   - `datum` is the **variable name**
   - `"D"` is the **value** you put in it
   - They are **different things**!

---

## Whiteboard Cheat Sheet

```
┌─────────────────────────────────────────────┐
│ DATUM EXPLAINED                             │
├─────────────────────────────────────────────┤
│                                             │
│  datum = VARIABLE (parameter)               │
│         ↑                                   │
│         This is the NAME of the variable    │
│                                             │
│  "D" = VALUE                                │
│   ↑                                         │
│   This is what you PUT IN the variable      │
│                                             │
│  When you call: append("D")                 │
│  → datum gets the value "D"                 │
│  → datum = "D"                              │
│                                             │
│  The method uses datum to create:           │
│  new SingleNode<T>(datum)                   │
│  Which becomes:                             │
│  new SingleNode<T>("D")                     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Common Confusion

### ❌ Wrong Understanding
"datum equals D" - This makes it sound like `datum` IS "D"

### ✅ Correct Understanding
"datum contains 'D'" or "datum has the value 'D'" - `datum` is a variable that HOLDS the value "D"

### The Difference
- **Variable name**: `datum` (the label)
- **Variable value**: `"D"` (what's inside)
- They're different! Like:
  - Variable name: `myName`
  - Variable value: `"Solomon"`

---

## Final Whiteboard Summary

```
DATUM = PARAMETER (VARIABLE)

When you call: append("D")
                    │
                    ▼
datum receives the value "D"
    │
    ▼
datum = "D"  (the variable now contains "D")
    │
    ▼
new SingleNode<T>(datum)
                    │
                    ▼
new SingleNode<T>("D")  (creates node with "D")
```

**Remember:**
- `datum` = the variable (the box)
- `"D"` = the value (what's in the box)
- When you call `append("D")`, you're putting `"D"` into the `datum` box!

