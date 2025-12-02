## CP213 Midterm Deep Study — Layered Mastery Program

Purpose: Turn first-time comprehension into durable skill for Chapters 1–6 using layered drills, code katas, and timed exam simulations.

---

### Layer 0 — Daily Spine (15–25 min)
- Warm-up (2 min): Recite from memory: JVM/bytecode, `Scanner` newline fix, string equality, random `[a,b]` formula, array bounds rule.
- Flash Recall (8–12 min): Pick any 10 from `midterm_quizlet.md` and answer aloud, then verify.
- Micro-Kata (5–10 min): Implement any one function below from scratch (no copy/paste), compile/run.

---

### Layer 1 — Micro-Katas (10–15 min each)
Implement from a blank file. Prioritize clarity over tricks. Add a tiny `main` test.

1) maxOfArray(int[] a): return max or `Integer.MIN_VALUE` if empty.
2) reverseInPlace(int[] a): swap ends inward.
3) linearSearch(int[] a, int t): return index or -1.
4) clamp(double x, double lo, double hi): inclusive bounds.
5) toTitleCase(String s): words separated by whitespace; handle empty.
6) parseInts(Scanner in): read unknown count until EOF into partially filled array semantics (use `ArrayList` then copy to int[]).
7) randomInRange(int lo, int hi, Random r): inclusive.
8) formatMoney(double amt): `"$%.2f"`.
9) safeEquals(String a, String b): null-safe string content equality.
10) countVowels(String s): lowercase/uppercase.

Stretch: binarySearch (sorted array), selectionSort, bubbleSort.

---

### Layer 2 — Concept Drills (20–40 min)
Do one per session, write code + a 3–5 sentence explanation of the concept.

- Encapsulation Drill: A `Student` with private fields (`id`, `name`, `scores:int[]`), defensive copy in getter/setter, constructor validation.
- Constructor Chaining: Provide default, partial, and full constructors using `this(...)`. Add a copy constructor.
- Static vs Instance: Track `totalInstances` statically; show instance state unaffected by static counters.
- Scanner I/O Robustness: Read mixed types; demonstrate the `nextInt()/nextLine()` newline fix with a reproducible test.
- Arrays & Partially Filled: Implement a simple `IntBag` (fixed capacity, `add`, `size`, `get`, `toArray`) using a `count` tracker.

Deliverable: Brief README note per drill describing invariants and edge cases.

---

### Layer 3 — Integration Katas (45–60 min)

1) GradeBook
- Input: lines of `name grade grade grade` until EOF.
- Output: per-student average, class max/min/mean.
- Focus: `Scanner` parsing, arrays/ArrayList, formatting (`printf`).

2) Inventory Manager
- Model: `Item{code:String, qty:int, price:double}` with validation, copy constructor, defensive copies.
- Ops: add/remove/update, total value, top-N by value.
- Focus: Encapsulation, static factory (`fromCSV`), sorting by multiple keys.

3) Matrix Playground
- Build 2D int arrays; implement add, multiply, transpose.
- Focus: 2D indexing correctness, bounds safety, tests for ragged arrays (reject or normalize).

Deliverable: Each kata has a `main` demo and clear console output.

---

### Layer 4 — Exam Simulations (60–90 min, timed)
Structure: 3 sections. No notes; only `javac`/`java` allowed.

Section A (Concept Q&A, 10 min):
- 8 rapid prompts (e.g., "Why `equals()` not `==` for `String`?", "Explain JVM/bytecode.")

Section B (Code Reading, 15–25 min):
- Trace output of 2 short programs; identify bugs (off-by-one, newline buffer, privacy leak).

Section C (Implementation, 35–55 min):
- Implement two tasks from Micro/Integration Katas (randomly pick).

Grading rubric: correctness (60%), clarity/style (20%), edge cases (20%).

---

### Spaced Repetition Schedule (2 weeks)
- Days 1–3: Layer 0 daily + 2 Micro-Katas/day.
- Days 4–6: Layer 0 daily + 1 Concept Drill/day.
- Day 7: Layer 0 + 1 Integration Kata.
- Days 8–10: Layer 0 + 2 Micro-Katas/day (new ones).
- Days 11–12: Layer 0 + 1 Concept Drill/day.
- Day 13: Full Exam Simulation.
- Day 14: Review mistakes; re-do weakest kata.

---

### Checklists
- Before coding: restate requirements, list edge cases, choose data structures.
- During coding: compile early/often, print intermediate values to trace.
- After coding: test empty/singleton/typical/edge/invalid cases.

---

### Reflection Prompts (write 3–5 sentences)
- What invariant did I rely on? How did I enforce it?
- Where could a privacy leak happen? How did I prevent it?
- What assumption about indices or lengths could fail?
- What’s the minimal test proving correctness?

---

### Minimal Reference (from memory)
- String equality: `Objects.equals(a, b)` or `a != null && a.equals(b)`.
- Random inclusive: `r.nextInt(hi - lo + 1) + lo`.
- Defensive copy (array): `return arr.clone();`
- Partially filled: keep `count`; bounds check on insert.
- 2D traversal: `for (int i=0; i<m.length; i++) for (int j=0; j<m[i].length; j++)`


