# CP213 Cumulative Exam Prep: "The University Lab Simulator"

**Objective:** Build a complete Java application from scratch that simulates a university computer lab environment. This task covers all major topics from the CP213 course.

**Rules:**
1.  Try to write the code **without** looking at previous assignments first.
2.  Use the `HINTS_AND_SCAFFOLDING.md` file only when you are stuck.
3.  Focus on **why** you are making design choices (Private vs Protected, Interface vs Abstract Class).

---

## Phase 1: The Core Hierarchy (Weeks 1, 4, 5, 7)
**Topics:** Classes, Inheritance, Encapsulation, Abstract Classes, toString/equals.

**Task:**
Create a class hierarchy to represent people in the university.
1.  Create an abstract class `UniversityMember`.
    -   Attributes: `String id` (must be 9 digits), `String name`.
    -   Constructor: Validates ID length.
    -   Abstract Method: `String getRole()` (returns "Student", "Prof", etc.).
    -   Methods: `toString()`, `equals()` (based on ID).
2.  Create a class `Student` extending `UniversityMember`.
    -   Attributes: `double gpa`.
    -   Method: `getRole()` returns "Student".
3.  Create a class `Professor` extending `UniversityMember`.
    -   Attributes: `String department`.
    -   Method: `getRole()` returns "Professor".

---

## Phase 1.5: Verification (The Exam Runner)
**Topics:** Main Method, Object Instantiation, Polymorphism Loop.

**Task:**
Before moving on, prove your hierarchy works.
1.  Create a class `ExamRunner` with a `main` method.
2.  Create a `Student` (ID: "123456789") and a `Professor` (ID: "987654321").
3.  Store them in a `UniversityMember[]` array (Polymorphism).
4.  Loop through the array and print `name + ": " + getRole()`.
5.  Create a second `Student` with the **same ID** as the first but a different name.
6.  Print `student1.equals(student2)`. It should be `true`.

---

## Phase 2: Interfaces & Polymorphism (Weeks 8, 10)
**Topics:** Interfaces, Polymorphism, Covariant Return Types.

**Task:**
Not everyone has the same access rights.
1.  Create an interface `LabAccess`.
    -   **Constant:** `int MAX_DAILY_QUOTA = 1000;` (Implicitly public static final).
    -   Method: `boolean canLogin()`.
    -   Method: `int getPrintQuota()`.
2.  Have `Student` and `Professor` implement `LabAccess`.
    -   Students can login if GPA > 1.0. Print quota: 50 pages.
    -   Professors can always login. Print quota: 500 pages.
3.  Create a `TeachingAssistant` class.
    -   **Challenge**: A TA is a Student, but has extra privileges.
    -   Make `TeachingAssistant` extend `Student`.
    -   Override `getPrintQuota()` to return 200 pages.
    -   **Covariant Return Type Challenge**: If you have a method that returns `Student` in the parent, override it to return `TeachingAssistant` in the child.

---

## Phase 3: The Lab System & Exceptions (Weeks 6, 9)
**Topics:** ArrayList, Exceptions, Custom Exceptions.

**Task:**
Manage the lab session.
1.  Create a custom exception `LabCapacityException`.
2.  Create a class `LabSession`.
    -   Attributes: `ArrayList<LabAccess> activeUsers`, `int capacity`.
    -   Method: `void enterLab(LabAccess user)` throws `LabCapacityException`.
        -   If lab is full, throw exception.
        -   If user `!canLogin()`, print "Access Denied".
    -   Method: `void viewUserList()`: Prints all users using polymorphism.

---

## Phase 4: Generics, Nested Classes & Cloning (Week 10)
**Topics:** Generics, Static Nested Classes, Cloneable Interface.

**Task:**
1.  **Static Nested Class:** Inside `WaitQueue<T>`, define `private static class Node<T>`.
    -   *Why?* Per your notes, if the Node doesn't need access to the Queue's members, it should be **static**.
