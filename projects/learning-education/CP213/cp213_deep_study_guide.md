# CP213 Deep Study Guide: Object-Oriented Programming
**Midterm Date: October 25th** | **Comprehensive Exam Preparation**

---

## 📚 **STUDY METHODOLOGY**

### **How to Use This Guide:**
1. **Read & Understand**: Go through each concept thoroughly
2. **Code Examples**: Type out and run all code examples
3. **Practice Problems**: Complete all exercises
4. **Self-Test**: Answer all review questions
5. **Create Your Own**: Write additional examples for each concept

### **Study Schedule (3 Weeks to Midterm):**
- **Week 1**: Foundation concepts (Variables, Control Flow, Methods)
- **Week 2**: Advanced topics (Static, Memory, Arrays)
- **Week 3**: Integration, practice problems, mock exams

---

## 🏗️ **FOUNDATION CONCEPTS (Lessons 1-4)**

### **1. VARIABLES & DATA TYPES**

#### **1.1 Variable Declaration Deep Dive**

**Core Components:**
```java
[access_modifier] [static] [final] type variable_name [= initial_value];
```

**Detailed Breakdown:**
- **Access Modifier**: Controls visibility (`public`, `private`, `protected`, package-private)
- **Static**: Makes variable belong to class, not instance
- **Final**: Makes variable constant (cannot be changed)
- **Type**: Data type (primitive or class)
- **Name**: Identifier following Java naming conventions
- **Initial Value**: Optional initialization

**Practice Exercise:**
```java
public class VariablePractice {
    // Instance variables
    private String name;
    public int age;
    protected double salary;
    
    // Static variables
    public static int totalEmployees = 0;
    private static final String COMPANY_NAME = "TechCorp";
    
    // Local variables (inside methods)
    public void calculateBonus() {
        double bonusRate = 0.1;  // Local variable
        double bonus = salary * bonusRate;
        System.out.println("Bonus: $" + bonus);
    }
}
```

**Self-Test Questions:**
1. What's the difference between `public static int count` and `private int count`?
2. When would you use `final` with a variable?
3. What happens if you don't initialize a local variable?

#### **1.2 Primitive Data Types Deep Analysis**

**Memory Layout & Precision:**

| Type | Size | Range | Precision | Use Case |
|------|------|-------|-----------|----------|
| `byte` | 1 byte | -128 to 127 | Exact | Small integers, file I/O |
| `short` | 2 bytes | -32,768 to 32,767 | Exact | Medium integers, arrays |
| `int` | 4 bytes | -2³¹ to 2³¹-1 | Exact | General purpose integers |
| `long` | 8 bytes | -2⁶³ to 2⁶³-1 | Exact | Large integers, timestamps |
| `float` | 4 bytes | ±3.4×10³⁸ | ~7 digits | Approximate decimals |
| `double` | 8 bytes | ±1.7×10³⁰⁸ | ~15 digits | Precise decimals |
| `char` | 2 bytes | 0 to 65,535 | Unicode | Single characters |
| `boolean` | 1 bit | true/false | Exact | Logical values |

**Deep Dive Example:**
```java
public class DataTypeAnalysis {
    public static void main(String[] args) {
        // Integer overflow demonstration
        int maxInt = Integer.MAX_VALUE;
        System.out.println("Max int: " + maxInt);
        System.out.println("Max int + 1: " + (maxInt + 1)); // Overflow!
        
        // Floating point precision issues
        double a = 0.1;
        double b = 0.2;
        double sum = a + b;
        System.out.println("0.1 + 0.2 = " + sum); // Not exactly 0.3!
        
        // Character and Unicode
        char unicodeChar = '\u0041'; // 'A'
        System.out.println("Unicode 0041: " + unicodeChar);
        
        // Boolean operations
        boolean flag1 = true;
        boolean flag2 = false;
        System.out.println("flag1 && flag2: " + (flag1 && flag2));
        System.out.println("flag1 || flag2: " + (flag1 || flag2));
    }
}
```

