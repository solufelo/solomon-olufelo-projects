## CP213 Midterm Quizlet — First-Time Comprehension

Audience: First-time learner. Format: Active recall (Q → A), minimal redundancy, concrete examples, and quick gotchas. Scope: Chapters 1–6 (Java basics, I/O, control flow, classes, references/static, arrays).

---

### 1) Java Basics & Program Structure

- **Q**: What does the JVM do?  
  **A**: Executes platform-independent bytecode produced by `javac`.

- **Q**: Minimal Java program structure?  
  **A**: A `public class` with a `public static void main(String[] args)` method.

- **Q**: Difference between `println`, `print`, `printf`?  
  **A**: `println` adds newline; `print` doesn’t; `printf` formats with specifiers (e.g., `%.2f`).

- **Q**: Primitive vs reference types?  
  **A**: Primitives store values directly (`int`, `double`, etc.). References store addresses to objects (`String`, arrays, custom classes).

- **Example**: Integer overflow  
  `int x = Integer.MAX_VALUE; x = x + 1; // wraps to negative`

- **Gotcha**: Compare strings with `equals()`, not `==`.

---

### 2) Types, Casting, and Strings

- **Q**: Implicit vs explicit casting?  
  **A**: Implicit/widening (safe, small → large); explicit/narrowing (possible data loss, requires `(type)`).

- **Q**: Why is `0.1 + 0.2 != 0.3` exactly?  
  **A**: Binary floating-point precision; use `BigDecimal` or tolerances for equality.

- **Q**: What happens `(int)2.9`?  
  **A**: Truncates to `2` (not rounded).

- **Q**: String immutability implications?  
  **A**: Methods return new strings; concatenation in loops can be costly → prefer `StringBuilder`.

---

### 3) Console and File I/O (Scanner, Files)

- **Q**: Typical `Scanner` issues?  
  **A**: `nextInt()` leaves newline; call extra `nextLine()` before reading a full line.

- **Q**: File reading essentials?  
  **A**: Handle `FileNotFoundException`; use loop with `hasNextLine()`; close or use try-with-resources.

- **Example**: Clear buffer  
  `int n = sc.nextInt(); sc.nextLine(); String line = sc.nextLine();`

- **Gotcha**: Always check end-of-file; don’t assume fixed line counts.

---

### 4) Control Flow (Booleans, If/Switch, Loops, Random)

- **Q**: Short-circuit difference?  
  **A**: `&&` stops on first false; `||` on first true. Avoid `&`/`|` for boolean logic unless you need both sides evaluated.

- **Q**: When `switch` over `if-else`?  
  **A**: Many discrete cases on one expression; clearer than long if-else chains.

- **Q**: Loop selection?  
  **A**: `for` for known counts, `while` for condition-first, `do-while` when must run at least once.

- **Q**: Random numbers in a range `[a, b]`?  
  **A**: `rand.nextInt(b - a + 1) + a`.

- **Gotcha**: Off-by-one errors in bounds; verify inclusive/exclusive.

---

### 5) Class Design I (Class/Objects, Encapsulation, Methods, Constructors)

- **Q**: Encapsulation rules?  
  **A**: Keep fields `private`; expose behavior via public methods; return copies of mutable state.

- **Q**: Accessor vs mutator?  
  **A**: Accessor (getter) returns state; mutator (setter) changes state with validation.

- **Q**: Constructor basics?  
  **A**: Initializes fields; default provided only if none declared; can chain using `this(...)`.

- **Q**: Method overloading?  
  **A**: Same name, different parameter lists (number, types, order). Return type alone doesn’t overload.

- **Gotcha**: Don’t duplicate validation logic—centralize in constructors or private validators.

---

### 6) Class Design II (References, Privacy Leaks, Packages, Static)

- **Q**: Reference vs value semantics?  
  **A**: Variables of class/array types hold references; assignments copy references; two refs can alias same object.

- **Q**: What is a privacy leak?  
  **A**: Exposing internal mutable objects. Fix by defensive copying in getters/constructors.

- **Q**: When to use `static`?  
  **A**: Class-wide data/methods that don’t depend on instance state (utilities, counters, factories).

- **Example**: Static vs instance  
  Instance methods can use `this` fields; static methods cannot access instance state.

- **Gotcha**: Avoid overusing static—prefer instance design when behavior depends on object state.

---

### 7) Arrays (1D & 2D), Algorithms, Partially Filled

- **Q**: Array basics?  
  **A**: Fixed size; indexed `0..length-1`; `length` is a field, not a method.

- **Q**: Partially filled arrays tracking?  
  **A**: Maintain a separate `count` of used elements.

- **Q**: Common algorithms?  
  **A**: Linear search, (simple) sorts, sums/averages, max/min, copy/clone.

