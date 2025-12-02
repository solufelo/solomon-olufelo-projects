# CP213 Exam Priority Map

## 🎯 What Matters Most on the Exam

This guide shows you **exactly** where to focus your energy for maximum exam points.

---

## 📊 Exam Weight Distribution

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OOP Fundamentals          ████████████████ 30%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Inheritance/Polymorphism  ████████████ 25%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Arrays                    ███████ 15%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Exception Handling        ███████ 15%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Threading                 ██ 5%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Modern Java Features      ██ 5%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Input/Output              █ 3%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GUI (Swing)               █ 2%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔥 Priority Tier List

### **S-Tier** (Must Master - 55% of Exam)

#### **Slice 3: OOP Fundamentals** (30%)
**Why it matters**: Foundation of everything. Can't do polymorphism without understanding classes.

**What will be tested:**
- Writing complete class definitions
- Constructors (default, parameterized, overloaded)
- Getter/setter methods
- Access modifiers (public/private)
- Instance variables vs static variables
- Creating and using objects
- Encapsulation principles

**Exam question types:**
- "Write a class that..."
- "What is the output of this code?"
- "Identify the error in this class"
- "Implement getters and setters for..."

**Study focus**: 40% of your time

---

#### **Slice 6: Inheritance & Polymorphism** (25%)
**Why it matters**: Core OOP concepts. Heavily tested with code analysis.

**What will be tested:**
- Extends keyword and class hierarchies
- Method overriding (@Override)
- Super keyword (constructors and methods)
- Abstract classes and methods
- Polymorphic behavior
- Type casting (upcasting/downcasting)
- instanceof operator

**Exam question types:**
- "Complete the class hierarchy..."
- "What method is called when...?"
- "Write an abstract class..."
- "Trace the output through inheritance..."

**Study focus**: 35% of your time

---

### **A-Tier** (Important - 30% of Exam)

#### **Slice 5: Arrays** (15%)
**What will be tested:**
- Array declaration and initialization
- Accessing/modifying elements
- For loops and for-each loops
- 2D arrays
- Common algorithms (search, find min/max, sum)
- Array bounds and errors

**Study focus**: 15% of your time

---

#### **Slice 7: Exception Handling** (15%)
**What will be tested:**
- Try-catch-finally blocks
- Throwing exceptions
- Multiple catch blocks
- Creating custom exceptions
- Checked vs unchecked exceptions

**Study focus**: 10% of your time

---

### **B-Tier** (Nice to Know - 10% of Exam)

#### **Slice 10: Threading** (5%)
#### **Slice 9: Modern Java** (5%)

**Study focus**: 5% of your time combined

---

### **C-Tier** (Basic Knowledge - 5% of Exam)

#### **Slice 2: Input/Output** (3%)
#### **Slice 8: GUI** (2%)

**Study focus**: Minimal time - just understand basics

---

## 🎯 Time Allocation Strategy

**If you have 40 hours total:**

```
Slice 3 (OOP Fundamentals):           16 hours ████████████████
Slice 6 (Inheritance/Polymorphism):   14 hours ██████████████
Slice 5 (Arrays):                      6 hours ██████
Slice 7 (Exceptions):                  4 hours ████
Slices 1,2,4,9,10:                     6 hours total
Slice 8 (GUI):                         1 hour  █
Practice Exams:                        8 hours ████████
```

---

## 📝 Common Exam Question Patterns

### **Type 1: Write a Complete Class** (30% of exam)
**Example**: "Write a class `BankAccount` with private fields `balance` and `accountNumber`, appropriate constructors, getters/setters, and a `withdraw()` method."

**Skills needed**: Slice 3 mastery

---

### **Type 2: Code Tracing** (25% of exam)
**Example**: "What is the output of this program?" (Shows inheritance with overridden methods)

**Skills needed**: Slice 6 mastery

---

### **Type 3: Error Identification** (20% of exam)
**Example**: "Identify all errors in this code."

**Skills needed**: Slices 3, 5, 6, 7

---

### **Type 4: Fill in the Blank** (15% of exam)
**Example**: "Complete this method that sorts an array..."

**Skills needed**: Slices 5, 7

---

### **Type 5: Short Answer** (10% of exam)
**Example**: "Explain the difference between method overloading and overriding."

**Skills needed**: Conceptual understanding from all slices

