# cp213 - obj oriented programming

## **Variables**

The Java programming language uses both instances "variables" and "fields" as part of its terminology. In Java, to declare a class variable/field, you need to specify:

**Access modifierField typeField name**

- Access modifier
- Field type
- Field name
- **public** modifier means the field is accessible from all classes.
- **private** modifier means the field is accessible only within its own class.
- **protected** modifier means the field is accessible within a class package (a directory that holds all related classes). More on Java package in later lessons.

### **2.1.3 Instance, Static, Local and Parameter Variables**

Java differentiates between instance, static, local, and parameter variables.

- **Class variables or static fields** are fields declared with the **static** modifier; there is exactly one copy of a class variable, regardless of how many times the class has been instantiated.
    
    For example, in the Student class, you might have a static variable called
    
    **static String university_name;** This makes sense because all students in the same university will have the same value for the **university_name** instance variable.
    
- **Instance variables (non-static fields**) are unique to each instance of a class.
    
    For example, if you have a class called student, your class might have an instance variable such as **String student _number;** which will be unique for every student object instantiated from the Student class.
    
- **Local variables** hold temporary state inside a method. If you have a method to calculate student grade averages, you need local variables, such as **double average,** to hold computation results that might be used for printing or as a return value from the method

![image.png](image.png)

## **3.1 Integers**

Java has four different variable types to hold whole numbers. The types are different from each other on the size of the value they can hold. The types are:

**byte, its length is 1 byte or 8 bitsshort, its length is 2 bytes or 16 bitsint, its length is 4 bytes or 32 bitslong, its length is 8 bytes or 64 bits**

- byte, its length is 1 byte or 8 bits
- short, its length is 2 bytes or 16 bits
- int, its length is 4 bytes or 32 bits
- long, its length is 8 bytes or 64 bits

```
The types are different from each other by the size of the value they can hold. for example, when you declare
 a variable of type byte, the variable can have  2 to power 8= 256 possible values.
 The value range of byte is between −2 to power 7 to  2 to power 7 - 1, i.e., -128 to 127.
 It is for this reason that if you declare byte b = 127 it will be fine, but if you declare byte b = 300,
 the compiler will not accept it  without casting ( byte b = (byte) 300 ) which results in an incorrect outcome.
```

## **3.2 Real numbers**

Java has two variable types to hold numbers with fraction values. Like integers, the types are different from each other in the size of the value they can hold. The types are:

**float, its length is 4 bytes or 32 bitsdouble, its length is 8 bytes or 64 bits**

- float, its length is 4 bytes or 32 bits
- double, its length is 8 bytes or 64 bits

## **3.3 char and boolean**

In addition to whole and fraction numbers, Java has two other primitive variable types,

**char andboolean**

- **char** and
- **boolean**

The **char** length is 2 bytes or 16 bits and **boolean** represents one bit of information and it takes **true** or **false** value. Variables of type **int** can be assigned to **char** (e.g., char a = 98). You cannot assign int values to a boolean variable nor you can assign a true/false value to an int variable.

**Note,** in Java, you cannot assign one and zero to a boolean type, the value must be true/false. This is possible in other programming languages such as C++, but not in Java.

## **3.4 Primitive Types Ordering**

When lining-up Java primitive data types based on their size, they form this line:  **byte🡢short🡢int🡢long🡢float🡢double**. Values of any type from the left-hand side of the line can be assigned to any successor type from right (e.g., int to double, long to double). To assign values the other way around, you need to do explicit typecasting.

See the example below:

int x = 2;

double y ;

y =x ;  is a valid statement.  y is big enough to hold the value of x.

But to assign y to x, you need to do typecasting.  x= (int)y ;

y might be a large number that cannot be saved in x variable.

Note, the range of values that can be represented by a float or double type is much larger than the range that can be represented by a long type. This is because both float and double types use exponent to represent values.

## **3.5 Default Variable Initializations**

Class instance variables are automatically initialized in Java

- *boolean types* are initialized to **false**.
- *primitives holding numbers* (short, byte, int, double, and float) are initialized to **the zero**
- *char types* are initialized to **space**
- *class types* are initialized to **null**

It is a better practice to explicitly initialize instance variables yourself in the class **constructor.** 

More on constructors in later lessons.

In Java, you can define and initialize multiple variables of the same type in one line.

For example:

This is correct in java: int x =2, y =4, z =5; variable declarations are separated from each other by a comma.

Different from double, when you initialize float, you include a letter f in the value. e.g., **`float** price **=** **2.3f;**`

**Note,** Local variables are not automatically initialized. It is the programmer’s responsibility to initialize local variables.

## **3.6 Type Casting**

A type cast takes a value of one type and produces a value of another type with an "equivalent" value.  For example, int x , double y ;  y= (double)x; Here x value is changed from int to double before is assigned to y.

**Note**, when casting, the desired type is placed inside parentheses immediately in front of the variable to be cast. The type and value of the variable to be cast does not change.

If x and y are integers are to be divided, and the fractional portion of the result must be preserved, at least one of the two must be a typecast to a floating-point type before the division operation is performed.

Here is an example:

int x =5, y =2 ;

double result = x / (double)y;  this will become  5/2.0  and the result would be 2.5.

When typecasting from a floating-point to an integer type, the number is truncated, not rounded: **(int)2.9** evaluates to **2**, not **3**. When the value of an integer type is assigned to a variable of a floating-point type, Java performs an automatic type cast called a *type coercion* **double d = 5;**

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

![image.png](image%201.png)

![image.png](image%202.png)

![image.png](image%203.png)

When using Java documentation tags, follow these guidelines:

@param Parameter_Name Parameter_Description

@return Description_Of_Value_Returned

@throws Exception_Type Explanation

@deprecated

@see Package_Name.Class_Name

@author Author

@version Version_Information

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

### **Bytecode**

- Compiled version of Java code created by `javac`.
- Platform-independent and runs on the JVM.
- Ensures Java's "write once, run anywhere" principle.

---

### **Class**

- Blueprint for creating objects.
- Defines attributes (variables) and behaviors (methods).
- Central to object-oriented programming.

---

### **Instance Variable**

- Declared inside a class but outside methods.
- Each object has its own copy.
- Represents the state of an object.

---

### **Java, javac, and Javadoc**

- **Java**: The programming language itself.
- **javac**: The Java compiler that translates `.java` files into bytecode.
- **Javadoc**: Tool for generating documentation from comments in code.

---

### **Java Virtual Machine (JVM)**

- Executes Java bytecode.
- Provides platform independence.
- Handles memory management and security.

---

### **Method**

- Block of code that performs a task.
- Can accept parameters and return values.
- Improves code reusability and organization.

---

### **Object**

- Instance of a class.
- Contains its own values for instance variables.
- Represents real-world entities in Java programs.

---

### **Private**

- Access modifier in Java.
- Restricts access to class members (variables or methods).
- Only accessible within the same class.

---

### **Public**

- Access modifier in Java.
- Makes class members accessible from anywhere.
- Often used for main methods and APIs.

---

### **Shorthand Operator**

- Used to simplify expressions (e.g., `+=`, `=`, `=`, `/=`).
- Updates a variable in a shorter form.
- Example: `x += 5;` is the same as `x = x + 5;`.

---

### **System.out.print and System.out.println**

- Used for output to the console.
- `print` displays text without a new line.
- `println` displays text and moves the cursor to the next line.

---

### **Variable Casting**

- Converting a variable from one type to another.
- **Implicit casting** (widening): smaller to larger type (e.g., int → double).
- **Explicit casting** (narrowing): larger to smaller type (e.g., double → int).

**System.out.println("The year is " + 2020);**

Printf allows us to have much more control over our output code. The println, print, and printf methods are all from the PrintStream class.

The java method printf does not advance to the next line after outputting.

The printf method can have any number of arguments. The first argument is always a string that contains format specifiers for the remaining arguments. All arguments except the first one are values for output to the screen.

Example:

