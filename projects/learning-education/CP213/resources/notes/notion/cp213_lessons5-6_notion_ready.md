# CP213 Lessons 5-6: Exam Prep Toolkit
**Midterm Date: October 25th**

---

## 📚 **FOUNDATION REVIEW: Lessons 1-4 Core Concepts**

### 🔹 **Variables & Data Types**

#### **Variable Declaration Components:**
- **Access modifier** (public, private, protected)
- **Field type** (int, String, double, etc.)
- **Field name** (identifier)

#### **Variable Types:**
- **Static fields**: One copy per class, shared across all instances
- **Instance variables**: Unique to each object instance
- **Local variables**: Temporary state inside methods
- **Parameter variables**: Method input parameters

#### **Primitive Data Types:**
| Type | Size | Range |
|------|------|-------|
| byte | 1 byte (8 bits) | -128 to 127 |
| short | 2 bytes (16 bits) | -32,768 to 32,767 |
| int | 4 bytes (32 bits) | -2³¹ to 2³¹-1 |
| long | 8 bytes (64 bits) | -2⁶³ to 2⁶³-1 |
| float | 4 bytes (32 bits) | ±3.4×10³⁸ |
| double | 8 bytes (64 bits) | ±1.7×10³⁰⁸ |
| char | 2 bytes (16 bits) | Unicode characters |
| boolean | 1 bit | true or false |

#### **Type Casting:**
- **Implicit (Widening)**: byte → short → int → long → float → double
- **Explicit (Narrowing)**: Requires `(type)` cast
- **Division**: `double result = x / (double)y;` preserves decimal
- **Truncation**: `(int)2.9` = 2 (not rounded)

#### **Default Initializations:**
- **boolean**: false
- **Numbers**: 0
- **char**: space character
- **Objects**: null
- **Local variables**: NOT initialized (programmer responsibility)

### 🔹 **Control Flow**

#### **Comparison Operators:**
- `==` (equal), `!=` (not equal)
- `>`, `>=`, `<`, `<=`
- **String comparison**: Use `.equals()`, not `==`

#### **Logical Operators:**
- `&&` (AND) - short-circuit evaluation
- `||` (OR) - short-circuit evaluation  
- `!` (NOT)

#### **If-Else Statements:**
```java
if (condition) {
    // code
} else if (condition2) {
    // code
} else {
    // code
}
```

#### **Switch Statement:**
```java
switch (expression) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
        break;
}
```

#### **Loops:**
- **while**: Condition checked before each iteration
- **do-while**: Executes at least once, condition checked after
- **for**: `for (init; condition; update) { }`
- **for-each**: `for (type var : collection) { }`

#### **Loop Control:**
- **break**: Exit loop immediately
- **continue**: Skip to next iteration
- **labeled break**: Exit outer loop from inner loop

### 🔹 **Methods & Constructors**

#### **Method Basics:**
- **Signature**: method name + parameter list
- **Overloading**: Same name, different parameters
- **Call-by-value**: Arguments are copied, not referenced

#### **Constructors:**
- **Purpose**: Initialize instance variables
- **Name**: Same as class name
- **No return type**
- **Overloading**: Multiple constructors with different parameters
- **Default constructor**: Provided if no constructors defined

### 🔹 **Input/Output & Formatting**

#### **Scanner Class:**
```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
String line = input.nextLine();
```

#### **Print Methods:**
- `System.out.print()` - no newline
- `System.out.println()` - adds newline
- `System.out.printf()` - formatted output

#### **Format Specifiers:**
- `%d` - integer
- `%f` - floating-point
- `%s` - string
- `%c` - character
- `%.2f` - 2 decimal places

#### **NumberFormat & Locale:**
```java
NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);
String formatted = currency.format(39.80); // $39.80
```

### 🔹 **Wrapper Classes**

#### **Autoboxing/Unboxing:**
```java
Integer i = 42;        // autoboxing
int j = i;             // unboxing
```

#### **Conversion Methods:**
- `Integer.parseInt("123")` → int
- `Double.parseDouble("3.14")` → double
- `String.valueOf(42)` → "42"

### 🔹 **Key Java Concepts**

#### **JVM & Compilation:**
- **javac**: Compiles .java to .class (bytecode)
- **JVM**: Executes bytecode
- **Platform independence**: Write once, run anywhere

#### **Memory Management:**
- **Stack**: Local variables, method parameters
- **Heap**: Objects, instance variables
- **Garbage Collection**: Automatic memory cleanup

#### **String Handling:**
- **String Pool**: Shared string literals
- **Immutability**: Strings cannot be changed
- **Methods**: `.equals()`, `.compareTo()`, `.charAt()`

---

## 📚 **Lesson 5: More on Classes, Class Design, and Parameters**

