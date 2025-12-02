# Assignment 3 - Next Steps

## ✅ Completed

All required classes have been implemented:
- ✅ `SingleLink.java` - Abstract parent class
- ✅ `SingleStack.java` - Stack implementation
- ✅ `SingleQueue.java` - Queue implementation  
- ✅ `SinglePriorityQueue.java` - Priority queue implementation
- ✅ `SingleList.java` - List implementation

## ⚠️ Action Required

### 1. Get Starter Files from Course Materials

You need to obtain the following files from your course materials (A03Given directory or course website):

- **`SingleNode.java`** - Currently a placeholder, MUST be replaced with actual file
- **`A03Main.java`** - Testing class (may already exist or need to be created)
- **`Food.java`** - Can be copied from `workspace/oluf9170_a02/src/cp213/Food.java`
- **`Movie.java`** - Can be copied from `workspace/oluf9170_a02/src/cp213/Movie.java`

### 2. Copy Files

```bash
# Copy Food and Movie from Assignment 2
cp workspace/oluf9170_a02/src/cp213/Food.java workspace/oluf9170_a03/src/cp213/
cp workspace/oluf9170_a02/src/cp213/Movie.java workspace/oluf9170_a03/src/cp213/
```

### 3. Replace SingleNode.java

**IMPORTANT**: The current `SingleNode.java` is just a placeholder. You MUST replace it with the actual file from your course materials. The actual SingleNode class should have:
- Constructor: `SingleNode(T datum)`
- Method: `T getDatum()`
- Method: `SingleNode<T> getNext()`
- Method: `void setNext(SingleNode<T> next)`

### 4. Compile and Test

```bash
cd workspace/oluf9170_a03
javac -d bin src/cp213/*.java
java -cp bin cp213.A03Main
```

### 5. Review Implementation

Before testing, review the implementations:
- Check that all methods match the assignment requirements
- Verify method signatures are correct
- Ensure package name is `cp213`
- Add your name, ID, and email to all files if not already present

### 6. Test Thoroughly

Test with:
- Integer objects
- String objects
- Food objects
- Movie objects

Compare output with `testing.txt` (if provided) or expected results from assignment documentation.

## 📁 File Structure

```
workspace/oluf9170_a03/
├── src/
│   └── cp213/
│       ├── SingleNode.java      ← NEEDS TO BE REPLACED
│       ├── SingleLink.java      ✅ COMPLETED
│       ├── SingleStack.java     ✅ COMPLETED
│       ├── SingleQueue.java     ✅ COMPLETED
│       ├── SinglePriorityQueue.java ✅ COMPLETED
│       ├── SingleList.java      ✅ COMPLETED
│       ├── A03Main.java         ← NEEDS TO BE OBTAINED
│       ├── Food.java            ← COPY FROM A02
│       └── Movie.java           ← COPY FROM A02
├── bin/                         (compiled classes)
├── ASSIGNMENT3_STATUS.md        ✅ CREATED
└── NEXT_STEPS.md               ✅ THIS FILE
```

## 📚 Resources

- Guides: `/home/solom/Projects/CP213/guides/assignment3/`
- Status Tracker: `ASSIGNMENT3_STATUS.md`
- Assignment Guide: `guides/assignment3/ASSIGNMENT_3_SIMPLIFIED.md`

## 🐛 Common Issues

1. **Compilation Errors**: Make sure SingleNode.java is the actual file from course materials
2. **NullPointerException**: Check that nodes are properly initialized before use
3. **Wrong Order**: For SinglePriorityQueue and SingleList, verify compareTo() logic is correct
4. **Empty Structure**: Always check if structure is empty before accessing front/rear

## 💡 Tips

- Use the guides in `guides/assignment3/` for detailed explanations
- Test with simple cases first (empty, one item, two items)
- Use the helper methods from SingleLink (append, moveFrontToFront, moveFrontToRear) where possible
- For SinglePriorityQueue: Lower compareTo value = Higher priority
- For SingleList: Maintains ascending sorted order