**Critical Understanding Points:**
1. **Integer Overflow**: What happens when you exceed the range?
2. **Floating Point Precision**: Why doesn't 0.1 + 0.2 = 0.3?
3. **Unicode**: How characters are represented internally
4. **Boolean Logic**: Short-circuit evaluation implications

#### **1.3 Type Casting Deep Analysis**

**Implicit vs Explicit Casting:**

```java
public class TypeCastingDeep {
    public static void main(String[] args) {
        // Implicit casting (widening) - safe
        byte b = 100;
        short s = b;        // byte → short
        int i = s;          // short → int
        long l = i;         // int → long
        float f = l;        // long → float
        double d = f;       // float → double
        
        // Explicit casting (narrowing) - potentially dangerous
        double pi = 3.14159;
        int truncated = (int) pi;  // 3 (truncated, not rounded)
        
        // Data loss examples
        long bigNumber = 3000000000L;
        int smallInt = (int) bigNumber;  // Data loss!
        System.out.println("Original: " + bigNumber);
        System.out.println("Casted: " + smallInt);
        
        // Division and casting
        int x = 5, y = 2;
        double result1 = x / y;           // 2.0 (integer division)
        double result2 = x / (double) y;  // 2.5 (floating division)
        
        System.out.println("Integer division: " + result1);
        System.out.println("Floating division: " + result2);
    }
}
```

**Advanced Casting Scenarios:**
```java
// Object casting (will be covered in inheritance)
Object obj = "Hello";
String str = (String) obj;  // Safe cast

// Class casting
Number num = new Integer(42);
Integer intVal = (Integer) num;  // Safe cast
```

### **2. CONTROL FLOW DEEP DIVE**

#### **2.1 Boolean Expressions & Logic**

**Truth Tables & Logical Operations:**

| A | B | A && B | A \|\| B | !A |
|---|---|--------|----------|-----|
| T | T | T      | T        | F  |
| T | F | F      | T        | F  |
| F | T | F      | T        | T  |
| F | F | F      | F        | T  |

**Short-Circuit Evaluation Deep Dive:**
```java
public class ShortCircuitAnalysis {
    public static void main(String[] args) {
        int x = 0;
        
        // Short-circuit AND: stops at first false
        if (x != 0 && 10 / x > 5) {  // Safe! Division never happens
            System.out.println("This won't execute");
        }
        
        // Short-circuit OR: stops at first true
        if (x == 0 || 10 / x > 5) {  // Safe! Division never happens
            System.out.println("This will execute");
        }
        
        // Non-short-circuit operators (& and |)
        if (x != 0 & 10 / x > 5) {   // DANGEROUS! Division always happens
            System.out.println("This will crash!");
        }
    }
}
```

**Complex Boolean Expressions:**
```java
public class ComplexBoolean {
    public static void main(String[] args) {
        int age = 25;
        boolean hasLicense = true;
        boolean hasInsurance = false;
        double income = 45000;
        
        // Complex condition with proper precedence
        boolean canDrive = (age >= 18) && hasLicense && (hasInsurance || income > 50000);
        
        // Equivalent with explicit parentheses
        boolean canDrive2 = ((age >= 18) && hasLicense) && (hasInsurance || (income > 50000));
        
        System.out.println("Can drive: " + canDrive);
    }
}
```

#### **2.2 If-Else Statements Deep Analysis**

**Nested Conditions & Best Practices:**
```java
public class IfElseDeep {
    public static void main(String[] args) {
        int score = 85;
        boolean isBonus = true;
        
        // Nested if-else (can be complex)
        if (score >= 90) {
            if (isBonus) {
                System.out.println("Grade: A+ with bonus");
            } else {
                System.out.println("Grade: A");
            }
        } else if (score >= 80) {
            if (isBonus) {
                System.out.println("Grade: B+ with bonus");
            } else {
                System.out.println("Grade: B");
            }
        } else if (score >= 70) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }
        
        // Alternative: Early returns (cleaner code)
        String grade = calculateGrade(score, isBonus);
        System.out.println("Grade: " + grade);
    }
    
    public static String calculateGrade(int score, boolean isBonus) {
        if (score >= 90) {
            return isBonus ? "A+ with bonus" : "A";
        }
        if (score >= 80) {
            return isBonus ? "B+ with bonus" : "B";
        }
        if (score >= 70) {
            return "C";
        }
        return "F";
    }
}
```

