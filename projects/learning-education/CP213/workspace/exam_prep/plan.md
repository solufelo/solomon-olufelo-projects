# Development Plan

## Current Focus: The University Lab Simulator (Exam Prep)

- [x] **Phase 1: Core Hierarchy**
  - Created `UniversityMember` (Abstract), `Student`, `Professor`.
  - Validated IDs and enforced encapsulation.

- [x] **Phase 1.5: Verification**
  - Created `ExamRunner` to test polymorphism.

- [x] **Phase 2: Interfaces**
  - Created `LabAccess` interface.
  - Implemented `TeachingAssistant` (extends Student, implements LabAccess with overrides).

- [ ] **Phase 3: Lab System & Exceptions** (CURRENT)
  - [ ] Implement `LabCapacityException` (Checked Exception).
  - [ ] Implement `LabSession` (ArrayList management).
  - [ ] Update `ExamRunner` to handle exceptions.

- [ ] **Phase 4: Generics & Custom Data Structures**
  - Create `Node<T>` class.
  - Create `WaitQueue<T>` implementing a Linked List from scratch (no `java.util.LinkedList`).

- [ ] **Phase 5: The GUI**
  - Build a Swing interface for the simulator.

- [ ] **Phase 6: The Library System** (Maps & Data Structures)
  - Implement `Book` and `Library` classes.
  - Use `HashMap` for O(1) member lookups and tracking loans.

- [ ] **Phase 7: Academic Records "Backend"** (Static Logic)
  - `AcademicRegistrar` class.
  - Graduation validation (connects Library, Student, and Finance).
  - Probation reporting.

- [ ] **Phase 8: Persistence (File I/O)**
  - Read `students.csv` to load initial data.
  - Write "at-risk" reports to text files.

- [ ] **Phase 9: Algorithms (Recursion & Sorting)**
  - Implement recursive file search (`FileNode`).
  - Implement custom Comparators for sorting students by GPA/Name.
