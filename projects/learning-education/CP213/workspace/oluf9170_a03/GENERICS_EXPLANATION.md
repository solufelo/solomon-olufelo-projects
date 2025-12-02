# Understanding `T datum` in `append(final T datum)`

## Breaking Down the Method Signature

```java
public void append(final T datum)
```

### 1. `T` - Generic Type Parameter

- **`T`** is a **generic type** (also called a type parameter)
- It's declared at the class level: `public class SingleList<T extends Comparable<T>>`
- `T` can be **any type** that implements `Comparable<T>`
- Examples of `T`:
  - `String` (if you create `SingleList<String>`)
  - `Integer` (if you create `SingleList<Integer>`)
  - `Double` (if you create `SingleList<Double>`)
  - Any custom class that implements `Comparable<T>`

### 2. `datum` - Parameter Name

- **`datum`** is just the **name** of the parameter
- It means "data" or "item" (singular form of "data")
- You could call it anything: `item`, `value`, `data`, `element`, etc.
- This is the **actual value** you want to add to the list

### 3. `final` - Modifier

- **`final`** means the parameter **cannot be reassigned** inside the method
- It's a safety feature to prevent accidental changes
- The parameter value itself can't be changed (though if it's an object, the object's contents can be modified)

## Real-World Examples

### Example 1: List of Strings
```java
SingleList<String> nameList = new SingleList<String>();
nameList.append("Alice");  // T = String, datum = "Alice"
nameList.append("Bob");    // T = String, datum = "Bob"
```

In this case:
- `T` = `String`
- `datum` = `"Alice"` (the actual string value)

### Example 2: List of Integers
```java
SingleList<Integer> numberList = new SingleList<Integer>();
numberList.append(42);  // T = Integer, datum = 42
numberList.append(100); // T = Integer, datum = 100
```

In this case:
- `T` = `Integer`
- `datum` = `42` (the actual integer value)

### Example 3: List of Custom Objects
```java
// Assuming Person implements Comparable<Person>
SingleList<Person> personList = new SingleList<Person>();
Person alice = new Person("Alice", 25);
personList.append(alice);  // T = Person, datum = alice
```

In this case:
- `T` = `Person`
- `datum` = `alice` (the actual Person object)

## Visual Breakdown

```
public void append(final T datum)
          │      │   │  │    │
          │      │   │  │    └─ Parameter name: "datum"
          │      │   │  └────── Type: T (generic)
          │      │   └───────── Modifier: final (can't reassign)
          │      └───────────── Return type: void (returns nothing)
          └──────────────────── Method name: append
```

## Why Use Generics?

Generics allow you to create **one class** that works with **many different types**:

```java
// One class definition works for all these:
SingleList<String>    // Works with strings
SingleList<Integer>   // Works with integers
SingleList<Double>    // Works with doubles
SingleList<MyClass>   // Works with any comparable class
```

Without generics, you'd need separate classes:
- `SingleListString` for strings
- `SingleListInteger` for integers
- `SingleListDouble` for doubles
- etc. (lots of duplicate code!)

## Summary

- **`T`** = The type of data the list stores (generic/placeholder)
- **`datum`** = The actual item/value you're adding (parameter name)
- **`final`** = Can't reassign the parameter inside the method
- **`append`** = Method that adds the item to the end of the list

**In simple terms:** `append(final T datum)` means "add this item (datum) of type T to the end of the list"