### **1.1.5 Formatting Money Amounts with printf**

When displaying monetary values stored as double types, **%.2f** is an ideal format specifier. This format displays exactly two decimal places and uses only the minimum width needed to show the value:

```java
public static void MoneyFormat() {
		double salePrice = 1199.99;
		String name = "Android phone";
		System.out.printf("$%.2f for each %s", salePrice, name);
		System.out.println();
		System.out.println("is an expensive price");
}

```

The output will be:

```
$1199.99 for each Android phone.
is an expensive price
```

## **1.2 Common printf Format Specifiers**

**printf** supports various format specifiers. Here are the most commonly used ones:

- **%c** character
- **%d** decimal (integer) number (base 10)
- **%e** exponential floating-point number
- **%f** floating-point number
- **%i** integer (base 10)
- **%o** octal number (base 8)
- **%s** String
- **%u** unsigned decimal (integer) number
- **%x** number in hexadecimal (base 16)
- **%t** formats date/time
- **%%** print a percent sign
- **\%** print a percent sign

# **Lesson 02**

# 2 Java NumberFormat class

## **2.1 Specifying Locale**

You can explicitly specify the currency symbol for your output. To do so, you need to provide a location from the **Locale** class as an argument to the **getCurrencyInstance()** method. You also need to import the Locale class to your code,  **import java.util.Locale;**

In the example below, we use the print method for formatting money in three different ways, default (which is American), English, and Germany formatting.The output format is changed based on the Locale value passed to the ***getCurrencyInstance**() method.*

```java
package lesson02;

import java.text.NumberFormat;
import java.util.Locale;

public class MoneyFormat {
	public static NumberFormat moneyFormatter;

	public static void print() {

		System.out.println(moneyFormatter.format(39.8));
		System.out.println(moneyFormatter.format(39.81111));
		System.out.println(moneyFormatter.format(39.89999));
		System.out.println(moneyFormatter.format(39));
		System.out.println(moneyFormatter.format(39.33333));
		System.out.println();
	}

  public static void main(String[] args) {
	System.out.println("Default location:");
	moneyFormatter = NumberFormat.getCurrencyInstance();
	print();
	System.out.println("English location:");
	moneyFormatter =
      NumberFormat.getCurrencyInstance(Locale.ENGLISH);
	 print();
      System.out.println("Germany location:");
	  moneyFormatter =
       NumberFormat.getCurrencyInstance(Locale.GERMANY);
	  print();
	}
}

```

The default location output:

```

$39.80
$39.81
$39.90
$39.00
$39.33

```

The English location output:

```

¤39.80
¤39.81
¤39.90
¤39.00
¤39.33

```

The Germany location output:

```

39,80 €
39,81 €
39,90 €
39,00 €
39,33 €

```

The **NumberFormat** class has other uses such as formatting the output as a percentage, setting the minimum and the maximum number of digits to your output, rounding the output and parse numbers, etc. These uses are described in the Oracle documentation that you can refer to when needed.

## 🌍 Java `Locale` & Currency Formatting (NumberFormat)

- **`NumberFormat.getCurrencyInstance()`** → Formats numbers as money based on locale.
- **Default locale** = your system’s region (often `Locale.US` → `$`).
- **Language-only locales** (e.g., `Locale.ENGLISH`) → show **generic currency sign `¤`**, because no country is specified.
- **Country-specific locales** → show correct currency & formatting rules.

### 🔑 Examples

```java
NumberFormat.getCurrencyInstance();        // Default (US) → $39.80
NumberFormat.getCurrencyInstance(Locale.ENGLISH); // Generic → ¤39.80
NumberFormat.getCurrencyInstance(Locale.GERMANY); // Euro → 39,80 €

```

### 🌐 Common Locales

- `Locale.US` → `$`
- `Locale.CANADA` → `$`
- `Locale.UK` → `£`
- `Locale.JAPAN` → `￥`
- `Locale.GERMANY` → `€`

👉 Use **language + country locale** (e.g., `Locale.US`) instead of just `Locale.ENGLISH` to get real currency symbols.

## 📦 Lesson 02 – Importing Packages & Classes

### 🔹 What is a Package?

- A **package** = collection of related classes & interfaces.
- Stored in **JAR files** (Java Archive).
- Helps organize source code like folders (e.g., keep HTML, images, scripts, Java classes separate).
- Example: `java.lang`, `java.util`, `java.text`.

### 🔹 Why Use Packages?

- Keeps code **organized**.
- Groups related classes together.
- Makes large projects **manageable**.
- Allows code to be **reused & shared**.

### 🔹 Importing Packages

- Some packages are imported **automatically** (e.g., `java.lang` → `Math`, `String`, wrapper classes).
- To use others, you need the **import statement**:
    
    ```java
    import java.text.NumberFormat;   // import one class
    import java.text.*;              // import entire package
    
    ```
    
- Import statements must be at the **top of the file**, after `package` (if any) and before your class.

### 🔹 Creating Your Own Package

1. Group related classes into a **folder**.
2. Add a `package` statement at the **top of each file**:
    
    ```java
    package mypackage;
    
    ```
    
3. Folder structure must match the package name.

### 🔹 Example

```java
package wlu.cp213.lesson02;

import java.util.Scanner;

public class FormatedOutput { … }

```

### 🔹 Key Classes Used So Far

- `NumberFormat` → from `java.text` (for money formatting).
- `Locale` → from `java.util` (for regional settings).

## 📦 Lesson 02 – Packages (3.1 & 3.2)

### 🔹 3.1 Package Names & Directories

- A **package name** = directory path where Java looks for classes.
    - Example: `code.cp213.wlu.lesson02` → folder structure = `code/cp213/wlu/lesson02`.
- Java needs **two things** to find classes:
    1. **Package name**
    2. **CLASSPATH environment variable**
- **CLASSPATH** = list of directories Java searches for classes (similar to PATH).
    - `.` (dot) means **current working directory** is included.
- In Windows:
    - System Properties → Advanced → Environment Variables → Add/Edit `CLASSPATH`.
    - Example: `C:\jdk-12.0.1\lib;.`
- In **Eclipse**:
    - Project → Right-click → **Build Path → Configure Build Path** (to see JRE/JDK libraries).
    - Run Configurations → Shows `classpath` option Eclipse uses to run code.

---

### 🔹 3.2 Name Clashes

- Packages help avoid **class name conflicts** (e.g., two different `Student` classes).
- Solution = use **fully qualified names** (`package_name.ClassName`).
    - Example: `wlu.cp213.projectName.groupName.ClassName`.
- If using the **fully qualified name**, you don’t need an `import` statement.

---

👉 **Key Takeaway**:

- Packages = **folders** for organizing Java classes.
- **CLASSPATH** tells Java *where to search*.
- Fully qualified names prevent **ambiguity** when classes share the same name.

## 🔢 Lesson 02 – Java `DecimalFormat` Class

### 🔹 What it Does

- `DecimalFormat` = class for **custom number formatting**.
- Can format numbers as **percentages, fixed decimals, or scientific (E) notation**.
- Requires `import java.text.DecimalFormat;`.

---

### 🔹 Example Code

```java
import java.text.DecimalFormat;

public class UsingDecimalFormat {
    public static void main(String[] args) {
        // Percentage format
        DecimalFormat percent = new DecimalFormat("0.00%");
        System.out.println(percent.format(0.308)); // 30.80%

        // Scientific notation
        DecimalFormat eNotation1 = new DecimalFormat("#0.###E0");
        DecimalFormat eNotation2 = new DecimalFormat("00.###E0");

        System.out.println(eNotation1.format(123.456));   // 1.2346E2
        System.out.println(eNotation2.format(123.456));   // 12.346E1

        double smallNumber = 0.0000123456;
        System.out.println(eNotation1.format(smallNumber)); // 1.235E-5
        System.out.println(eNotation2.format(smallNumber)); // 12.346E-6
    }
}

```

---

### 🔹 Output

```
30.80%
1.2346E2
12.346E1
1.235E-5
12.346E-6

```

