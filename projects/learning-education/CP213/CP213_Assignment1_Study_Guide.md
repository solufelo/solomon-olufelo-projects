# CP213 Assignment 1 - Complete Study Guide

**Author:** Solomon Olufelo (210729170) - oluf9170@mylaurier.ca  
**Assignment:** A01 - Simple Methods  
**Due:** October 5, 2025, 11:59 PM  
**Project:** oluf9170_a01

---

## 📋 Assignment Overview

### Classes to Implement
- [x] **Cipher** - Encryption algorithms ✅ COMPLETED
- [ ] **LeapYear** - Calendar calculations
- [ ] **Numbers** - Mathematical operations
- [ ] **SerialNumber** - String validation & file processing
- [ ] **Strings** - Advanced string manipulation

### Key Requirements
- All methods are `static` - no object creation needed
- Package: `cp213` (do not change)
- Add name, ID, email to all files
- Generate Javadoc documentation
- Test thoroughly in `testing.txt`
- Export as `oluf9170_a01.zip`

---

## 🔐 CIPHER CLASS ✅ COMPLETED

### Core Concepts
- **Modular arithmetic** for alphabet wrapping
- **Character-to-position mapping**: `char - 'A'` gives position (0-25)
- **Position-to-character mapping**: `(char)('A' + position)` gives character

### Key Methods
```java
// Shift cipher: move each letter n positions
public static String shift(String string, int n)

// Substitution cipher: replace using cipher alphabet  
public static String substitute(String string, String ciphertext)
```

### Critical Implementation Details
```java
// Handle negative shifts correctly
int newPosition = (originalPosition + n % ALPHA_LENGTH + ALPHA_LENGTH) % ALPHA_LENGTH;

// Always convert to uppercase first
String upperString = string.toUpperCase();

// Use StringBuilder for efficiency
StringBuilder result = new StringBuilder();
```

---

## 📅 LEAPYEAR CLASS

### Core Concept: Leap Year Rules
1. **Divisible by 4** → leap year
2. **EXCEPT divisible by 100** → not leap year  
3. **EXCEPT divisible by 400** → leap year

### Methods to Implement

#### `isLeapYear(int year)`
**Algorithm:**
```java
return (year % 4 == 0) && (year % 100 != 0 || year % 400 == 0);
```

**Examples:**
- 2000: ✅ (divisible by 400)
- 1900: ❌ (divisible by 100, not 400)
- 2004: ✅ (divisible by 4, not 100)
- 2001: ❌ (not divisible by 4)

#### `leapYearsBetween(int start, int end)`
**Algorithm:**
```
count = 0
for year from (start + 1) to (end - 1):
    if isLeapYear(year):
        count++
return count
```

#### `dayOfYear(int year, int month, int day)`
**Algorithm:**
```java
int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
if (isLeapYear(year)) daysInMonth[1] = 29;

int totalDays = day;
for (int i = 0; i < month - 1; i++) {
    totalDays += daysInMonth[i];
}
return totalDays;
```

---

## 🔢 NUMBERS CLASS

### Method 1: `closest(double target, double v1, double v2)`
**Concept:** Find which value is closer to target using absolute distance.

**Algorithm:**
```java
double distance1 = Math.abs(target - v1);
double distance2 = Math.abs(target - v2);
return (distance1 <= distance2) ? v1 : v2;  // v1 wins ties
```

### Method 2: `isPrime(int n)`
**Concept:** Prime numbers have exactly 2 factors: 1 and themselves.

**Algorithm:**
```java
if (n <= 1) return false;
if (n == 2) return true;
if (n % 2 == 0) return false;  // Even numbers > 2 not prime

// Check odd divisors up to √n
for (int i = 3; i * i <= n; i += 2) {
    if (n % i == 0) return false;
}
return true;
```

**Why √n?** If n has a factor > √n, it must also have a factor < √n.

### Method 3: `sumPartialHarmonic(int n)`
**Concept:** Sum of series: 1/1 + 1/2 + 1/3 + ... + 1/n

**Algorithm:**
```java
double sum = 0.0;
for (int i = 1; i <= n; i++) {
    sum += 1.0 / i;  // Use 1.0 for floating-point division
}
return sum;
```

---

## 🏷️ SERIALNUMBER CLASS

### Method 1: `allDigits(String string)`
**Concept:** Check if all characters are digits (0-9).

**Algorithm:**
```java
for (int i = 0; i < string.length(); i++) {
    if (!Character.isDigit(string.charAt(i))) {
        return false;
    }
}
return true;  // Empty string returns true
```

### Method 2: `validSn(String sn)`
**Concept:** Validate format `SN/nnnn-nnn` where n = digit.

**Pattern Requirements:**
- Length exactly 10
- Starts with "SN/"
- Positions 3-6: digits
- Position 7: "-"
- Positions 8-10: digits

**Algorithm:**
```java
if (sn.length() != 10) return false;
if (!sn.startsWith("SN/")) return false;
if (sn.charAt(7) != '-') return false;

// Check digits in positions 3-6 and 8-10
for (int i = 3; i <= 6; i++) {
    if (!Character.isDigit(sn.charAt(i))) return false;
}
for (int i = 8; i <= 9; i++) {
    if (!Character.isDigit(sn.charAt(i))) return false;
}
return true;
```

### Method 3: `validSnFile(Scanner fileIn, PrintStream goodSns, PrintStream badSns)`
**Concept:** Process file line by line, validate each serial number.

**Algorithm:**
```java
while (fileIn.hasNextLine()) {
    String line = fileIn.nextLine();
    if (validSn(line)) {
        goodSns.println(line);
    } else {
        badSns.println(line);
    }
}
```