- **Q**: 2D arrays?  
  **A**: Array of arrays; may be ragged; nested loops for traversal.

- **Gotcha**: `ArrayIndexOutOfBoundsException`—validate indices; prefer iterating with bounds from `array.length`.

---

### Essential Code Patterns (Flash-Recall)

```java
// Defensive copy in getter
public int[] getScores() { return scores.clone(); }

// Partially filled append
if (count < data.length) { data[count++] = value; }

// Linear search
int idx = -1; for (int i = 0; i < a.length; i++) if (a[i] == t) { idx = i; break; }

// Random in [lo, hi]
int r = rand.nextInt(hi - lo + 1) + lo;

// Clear Scanner buffer after nextInt
int n = sc.nextInt(); sc.nextLine();
```

---

### First-Time Comprehension Drills (Spaced Prompts)

- Day 1 (10 min):
  - Explain primitive vs reference types (no notes).
  - Write a minimal program and print formatted output with `printf`.

- Day 2 (10 min):
  - Show two casting examples: widening and narrowing; predict outcomes.
  - Fix a `Scanner` `nextInt()/nextLine()` bug in a snippet (from memory).

- Day 3 (10 min):
  - Create one `if-else`, one `switch`, one `for` loop; state when each is best.
  - Generate a random number in `[5, 12]` and justify formula.

- Day 4 (10 min):
  - Design a tiny class with private fields, getters, a validating setter, and two overloaded constructors.
  - Explain why a getter should return a copy for an array field.

- Day 5 (10 min):
  - Implement `max(int[] a)` and `reverseInPlace(int[] a)` from scratch.
  - Create a ragged 2D array and print it.

---

### Quick Self-Check (Yes/No)

1. I can state what the JVM, JDK, and bytecode are.  
2. I can avoid string `==` mistakes and use `equals()`.  
3. I know how to clear `Scanner` input buffer safely.  
4. I can choose between `if-else`, `switch`, `for`, `while`, `do-while`.  
5. I can write and explain an accessor, mutator, constructor chain.  
6. I can prevent privacy leaks with defensive copies.  
7. I can implement linear search and a simple sort; handle partially filled arrays.  

---

Sources consolidated from: `study-guide.md`, `exam-prep.md`, deep dives and flashcards in `resources/` and chapter folders.

---

### Chapter Quick Hits (Incorporated from Flashcards)

#### Chapter 1 — Getting Started
- **Q**: Why bytecode and JVM?  
  **A**: Compile once to bytecode, run anywhere via JVM (platform independence).
- **Q**: Define class, object, method.  
  **A**: Class = template; Object = instance; Method = behavior/action.
- **Q**: App vs Applet (historic).  
  **A**: App runs on JVM as an application; Applet ran inside browsers.

#### Chapter 2 — Console I/O
- **Q**: `print` vs `println` vs `printf`?  
  **A**: Same as above; `printf` uses format specifiers (e.g., `%.2f`).
- **Q**: Common `Scanner` pitfall?  
  **A**: `nextInt()` leaves newline; call extra `nextLine()` before reading a full line.
- **Q**: File input essentials?  
  **A**: Use `Scanner(new FileInputStream(path))`, handle `FileNotFoundException`, close resources.

#### Chapter 3 — Flow of Control
- **Q**: String comparisons?  
  **A**: Use `equals()`/`equalsIgnoreCase()`, not `==`.
- **Q**: Loop selection?  
  **A**: `for` for counts; `while` for condition-first; `do-while` runs at least once.
- **Q**: Random in `[a,b]`?  
  **A**: `rand.nextInt(b - a + 1) + a`.

#### Chapter 4 — Defining Classes I
- **Q**: Encapsulation rule of thumb?  
  **A**: Private fields, public methods; validate in setters/constructors.
- **Q**: Overloading constraints?  
  **A**: Differ by parameter list (number/types/order), not return type.
- **Q**: Constructors basics?  
  **A**: Initialize fields; default exists only if none declared; chain with `this(...)`.

#### Chapter 5 — Defining Classes II
- **Q**: Reference vs value semantics?  
  **A**: Assigning objects copies references (aliasing), not deep copies.
- **Q**: Privacy leak?  
  **A**: Returning internal mutable references; fix with defensive copies.
- **Q**: Packages/imports?  
  **A**: Organize classes; `import` brings types into scope; `java.lang` auto-imported.

#### Chapter 6 — Arrays
- **Q**: Array essentials?  
  **A**: Fixed size; `length` field; `0..length-1`; bounds checked at runtime.
- **Q**: Partially filled arrays?  
  **A**: Track used count separately from capacity.
- **Q**: 2D arrays (ragged)?  
  **A**: Arrays of arrays; rows can differ in length; traverse with nested loops.


