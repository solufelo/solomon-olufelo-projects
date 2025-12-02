# Assignment 3 - Simplified Guide

## ⚠️ Critical Requirements (Auto-Graded)
- **Project name and class names must match exactly** - auto-grading will fail otherwise
- **Package name must be `cp213`** - do not change
- **Do not modify classes marked "Do Not Change"** (e.g., `SingleNode`)
- **Do not change method signatures** (parameters, return types, visibility)
- **Only use standard Java JDK libraries** - no external imports

## What to Complete
Complete all methods in these classes:
- `SingleLink` (abstract parent class)
- `SingleStack`
- `SingleQueue`
- `SinglePriorityQueue`
- `SingleList`

## Testing
- Use `A03Main` class for testing
- Test with: `Integer`, `String`, and `Food/Movie` objects
- Reference: `testing.txt` for sample results

## Key Concepts

### SingleLink (Parent Class)
- Uses `SingleNode` to create linked structures
- Attributes: `front` (first node), `rear` (last node), `length` (count)
- Contains helper methods: `append()`, `moveFrontToFront()`, `moveFrontToRear()`
- Includes iterator for enhanced for-loops
- You can add private helper methods to child classes

### SinglePriorityQueue & SingleList
- **Require Comparable objects** (use `compareTo()` method)
- Generic type: `SinglePriorityQueue<T extends Comparable<T>>`
- Must be able to compare values to determine priority/order

## Additional Resources
- Assignment Documentation: [Assignment 3 Documentation]
- Sample Test Results: [Sample Test Results]
- Your CP164 linked list implementations may be helpful (similar algorithms)