**Ternary Operator Deep Dive:**
```java
public class TernaryDeep {
    public static void main(String[] args) {
        int a = 10, b = 20;
        
        // Simple ternary
        int max = (a > b) ? a : b;
        
        // Nested ternary (use sparingly!)
        String result = (a > b) ? "A is greater" : 
                       (a < b) ? "B is greater" : "Equal";
        
        // Complex ternary with method calls
        String message = (a > 0) ? 
            "Positive: " + Math.sqrt(a) : 
            "Non-positive: " + Math.abs(a);
        
        System.out.println("Max: " + max);
        System.out.println("Result: " + result);
        System.out.println("Message: " + message);
    }
}
```

#### **2.3 Switch Statements Deep Analysis**

**Advanced Switch Features:**
```java
public class SwitchDeep {
    public static void main(String[] args) {
        String day = "MONDAY";
        
        // Traditional switch with fall-through
        switch (day) {
            case "MONDAY":
            case "TUESDAY":
            case "WEDNESDAY":
            case "THURSDAY":
            case "FRIDAY":
                System.out.println("Weekday");
                break;
            case "SATURDAY":
            case "SUNDAY":
                System.out.println("Weekend");
                break;
            default:
                System.out.println("Invalid day");
        }
        
        // Switch with expressions (Java 14+)
        String dayType = switch (day) {
            case "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY" -> "Weekday";
            case "SATURDAY", "SUNDAY" -> "Weekend";
            default -> "Invalid";
        };
        
        System.out.println("Day type: " + dayType);
    }
}
```

**Switch with Different Types:**
```java
public class SwitchTypes {
    public static void main(String[] args) {
        // Integer switch
        int month = 3;
        String season = switch (month) {
            case 12, 1, 2 -> "Winter";
            case 3, 4, 5 -> "Spring";
            case 6, 7, 8 -> "Summer";
            case 9, 10, 11 -> "Fall";
            default -> "Invalid month";
        };
        
        // Character switch
        char grade = 'B';
        String description = switch (grade) {
            case 'A' -> "Excellent";
            case 'B' -> "Good";
            case 'C' -> "Average";
            case 'D' -> "Below Average";
            case 'F' -> "Fail";
            default -> "Invalid grade";
        };
        
        System.out.println("Season: " + season);
        System.out.println("Description: " + description);
    }
}
```

#### **2.4 Loops Deep Analysis**

**While Loop Deep Dive:**
```java
public class WhileLoopDeep {
    public static void main(String[] args) {
        // Basic while loop
        int count = 0;
        while (count < 5) {
            System.out.println("Count: " + count);
            count++;
        }
        
        // While loop with complex condition
        int number = 12345;
        int digitCount = 0;
        while (number > 0) {
            digitCount++;
            number /= 10;  // Remove last digit
        }
        System.out.println("Number of digits: " + digitCount);
        
        // Infinite loop with break
        int sum = 0;
        int value = 1;
        while (true) {
            sum += value;
            value++;
            if (sum > 100) {
                break;  // Exit loop
            }
        }
        System.out.println("Sum: " + sum);
    }
}
```

**For Loop Deep Dive:**
```java
public class ForLoopDeep {
    public static void main(String[] args) {
        // Standard for loop
        for (int i = 0; i < 5; i++) {
            System.out.println("i: " + i);
        }
        
        // Multiple variables in for loop
        for (int i = 0, j = 10; i < j; i++, j--) {
            System.out.println("i: " + i + ", j: " + j);
        }
        
        // For loop with complex initialization
        for (int i = 1, factorial = 1; i <= 5; i++) {
            factorial *= i;
            System.out.println(i + "! = " + factorial);
        }
        
        // Nested for loops
        for (int row = 1; row <= 3; row++) {
            for (int col = 1; col <= 3; col++) {
                System.out.print("(" + row + "," + col + ") ");
            }
            System.out.println();
        }
    }
}
```