---

## 🎭 STRINGS CLASS

### Method 1: `isPalindrome(String string)`
**Concept:** Reads same forwards/backwards, ignoring case, spaces, punctuation.

**Algorithm:**
```java
// Clean string: keep only letters, convert to lowercase
StringBuilder clean = new StringBuilder();
for (char c : string.toCharArray()) {
    if (Character.isLetter(c)) {
        clean.append(Character.toLowerCase(c));
    }
}

// Compare with reverse
String cleanStr = clean.toString();
String reversed = clean.reverse().toString();
return cleanStr.equals(reversed);
```

### Method 2: `isValid(String name)`
**Concept:** Valid Java variable name rules.

**Rules:**
- Not empty or just "_"
- First char: letter or underscore
- Rest: letters, digits, underscores

**Algorithm:**
```java
if (name == null || name.isEmpty() || name.equals("_")) {
    return false;
}

char first = name.charAt(0);
if (!Character.isLetter(first) && first != '_') {
    return false;
}

for (int i = 1; i < name.length(); i++) {
    char c = name.charAt(i);
    if (!Character.isLetterOrDigit(c) && c != '_') {
        return false;
    }
}
return true;
```

### Method 3: `pigLatin(String word)`
**Concept:** Transform to Pig Latin with vowel/consonant rules.

**Rules:**
- Vowel start: add "way"
- Consonant start: move consonants to end + "ay"
- 'y' is consonant at start, vowel elsewhere
- Preserve capitalization

**Algorithm:**
```java
if (word.isEmpty()) return word;

String vowels = "aeiouAEIOU";
int firstVowel = 0;

// Find first vowel (handle 'y' special case)
for (int i = 0; i < word.length(); i++) {
    char c = word.charAt(i);
    if (vowels.indexOf(c) != -1 || (c == 'y' || c == 'Y') && i > 0) {
        firstVowel = i;
        break;
    }
}

String result;
if (firstVowel == 0) {
    result = word + "way";  // Starts with vowel
} else {
    // Move consonants to end + "ay"
    result = word.substring(firstVowel) + word.substring(0, firstVowel) + "ay";
}

// Fix capitalization
if (Character.isUpperCase(word.charAt(0))) {
    result = Character.toUpperCase(result.charAt(0)) + 
             result.substring(1).toLowerCase();
}

return result;
```

---

## 🧠 KEY LEARNING CONCEPTS

### String Processing Patterns
- **Iteration:** `for (char c : string.toCharArray())`
- **Position access:** `string.charAt(i)`
- **Substring:** `string.substring(start, end)`
- **Building strings:** Use `StringBuilder` for efficiency

### Character Classification
- `Character.isDigit(c)` - checks 0-9
- `Character.isLetter(c)` - checks a-z, A-Z
- `Character.isLetterOrDigit(c)` - combines both
- `Character.toUpperCase(c)` / `Character.toLowerCase(c)`

### Mathematical Operations
- **Modular arithmetic:** `%` for remainder/wrapping
- **Absolute value:** `Math.abs()`
- **Square root:** `Math.sqrt()` or `i * i <= n`

### File I/O Patterns
- **Reading:** `scanner.hasNextLine()` and `scanner.nextLine()`
- **Writing:** `printStream.println(text)`

---

## ✅ Testing Strategy

### Test Categories for Each Method
1. **Normal cases** - typical expected inputs
2. **Edge cases** - empty strings, boundary values
3. **Error cases** - invalid inputs, null values
4. **Special cases** - method-specific scenarios

### Example Test Structure
```java
// Test normal case
System.out.println("isPrime(7): " + Numbers.isPrime(7)); // Expected: true

// Test edge case  
System.out.println("isPrime(1): " + Numbers.isPrime(1)); // Expected: false

// Test boundary
System.out.println("isPrime(2): " + Numbers.isPrime(2)); // Expected: true
```

---

## 🎯 Exam Success Tips

### Common Mistakes to Avoid
- **Modular arithmetic errors** - always handle negative numbers
- **Off-by-one errors** - check loop bounds carefully
- **Case sensitivity** - convert to consistent case first
- **Integer vs floating division** - use `1.0/i` not `1/i`
- **String immutability** - use StringBuilder for building

### Time Management
1. **Read all requirements** first
2. **Implement basic logic** before edge cases
3. **Test incrementally** - don't wait until the end
4. **Document as you go** - add comments explaining logic

### Debugging Techniques
- **Trace examples manually** first
- **Print intermediate values** during development
- **Test edge cases** systematically
- **Use meaningful variable names**

---

## 📚 Quick Reference

### Essential Java Methods
```java
// String methods
string.length()
string.charAt(i)
string.substring(start, end)
string.startsWith(prefix)
string.toUpperCase()
string.toLowerCase()

// Character methods
Character.isDigit(c)
Character.isLetter(c)
Character.isLetterOrDigit(c)
Character.toUpperCase(c)
Character.toLowerCase(c)

// Math methods
Math.abs(x)
Math.sqrt(x)

// File I/O
scanner.hasNextLine()
scanner.nextLine()
printStream.println(text)
```

### Boolean Logic Patterns
```java
// Multiple conditions
if (condition1 && condition2) { }
if (condition1 || condition2) { }

// Early return pattern
if (invalidInput) return false;
// continue with normal logic

// Loop with condition check
for (int i = 0; i < limit; i++) {
    if (found) break;
}
```

---

*Study this guide systematically, implement each method step by step, and test thoroughly. Focus on understanding the concepts, not memorizing code!* 🚀