---

### 🔹 Key Notes

- `"0.00%"` → formats as **percentage**.
- `"#0.###E0"` → **scientific notation**, 1+ digit before decimal (flexible).
- `"00.###E0"` → **scientific notation**, **forces 2 digits** before decimal.
- Great for **percentages, small numbers, large numbers**.

## ⌨️ Lesson 02 – Scanner Class (User Input)

### 🔹 Overview

- `Scanner` (since Java 5.0) = simple way to read user input.
- Part of `java.util` package → must `import java.util.Scanner;`.
- Works as a **wrapper** for `System.in` (keyboard input).
- Similar to:
    - `input()` in Python
    - `cin >>` in C++

---

### 🔹 Creating a Scanner Object

```java
Scanner keyboard = new Scanner(System.in);
Scanner input = new Scanner(System.in); // can use any variable name

```

---

### 🔹 Common Methods

- `nextInt()` → reads an `int`
- `nextDouble()` → reads a `double`
- `next()` → reads a **single word** (stops at whitespace)

⚡ Multiple inputs → separated by whitespace, read with multiple method calls.

---

### 🔹 Example

```java
import java.util.Scanner;

public class ReadUserInput {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter two words separated by space:");

        String string1 = input.next();
        String string2 = input.next();

        System.out.println("string1 is " + string1 +
                           " and string2 is " + string2);
    }
}

```

**Input**

```
Hello Class

```

**Output**

```
string1 is Hello and string2 is Class

```

---

👉 The `Scanner` class makes input handling easier than using `System.in` directly.

## ⌨️ Lesson 02 – Scanner Class (Extended Notes)

### 🔹 5.2 `nextLine()` Method

- Reads an **entire line** (until `\n` – Enter key).
- The returned string **does not include** the `\n`.

```java
String inputLine = keyboard.nextLine();

```

---

### 🔹 5.3 Example: Mixed Input Types

Reads `int`, `double`, `String`, and a full line:

```java
Scanner keyboard = new Scanner(System.in);

int n1 = keyboard.nextInt();
int n2 = keyboard.nextInt();

double d1 = keyboard.nextDouble();
double d2 = keyboard.nextDouble();

String word1 = keyboard.next();
String word2 = keyboard.next();

keyboard.nextLine(); // clears leftover newline
String line = keyboard.nextLine();

```

👉 Works for other types too (`boolean`, `byte`, `short`, etc.).

---

### 🔹 5.4 End-of-Line Issues

⚠️ Mixing `nextInt()` / `next()` with `nextLine()` causes problems because `nextInt()` leaves the `\n` in the buffer.

```java
int n = keyboard.nextInt();
String line1 = keyboard.nextLine(); // reads leftover "\n"
String line2 = keyboard.nextLine();

```

Results:

- `n = 2`
- `line1 = ""`
- `line2 = "Heads are better than"`

✅ Fix: add an **extra `nextLine()`** to clear the buffer.

```java
int n = keyboard.nextInt();
keyboard.nextLine(); // clears "\n"
String line1 = keyboard.nextLine();
String line2 = keyboard.nextLine();

```

---

### 🔹 5.5 Empty String

- If user presses Enter **without typing**, `nextLine()` returns `""` (empty string).

---

### 🔹 5.6 Custom Delimiters

Default = whitespace. Can be changed with `useDelimiter()`.

```java
Scanner input = new Scanner(System.in);
input.useDelimiter("end"); // now "end" is the delimiter

```

---

👉 **Key Takeaway:**

Use `nextLine()` carefully with other input methods. Clear the buffer if needed.

## ⌨️ Lesson 02 – 5.7 Non-Graded Activity

This exercise shows how to:

1. Read keyboard input with `Scanner`.
2. Handle the `next()` vs `nextLine()` issue.
3. Change the input delimiter.

---

### 📝 Example Code: `ReadUserInput`

```java
package lesson02;

import java.util.Scanner;

public class ReadUserInput {

    // 1. Mixing nextInt() + nextLine()
    public static void terminatorIssue() {
        System.out.println("enter an int and two lines");
        Scanner keyboard = new Scanner(System.in);

        int n = keyboard.nextInt();
        keyboard.nextLine(); // clears leftover newline
        String line1 = keyboard.nextLine();
        String line2 = keyboard.nextLine();

        System.out.println(" n is " + n);
        System.out.println(" line1 is " + line1);
        System.out.println(" line2 is " + line2);
    }

    // 2. Using next() for separate words
    public static void getUserInput() {
        Scanner input = new Scanner(System.in);
        System.out.println("please enter two words separated by space");

        String string1 = input.next();
        String string2 = input.next();

        System.out.println("string1 is " + string1 + " and string2 is " + string2);
    }

    // 3. Changing the delimiter
    public static void changeDelimiter() {
        Scanner input = new Scanner(System.in);
        input.useDelimiter("end"); // custom delimiter
        System.out.println(" enter words, 'end' is used as delimiter ");

        String s = input.next();
        System.out.println(s);
    }

    public static void main(String args[]) {
        // getUserInput();
        // terminatorIssue();
        changeDelimiter();
    }
}

```

---

### 🔑 Key Takeaways

- `terminatorIssue()` → shows why you need `keyboard.nextLine()` after `nextInt()` to clear the buffer.
- `getUserInput()` → `next()` reads tokens (separated by whitespace).
- `changeDelimiter()` → you can replace whitespace delimiter with custom ones (e.g., `"end"`).

## ⌨️ Lesson 02 – Scanner Class (Extended Uses)

### 🔹 5.8.1 Scanner Constructor with String

- Scanner can take a **string** as input instead of `System.in`:

```java
Scanner input = new Scanner("Hello/CP213/Class");
input.useDelimiter("/"); // set custom delimiter
while (input.hasNext()) {
    System.out.println(input.next());
}

```

**Output:**

```
Hello
CP213
Class

```

- Acts like `StringTokenizer` – useful for breaking a string into tokens.

---

### 🔹 5.8.2 Scanner for Reading Files

- Scanner can read **files** using `FileInputStream`:

```java
Scanner inputFile = new Scanner(new FileInputStream("score.txt"));

```

- Example workflow:
    1. Prompt user for file name
    2. Use `FileInputStream` to open the file
    3. Read file line by line with `hasNextLine()`, `nextInt()`, `nextLine()`, etc.
- **File pattern requirement:** e.g., one `int` per line followed by a name:

```
92
Abdul-Rahman
55
Rob
98
David

```

- Close file after reading: `inputFile.close();`

**Example snippet for reading a file:**

```java
while (inputFile.hasNextLine()) {
    int score = inputFile.nextInt();
    inputFile.nextLine(); // clear newline
    String name = inputFile.nextLine();
    System.out.println("Name: " + name + ", score: " + score);
}

```

---

### 🔹 5.8.3 Other Scanner Methods

- `next()`, `nextLine()`, `hasNextLine()`, `nextInt()`, `useDelimiter()` – commonly used
- Additional methods:
    - `match()` → returns last scanning match result
    - `skip(String pattern)` → skips input matching a pattern
    - `locale()` → returns the scanner’s locale

---

### 🔑 Key Takeaways

- Scanner is **flexible**: can read from **keyboard**, **string**, or **file**.
- Use `useDelimiter()` to customize token separators.
- Always handle **file not found exceptions** when reading files.

# 📘 Lesson 02 – Wrapper Classes in Java

### 🔹 What are Wrapper Classes?

- Java is **object-oriented** → many APIs (Collections, Serialization, Synchronization) work only with **objects**.
- Wrapper classes convert **primitive types ↔ objects**.
- Since Java 5.0:
    - **Autoboxing** → primitive → object (automatic)
    - **Unboxing** → object → primitive (automatic)

---

### 🔹 Examples of Autoboxing & Unboxing