**Enhanced For Loop (For-Each) Deep Dive:**
```java
public class ForEachDeep {
    public static void main(String[] args) {
        // Array iteration
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum: " + sum);
        
        // String iteration
        String text = "Hello";
        for (char c : text.toCharArray()) {
            System.out.println("Character: " + c);
        }
        
        // Limitations of for-each
        int[] arr = {1, 2, 3, 4, 5};
        // Cannot modify elements directly
        for (int num : arr) {
            num *= 2;  // This doesn't modify the array!
        }
        
        // Use traditional for loop for modification
        for (int i = 0; i < arr.length; i++) {
            arr[i] *= 2;  // This modifies the array
        }
    }
}
```

### **3. METHODS DEEP DIVE**

#### **3.1 Method Design & Best Practices**

**Method Signature Deep Analysis:**
```java
public class MethodDesign {
    // Method signature: access_modifier static final return_type method_name(parameters) throws exceptions
    public static final double calculateArea(double length, double width) throws IllegalArgumentException {
        if (length <= 0 || width <= 0) {
            throw new IllegalArgumentException("Length and width must be positive");
        }
        return length * width;
    }
    
    // Method overloading examples
    public static int add(int a, int b) {
        return a + b;
    }
    
    public static double add(double a, double b) {
        return a + b;
    }
    
    public static int add(int a, int b, int c) {
        return a + b + c;
    }
    
    // Varargs method
    public static int sum(int... numbers) {
        int total = 0;
        for (int num : numbers) {
            total += num;
        }
        return total;
    }
}
```

**Parameter Passing Deep Dive:**
```java
public class ParameterPassing {
    public static void main(String[] args) {
        // Primitive parameters
        int x = 10;
        modifyPrimitive(x);
        System.out.println("x after method call: " + x); // Still 10
        
        // Reference parameters
        int[] arr = {1, 2, 3};
        modifyArray(arr);
        System.out.println("arr[0] after method call: " + arr[0]); // Now 100
        
        // String parameters (special case)
        String str = "Hello";
        modifyString(str);
        System.out.println("str after method call: " + str); // Still "Hello"
    }
    
    public static void modifyPrimitive(int value) {
        value = 100;  // Doesn't affect original
    }
    
    public static void modifyArray(int[] array) {
        array[0] = 100;  // Affects original array
    }
    
    public static void modifyString(String text) {
        text = "Modified";  // Doesn't affect original (strings are immutable)
    }
}
```

#### **3.2 Method Overloading Deep Analysis**

**Overloading Resolution:**
```java
public class OverloadingDeep {
    // Exact match
    public static void method(int x) {
        System.out.println("int: " + x);
    }
    
    // Widening conversion
    public static void method(long x) {
        System.out.println("long: " + x);
    }
    
    // Boxing conversion
    public static void method(Integer x) {
        System.out.println("Integer: " + x);
    }
    
    // Varargs
    public static void method(int... x) {
        System.out.println("varargs: " + Arrays.toString(x));
    }
    
    public static void main(String[] args) {
        method(5);        // Calls method(int)
        method(5L);       // Calls method(long)
        method(new Integer(5)); // Calls method(Integer)
        method(1, 2, 3);  // Calls method(int...)
    }
}
```

### **4. CONSTRUCTORS DEEP DIVE**

#### **4.1 Constructor Design Patterns**

**Constructor Chaining:**
```java
public class ConstructorChaining {
    private String name;
    private int age;
    private String email;
    
    // Default constructor
    public ConstructorChaining() {
        this("Unknown", 0, "unknown@email.com");
    }
    
    // Two-parameter constructor
    public ConstructorChaining(String name, int age) {
        this(name, age, "unknown@email.com");
    }
    
    // Full constructor
    public ConstructorChaining(String name, int age, String email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
    
    // Copy constructor
    public ConstructorChaining(ConstructorChaining other) {
        this(other.name, other.age, other.email);
    }
}
```