2.  **Cloning:**
    -   Make `UniversityMember` implement `Cloneable`.
    -   Override `clone()` to perform a **Deep Copy** (if applicable) or prove it's a shallow copy.
3.  **The Queue:** Implement the `WaitQueue<T>` using the inner Node class.

---

## Phase 5: The GUI (Weeks 11, 12)
**Topics:** Swing, Event Listeners, Anonymous Inner Classes.

**Task:**
Create a visual control panel.
1.  Create `LabSimulatorGUI`.
2.  **Components**:
    -   Text fields for Name and ID.
    -   Buttons: "Add Student", "Add Prof", "Enter Lab".
    -   Text Area: Shows current lab status / logs.
3.  **Events (Anonymous Classes):**
    -   Use an **Anonymous Inner Class** (or Lambda) for the `ActionListener` on the "Enter Lab" button.
    -   Clicking "Enter Lab" creates the object and calls `labSession.enterLab()`.
    -   Catch exceptions and show them in a pop-up dialog (`JOptionPane`).

---

## Phase 6: The Library & Loan Backend (Maps & Associations)
**Topics:** HashMap, HashSet, Association Classes.

**Task:**
The university needs a persistent way to track resources.
1.  Create a `Book` class (title, author, ISBN).
2.  Create a `LibrarySystem` class.
    -   **Member Lookup:** `HashMap<String, UniversityMember>` (Key: ID, Value: Member object).
    -   **Loan Tracking:** `HashMap<UniversityMember, ArrayList<Book>>`.
3.  **Logic:**
    -   `void checkOutBook(String memberId, Book book)`:
        -   Look up member. If not found, throw exception.
        -   Check if they already have overdue books (add an `isOverdue` boolean to Book?).
        -   Add to their loan list.

---

## Phase 7: Academic Records "Backend" (Static Logic & State)
**Topics:** Static Methods, Complex State Logic, Aggregation.

**Task:**
We need a central system to check graduation eligibility and academic standing.
1.  Create a class `AcademicRegistrar`.
2.  **Static Logic:**
    -   `static boolean canGraduate(Student s)`:
        -   Must have GPA > 5.0.
        -   Must have **zero** outstanding books in the `LibrarySystem`.
        -   Must have paid all tuition (Add a `balance` field to Student?).
3.  **Probation System:**
    -   Method `processProbation(ArrayList<Student> allStudents)`:
        -   Loops through everyone.
        -   If GPA < 5.0, print "ACADEMIC PROBATION ALERT: [Name]".

---

## Phase 8: Persistence & Serialization (Bonus Guru Level)
**Topics:** Serializable Interface, File I/O.

**Task:**
The system should remember users after a restart.
1.  **Serialization:**
    -   Make `UniversityMember` implement `Serializable` (Marker Interface).
    -   Use `ObjectOutputStream` to save the entire `HashMap` of members to a `.ser` file.
    -   Use `ObjectInputStream` to load them back.
2.  **Text I/O:**
    -   Create `data/students.txt` (CSV format) as a backup.

---

## Phase 9: Algorithms & Recursion (Bonus Guru Level)
**Topics:** Recursion, Sorting, Comparators.

**Task:**
1.  **Sorting:**
    -   Sort students by GPA (Descending) using a custom `Comparator`.
    -   Sort students by Name (Alphabetical) using a custom `Comparator`.
2.  **Recursion (File System Simulation):**
    -   Simulate a user's home directory on the lab computer.
    -   Create a `FileNode` class (name, isDirectory, `ArrayList<FileNode> children`).
    -   Method `searchFile(FileNode root, String fileName)`: Recursively searches for a file and returns the path.

---

## Final Review Check
-   [ ] Did you validate the ID in the constructor?
-   [ ] Did you use `super()` correctly?
-   [ ] Did you handle exceptions with try-catch in the GUI?
-   [ ] Did you use the Interface type (`LabAccess`) for the ArrayList, not specific classes?
-   [ ] Did you use HashMaps correctly in the Library?

**Ready? Start coding in `src/exam_prep/`!**