```java
// Autoboxing
Integer value = 22;       // int → Integer
Character ch = 'a';       // char → Character

// In collections
ArrayList<Integer> list = new ArrayList<>();
for (int i = 1; i < 10; i++) {
    list.add(i);  // int → Integer automatically
}

// Unboxing
for (Integer i : list) {
    if (i % 2 == 0) sum += i; // Integer → int automatically
}

```

---

### 🔹 Useful Constants

- `Integer.MAX_VALUE`, `Integer.MIN_VALUE`
- `Double.MAX_VALUE`, `Double.MIN_VALUE`
- `Boolean.TRUE`, `Boolean.FALSE`

---

### 🔹 Useful Static Methods

- **Convert String → Number:**
    - `Integer.parseInt("123") → 123`
    - `Double.parseDouble("3.14") → 3.14`
- **Convert Number → String:**
    - `Double.toString(123.99) → "123.99"`

---

### 🔹 Example: String to Double Conversion

```java
Scanner keyboard = new Scanner(System.in);
System.out.println("Enter two numbers separated by a comma:");
String input = keyboard.nextLine();

StringTokenizer tokens = new StringTokenizer(input, ",");
String s1 = tokens.nextToken();
String s2 = tokens.nextToken();

double n1 = Double.parseDouble(s1);
double n2 = Double.parseDouble(s2);

System.out.println("Converted: " + n1 + " and " + n2);

```

**Output:**

```
Enter two numbers separated by a comma:
3.5, 44.5
Converted: 3.5 and 44.5

```

---

✅ **Key Takeaway:** Wrapper classes bridge **primitives ↔ objects**, making them essential for Java collections, parsing, and data conversion.

# 📝 Java Wrapper Class Cheatsheet

### 🔹 Wrapper Classes

| Primitive | Wrapper Class |
| --- | --- |
| boolean | Boolean |
| char | Character |
| byte | Byte |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |

---

### 🔹 Common Constants

| Wrapper | Max Value | Min Value |
| --- | --- | --- |
| Integer | `Integer.MAX_VALUE` | `Integer.MIN_VALUE` |
| Double | `Double.MAX_VALUE` | `Double.MIN_VALUE` |
| Long | `Long.MAX_VALUE` | `Long.MIN_VALUE` |
| Float | `Float.MAX_VALUE` | `Float.MIN_VALUE` |
| Boolean | `Boolean.TRUE`, `Boolean.FALSE` | – |

---

### 🔹 Conversion Methods

| Purpose | Method Example | Result |
| --- | --- | --- |
| String → int | `Integer.parseInt("123")` | `123` (int) |
| String → double | `Double.parseDouble("3.14")` | `3.14` (double) |
| String → long | `Long.parseLong("99999")` | `99999` (long) |
| String → boolean | `Boolean.parseBoolean("true")` | `true` (bool) |
| String → wrapper object | `Integer.valueOf("123")` | `Integer(123)` |
| Wrapper → String | `Double.toString(12.34)` | `"12.34"` |
| Primitive → String | `String.valueOf(10)` | `"10"` |
| Wrapper → primitive | `int x = myInteger.intValue();` | `123` (int) |

---

### 🔹 Autoboxing & Unboxing

```java
// Autoboxing
Integer a = 10;     // int → Integer
Double d = 3.14;    // double → Double

// Unboxing
int x = a;          // Integer → int
double y = d;       // Double → double

```

---

✅ **Quick Rule of Thumb:**

- `parseXxx()` → returns **primitive**
- `valueOf()` → returns **wrapper object**
- `toString()` / `String.valueOf()` → returns **String**

```java
package lesson02;

import java.util.Scanner;
import java.util.StringTokenizer;

public class StringToDouble {

	public static void main (String args []) {
		Scanner keyboard = new Scanner (System.in) ;
		System.out.println("please enter two numbers on a line seperated by comma") ;
		String input = keyboard.nextLine() ;

		StringTokenizer tokens = new StringTokenizer (input, ",");

		String string1 ="" ;
		String string2 ="" ;

		if (tokens.countTokens() == 2) {

			string1 = tokens.nextToken() ;
			string2 = tokens.nextToken() ;
		}else {
			System.out.println (" restart again") ;
			System.exit(0);
		}
		double number1 = Double.parseDouble(string1);
		double number2 = Double.parseDouble(string2);

		System.out.println ("both strings convered to numbers "
                                + number1  + " and " + number2) ;
```

### Step 1 – Importing tools

```java
import java.util.Scanner;
import java.util.StringTokenizer;

```

- `Scanner` → lets us read user input.
- `StringTokenizer` → helps us split a string into smaller pieces (tokens).

---

### Step 2 – Create a Scanner

```java
Scanner keyboard = new Scanner(System.in);

```

- `System.in` = the keyboard.
- Now we can read what the user types.

---

### Step 3 – Ask the user for input

```java
System.out.println("please enter two numbers on a line separated by comma");
String input = keyboard.nextLine();

```

- User types:
    
    ```
    3.5,44.5
    
    ```
    
- `input` = `"3.5,44.5"` (all as one string right now).

---

### Step 4 – Split the string

```java
StringTokenizer tokens = new StringTokenizer(input, ",");

```

- `,` = the separator (delimiter).
- Now `tokens` knows `"3.5"` is the first piece and `"44.5"` is the second piece.

---

### Step 5 – Store the two pieces

```java
String string1 = "";
String string2 = "";

if (tokens.countTokens() == 2) {
    string1 = tokens.nextToken(); // "3.5"
    string2 = tokens.nextToken(); // "44.5"
} else {
    System.out.println("restart again");
    System.exit(0);
}

```

- We check if there are **exactly 2 tokens**.
- If yes → we take them out.
- If not → program ends.

---

### Step 6 – Convert Strings to numbers

```java
double number1 = Double.parseDouble(string1);
double number2 = Double.parseDouble(string2);

```

- `"3.5"` (string) → `3.5` (double number).
- `"44.5"` (string) → `44.5` (double number).

---

### Step 7 – Print the result

```java
System.out.println("both strings converted to numbers " + number1 + " and " + number2);

```

- Output:
    
    ```
    both strings converted to numbers 3.5 and 44.5
    
    ```
    

---

✨ So in plain words:

1. Ask user for a line with two numbers separated by a comma.
2. Break the line into two strings.
3. Convert each string into a `double`.
4. Print them as real numbers.

| Keyword | Definition |
| --- | --- |
| Autoboxing | Automatically converts primitive types (like `int`, `double`) into their wrapper class objects (`Integer`, `Double`) for use in contexts that require objects. |
| DecimalFormat class | Formats numbers into readable strings according to patterns, such as percentages, scientific notation, or fixed decimal places. |
| FileInputStream class | Reads raw byte data from a file; can be used with `Scanner` to process text line by line. |
| format() | Method used in classes like `PrintStream` or `DecimalFormat` to create formatted output for numbers, text, or dates. |
| format specifier | Placeholder in `printf()` or `format()` methods that defines how a value should be displayed (e.g., `%d` for integers, `%f` for floats). |
| getCurrencyInstance() | Method from `NumberFormat` that returns a currency formatter for a locale, automatically applying the correct currency symbol. |
| IntValue | Method of wrapper classes like `Integer` that converts an object back into its primitive type; largely replaced by autoboxing. |
| Locale | Represents a specific geographic, political, or cultural region, used for formatting numbers, currencies, and dates. |
| nextInt(), nextDouble(), etc. | `Scanner` methods that read input as specific primitive types, such as integers or doubles, from keyboard or files. |
| nextLine() and hasNextLine() | `nextLine()` reads an entire line of input; `hasNextLine()` checks if another line of input exists. |
| NumberFormat class | Formats numbers according to locale, including currencies and percentages, for readable or region-appropriate output. |
| print, println, printf | Methods of `PrintStream` for output; `print()` writes without newline, `println()` adds a newline, `printf()` allows formatted output. |
| PrintStream | Class providing methods like `print()`, `println()`, and `printf()` to write formatted data to console or other streams. |
| Scanner class | Reads input from keyboard, files, or strings, supporting multiple data types and custom delimiters. |
| specifier justification and "\n" | Controls output alignment in `printf()` (e.g., left-justified with `-`) and uses `\n` to move to a new line. |
| Unboxing | Automatically converts wrapper class objects back into their corresponding primitive types. |
| useDelimiter() | Changes the pattern used by a `Scanner` object to separate input tokens (e.g., `useDelimiter(",")`). |
| valueOf | Static method in wrapper classes converting a primitive type or string into its corresponding object (e.g., `Integer.valueOf(5)`). |
| Wrapping | Converting a primitive type into its corresponding wrapper class object to allow usage in object-required contexts. |