**Constructor Best Practices:**
```java
public class ConstructorBestPractices {
    private final String name;  // Immutable field
    private final int id;
    private static int nextId = 1;
    
    // Private constructor for factory methods
    private ConstructorBestPractices(String name, int id) {
        this.name = name;
        this.id = id;
    }
    
    // Factory method
    public static ConstructorBestPractices create(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be null or empty");
        }
        return new ConstructorBestPractices(name, nextId++);
    }
    
    // Builder pattern
    public static class Builder {
        private String name;
        private int id = nextId++;
        
        public Builder name(String name) {
            this.name = name;
            return this;
        }
        
        public ConstructorBestPractices build() {
            if (name == null) {
                throw new IllegalStateException("Name is required");
            }
            return new ConstructorBestPractices(name, id);
        }
    }
}
```

---

## 🚀 **ADVANCED CONCEPTS (Lessons 5-6)**

### **5. STATIC CONCEPTS DEEP DIVE**

#### **5.1 Static Variables Deep Analysis**

**Static vs Instance Variables:**
```java
public class StaticDeep {
    // Instance variables - each object has its own copy
    private String name;
    private int instanceCount = 0;
    
    // Static variables - shared across all instances
    private static int totalInstances = 0;
    private static final String CLASS_NAME = "StaticDeep";
    
    public StaticDeep(String name) {
        this.name = name;
        instanceCount++;
        totalInstances++;
    }
    
    // Instance method - can access both instance and static variables
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Instance count: " + instanceCount);
        System.out.println("Total instances: " + totalInstances);
    }
    
    // Static method - can only access static variables
    public static void displayClassInfo() {
        System.out.println("Class: " + CLASS_NAME);
        System.out.println("Total instances created: " + totalInstances);
        // System.out.println("Name: " + name); // ERROR! Cannot access instance variable
    }
    
    public static void main(String[] args) {
        StaticDeep obj1 = new StaticDeep("Alice");
        StaticDeep obj2 = new StaticDeep("Bob");
        
        obj1.displayInfo();
        obj2.displayInfo();
        StaticDeep.displayClassInfo();
    }
}
```

**Static Initialization Blocks:**
```java
public class StaticInitialization {
    // Static variables
    private static int[] numbers;
    private static String message;
    
    // Static initialization block
    static {
        System.out.println("Static block 1 executing...");
        numbers = new int[10];
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = i * i;
        }
    }
    
    // Another static block
    static {
        System.out.println("Static block 2 executing...");
        message = "Static initialization complete";
    }
    
    public static void main(String[] args) {
        System.out.println("Main method executing...");
        System.out.println("Message: " + message);
        System.out.println("Numbers: " + Arrays.toString(numbers));
    }
}
```

#### **5.2 Static Methods Deep Analysis**

**When to Use Static Methods:**
```java
public class StaticMethodsDeep {
    // Utility methods - good candidates for static
    public static double calculateDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }
    
    public static boolean isPrime(int number) {
        if (number < 2) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
    
    // Factory methods - good candidates for static
    public static StaticMethodsDeep createFromString(String data) {
        // Parse string and create object
        return new StaticMethodsDeep();
    }
    
    // Methods that don't need instance state
    public static String formatCurrency(double amount) {
        return String.format("$%.2f", amount);
    }
    
    // Constants and configuration
    private static final double PI = 3.14159;
    public static double calculateCircleArea(double radius) {
        return PI * radius * radius;
    }
}
```

### **6. MEMORY MANAGEMENT DEEP DIVE**

#### **6.1 Stack vs Heap Deep Analysis**

