# Testing linearSearch - Guide

## 🔍 Understanding Private Method Testing

### The Challenge:
- `linearSearch` is a **private** method
- Private methods **cannot be called** from outside the class (like from `A03Main`)
- So how do we test it?

### The Solution:
- Test it **indirectly** through public methods that use it
- When those public methods work correctly, `linearSearch` is working correctly too!

---

## 🎯 Methods That Use `linearSearch`

These public methods will use `linearSearch`:

1. **`remove(T key)`** - Uses `linearSearch` to find the node to remove
2. **`find(T key)`** - Uses `linearSearch` to find where the key is
3. **`contains(T key)`** - Might use `linearSearch` (or check front separately)
4. **`removeMany(T key)`** - Uses `linearSearch` repeatedly

---

## 🧪 Testing Strategy

### Step 1: Implement a Simple Method That Uses `linearSearch`

Start with a simple method like `contains()` or `find()` that uses `linearSearch`.

### Step 2: Test That Method

When you test `contains()` or `find()`, you're indirectly testing `linearSearch`.

### Step 3: Verify Results

If the method works correctly, `linearSearch` is working correctly!

---

## 💡 Example: Testing Through `contains()`

### Implementation of `contains()` (using `linearSearch`):

```java
public boolean contains(final T key) {
    // Check if list is empty
    if (this.front == null) {
        return false;
    }
    
    // Check if key is at front (linearSearch can't detect this)
    if (this.front.getDatum().compareTo(key) == 0) {
        return true;
    }
    
    // Use linearSearch for rest of list
    SingleNode<T> previous = linearSearch(key);
    
    // If previous is not null, key was found
    return previous != null;
}
```

### Test in `A03Main`:

The test file already has tests for `contains()`:

```java
System.out.println(String.format("contains %d {false}: %b", badValue, source.contains(badValue)));
int object = testValues[length / 2];
System.out.println(String.format("contains %d {true}: %b", object, source.contains(object)));
```

**When this test passes**, it means `linearSearch` is working!

---

## 🎯 Step-by-Step Testing Plan

### Option 1: Test Through Public Methods (Recommended)

1. **Implement `contains()` method** that uses `linearSearch`
2. **Run the existing tests** in `A03Main`
3. **Check if `contains()` works correctly**
4. If yes, `linearSearch` is working!

### Option 2: Add Temporary Test Method (For Debugging)

If you want to test `linearSearch` directly for debugging, you can temporarily add a public test method:

```java
// TEMPORARY - Remove before submitting!
public SingleNode<T> testLinearSearch(T key) {
    return linearSearch(key);
}
```

Then test it in `A03Main`:

```java
// Test linearSearch directly
SingleList<Integer> testList = new SingleList<>();
testList.append(10);
testList.append(20);
testList.append(30);

SingleNode<Integer> result = testList.testLinearSearch(20);
if (result != null) {
    System.out.println("Found! Previous node data: " + result.getDatum());
} else {
    System.out.println("Not found or at front");
}
```

**Remember to remove this test method before submitting!**

---

## 🧪 Detailed Testing Scenarios

### Test Case 1: Key Found in Middle
**Setup:**
```java
SingleList<Integer> list = new SingleList<>();
list.append(10);
list.append(20);
list.append(30);
// List: [10] → [20] → [30]
```

**Test `contains(20)`:**
- Should return `true`
- This means `linearSearch(20)` found the node correctly

**Test `find(20)`:**
- Should return `20`
- This means `linearSearch(20)` found the node correctly

**Test `remove(20)`:**
- Should return `20`
- List should become: `[10] → [30]`
- This means `linearSearch(20)` found the previous node correctly

### Test Case 2: Key at Front
**Setup:**
```java
SingleList<Integer> list = new SingleList<>();
list.append(10);
list.append(20);
list.append(30);
// List: [10] → [20] → [30]
```

**Test `contains(10)`:**
- Should return `true`
- `linearSearch(10)` returns `null` (key at front)
- Method should check front separately

**Test `find(10)`:**
- Should return `10`
- Method should check front separately

**Test `remove(10)`:**
- Should return `10`
- List should become: `[20] → [30]`
- Method should handle front case separately

### Test Case 3: Key Not Found
**Setup:**
```java
SingleList<Integer> list = new SingleList<>();
list.append(10);
list.append(20);
list.append(30);
// List: [10] → [20] → [30]
```

**Test `contains(99)`:**
- Should return `false`
- `linearSearch(99)` returns `null` (not found)

**Test `find(99)`:**
- Should return `null`
- `linearSearch(99)` returns `null` (not found)

**Test `remove(99)`:**
- Should return `null`
- List should remain: `[10] → [20] → [30]`
- `linearSearch(99)` returns `null` (not found)

### Test Case 4: Empty List
**Setup:**
```java
SingleList<Integer> list = new SingleList<>();
// List: empty
```

**Test `contains(10)`:**
- Should return `false`
- `linearSearch` shouldn't be called (list is empty)

**Test `find(10)`:**
- Should return `null`
- `linearSearch` shouldn't be called (list is empty)

### Test Case 5: Single Node
**Setup:**
```java
SingleList<Integer> list = new SingleList<>();
list.append(10);
// List: [10]
```

**Test `contains(10)`:**
- Should return `true`
- Key is at front, so check front separately

**Test `contains(20)`:**
- Should return `false`
- `linearSearch(20)` returns `null` (not found)

---

## 🔍 Debugging Tips

### If Tests Fail:

1. **Add print statements** (temporarily) in `linearSearch`:
```java
private SingleNode<T> linearSearch(final T key) {
    SingleNode<T> previous = null;
    SingleNode<T> current = this.front;
    
    System.out.println("Searching for: " + key);  // DEBUG
    int count = 0;
    
    while(current != null){
        System.out.println("Checking node " + count + ": " + current.getDatum());  // DEBUG
        if(current.getDatum().compareTo(key) == 0) {
            System.out.println("Found! Previous: " + (previous != null ? previous.getDatum() : "null"));  // DEBUG
            return previous;
        }
        previous = current;
        current = current.getNext();
        count++;
    }
    System.out.println("Not found");  // DEBUG
    return null;
}
```

2. **Check the logic step by step**:
   - Is `current` initialized correctly?
   - Is the loop condition correct?
   - Is the comparison correct?
   - Are we moving forward correctly?

3. **Test with simple cases first**:
   - Empty list
   - Single node
   - Two nodes
   - Then more complex cases

---

## ✅ Verification Checklist

When testing through public methods, verify:

- [ ] `contains()` returns `true` for existing keys
- [ ] `contains()` returns `false` for non-existing keys
- [ ] `contains()` handles key at front correctly
- [ ] `contains()` handles empty list correctly
- [ ] `find()` returns correct data for existing keys
- [ ] `find()` returns `null` for non-existing keys
- [ ] `remove()` removes correct node
- [ ] `remove()` updates list correctly
- [ ] `remove()` handles key at front correctly
- [ ] `remove()` handles key not found correctly

---

## 🎓 Key Takeaways

1. **Private methods are tested indirectly** through public methods
2. **When public methods work**, private helpers work too
3. **Start with simple methods** like `contains()` or `find()`
4. **Test edge cases**: empty list, single node, key at front, key not found
5. **Use existing test code** in `A03Main` - it's already set up!

---

## 🚀 Next Steps

1. **Implement `contains()` or `find()`** method
2. **Run the existing tests** in `A03Main`
3. **Verify the results** match expected output
4. **If tests pass**, `linearSearch` is working correctly!
5. **If tests fail**, debug using the tips above

Good luck! 🎉