### 🔹 **1. Static Variables**
- **Definition**: Class variables that belong to the class itself, not to any specific instance
- **Key Points**:
  - There is exactly one copy of a static variable regardless of how many objects are created
  - Shared across all instances of the class
  - Can be accessed using class name: `ClassName.staticVariable`
  - Initialized when the class is first loaded

### 🔹 **2. Static Methods**
- **Definition**: Methods that belong to the class itself, not to any specific instance
- **Key Points**:
  - Can be called without creating an instance: `ClassName.staticMethod()`
  - Cannot access instance variables directly (no `this` reference)
  - Can only access static variables and other static methods
  - Common examples: `Math.sqrt()`, `Integer.parseInt()`

### 🔹 **3. The Math and Character Classes**
- **Math Class**: Provides mathematical functions and constants
  - `Math.PI`, `Math.E` (constants)
  - `Math.sqrt()`, `Math.pow()`, `Math.abs()`, `Math.max()`, `Math.min()`
  - `Math.random()` (returns 0.0 to 1.0)
- **Character Class**: Provides methods for character manipulation
  - `Character.isLetter()`, `Character.isDigit()`, `Character.isUpperCase()`
  - `Character.toLowerCase()`, `Character.toUpperCase()`

### 🔹 **4. Variables in Computer Memory**
- **Stack Memory**: Stores local variables and method parameters
- **Heap Memory**: Stores objects and instance variables
- **Primitive Types**: Stored directly in memory (value semantics)
- **Reference Types**: Store memory address pointing to object (reference semantics)

### 🔹 **5. References in Computer Memory**
- **Reference Variables**: Hold memory addresses, not the actual object
- **Assignment**: `obj1 = obj2` copies the reference, not the object
- **Multiple References**: Multiple variables can reference the same object
- **Garbage Collection**: Objects become eligible when no references point to them

### 🔹 **6. Class Parameters**
- **Pass by Value**: Java always passes parameters by value
- **Primitive Parameters**: Copy of the value is passed
- **Reference Parameters**: Copy of the reference is passed
- **Immutability**: Cannot change what the parameter references, but can modify the object

### 🔹 **7. Use of = and == with Class Type Variables**
- **Assignment (=)**: 
  - `obj1 = obj2` makes both variables reference the same object
  - Changes to object through one reference affect the other
- **Equality (==)**:
  - Compares memory addresses, not object contents
  - Use `.equals()` method to compare object contents
  - `obj1 == obj2` checks if they reference the same object

### 🔹 **8. Keywords: null and Null Pointer Exception**
- **null**: Special value indicating no object reference
- **NullPointerException**: Runtime error when trying to use null reference
- **Prevention**: Always check for null before using object references
- **Common Causes**: Uninitialized reference variables, method returns null

### 🔹 **9. Anonymous Classes**
- **Definition**: Classes without names, defined and instantiated simultaneously
- **Syntax**: `new ClassName() { /* class body */ }`
- **Use Cases**: Event handlers, one-time implementations
- **Limitations**: Cannot have constructors, limited to single use

### 🔹 **10. Lambda Expressions**
- **Definition**: Concise way to represent anonymous functions
- **Syntax**: `(parameters) -> expression` or `(parameters) -> { statements }`
- **Use Cases**: Functional interfaces, collections processing
- **Benefits**: Reduces boilerplate code, improves readability

### 🔹 **11. Class Design and Privacy Leak**
- **Privacy Leak**: When private data becomes accessible outside the class
- **Common Causes**: Returning references to private objects
- **Prevention**: Return copies of objects, not references
- **Class Invariant**: Statement always true for every object of the class

### 🔹 **12. Copy Constructors**
- **Definition**: Constructor that creates new object by copying another
- **Purpose**: Create independent copies of objects
- **Deep vs Shallow Copy**: Deep copy copies all referenced objects too
- **Implementation**: `public ClassName(ClassName other) { /* copy logic */ }`

### 🔹 **13. Privacy Leaks Prevention**
- **Defensive Copying**: Return copies instead of original references
- **Immutable Objects**: Objects that cannot be modified after creation
- **Getter Methods**: Should return copies of mutable objects
- **Validation**: Check parameters in constructors and setters

---

## 📚 **Lesson 6: Arrays, ArrayList, Enumeration and Multi-Dimensional Arrays**

### 🔹 **1. Introduction to Arrays**
- **Definition**: Collection of elements of the same type
- **Fixed Size**: Array size cannot be changed after creation
- **Indexed Access**: Elements accessed using index (0-based)
- **Memory**: Contiguous memory allocation

### 🔹 **2. Creating and Accessing Arrays**
- **Declaration**: `type[] arrayName;` or `type arrayName[];`
- **Creation**: `arrayName = new type[size];`
- **Combined**: `type[] arrayName = new type[size];`
- **Initialization**: `type[] arrayName = {value1, value2, ...};`
- **Access**: `arrayName[index]`