**Memory Layout Visualization:**
```java
public class MemoryDeep {
    // Instance variables stored in heap
    private String name;
    private int[] numbers;
    
    public MemoryDeep(String name) {
        this.name = name;  // Reference stored in heap
        this.numbers = new int[1000];  // Array object in heap
    }
    
    public void methodWithLocalVariables() {
        // Local variables stored in stack
        int localVar = 42;
        String localString = "Hello";
        int[] localArray = new int[10];  // Array object in heap, reference in stack
        
        // Method parameters also in stack
        processData(localVar, localString, localArray);
    }
    
    private void processData(int param1, String param2, int[] param3) {
        // Parameters are copies in stack
        param1 = 100;  // Doesn't affect original
        param2 = "Modified";  // Doesn't affect original
        param3[0] = 999;  // Affects original array!
    }
}
```

**Garbage Collection Deep Dive:**
```java
public class GarbageCollectionDeep {
    public static void main(String[] args) {
        // Object creation and reference management
        String str1 = new String("Hello");
        String str2 = str1;  // Both reference same object
        
        str1 = null;  // str1 no longer references object
        // Object still exists because str2 references it
        
        str2 = null;  // Now object is eligible for garbage collection
        
        // Memory-intensive operations
        for (int i = 0; i < 1000; i++) {
            String temp = new String("String " + i);
            // temp goes out of scope, object becomes eligible for GC
        }
        
        // Explicit garbage collection (not recommended in production)
        System.gc();  // Suggests garbage collection
    }
}
```

### **7. ARRAYS DEEP DIVE**

#### **7.1 Array Fundamentals Deep Analysis**

**Array Memory Layout:**
```java
public class ArrayDeep {
    public static void main(String[] args) {
        // Array declaration and initialization
        int[] numbers = new int[5];  // All elements initialized to 0
        String[] names = {"Alice", "Bob", "Charlie"};  // Array literal
        
        // Array bounds and safety
        try {
            System.out.println(numbers[5]);  // ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }
        
        // Array copying
        int[] original = {1, 2, 3, 4, 5};
        int[] copy1 = original;  // Shallow copy - same reference
        int[] copy2 = original.clone();  // Deep copy - new array
        int[] copy3 = Arrays.copyOf(original, original.length);  // Another deep copy
        
        original[0] = 999;
        System.out.println("Original[0]: " + original[0]);  // 999
        System.out.println("Copy1[0]: " + copy1[0]);        // 999 (same reference)
        System.out.println("Copy2[0]: " + copy2[0]);        // 1 (different array)
        System.out.println("Copy3[0]: " + copy3[0]);        // 1 (different array)
    }
}
```

**Array Algorithms Deep Dive:**
```java
public class ArrayAlgorithms {
    // Linear search
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;  // Not found
    }
    
    // Binary search (requires sorted array)
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;  // Not found
    }
    
    // Bubble sort
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    // Selection sort
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            // Swap elements
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}
```

#### **7.2 Multidimensional Arrays Deep Dive**

**2D Array Deep Analysis:**
```java
public class MultiDimensionalDeep {
    public static void main(String[] args) {
        // Regular 2D array
        int[][] matrix = new int[3][4];  // 3 rows, 4 columns
        
        // Initialize with values
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = i * matrix[i].length + j;
            }
        }
        
        // Print matrix
        printMatrix(matrix);
        
        // Ragged array (different row lengths)
        int[][] ragged = new int[3][];
        ragged[0] = new int[2];
        ragged[1] = new int[4];
        ragged[2] = new int[3];
        
        // Initialize ragged array
        for (int i = 0; i < ragged.length; i++) {
            for (int j = 0; j < ragged[i].length; j++) {
                ragged[i][j] = (i + 1) * (j + 1);
            }
        }
        
        printRaggedArray(ragged);
        
        // Matrix operations
        int[][] matrix1 = {{1, 2}, {3, 4}};
        int[][] matrix2 = {{5, 6}, {7, 8}};
        int[][] result = multiplyMatrices(matrix1, matrix2);
        printMatrix(result);
    }
    
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int value : row) {
                System.out.printf("%4d ", value);
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public static void printRaggedArray(int[][] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.printf("%4d ", array[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public static int[][] multiplyMatrices(int[][] a, int[][] b) {
        int rows = a.length;
        int cols = b[0].length;
        int[][] result = new int[rows][cols];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                for (int k = 0; k < a[0].length; k++) {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        
        return result;
    }
}
```

