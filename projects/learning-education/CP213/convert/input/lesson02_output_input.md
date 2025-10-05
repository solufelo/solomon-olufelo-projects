# Lesson 02: Output, Input, and Formatting

## **System.out.print and System.out.println**

- Used for output to the console.
- `print` displays text without a new line.
- `println` displays text and moves the cursor to the next line.

**System.out.println("The year is " + 2020);**

## **printf Method**

Printf allows us to have much more control over our output code. The println, print, and printf methods are all from the PrintStream class.

The java method printf does not advance to the next line after outputting.

The printf method can have any number of arguments. The first argument is always a string that contains format specifiers for the remaining arguments. All arguments except the first one are values for output to the screen.

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

## **2 Java NumberFormat class**

### **2.1 Specifying Locale**

You can explicitly specify the currency symbol for your output. To do so, you need to provide a location from the **Locale** class as an argument to the **getCurrencyInstance()** method. You also need to import the Locale class to your code, **import java.util.Locale;**

In the example below, we use the print method for formatting money in three different ways, default (which is American), English, and Germany formatting.The output format is changed based on the Locale value passed to the ***getCurrencyInstance**() method.*

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
        moneyFormatter = NumberFormat.getCurrencyInstance(Locale.ENGLISH);
        print();
        System.out.println("Germany location:");
        moneyFormatter = NumberFormat.getCurrencyInstance(Locale.GERMANY);
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

The **NumberFormat** class has other uses such as formatting the output as a percentage, setting the minimum and the maximum number of digits to your output, rounding the output and parse numbers, etc. These uses are described in the Oracle documentation that you can refer to when needed.

## **🌍 Java Locale & Currency Formatting (NumberFormat)**

- **`NumberFormat.getCurrencyInstance()`** → Formats numbers as money based on locale.
- **Default locale** = your system's region (often `Locale.US` → `$`).
- **Language-only locales** (e.g., `Locale.ENGLISH`) → show **generic currency sign ¤**, because no country is specified.
- **Country-specific locales** → show correct currency & formatting rules.

### **🔑 Examples**

```java
NumberFormat.getCurrencyInstance();        // Default (US) → $39.80
NumberFormat.getCurrencyInstance(Locale.ENGLISH); // Generic → ¤39.80
NumberFormat.getCurrencyInstance(Locale.GERMANY); // Euro → 39,80 €
```

### **🌐 Common Locales**

- `Locale.US` → `$`
- `Locale.CANADA` → `$`
- `Locale.UK` → `£`
- `Locale.JAPAN` → `￥`
- `Locale.GERMANY` → `€`

👉 Use **language + country locale** (e.g., `Locale.US`) instead of just `Locale.ENGLISH` to get real currency symbols.

## **📦 Lesson 02 – Importing Packages & Classes**

### **🔹 What is a Package?**

- A **package** = collection of related classes & interfaces.
- Stored in **JAR files** (Java Archive).
- Helps organize source code like folders (e.g., keep HTML, images, scripts, Java classes separate).
- Example: `java.lang`, `java.util`, `java.text`.

### **🔹 Why Use Packages?**

- Keeps code **organized**.
- Groups related classes together.
- Makes large projects **manageable**.
- Allows code to be **reused & shared**.

### **🔹 Importing Packages**

- Some packages are imported **automatically** (e.g., `java.lang` → `Math`, `String`, wrapper classes).
- To use others, you need the **import statement**:
    
    ```java
    import java.text.NumberFormat;   // import one class
    import java.text.*;              // import entire package
    ```
    
- Import statements must be at the **top of the file**, after `package` (if any) and before your class.

### **🔹 Creating Your Own Package**

1. Group related classes into a **folder**.
2. Add a `package` statement at the **top of each file**:
    
    ```java
    package mypackage;
    ```
    
3. Folder structure must match the package name.

### **🔹 Example**

```java
package wlu.cp213.lesson02;

import java.util.Scanner;

public class FormatedOutput { … }
```

