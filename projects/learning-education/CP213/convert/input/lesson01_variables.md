# Lesson 01: Variables and Data Types

## **Variables**

The Java programming language uses both instances "variables" and "fields" as part of its terminology. In Java, to declare a class variable/field, you need to specify:

**Access modifier Field type Field name**

- Access modifier
- Field type
- Field name
- **public** modifier means the field is accessible from all classes.
- **private** modifier means the field is accessible only within its own class.
- **protected** modifier means the field is accessible within a class package (a directory that holds all related classes). More on Java package in later lessons.

### **2.1.3 Instance, Static, Local and Parameter Variables**

Java differentiates between instance, static, local, and parameter variables.

- **Class variables or static fields** are fields declared with the **static** modifier; there is exactly one copy of a class variable, regardless of how many times the class has been instantiated.
    
    For example, in the Student class, you might have a static variable called
    
    **static String university_name;** This makes sense because all students in the same university will have the same value for the **university_name** instance variable.
    
- **Instance variables (non-static fields)** are unique to each instance of a class.
    
    For example, if you have a class called student, your class might have an instance variable such as **String student_number;** which will be unique for every student object instantiated from the Student class.
    
- **Local variables** hold temporary state inside a method. If you have a method to calculate student grade averages, you need local variables, such as **double average,** to hold computation results that might be used for printing or as a return value from the method

## **3.1 Integers**

Java has four different variable types to hold whole numbers. The types are different from each other on the size of the value they can hold. The types are:

**byte, its length is 1 byte or 8 bits**
**short, its length is 2 bytes or 16 bits**
**int, its length is 4 bytes or 32 bits**
**long, its length is 8 bytes or 64 bits**

- byte, its length is 1 byte or 8 bits
- short, its length is 2 bytes or 16 bits
- int, its length is 4 bytes or 32 bits
- long, its length is 8 bytes or 64 bits

```
The types are different from each other by the size of the value they can hold. for example, when you declare
a variable of type byte, the variable can have 2 to power 8= 256 possible values.
The value range of byte is between −2 to power 7 to 2 to power 7 - 1, i.e., -128 to 127.
It is for this reason that if you declare byte b = 127 it will be fine, but if you declare byte b = 300,
the compiler will not accept it without casting ( byte b = (byte) 300 ) which results in an incorrect outcome.
```

## **3.2 Real numbers**

Java has two variable types to hold numbers with fraction values. Like integers, the types are different from each other in the size of the value they can hold. The types are:

**float, its length is 4 bytes or 32 bits**
**double, its length is 8 bytes or 64 bits**

- float, its length is 4 bytes or 32 bits
- double, its length is 8 bytes or 64 bits

## **3.3 char and boolean**

In addition to whole and fraction numbers, Java has two other primitive variable types,

**char** and **boolean**

- **char** and
- **boolean**

The **char** length is 2 bytes or 16 bits and **boolean** represents one bit of information and it takes **true** or **false** value. Variables of type **int** can be assigned to **char** (e.g., char a = 98). You cannot assign int values to a boolean variable nor you can assign a true/false value to an int variable.

**Note,** in Java, you cannot assign one and zero to a boolean type, the value must be true/false. This is possible in other programming languages such as C++, but not in Java.

## **3.4 Primitive Types Ordering**

When lining-up Java primitive data types based on their size, they form this line: **byte🡢short🡢int🡢long🡢float🡢double**. Values of any type from the left-hand side of the line can be assigned to any successor type from right (e.g., int to double, long to double). To assign values the other way around, you need to do explicit typecasting.

See the example below:

```java
int x = 2;
double y;
y = x; // is a valid statement. y is big enough to hold the value of x.
```

But to assign y to x, you need to do typecasting. `x = (int)y;`

y might be a large number that cannot be saved in x variable.

Note, the range of values that can be represented by a float or double type is much larger than the range that can be represented by a long type. This is because both float and double types use exponent to represent values.

## **3.5 Default Variable Initializations**

Class instance variables are automatically initialized in Java

- *boolean types* are initialized to **false**.
- *primitives holding numbers* (short, byte, int, double, and float) are initialized to **the zero**
- *char types* are initialized to **space**
- *class types* are initialized to **null**

It is a better practice to explicitly initialize instance variables yourself in the class **constructor.**

More on constructors in later lessons.

In Java, you can define and initialize multiple variables of the same type in one line.

For example:

This is correct in java: `int x = 2, y = 4, z = 5;` variable declarations are separated from each other by a comma.

Different from double, when you initialize float, you include a letter f in the value. e.g., **`float price = 2.3f;`**

**Note,** Local variables are not automatically initialized. It is the programmer's responsibility to initialize local variables.

## **3.6 Type Casting**

A type cast takes a value of one type and produces a value of another type with an "equivalent" value. For example, `int x, double y; y = (double)x;` Here x value is changed from int to double before is assigned to y.

**Note**, when casting, the desired type is placed inside parentheses immediately in front of the variable to be cast. The type and value of the variable to be cast does not change.