### **8. ARRAYLIST DEEP DIVE**

#### **8.1 ArrayList vs Array Deep Comparison**

**Performance Analysis:**
```java
public class ArrayListDeep {
    public static void main(String[] args) {
        // ArrayList creation and basic operations
        ArrayList<Integer> list = new ArrayList<>();
        
        // Adding elements
        list.add(10);
        list.add(20);
        list.add(30);
        list.add(1, 15);  // Insert at index 1
        
        System.out.println("List: " + list);
        System.out.println("Size: " + list.size());
        System.out.println("Element at index 1: " + list.get(1));
        
        // Modifying elements
        list.set(0, 5);
        System.out.println("After set: " + list);
        
        // Removing elements
        list.remove(1);  // Remove by index
        System.out.println("After remove by index: " + list);
        
        list.remove(Integer.valueOf(30));  // Remove by value
        System.out.println("After remove by value: " + list);
        
        // Performance comparison
        performanceComparison();
    }
    
    public static void performanceComparison() {
        int size = 100000;
        
        // Array performance
        long start = System.nanoTime();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = i;
        }
        long arrayTime = System.nanoTime() - start;
        
        // ArrayList performance
        start = System.nanoTime();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            list.add(i);
        }
        long listTime = System.nanoTime() - start;
        
        System.out.println("Array time: " + arrayTime / 1_000_000 + " ms");
        System.out.println("ArrayList time: " + listTime / 1_000_000 + " ms");
    }
}
```

**ArrayList Advanced Operations:**
```java
public class ArrayListAdvanced {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        names.add("David");
        names.add("Eve");
        
        // Iterator usage
        Iterator<String> iterator = names.iterator();
        while (iterator.hasNext()) {
            String name = iterator.next();
            if (name.length() > 4) {
                iterator.remove();  // Safe removal during iteration
            }
        }
        System.out.println("After iterator removal: " + names);
        
        // ListIterator (bidirectional)
        ListIterator<String> listIterator = names.listIterator();
        while (listIterator.hasNext()) {
            String name = listIterator.next();
            if (name.equals("Bob")) {
                listIterator.set("Robert");  // Modify current element
            }
        }
        System.out.println("After ListIterator modification: " + names);
        
        // Sublist operations
        List<String> sublist = names.subList(1, 3);
        sublist.clear();  // Removes elements from original list
        System.out.println("After sublist clear: " + names);
    }
}
```

---

## 🎯 **PRACTICE PROBLEMS & EXERCISES**

### **Problem Set 1: Foundation Concepts**

**Problem 1: Variable Scope Analysis**
```java
public class ScopeProblem {
    private static int staticVar = 10;
    private int instanceVar = 20;
    
    public void method1() {
        int localVar = 30;
        // TODO: What variables are accessible here?
        // TODO: What happens if you try to access variables from other methods?
    }
    
    public static void method2() {
        // TODO: What variables are accessible here?
        // TODO: Can you access instanceVar? Why or why not?
    }
}
```

**Problem 2: Type Casting Challenge**
```java
public class CastingProblem {
    public static void main(String[] args) {
        double d = 3.14159;
        int i = (int) d;
        
        // TODO: What is the value of i?
        // TODO: How would you round instead of truncate?
        
        byte b = 127;
        b++;
        // TODO: What is the value of b? Why?
    }
}
```

**Problem 3: Loop Logic**
```java
public class LoopProblem {
    public static void main(String[] args) {
        // TODO: Write a loop that prints numbers 1 to 10
        // TODO: Write a loop that prints even numbers from 2 to 20
        // TODO: Write a loop that calculates factorial of 5
        // TODO: Write nested loops that print a multiplication table
    }
}
```

### **Problem Set 2: Advanced Concepts**

**Problem 4: Static vs Instance**
```java
public class StaticProblem {
    // TODO: Design a class that tracks how many instances have been created
    // TODO: Include both instance and static methods
    // TODO: Demonstrate the difference between static and instance access
}
```