# 📘 Lesson 03: Control Flow in Java

## 1. Introduction

- Code executes **top to bottom**, unless modified by **control flow statements**.
- Control flow allows **branching** (decisions) and **looping** (repetition).

### 🔹 Types of Control Flow in Java

- **Decision-making:** `if-then`, `if-then-else`, `switch`
- **Looping:** `for`, `while`, `do-while`
- **Branching:** `break`, `continue`, `return`

---

## 2. Boolean Expressions & Operators

### 🔹 Comparison Operators

| Operator | Meaning |
| --- | --- |
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `>=` | greater than or equal to |
| `<` | less than |
| `<=` | less than or equal to |

➡️ Remember: **`==` for equality**, **`=` for assignment**

**Example:**

```java
int x = 5, y = 8;
boolean z = x < y;
System.out.println(x < y); // true

```

---

### 2.2 Comparing Strings

- `==` → compares memory addresses (not values).
- Use methods:
    - `str1.equals(str2)`
    - `str1.equalsIgnoreCase(str2)`

---

### 2.3 Lexicographic Ordering

- Based on **ASCII** values:
    - Uppercase letters come before lowercase.
- Use `compareTo` methods:
    - `s1.compareTo(s2)` → `<0`, `=0`, or `>0`
    - `s1.compareToIgnoreCase(s2)` → ignores case differences.

---

### 2.4 Building Boolean Expressions

- **AND (`&&`)** → true only if both are true.
- **OR (`||`)** → true if at least one is true.
- **NOT (`!`)** → negates a condition.

❌ Invalid:

```java
min < result < max

```

✅ Correct:

```java
(min < result) && (result < max)

```

---

### 2.5 Evaluating Boolean Expressions

- Produce `true` or `false`.
- Can assign to variables:

```java
int x = 3, y = 5;
boolean z = x > y; // false

```

⚠️ **Common mistake:**

```java
boolean b = false;
if (b = true) {   // assignment, not comparison
    System.out.println("Hello"); // executes
}

```

---

### 2.6 Short-Circuit vs Complete Evaluation

- **Short-circuit (lazy):**
    - `&&`: stops if first is `false`.
    - `||`: stops if first is `true`.

✅ Prevents runtime errors:

```java
int kids = 0, toys = 3;
if ((toys / 3) >= 2 && (toys / kids) >= 2) {
    // safe: second part never runs
}

```

- **Complete evaluation:**
    - Use `&` and `|` instead of `&&` and `||`.
    - Forces evaluation of both sides.

# 📘 Lesson 03: Branching with If-Else Statements

## 3.0 If-Else Basics

- **Definition**: Lets a program choose between two paths depending on a Boolean condition.
- **Syntax**:

```java
if (Boolean_Expression)
    Yes_Statement;
else
    No_Statement;

```

- **Example**:

```java
int mark = 0;
if (mark > 85)
    System.out.println("Your grade is A");
else
    System.out.println("Your grade is not A");

```

👉 **Java vs Python**:

- Java requires **parentheses** around conditions and **braces `{ }`** for multiple statements.
- Python uses `:` with indentation (`if ...:`, `elif ...:`, `else:`).

---

## 3.1 Compound Statements

- If a branch has **multiple statements**, group them in `{ }`.

```java
if (myScore > yourScore) {
    System.out.println("I win!");
    wager += 100;
} else {
    System.out.println("I wish these were golf scores.");
    wager = 0;
}

```

---

## 3.2 Omitting Else

- `else` is optional → creates a simple `if` statement.

```java
if (weight > ideal)
    calorieIntake -= 500;

```

- With multiple actions, braces are required:

```java
if (weight > ideal) {
    calorieIntake -= 500;
    System.out.println("Increase exercise rate!");
    exerciseRate *= 1.3;
}

```

---

## 3.3 Nested If-Else

- If statements can be placed **inside each other**.

```java
if (a > b) {
    if (c > d) {
        if (g < h) {
            // code
        }
    }
} else if (m == n) {
    if (z > y) {
        // code
    }
}

```

👉 Use indentation for clarity.

---

## 3.4 Multiway If-Else

- Chains multiple conditions.

```java
if (number < 100 && number >= 1) {
    System.out.println("Two-digit number");
} else if (number < 1000 && number >= 100) {
    System.out.println("Three-digit number");
} else if (number < 10000 && number >= 1000) {
    System.out.println("Four-digit number");
} else {
    System.out.println("Number not in range 1–99999");
}

```

---

## 3.5 Ternary Operator (`?:`)

- Shorthand for simple if-else assignments.

```java
int max = (n1 > n2) ? n1 : n2;

```

- Reads as:
    - If condition is **true**, take first value.
    - If **false**, take second value.

✅ Summary:

---

- **if-else** controls branching.
- **Compound** → multiple statements in `{ }`.
- **Omitting else** → runs only when condition is true.
- **Nested if** → allows deeper decisions.
- **Multiway if-else** → handles multiple conditions.
- **Ternary operator** → compact shorthand.

## 🧠 3.5 Method Use

### ✳️ Key Concept

- A **method invocation that returns a value** can be used anywhere that a value of the same type can be used.
- Example:
    
    ```java
    typeReturned variable = objectName.methodName();
    
    ```
    

### 💡 Examples

```java
BankAccount ac = new BankAccount("123", "AR Yunis", 100);
String myAccountNumber = ac.getAccountNumber();
System.out.println(myAccountNumber);
System.out.println(ac.getAccountNumber());

```

### ⚙️ Void Methods

- Invoking a **void method** is simply a statement:
    
    ```java
    objectName.methodName();
    
    ```
    
- You can ignore a return value if you don’t need it:
    
    ```java
    account.getCustomerName(); // return value discarded
    
    ```
    

---

## 🧠 3.6 Method Parameters

### ✳️ Key Concept

- **Parameters (formal parameters):** placeholders in a method definition.
- **Arguments (actual parameters):** real values passed into the method.

### 💡 Example

```java
public double deposit(String accountNumber, double amount) { … }

```

### ⚙️ Rules

- Number, order, and types of arguments must **match** the parameters.
- Java uses **call-by-value**: the values are copied, not the memory references.

```java
public void myMethod(int a, int b, double c) { … }
int a = 1, b = 2;
double c = 3.0;
myMethod(a, b, c); // same as myMethod(1,2,3);

```

---

## 🧠 3.7 Automatic Type Conversion

### ✳️ Key Concept

If argument and parameter types don’t match, **Java automatically promotes** compatible primitive types (e.g., `int` → `double`).

### 💡 Example

```java
public void myMethod(int a, int b, double c) { … }
int a = 1, b = 2, c = 3;
myMethod(a, b, c); // int → double conversion

```

---

## 🧠 3.8 Parameters Are Local Variables

### ✳️ Key Concept

- Parameters are **local variables** initialized with argument values.
- Changing parameters **inside** a method does not affect arguments **outside**.

### 💡 Example

```java
public void myMethod(int a, int b, double c) {
    a = b + (int)c;
    b = (int)c + a;
    c = a + b;
}

```

Result:

- Values inside the method change.
- Original values in `main()` stay the same.
    
    ➡️ **Demonstrates call-by-value.**
    

---

## 🧠 3.9 Non-Graded Activity – Call By Value

**Task:**

- Create method:
    
    ```java
    public static void callByValue(int a, double b)
    
    ```
    
