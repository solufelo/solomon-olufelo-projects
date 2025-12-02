# Assignment 3 - Status Tracker

**Student**: Solomon Olufelo (210729170)  
**Assignment**: A03 - Linear Linked Structures  
**Due Date**: November 9, 2025  
**Project**: oluf9170_a03

## Progress Status

### Files Needed
- [ ] `SingleNode.java` (Given - Do Not Modify)
- [ ] `SingleLink.java` (Abstract parent class - TO IMPLEMENT)
- [ ] `SingleStack.java` (TO IMPLEMENT)
- [ ] `SingleQueue.java` (TO IMPLEMENT)
- [ ] `SinglePriorityQueue.java` (TO IMPLEMENT)
- [ ] `SingleList.java` (TO IMPLEMENT)
- [ ] `A03Main.java` (Testing class)
- [ ] `Food.java` (Reuse from A02)
- [ ] `Movie.java` (Reuse from A02)

### Implementation Status

#### SingleLink (Abstract Parent Class) ✅ COMPLETED
- [x] Constructor
- [x] `append(SingleLink<T> source)` helper method
- [x] `moveFrontToFront(SingleLink<T> source)` helper method
- [x] `moveFrontToRear(SingleLink<T> source)` helper method
- [x] `getLength()` method
- [x] `isEmpty()` method
- [x] `peek()` method
- [x] `iterator()` method (for enhanced for-loops)
- [x] `toString()` method
- [x] `SingleLinkIterator` inner class

#### SingleStack ✅ COMPLETED
- [x] Constructor
- [x] `push(T datum)` - Add to front
- [x] `pop()` - Remove from front

#### SingleQueue ✅ COMPLETED
- [x] Constructor
- [x] `enqueue(T datum)` - Add to rear
- [x] `dequeue()` - Remove from front

#### SinglePriorityQueue ✅ COMPLETED
- [x] Constructor
- [x] `insert(T datum)` - Insert in priority order
- [x] `remove()` - Remove highest priority
- **Note**: Requires `T extends Comparable<T>`

#### SingleList ✅ COMPLETED
- [x] Constructor
- [x] `append(T datum)` - Add to end
- [x] `insert(T datum)` - Insert in sorted order
- [x] `remove(T datum)` - Remove specific item
- [x] `linearSearch(T key)` - Helper method to find nodes
- **Note**: Requires `T extends Comparable<T>`

## Key Requirements Checklist

- [ ] Package name is `cp213` (do not change)
- [ ] All class names match exactly
- [ ] No modifications to classes marked "Do Not Change"
- [ ] Method signatures match exactly (no changes)
- [ ] Only standard Java JDK libraries used
- [ ] Name, ID, email added to all files
- [ ] Javadoc documentation added
- [ ] Testing completed with A03Main
- [ ] Testing with Integer, String, Food, Movie objects

## Resources

- Guides: `/home/solom/Projects/CP213/guides/assignment3/`
- SINGLELINK_EXPLANATION.md - Complete explanation of SingleLink
- APPEND_METHOD_GUIDE.md - Step-by-step append() implementation
- METHOD_DISCOVERY_GUIDE.md - How to use getDatum(), compareTo(), etc.
- ITERATOR_GUIDE.md - Understanding iterators
- LINEAR_SEARCH_*.md - Linear search implementation guides

## Notes

- SinglePriorityQueue and SingleList require Comparable objects
- Use helper methods from SingleLink (append, moveFrontToFront, moveFrontToRear)
- Test thoroughly with different data types
- Reference testing.txt for expected results