### 🔹 **3. Arrays and References**
- **Array Variables**: Hold references to array objects
- **Assignment**: `arr1 = arr2` makes both reference the same array
- **Length Property**: `arrayName.length` gives array size
- **Bounds Checking**: Java checks array bounds at runtime

### 🔹 **4. Arguments for the Method main**
- **Command Line Arguments**: `public static void main(String[] args)`
- **args Array**: Contains command line arguments as strings
- **Indexing**: `args[0]` is first argument, `args[1]` is second, etc.
- **Length**: `args.length` gives number of arguments

### 🔹 **5. Partially Filled Arrays**
- **Concept**: Arrays that are not completely filled
- **Tracking**: Use separate variable to track actual number of elements
- **Operations**: Add, remove, search elements
- **Efficiency**: Better than ArrayList for fixed-size scenarios

### 🔹 **6. ArrayList**
- **Definition**: Dynamic array that can grow and shrink
- **Import**: `import java.util.ArrayList;`
- **Creation**: `ArrayList<Type> list = new ArrayList<>();`
- **Methods**:
  - `add(element)` - adds element to end
  - `add(index, element)` - adds element at specific index
  - `get(index)` - retrieves element at index
  - `set(index, element)` - replaces element at index
  - `remove(index)` - removes element at index
  - `size()` - returns number of elements
  - `clear()` - removes all elements

### 🔹 **7. Variable Arguments (Varargs)**
- **Definition**: Method parameter that accepts variable number of arguments
- **Syntax**: `methodName(Type... parameterName)`
- **Usage**: Arguments are treated as array inside method
- **Limitations**: Only one varargs parameter per method, must be last parameter

### 🔹 **8. Enumerated Types (Enums)**
- **Definition**: Special class representing group of constants
- **Syntax**: `enum EnumName { VALUE1, VALUE2, VALUE3 }`
- **Usage**: `EnumName.VALUE1`
- **Methods**: `values()`, `valueOf()`, `ordinal()`
- **Benefits**: Type safety, prevents invalid values

### 🔹 **9. Multidimensional Arrays**
- **Definition**: Arrays with more than one index
- **Declaration**: `type[][] arrayName;`
- **Creation**: `arrayName = new type[rows][columns];`
- **Access**: `arrayName[row][column]`
- **Visualization**: First index = row, second index = column

#### **9.1 Using the length Instance Variable**
- **Row Length**: `arrayName.length` gives number of rows
- **Column Length**: `arrayName[row].length` gives number of columns in that row
- **Nested Loops**: Use for processing 2D arrays

#### **9.2 Ragged Arrays**
- **Definition**: 2D arrays where rows have different lengths
- **Creation**: Create rows separately with different sizes
- **Use Cases**: When data naturally has varying row lengths
- **Access**: Same as regular 2D arrays

#### **9.3 Multidimensional Array Parameters and Return Values**
- **Parameters**: `methodName(type[][] parameter)`
- **Return Types**: `type[][] methodName()`
- **Usage**: Same syntax as 1D arrays but with multiple brackets

---

## 🎯 **Midterm Exam Focus Areas**

### **High Priority Topics:**
1. **Static vs Instance** - Know when to use static methods/variables
2. **Memory Management** - References, null, garbage collection
3. **Array Operations** - Creation, access, bounds checking
4. **ArrayList Methods** - add, get, set, remove, size
5. **Privacy Leaks** - How to prevent, defensive copying
6. **Class Design** - Constructors, equals, toString methods

### **Medium Priority Topics:**
1. **Lambda Expressions** - Basic syntax and usage
2. **Multidimensional Arrays** - 2D array operations
3. **Enums** - Basic enum creation and usage
4. **Math/Character Classes** - Common static methods

### **Practice Problems to Master:**
1. Create a class with static and instance variables
2. Implement defensive copying in getter methods
3. Write methods that work with 2D arrays
4. Use ArrayList to store and manipulate data
5. Handle null references safely
6. Implement equals and toString methods

---

## 📝 **Quick Reference Cheat Sheet**

### **Static Keywords:**
```java
static int count = 0;           // Static variable
public static void method() {}  // Static method
ClassName.staticVariable;       // Access static variable
ClassName.staticMethod();       // Call static method
```

### **Array Essentials:**
```java
int[] arr = new int[10];        // Create array
arr[0] = 5;                     // Access element
int len = arr.length;           // Get length
int[][] matrix = new int[3][4]; // 2D array
```

### **ArrayList Essentials:**
```java
ArrayList<String> list = new ArrayList<>();
list.add("item");               // Add element
String item = list.get(0);      // Get element
list.set(0, "new");             // Set element
list.remove(0);                 // Remove element
int size = list.size();         // Get size
```

### **Null Safety:**
```java
if (obj != null) {              // Check for null
    obj.method();               // Safe to use
}
```

---

**Good luck with your midterm on October 25th! 🍀**