- In `main`:
    
    ```java
    int x = 25;
    double y = 99.99;
    callByValue(x, y);
    
    ```
    
- Print and observe: changes inside method don’t affect `x` and `y`.

---

## 🧠 3.10 Method Variables

### ✳️ Key Concept

- Variables declared **inside a method** are **local variables**.
- Java does **not** have global variables.
- `static` variables are shared across **all objects of the same class**.

### 💡 Example

```java
public double deposit(String accountNumber, double amount) {
    double balance = 0.0;
    if (this.accountNumber == accountNumber)
        balance = balance + amount;
    return balance;
}

```

---

## 🧠 3.11 Method Overloading

### ✳️ Key Concept

- **Overloading** = same method name, different parameter lists (number/type/order).
- Must differ in **method signature**.
- Return type alone cannot differentiate methods.

### 💡 Example

```java
public double deposit(double amount) { … }
public double deposit(String accountNumber, double amount) { … }

```

🚫 Invalid:

```java
public int addNumbers(int a, int b) { … }
public double addNumbers(int a, int b) { … } // ❌ same signature

```

---

## 🧠 3.12 Overloading + Automatic Type Conversion

- If no exact match for a method call exists, **Java attempts type conversion**.
- May lead to **ambiguous** method calls → compile error.

### 💡 Example

```java
public double specialInterestRate(double discount) { … }

int discount = 1;
baccount1.specialInterestRate(discount); // int → double

```

## 4. The Switch Statement

- **Purpose**: Implements **multiway branching** in Java.
- **Syntax**:

```java
switch (Controlling_Expression) {
    case Case_Label_1:
        // code
        break;
    case Case_Label_2:
        // code
        break;
    default:
        // code if no case matches
        break;
}

```

### Key Rules

- The **controlling expression** must be `char`, `int`, `short`, `byte`, or from Java 7+, a `String`.
- Each **case label** must be the same type as the controlling expression.
- Case labels can be in any order but must be **unique**.
- Use `break;` to stop execution after a case.
    - If omitted, execution will **fall through** to the next case.

---

### 4.1 Default Section

- Handles all values **not explicitly matched** by any case.
- Optional, but good practice to include.
- Usually placed last.

---

### Example

```java
int numberOfIceCreamFlavors = 15;

switch (numberOfIceCreamFlavors) {
    case 15:
        System.out.println("Nice selection.");
        break;
    case 1:
        System.out.println("I bet it's vanilla.");
        break;
    default:
        System.out.println("Unknown number of flavors.");
        break;
}

```

---

### 4.1.1 Non-Graded Activity

```java
import java.util.Scanner;

public class SwitchClass {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Type a number that represents your lucky day");
        int luckyDay = keyboard.nextInt();

        switch (luckyDay) {
            case 1:
                System.out.println("Your lucky day is Monday");
                break;
            case 2:
                System.out.println("Your lucky day is Tuesday");
                break;
            case 3:
            case 4:
            case 5:
                System.out.println("Your lucky day is Wednesday, Thursday or Friday");
                System.out.println("is acceptable.");
                break;
            default:
                System.out.println("Your lucky day is either Saturday or Sunday");
                break;
        }
    }
}

```

# 4. The Switch Statement

### 📌 Purpose

- Implements **multiway branching** in Java.

---

### 📝 Syntax

```java
switch (Controlling_Expression) {
    case Case_Label_1:
        // code
        break;
    case Case_Label_2:
        // code
        break;
    default:
        // code if no case matches
        break;
}

```

---

### ⚖️ Key Rules

- Controlling expression must be: `char`, `int`, `short`, `byte`, or (Java 7+) `String`.
- Each **case label** must be the same type as the controlling expression.
- Labels can be in any order but must be **unique**.
- `break;` ends execution of a case.
- If `break` is omitted → execution **falls through** to the next case.

---

### 4.1 Default Section

- Handles all values **not explicitly matched** by any case.
- **Optional**, but good practice to include.
- Usually placed **last**.

---

### ✅ Example

```java
int numberOfIceCreamFlavors = 15;

switch (numberOfIceCreamFlavors) {
    case 15:
        System.out.println("Nice selection.");
        break;
    case 1:
        System.out.println("I bet it's vanilla.");
        break;
    default:
        System.out.println("Unknown number of flavors.");
        break;
}

```

---

### 4.1.1 Non-Graded Activity

```java
import java.util.Scanner;

public class SwitchClass {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Type a number that represents your lucky day");
        int luckyDay = keyboard.nextInt();

        switch (luckyDay) {
            case 1:
                System.out.println("Your lucky day is Monday");
                break;
            case 2:
                System.out.println("Your lucky day is Tuesday");
                break;
            case 3:
            case 4:
            case 5:
                System.out.println("Your lucky day is Wednesday, Thursday or Friday");
                System.out.println("is acceptable.");
                break;
            default:
                System.out.println("Your lucky day is either Saturday or Sunday");
                break;
        }
    }
}

```

# 🏗️ 4 Constructors

## 🧠 4.1 Constructor Basics

### ✳️ Key Concept

- Special method to **initialize instance variables**.
- Must have **same name as class** and **no return type**.
- Often **overloaded**.

### 💡 Example

```java
public class BankAccount {
    public BankAccount(String id, String name, double balance) { … }
}

```

---

## 🧠 4.2 Constructor Call

### ✳️ Key Concept

- Called automatically with `new`:
    
    ```java
    ClassName obj = new ClassName(args);
    
    ```
    
- Each `new` creates a **new object**.

```java
A a1 = new A();
A a2 = new A(); // distinct objects

```

---

## 🧠 4.3 Invoking Methods Inside Constructors

### 💡 Example

```java
public BankAccount(String name) {
    this.customer_name = name;
    setAccountNumber(getAccountNumber() + 1);
    setBalance(0.0);
}

```

- One constructor can call another:
    
    ```java
    public BankAccount(String name, int accountNumber, int amount) {
        this(accountNumber, amount);
        this.customer_name = name;
    }
    
    ```
    

---

## 🧠 4.4 No-Argument Constructor

- If **no constructor** is defined, Java provides a **default no-argument** one.
- If **any constructor** is defined, you must create your own no-arg constructor if needed.

**Example Practice:**

- Write a class with:
    - No-arg constructor
    - One-arg constructor
    - Two-arg constructor
        
        ➡️ This is **constructor overloading**.
        

---

# 🧩 Flashcard-Ready Summary

| 🔑 Concept | 🧠 Definition / Example |
| --- | --- |
| **Method Use** | Call methods to perform actions or return values; void = no return. |
| **Method Parameters** | Formal vs actual parameters; Java uses call-by-value. |
| **Automatic Conversion** | Java auto-promotes compatible types (e.g., int → double). |
| **Local Variables** | Declared within a method; parameters act as locals. |
| **Overloading** | Same name, different parameters; compile-time decision. |
| **Constructor** | Initializes new objects; same name as class, no return. |

# 5. Loops in Java

Loops allow you to **repeat a block of code** multiple times. Each repetition is called an **iteration**, and the code inside the loop is called the **loop body**.

Java has **three types of loops**:

1. `while` loop
2. `do-while` loop
3. `for` loop

---

## 5.1 while Statement

- Executes the loop **only if** the Boolean expression is true.
- **Condition is checked before** each iteration.
- Loop body can be **a single statement** or **multiple statements enclosed in braces `{}`**.

**Syntax:**

```java
while (Boolean_Expression)
    Statement;

```

Or with a compound body:

```java
while (Boolean_Expression) {
    Statement_1;
    Statement_2;
    ...
    Statement_Last;
}

```

---

## 5.2 do-while Statement

- Executes the loop body **at least once**.
- Boolean expression is **checked after** the loop body executes.
- Acts like a `while` loop after the first iteration.
- Loop body can also be **single or compound statements**.
- **Important:** there is a **semicolon after the Boolean expression**.

**Syntax:**