**Problem 5: Array Manipulation**
```java
public class ArrayProblem {
    // TODO: Write a method that finds the maximum value in an array
    // TODO: Write a method that reverses an array in-place
    // TODO: Write a method that removes duplicates from an array
    // TODO: Write a method that merges two sorted arrays
}
```

**Problem 6: ArrayList Operations**
```java
public class ArrayListProblem {
    // TODO: Create an ArrayList of Student objects
    // TODO: Implement methods to add, remove, and search students
    // TODO: Sort students by grade
    // TODO: Find students with grades above a certain threshold
}
```

---

## 📝 **SELF-ASSESSMENT QUESTIONS**

### **Foundation Concepts (Lessons 1-4)**

1. **Variables & Data Types:**
   - What's the difference between `int x = 5` and `Integer x = 5`?
   - When would you use `float` instead of `double`?
   - What happens when you assign a `long` to an `int`?

2. **Control Flow:**
   - When should you use `switch` instead of `if-else`?
   - What's the difference between `while` and `do-while`?
   - How do you exit a nested loop from the inner loop?

3. **Methods:**
   - What's method overloading and when would you use it?
   - How does Java pass parameters to methods?
   - What's the difference between a method signature and method body?

4. **Constructors:**
   - When is a default constructor provided?
   - How do you call one constructor from another?
   - What's the difference between a constructor and a method?

### **Advanced Concepts (Lessons 5-6)**

5. **Static Concepts:**
   - When should you make a method static?
   - Can static methods access instance variables?
   - What's the difference between static and instance variables?

6. **Memory Management:**
   - What's the difference between stack and heap memory?
   - When does an object become eligible for garbage collection?
   - What's a memory leak and how do you prevent it?

7. **Arrays:**
   - What's the difference between an array and an ArrayList?
   - How do you create a ragged array?
   - What's the time complexity of accessing an array element?

8. **ArrayList:**
   - When should you use ArrayList instead of arrays?
   - What's the difference between `remove(int)` and `remove(Object)`?
   - How does ArrayList handle capacity expansion?

---

## 🎯 **EXAM PREPARATION STRATEGY**

### **Week 1: Foundation Mastery**
- **Day 1-2**: Variables, data types, type casting
- **Day 3-4**: Control flow (if-else, switch, loops)
- **Day 5-6**: Methods and constructors
- **Day 7**: Review and practice problems

### **Week 2: Advanced Topics**
- **Day 1-2**: Static concepts and memory management
- **Day 3-4**: Arrays and array algorithms
- **Day 5-6**: ArrayList and collections
- **Day 7**: Integration and complex problems

### **Week 3: Exam Preparation**
- **Day 1-2**: Review all concepts, identify weak areas
- **Day 3-4**: Practice coding problems
- **Day 5-6**: Mock exams and time management
- **Day 7**: Final review and confidence building

### **Study Tips:**
1. **Code Everything**: Don't just read - type out every example
2. **Debug Actively**: When code doesn't work, figure out why
3. **Ask Questions**: What happens if you change this? What if you do that?
4. **Practice Regularly**: 30 minutes daily is better than 3 hours once
5. **Test Yourself**: Use the self-assessment questions regularly

---

## 🏆 **SUCCESS METRICS**

### **By End of Week 1:**
- [ ] Can explain all primitive data types and their ranges
- [ ] Can write nested if-else statements confidently
- [ ] Can implement all types of loops correctly
- [ ] Can design methods with proper parameters and return types

### **By End of Week 2:**
- [ ] Can explain static vs instance concepts clearly
- [ ] Can trace memory allocation for complex programs
- [ ] Can implement array algorithms (search, sort)
- [ ] Can use ArrayList effectively for dynamic data

### **By End of Week 3:**
- [ ] Can solve complex programming problems in 30 minutes
- [ ] Can debug code quickly and efficiently
- [ ] Can explain concepts to others clearly
- [ ] Feel confident about the midterm exam

---

**Remember: Understanding beats memorization. Focus on concepts, not just syntax!**

**Good luck with your CP213 midterm! 🍀**