### **🔹 Key Classes Used So Far**

- `NumberFormat` → from `java.text` (for money formatting).
- `Locale` → from `java.util` (for regional settings).

## **🔢 Lesson 02 – Java DecimalFormat Class**

### **🔹 What it Does**

- `DecimalFormat` = class for **custom number formatting**.
- Can format numbers as **percentages, fixed decimals, or scientific (E) notation**.
- Requires `import java.text.DecimalFormat;`.

### **🔹 Example Code**

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

### **🔹 Output**

```
30.80%
1.2346E2
12.346E1
1.235E-5
12.346E-6
```

### **🔹 Key Notes**

- `"0.00%"` → formats as **percentage**.
- `"#0.###E0"` → **scientific notation**, 1+ digit before decimal (flexible).
- `"00.###E0"` → **scientific notation**, **forces 2 digits** before decimal.
- Great for **percentages, small numbers, large numbers**.

## **⌨️ Lesson 02 – Scanner Class (User Input)**

### **🔹 Overview**

- `Scanner` (since Java 5.0) = simple way to read user input.
- Part of `java.util` package → must `import java.util.Scanner;`.
- Works as a **wrapper** for `System.in` (keyboard input).
- Similar to:
    - `input()` in Python
    - `cin >>` in C++

### **🔹 Creating a Scanner Object**

```java
Scanner keyboard = new Scanner(System.in);
Scanner input = new Scanner(System.in); // can use any variable name
```

### **🔹 Common Methods**

- `nextInt()` → reads an `int`
- `nextDouble()` → reads a `double`
- `next()` → reads a **single word** (stops at whitespace)

⚡ Multiple inputs → separated by whitespace, read with multiple method calls.

### **🔹 Example**

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

👉 The `Scanner` class makes input handling easier than using `System.in` directly.

## **⌨️ Lesson 02 – Scanner Class (Extended Notes)**

### **🔹 5.2 nextLine() Method**

- Reads an **entire line** (until `\n` – Enter key).
- The returned string **does not include** the `\n`.

```java
String inputLine = keyboard.nextLine();
```

### **🔹 5.3 Example: Mixed Input Types**

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

### **🔹 5.4 End-of-Line Issues**

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

### **🔹 5.5 Empty String**

- If user presses Enter **without typing**, `nextLine()` returns `""` (empty string).

### **🔹 5.6 Custom Delimiters**

Default = whitespace. Can be changed with `useDelimiter()`.

```java
Scanner input = new Scanner(System.in);
input.useDelimiter("end"); // now "end" is the delimiter
```

👉 **Key Takeaway:**

Use `nextLine()` carefully with other input methods. Clear the buffer if needed.

## **📘 Lesson 02 – Wrapper Classes in Java**

### **🔹 What are Wrapper Classes?**

- Java is **object-oriented** → many APIs (Collections, Serialization, Synchronization) work only with **objects**.
- Wrapper classes convert **primitive types ↔ objects**.
- Since Java 5.0:
    - **Autoboxing** → primitive → object (automatic)
    - **Unboxing** → object → primitive (automatic)

### **🔹 Examples of Autoboxing & Unboxing**

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

### **🔹 Useful Constants**

- `Integer.MAX_VALUE`, `Integer.MIN_VALUE`
- `Double.MAX_VALUE`, `Double.MIN_VALUE`
- `Boolean.TRUE`, `Boolean.FALSE`

### **🔹 Useful Static Methods**

- **Convert String → Number:**
    - `Integer.parseInt("123") → 123`
    - `Double.parseDouble("3.14") → 3.14`
- **Convert Number → String:**
    - `Double.toString(123.99) → "123.99"`

### **🔹 Example: String to Double Conversion**

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

✅ **Key Takeaway:** Wrapper classes bridge **primitives ↔ objects**, making them essential for Java collections, parsing, and data conversion.

## **📝 Java Wrapper Class Cheatsheet**

### **🔹 Wrapper Classes**