```java
do
    Statement;
while (Boolean_Expression);

```

Or with a compound body:

```java
do {
    Statement_1;
    Statement_2;
    ...
    Statement_Last;
} while (Boolean_Expression);

```

---

## 5.3 Example: while vs do-while

```java
package lesson03;

public class WhileExample {

    public static void main(String[] args) {
        int countDown;

        System.out.println("First while loop:");
        countDown = 5;
        while (countDown > 0) {
            System.out.println("Hello");
            countDown -= 1;
        }

        System.out.println("Second while loop:");
        countDown = 0;
        while (countDown > 0) { // Won't run
            System.out.println("Hello");
            countDown -= 1;
        }

        System.out.println("First do-while loop:");
        countDown = 5;
        do {
            System.out.println("Hello");
            countDown -= 1;
        } while (countDown > 0);

        System.out.println("Second do-while loop:");
        countDown = 0;
        do { // Executes at least once
            System.out.println("Hello");
            countDown -= 1;
        } while (countDown > 0);
    }
}

```

**Key takeaway:**

- `while` may not execute if the condition is false at the start.
- `do-while` **always executes at least once**.

# 5. Loops in Java (continued)

## 5.4 The `for` Statement

The `for` loop is commonly used to iterate over a range of values with a control variable.

**Syntax:**

```java
for (Initializing; Boolean_Expression; Update) {
    Statement_1;
    Statement_2;
    ...
    Statement_Last;
}

```

- **Initializing:** Set up control variable(s). Can declare multiple variables separated by commas.
- **Boolean_Expression:** Condition checked before each iteration.
- **Update:** Changes control variable(s) after each iteration. Can contain multiple updates separated by commas.
- **Body:** Single or compound statements.

**Examples:**

```java
// Single statement
for (int i = 0; i < 3; i++)
    System.out.println("i is " + i);

// Multiple statements
int j = 0;
for (int i = 0; i < 3; i++) {
    j += 1;
    System.out.println("hello " + j);
    System.out.println("j is " + j);
}

```

**Multiple Initialization Example:**

```java
int j = 0;
for (int i = 0; (i + j) < 6; i++) {
    j++;
    System.out.println("i and j: " + i + " " + j);
}

```

**Multiple Updates Example:**

```java
for (int i = 0, j = 0; (i + j) < 6; i++, j++, System.out.println("i and j: " + i + " " + j));

```

---

## 5.4.1 Infinite Loops

- Loops must modify the condition to eventually terminate.
- Equality (`==`) and inequality (`!=`) checks with `double` or `float` may cause **infinite loops** due to precision errors.
- Example of risky loop:

```java
double x = 1.0 / 3;
for (int i = 0, j = 0; x != 0.33333; i++) {
    j++;
    System.out.println("i and j: " + i + " " + j);
}

```

- A `for(;;)` statement is a valid infinite loop.

---

## 5.4.2 Nested Loops

- Loops can be **nested** like other control structures.
- Inner loop executes **completely** for every iteration of the outer loop.

**Example:**

```java
for (int rowNum = 1; rowNum <= 3; rowNum++) {
    for (int columnNum = 1; columnNum <= 2; columnNum++) {
        System.out.print("row " + rowNum + " column " + columnNum + " ");
    }
    System.out.println();
}

```

---

## 5.5 For-each Loop (Enhanced for loop)

- Introduced in **Java 5** for **arrays** and **collections**.
- Iterates through elements **without using indices**.

**Syntax:**

```java
for (type var : arrayOrCollection) {
    body-of-loop;
}

```

**Array Example:**

```java
double sum = 0;
double[] price = {1.5, 2.5, 3.5, 4, 0.5};

// Basic for loop
for (int i = 0; i < price.length; i++)
    sum += price[i];
System.out.println(sum);

// For-each loop
sum = 0;
for (double p : price)
    sum += p;
System.out.println(sum);

```

**Collection Example:**

```java
Collection<String> myCollectionItem = new ArrayList<>();
myCollectionItem.add("1 - H - Hydrogen");
myCollectionItem.add("2 - He - Helium");
myCollectionItem.add("3 - Li - Lithium");

System.out.println("Using iterator:");
Iterator<String> iter = myCollectionItem.iterator();
while (iter.hasNext()) {
    System.out.println(iter.next());
}

System.out.println("Using for-each:");
for (String item : myCollectionItem)
    System.out.println(item);

```

**Rules for For-each Loop:**

- Loop variable **cannot be assigned** inside the loop.
- Can **only iterate one collection** at a time.
- Iterates **forward by single steps**.

# 5.6 The `break` and `continue` Statements

### `break`

- Syntax: `break;`
- Immediately **terminates the nearest enclosing loop or switch statement**.
- Control moves to the statement immediately after the loop or switch.
- Does **not** terminate the program.

**Example – break in inner loop:**

```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println(i + " , " + j);
        break;  // exits inner loop only
    }
}

```

**Output:**

```
0 , 0
1 , 0
2 , 0

```

---

### `continue`

- Syntax: `continue;`
- Ends the **current iteration** of the nearest enclosing loop.
- Control moves to the **next iteration** of the loop.
- In a `for` loop, it transfers control to the **update expression**.

**Example – continue in nested loop:**

```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i >= 1)
            continue;
        System.out.println(i + " , " + j);
    }
}

```

**Output:**

```
0 , 0
0 , 1
0 , 2

```

---

# 5.7 Labeled Break Statement

- Used to **break out of an outer loop** from an inner loop.
- Syntax:

```java
labelName: for(...) {
    for(...) {
        break labelName;  // exits the labeled loop
    }
}

```

**Example:**

```java
endBothLoops:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println(i + " , " + j);
        break endBothLoops;
    }
}

```

**Output:**

```
0 , 0

```

- Similarly, `continue` can be used with labels in Java 8+.

---

# 5.7.1 Program Termination

- `System.exit(0);` immediately terminates the **entire program**.
- The argument `0` indicates a normal termination.

---

# 5.8 Common Loop Errors

1. **Infinite loops:** Condition never becomes false.
2. **Off-by-one errors:** Loop executes **one extra or one fewer iteration** than intended.
3. **Floating-point comparisons:** Avoid `==` or `!=` in Boolean expressions for `float`/`double`.

# 5.9 Java Iterator Interface

The **Iterator** interface in Java provides a standard way to traverse elements in any collection (like `ArrayList`, `HashSet`, etc.).

---

### Using a `for` loop with ArrayList:

```java
ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.add("Cherry");

for (int i = 0; i < list.size(); i++) {
    String s = list.get(i);
    System.out.println(s);
}

```

### Using an `Iterator`:

```java
Iterator<String> itr = list.iterator();
while (itr.hasNext()) {
    String s = itr.next();
    System.out.println(s);
}

```

**Key Points:**

- `iterator()` returns an `Iterator` object for the collection.
- `hasNext()` checks if there are more elements to traverse.
- `next()` returns the next element in the collection.
- Using `Iterator` is preferred when you want to remove elements safely during iteration.

---

# 5.10 Assertion Checks

An **assertion** is a statement that tests a condition which should always be true if the program is running correctly.

### Syntax:

```java
assert Boolean_Expression;   // Example: assert database_version == 1.2;

```

- If the expression evaluates to **true**, the program continues normally.
- If **false**, the program throws an `AssertionError` and stops execution.
- Assertions are mainly used for **debugging and testing**, not for production logic.

---

### Enabling Assertions

By default, assertions are **disabled**. To enable them:

**Command line:**

```bash
java -enableassertions ProgramName

```

Or using **Eclipse configuration**, enable assertions in the runtime settings.

---

### Example Use Case:

```java
double database_version = 1.0;
assert database_version == 1.2;  // Throws AssertionError if false

```

- Helps ensure assumptions in your code are valid.
- Useful in team environments to catch version mismatches or logic errors early.

---

**Summary Table**