---

## 🚨 High-Yield Topics (Study These First!)

### **1. Class Construction** (Slice 3)
```java
// This pattern appears on EVERY exam
public class Student {
    private String name;
    private int age;
    
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

### **2. Inheritance Hierarchy** (Slice 6)
```java
// Common exam question pattern
public class Animal {
    public void makeSound() { System.out.println("Generic sound"); }
}

public class Dog extends Animal {
    @Override
    public void makeSound() { System.out.println("Woof"); }
}

// Question: What does this print?
Animal a = new Dog();
a.makeSound();  // "Woof" - polymorphism!
```

### **3. Array Processing** (Slice 5)
```java
// Always appears in some form
int[] scores = {85, 92, 78, 95};
int sum = 0;
for (int score : scores) {
    sum += score;
}
double average = sum / (double) scores.length;
```

### **4. Try-Catch** (Slice 7)
```java
// Standard exception handling pattern
try {
    // risky code
} catch (SpecificException e) {
    // handle it
} finally {
    // always runs
}
```

---

## 📅 Week-by-Week Priority Schedule

### **Week 1-2: Foundation**
- ✅ Complete Slice 1 (basics)
- ✅ Complete Slice 2 (I/O)
- 🎯 **START Slice 3** (most important!)

### **Week 3: OOP Mastery**
- 🎯 **FINISH Slice 3** (spend extra time here!)
- Practice all Slice 3 problems twice
- Build multiple classes from scratch

### **Week 4: Inheritance Deep Dive**
- 🎯 **Complete Slice 6** (second most important!)
- Practice inheritance chains
- Master polymorphism

### **Week 5: Arrays & Exceptions**
- ✅ Complete Slice 5 (arrays)
- ✅ Complete Slice 7 (exceptions)

### **Week 6: Fill Gaps**
- ✅ Complete remaining slices (4, 9, 10)
- Quick review of Slice 8

### **Week 7-8: Practice & Review**
- 📝 Take 3 full practice exams
- Review all flashcards
- Redo weak areas

---

## 🎯 Emergency Prep (1 Week Before Exam)

**If you're behind, focus ONLY on these:**

### **Day 1-2: OOP Fundamentals** (Slice 3)
- Read concepts twice
- Do ALL practice problems
- Build 2 classes from scratch

### **Day 3-4: Inheritance & Polymorphism** (Slice 6)
- Read concepts twice
- Trace code examples by hand
- Practice method overriding

### **Day 5: Arrays** (Slice 5)
- Learn basic array operations
- Practice loops with arrays
- Memorize common patterns

### **Day 6: Exceptions + Review** (Slice 7)
- Learn try-catch-finally
- Review flashcards from Slices 3, 5, 6
- Take one practice exam

### **Day 7: Final Review**
- Light flashcard review
- Sleep well
- Stay confident

---

## 💯 Point Optimization Strategy

**To get 70% (C)**: Master Slices 3, 6  
**To get 80% (B)**: Master Slices 3, 6, 5  
**To get 90% (A)**: Master Slices 3, 6, 5, 7 + light coverage of others  
**To get 95%+ (A+)**: Master everything

---

## 🧠 Memory Aids for High-Yield Concepts

### **OOP Principles** (P.I.E.A.)
- **P**olymorphism
- **I**nheritance
- **E**ncapsulation
- **A**bstraction

### **Access Modifiers** (from most to least restrictive)
- **Private** → Only in this class
- **Default** → Only in this package
- **Protected** → Package + subclasses
- **Public** → Everywhere

### **Constructor Rules** (C.N.O.S.)
- **C**alled when object is created
- **N**o return type
- **O**verloadable
- **S**ame name as class

---

## ✅ Pre-Exam Checklist

**2 Days Before:**
- [ ] Can write a complete class from scratch
- [ ] Can explain inheritance with examples
- [ ] Can process arrays with loops
- [ ] Can write try-catch blocks
- [ ] Scored 80%+ on all self-assessments

**1 Day Before:**
- [ ] Light review only
- [ ] Flashcards for 30 minutes
- [ ] Good night's sleep

**Exam Day:**
- [ ] Arrive early
- [ ] Start with easiest questions
- [ ] Budget time (don't spend 20 min on one question!)

---

**Focus = Results. Master the big topics, pass the exam. Let's go! 💪**