| Primitive | Wrapper Class |
|-----------|---------------|
| boolean   | Boolean       |
| char      | Character     |
| byte      | Byte          |
| short     | Short         |
| int       | Integer       |
| long      | Long          |
| float     | Float         |
| double    | Double        |

### **🔹 Common Constants**

| Wrapper | Max Value | Min Value |
|---------|-----------|-----------|
| Integer | `Integer.MAX_VALUE` | `Integer.MIN_VALUE` |
| Double  | `Double.MAX_VALUE` | `Double.MIN_VALUE` |
| Long    | `Long.MAX_VALUE` | `Long.MIN_VALUE` |
| Float   | `Float.MAX_VALUE` | `Float.MIN_VALUE` |
| Boolean | `Boolean.TRUE`, `Boolean.FALSE` | – |

### **🔹 Conversion Methods**

| Purpose | Method Example | Result |
|---------|----------------|--------|
| String → int | `Integer.parseInt("123")` | `123` (int) |
| String → double | `Double.parseDouble("3.14")` | `3.14` (double) |
| String → long | `Long.parseLong("99999")` | `99999` (long) |
| String → boolean | `Boolean.parseBoolean("true")` | `true` (bool) |
| String → wrapper object | `Integer.valueOf("123")` | `Integer(123)` |
| Wrapper → String | `Double.toString(12.34)` | `"12.34"` |
| Primitive → String | `String.valueOf(10)` | `"10"` |
| Wrapper → primitive | `int x = myInteger.intValue();` | `123` (int) |

### **🔹 Autoboxing & Unboxing**

```java
// Autoboxing
Integer a = 10;     // int → Integer
Double d = 3.14;    // double → Double

// Unboxing
int x = a;          // Integer → int
double y = d;       // Double → double
```

✅ **Quick Rule of Thumb:**

- `parseXxx()` → returns **primitive**
- `valueOf()` → returns **wrapper object**
- `toString()` / `String.valueOf()` → returns **String**

## **Key Terms Glossary**

| Keyword | Description & Notes |
|---------|-------------------|
| **Autoboxing** | Automatically converts primitive types (like `int`, `double`) into their wrapper class objects (`Integer`, `Double`) for use in contexts that require objects. |
| **DecimalFormat class** | Formats numbers into readable strings according to patterns, such as percentages, scientific notation, or fixed decimal places. |
| **format()** | Method used in classes like `PrintStream` or `DecimalFormat` to create formatted output for numbers, text, or dates. |
| **format specifier** | Placeholder in `printf()` or `format()` methods that defines how a value should be displayed (e.g., `%d` for integers, `%f` for floats). |
| **getCurrencyInstance()** | Method from `NumberFormat` that returns a currency formatter for a locale, automatically applying the correct currency symbol. |
| **Locale** | Represents a specific geographic, political, or cultural region, used for formatting numbers, currencies, and dates. |
| **nextInt(), nextDouble(), etc.** | `Scanner` methods that read input as specific primitive types, such as integers or doubles, from keyboard or files. |
| **nextLine() and hasNextLine()** | `nextLine()` reads an entire line of input; `hasNextLine()` checks if another line of input exists. |
| **NumberFormat class** | Formats numbers according to locale, including currencies and percentages, for readable or region-appropriate output. |
| **print, println, printf** | Methods of `PrintStream` for output; `print()` writes without newline, `println()` adds a newline, `printf()` allows formatted output. |
| **PrintStream** | Class providing methods like `print()`, `println()`, and `printf()` to write formatted data to console or other streams. |
| **Scanner class** | Reads input from keyboard, files, or strings, supporting multiple data types and custom delimiters. |
| **Unboxing** | Automatically converts wrapper class objects back into their corresponding primitive types. |
| **valueOf** | Static method in wrapper classes converting a primitive type or string into its corresponding object (e.g., `Integer.valueOf(5)`). |
| **Wrapping** | Converting a primitive type into its corresponding wrapper class object to allow usage in object-required contexts. |