| Feature | Description | Example |
| --- | --- | --- |
| Iterator | Traverses elements in collections | `itr.next()` |
| hasNext() | Checks if more elements exist | `itr.hasNext()` |
| Assertions | Verifies conditions during runtime | `assert x > 0;` |
| Enabling assertions | Must be enabled explicitly | `java -enableassertions ProgramName` |

# 6 Generating Random Numbers

Java provides the **`Random`** class in the `java.util` package to generate pseudo-random numbers. These are **not truly random**, but are sufficiently unpredictable for most applications.

---

### Importing the Random Class

```java
import java.util.Random;

```

### Creating a Random Object

```java
Random rnd = new Random();

```

---

### Generating Random Numbers

| Method | Description | Example |
| --- | --- | --- |
| `nextInt(n)` | Random integer from `0` to `n-1` | `int i = rnd.nextInt(10); // 0-9` |
| `nextDouble()` | Random double between `0.0` (inclusive) and `1.0` (exclusive) | `double d = rnd.nextDouble();` |
| `nextBoolean()` | Random boolean value (`true` or `false`) | `boolean b = rnd.nextBoolean();` |
| `nextLong()` | Random long value | `long l = rnd.nextLong();` |
| `nextFloat()` | Random float between `0.0` and `1.0` | `float f = rnd.nextFloat();` |

---

### Example: Simulating a Coin Flip

```java
package lesson03;

import java.util.Random;

public class CoinFlipDemo {

    public static void main(String[] args) {
        Random randomGenerator = new Random();
        int counter = 1;

        while (counter <= 5) {
            System.out.print("Flip number " + counter + ": ");
            int coinFlip = randomGenerator.nextInt(2); // 0 or 1

            if (coinFlip == 1)
                System.out.println("Heads");
            else
                System.out.println("Tails");

            counter++;
        }
    }
}

```

**Explanation:**

- `nextInt(2)` generates either `0` or `1`.
- The `if` statement checks the value to print “Heads” or “Tails”.
- The loop runs 5 times, simulating 5 coin flips.

---

### Tips:

- You can experiment with other `Random` methods like `nextDouble()`, `nextLong()`, `nextBoolean()`, or even generate numbers in a custom range.
- Random numbers are **pseudo-random**, meaning if you use the same seed (optional in `new Random(seed)`), the sequence of numbers is repeatable.

| Keyword | Description & Notes |
| --- | --- |
| **assert** | Checks a Boolean condition; throws `AssertionError` if false; mainly used for debugging. |
| **break** | Exits the nearest enclosing loop or `switch`; can be labeled to exit outer loops in nested loops. |
| **continue** | Skips the rest of the current loop iteration; in a `for` loop, moves to the update expression. |
| **do-while** | Executes the loop body **at least once**, then checks the condition; ends if false. |
| **for-each** | Enhanced loop to iterate arrays or collections; cannot modify loop variable; one element at a time. |
| **if-else** | Executes one branch if condition is true, another if false; can be nested or multiway (`else if`). |
| **iterator** | Interface to traverse collections; `hasNext()` checks for next element, `next()` retrieves it. |
| **java short-circuits** | Logical operators `&&` and ` |
| **labeled break** | Break with a label to exit a specific outer loop in nested loops. |
| **switch** | Multiway branching; executes the case that matches the controlling expression; use `break` to stop. |
| **ternary operator** | Compact `if-else` expression: `(condition) ? valueIfTrue : valueIfFalse`. |
| **while** | Executes the loop body **only if** the condition is true; condition checked before each iteration. |

### Notes & Tips:

- **Break & continue** are best used sparingly; overuse can make loops hard to read.
- **For-each** simplifies loops over arrays/collections, but can’t modify the elements directly.
- **Assertions** are mostly for development/testing, not production.
- **Ternary operator** is ideal for short, conditional assignments.
- **Infinite loops** often happen with `while(true)` or incorrect Boolean conditions; watch `==` with floating-point numbers.

## 📘 CP213 Lab 02: Strings – Fall 2025

**Due:** Sept 25, 2025 @ 11:59 PM

### 🔑 Key Distinction: `char` vs `String`

| **char** | **String** |
| --- | --- |
| primitive type | class type |
| `'x'` (single quotes) | `"David"` (double quotes) |
| cannot be null | can be null |
| cannot be empty | can be empty (`""`) |
| compared with `==`, `<`, `>` | compared with `.equals`, `.compareTo` |

---

### 🧩 String Class Basics

- Cannot access characters directly with `string[index]`.
- Use:
    - `charAt(int index)`
    - `toCharArray()`

---

### ✅ Equality

- `string1.equals(string2)` → returns **true/false**.
- Must be initialized (check `string1 != null`).
- `==` checks **reference**, not value.

---

### 🗃️ String Pool vs Heap

- Direct assignment (`String s = "David"`) → checks string pool.
- `new String("David")` → always creates a **new object in heap**.

**Example:**

```java
String s1 = "David";
String s2 = s1;
String s3 = "David";
String s4 = new String("David");

System.out.println(s1 == s3);     // true (same pool ref)
System.out.println(s1 == s4);     // false (different object)
System.out.println(s1.equals(s4));// true (same value)

```

---

### 🔍 compareTo Method

- Lexical (dictionary) ordering.

```java
s1.compareTo(s2)

```

- `0` → equal
- `< 0` → `s1` comes **before** `s2`
- `> 0` → `s1` comes **after** `s2`

---

### 🅰️ Character Class

- Used for static methods on `char`.
- Example:

```java
Character.isLowerCase('a'); // true
Character.isLowerCase('A'); // false

```

# 📒 CP213 – Full Glossary (Lesson Keywords)

### 🔹 Core OOP & Class Concepts

- **Object** → An instance of a class that contains state (fields) and behavior (methods).
- **Constructor** → Special method that runs when an object is created to initialize fields.
- **Default constructor** → A constructor with no parameters; provided automatically if no constructors are written.
- **Argument-constructor** → A constructor that accepts arguments to initialize object fields with custom values.
- **Instance variable** → Variables declared inside a class but outside methods; represent object state.

---

### 🔹 Methods & Calls

- **Method** → A block of code that performs an action; belongs to a class or object.
- **Method call (invocation)** → The act of running a method using `object.methodName()`.
- **Method argument** → Actual value passed into a method when it is called.
- **Method parameter** → Variable defined in the method declaration that receives the argument.
- **Method signature** → Includes the method name and parameter list (not return type).
- **Return type** → Declares the type of value a method returns (e.g., `int`, `String`, `void`).

---

### 🔹 Method Behaviors

- **Overloading** → Defining multiple methods with the same name but different parameter lists.
- **Overloading and automatic type conversion** → When Java automatically converts arguments (e.g., `int` → `double`) to match an overloaded method.
- **Overriding** → A subclass provides a new implementation for a method inherited from a superclass.

---

### 🔹 Access Control & Modifiers

- **Default modifier** → When no access modifier is given, visibility is package-private.
- **Public** → Accessible from any other class.
- **Private** → Accessible only within the same class.
- **Protected** → Accessible within the same package and subclasses.

---

### 🔹 Encapsulation & Data Management

- **Encapsulation** → Bundling data and methods together, controlling access with modifiers.
- **Information hiding** → Keeping object details private and exposing only necessary methods.
- **Set and get methods (mutators/accessors)** → Used to safely update or retrieve private variable values.
- **“this” argument** → Refers to the current object; used to differentiate between fields and parameters.

---

### 🔹 Interfaces & Inheritance

- **Extends** → Keyword for inheritance; a class extends another class to inherit behavior.
- **Implements** → Keyword for implementing an interface in a class.
- **Interface** → A collection of abstract methods that define a contract for classes to follow.

---

### 🔹 Utility & Overrides

- **equals() method** → Compares the value/content of two objects.
- **hashCode() method** → Returns a numerical hash representation of an object; must be consistent with equals.
- **toString() method** → Returns a string description of an object (useful for debugging).

---

### 🔹 Miscellaneous

- **Call by value** → In Java, method arguments are always passed by value (a copy is made).