If x and y are integers are to be divided, and the fractional portion of the result must be preserved, at least one of the two must be a typecast to a floating-point type before the division operation is performed.

Here is an example:

```java
int x = 5, y = 2;
double result = x / (double)y; // this will become 5/2.0 and the result would be 2.5.
```

When typecasting from a floating-point to an integer type, the number is truncated, not rounded: **(int)2.9** evaluates to **2**, not **3**. When the value of an integer type is assigned to a variable of a floating-point type, Java performs an automatic type cast called a *type coercion* `double d = 5;`

## **3.7 Type Assignment Example**

In java, not all types can be assigned to other types without explicit typecasting. Run the code below to see when variables of different types can be assigned to each other (e.g., int to double, long to double) and when to do explicit typecasting.

```java
package lesson01;
public class VariableAssignment {
    public static void main(String args[]) {
        int x = 2; double y;

        y = x; // this is possible
        x = y; // this is a mismatch error cannot assignment double to int

        x = (int) y; // explicit type casting

        byte b; short s;

        s = b; // correct
        b = s; // mismatch type

        s = x; // mismatch type
        b = x; // mismatch type

        x = b; // correct assignment
        x = s; // correct assignment

        long l;
        x = l; // mismatch type
        l = x;

        double d; float f;

        d = l;
        l = d; // mismatch type

        f = l;
        l = f; // mismatch type

        char c = 'a';
        char a = 98;
        int charvalue = (int) c;

        boolean bool1 = true;
        boolean bool2 = false;

        bool1 = 0; // type mismatch cannot convert from int to boolean
        bool2 = 1; // type mismatch cannot convert from int to boolean

        bool1 = (boolean) 1; // cannot cast from int to boolean
    }
}
```

## **Java Documentation (Javadoc)**

When using Java documentation tags, follow these guidelines:

- @param Parameter_Name Parameter_Description
- @return Description_Of_Value_Returned
- @throws Exception_Type Explanation
- @deprecated
- @see Package_Name.Class_Name
- @author Author
- @version Version_Information

For multiple parameters, place each **@param** tag on a separate line, listing them in the same order as they appear in the parameter list. Similarly, for multiple authors, use a separate **@author** tag for each person. Below is an example demonstrating proper @tag usage.

```java
package lesson01;
/**
 * class ForJavaDoc is used to demonstrate how to use tags to generate javadoc.
 *
 * @author Abdul-Rahman Mawlood
 *
 */
public class ForJavaDoc {
    private int number;
    private String name;
    private String manager;

    /**
     * constructor method which takes three parameters
     *
     * @param number uniquely identify employee
     * @param name name of employee
     * @param manager name of manager
     */
    public ForJavaDoc(int number, String name, String manager) {
        super();
        this.number = number;
        this.name = name;
        this.manager = manager;
    }
    /**
     * get method for number
     *
     * @return number return employee unique number
     */
    public int getNumber() {
        return number;
    }
    /**
     * set method for number
     *
     * @param number int value to set employee number
     *
     */
    public void setNumber(int number) {
        this.number = number;
    }
    /**
     * get method for name
     *
     * @return return employee name
     */
    public String getName() {
        return name;
    }
    /**
     * set method for name
     *
     * @param name String name to set employee name
     *
     */
    public void setName(String name) {
        this.name = name;
    }
    /**
     * get method for manger
     *
     * @return return manager name
     */
    public String getManager() {
        return manager;
    }
    /**
     * set method for manger
     *
     * @param manager set manager name
     *
     */
    public void setManager(String manager) {
        this.manager = manager;
    }
    /**
     * toString method for the class
     */
    @Override
    public String toString() {
        return "ForJavaDoc [number=" + number + ", name=" + name + ", manager=" + manager + "]";
    }
}
```

## **Key Terms Glossary**

| Keyword | Definition |
|---------|------------|
| **Bytecode** | Compiled version of Java code created by `javac`. Platform-independent and runs on the JVM. Ensures Java's "write once, run anywhere" principle. |
| **Class** | Blueprint for creating objects. Defines attributes (variables) and behaviors (methods). Central to object-oriented programming. |
| **Instance Variable** | Declared inside a class but outside methods. Each object has its own copy. Represents the state of an object. |
| **Java, javac, and Javadoc** | **Java**: The programming language itself. **javac**: The Java compiler that translates `.java` files into bytecode. **Javadoc**: Tool for generating documentation from comments in code. |
| **Java Virtual Machine (JVM)** | Executes Java bytecode. Provides platform independence. Handles memory management and security. |
| **Method** | Block of code that performs a task. Can accept parameters and return values. Improves code reusability and organization. |
| **Object** | Instance of a class. Contains its own values for instance variables. Represents real-world entities in Java programs. |
| **Private** | Access modifier in Java. Restricts access to class members (variables or methods). Only accessible within the same class. |
| **Public** | Access modifier in Java. Makes class members accessible from anywhere. Often used for main methods and APIs. |
| **Variable Casting** | Converting a variable from one type to another. **Implicit casting** (widening): smaller to larger type (e.g., int → double). **Explicit casting** (narrowing): larger to smaller type (e.g., double → int). |



