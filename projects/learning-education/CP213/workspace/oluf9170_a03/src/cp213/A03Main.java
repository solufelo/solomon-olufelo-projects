package cp213;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

/**
 * Comprehensive testing for Assignment 3 Data Structures.
 * Tests all methods in SingleStack, SingleQueue, SinglePriorityQueue, and SingleList.
 *
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-09-07
 */
public class A03Main {

    private static final String LINE = "-".repeat(40);
    private static final String TEST_LINE = "=".repeat(80);
    private static final String[] testStrings = { "xyz", "abc", "123", "string", "test" };

    /**
     * Main program to test all data structures.
     *
     * @param args (unused)
     */
    public static void main(final String[] args) {
        System.out.println("SingleLink Data Structures Tests");
        System.out.println();
        System.out.println("Tests are of the form:");
        System.out.println("  Test Operation {expected object}: actual object");
        System.out.println("  Contents: [contents from front to rear]");
        System.out.println();

        testSingleStack();
        testSingleQueue();
        testSinglePriorityQueue();
        testSingleList();
        testSingleListComprehensive();
        testWeird();
    }

    private static void testWeird() {
        // Test objects.
        Integer[] leftValues = { 5, 88, 38 };
        Integer[] rightValues = { 31, 47 };

        // Test SingleLists.
        SingleList<Integer> source = new SingleList<>();
        SingleList<Integer> left = new SingleList<>();
        SingleList<Integer> right = new SingleList<>();
        fillSingleList(left, leftValues);
        fillSingleList(right, rightValues);
        source.combine(left, right);
        System.out.println(String.format("  combine {%s}: %s", objectsToString(source), objectsToString(source)));
    }

    /**
     * Fills {@code target} with the contents of {@code objects}.
     *
     * @param target  {@code SingleList} to write to
     * @param objects array of Integer objects
     */
    private static void fillSingleList(SingleList<Integer> target, Integer[] objects) {
        for (Integer object : objects) {
            target.append(object);
        }
        return;
    }

    /**
     * Returns an array of random integers.
     *
     * @return an array of random integers
     */
    private static Integer[] getValues() {
        Random rd = new Random(); // creating Random object
        Integer[] arr = new Integer[7];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = rd.nextInt(50); // storing random integers in an array
        }
        return arr;
    }

    /**
     * Shuffles the contents of an {@code Object} array.
     *
     * @param array the {@code Object} array to shuffle
     */
    private static void shuffleArray(Object[] array) {
        int index = 0;
        Object temp = null;
        Random random = new Random();

        for (int i = array.length - 1; i > 0; i--) {
            index = random.nextInt(i + 1);
            temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }

    /**
     * Test {@code SingleStack}.
     */
    private static void testSingleStack() {
        System.out.println(TEST_LINE);
        System.out.println("Testing SingleStack");
        Integer[] testValues = getValues();
        System.out.println(LINE);
        System.out.println("SingleStack<Integer> source = new SingleStack<>();");
        final SingleStack<Integer> source = new SingleStack<>();
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println(LINE);
        System.out.println("Push objects: " + Arrays.toString(testValues));
        for (Integer object : testValues) {
            System.out.println("  push: " + object);
            source.push(object);
        }
        System.out.println("  isEmpty {false}: " + source.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", testValues[testValues.length - 1], source.peek()));
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println(LINE);
        System.out.println("source.splitAlternate(left, right)");
        final SingleStack<Integer> left = new SingleStack<>();
        final SingleStack<Integer> right = new SingleStack<>();
        source.splitAlternate(left, right);
        System.out.println("source");
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println("left");
        System.out.println("  isEmpty {false}: " + left.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", testValues[0], left.peek()));
        System.out.println("  Contents: " + objectsToString(left));
        System.out.println("right");
        System.out.println("  isEmpty {false}: " + right.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", testValues[1], right.peek()));
        System.out.println("  Contents: " + objectsToString(right));
        System.out.println(LINE);
        System.out.println("target.combine(left, right)");
        final SingleStack<Integer> target = new SingleStack<>();
        target.combine(left, right);
        System.out.println("target");
        System.out.println("  isEmpty {false}: " + target.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", testValues[testValues.length - 1], target.peek()));
        System.out.println("  Contents: " + objectsToString(target));
        System.out.println("left");
        System.out.println("  isEmpty {true}: " + left.isEmpty());
        System.out.println("  Contents: " + objectsToString(left));
        System.out.println("right");
        System.out.println("  isEmpty {true}: " + right.isEmpty());
        System.out.println("  Contents: " + objectsToString(right));
        System.out.println(LINE);
        System.out.println("Clear target");
        int i = testValues.length - 1;

        while (!target.isEmpty()) {
            System.out.println("  Pop {" + testValues[i] + "}: " + target.pop());
            i--;
        }
        System.out.println();
        System.out.println(LINE);
        System.out.println("Test Stack with strings");
        SingleStack<String> stringStack = new SingleStack<>();

        for (String string : testStrings) {
            stringStack.push(string);
        }
        while (!stringStack.isEmpty()) {
            System.out.println(stringStack.pop());
        }
    }

    /**
     * Test {@code SingleQueue}.
     */
    private static void testSingleQueue() {
        System.out.println(TEST_LINE);
        System.out.println("Testing SingleQueue");
        Integer[] testValues = getValues();
        System.out.println(LINE);
        System.out.println("SingleQueue<Integer> source = new SingleQueue<>();");
        final SingleQueue<Integer> source = new SingleQueue<>();
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println(LINE);
        System.out.println("Insert objects: " + Arrays.toString(testValues));
        for (Integer object : testValues) {
            System.out.println("  insert: " + object);
            source.insert(object);
        }
        System.out.println("  isEmpty {false}: " + source.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", testValues[0], source.peek()));
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println(LINE);
        System.out.println("source.splitAlternate(left, right)");
        final SingleQueue<Integer> left = new SingleQueue<>();
        final SingleQueue<Integer> right = new SingleQueue<>();
        source.splitAlternate(left, right);
        System.out.println("source");
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println("left");
        System.out.println("  isEmpty {false}: " + left.isEmpty());
        System.out.println("  peek {" + testValues[0] + "}: " + left.peek());
        System.out.println("  Contents: " + objectsToString(left));
        System.out.println("right");
        System.out.println("  isEmpty {false}: " + right.isEmpty());
        System.out.println("  peek {" + testValues[1] + "}: " + right.peek());
        System.out.println("  Contents: " + objectsToString(right));
        System.out.println(LINE);
        System.out.println("target.combine(left, right)");
        final SingleQueue<Integer> target = new SingleQueue<>();
        target.combine(left, right);
        System.out.println("target");
        System.out.println("  isEmpty {false}: " + target.isEmpty());
        System.out.println("  peek {" + testValues[0] + "}: " + target.peek());
        System.out.println("  Contents: " + objectsToString(target));
        System.out.println("left");
        System.out.println("  isEmpty {true}: " + left.isEmpty());
        System.out.println("  Contents: " + objectsToString(left));
        System.out.println("right");
        System.out.println("  isEmpty {true}: " + right.isEmpty());
        System.out.println("  Contents: " + objectsToString(right));
        System.out.println(LINE);
        System.out.println("Clear target");
        int i = 0;

        while (!target.isEmpty()) {
            System.out.println("  remove {" + testValues[i] + "}: " + target.remove());
            i++;
        }
        System.out.println();
        System.out.println(LINE);
        System.out.println("Test Queue with strings");
        SingleQueue<String> stringQueue = new SingleQueue<>();

        for (String string : testStrings) {
            stringQueue.insert(string);
        }
        while (!stringQueue.isEmpty()) {
            System.out.println(stringQueue.remove());
        }
    }

    /**
     * Test {@code SinglePriorityQueue}.
     */
    private static void testSinglePriorityQueue() {
        System.out.println(TEST_LINE);
        System.out.println("Testing SinglePriorityQueue");
        Integer[] testValues = getValues();
        Integer[] sortedValues = Arrays.copyOf(testValues, testValues.length);
        Arrays.sort(sortedValues);
        System.out.println(LINE);
        System.out.println("SinglePriorityQueue<Integer> source = new SinglePriorityQueue<>();");
        final SinglePriorityQueue<Integer> source = new SinglePriorityQueue<>();
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println(LINE);
        System.out.println("Insert objects: " + Arrays.toString(testValues));
        for (Integer object : testValues) {
            System.out.println("  insert: " + object);
            source.insert(object);
        }
        System.out.println("  isEmpty {false}: " + source.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", sortedValues[0], source.peek()));
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println(LINE);
        Integer key = sortedValues[sortedValues.length / 2];
        System.out.println("source.splitByKey(" + key + ", left, right)");
        final SinglePriorityQueue<Integer> left = new SinglePriorityQueue<>();
        final SinglePriorityQueue<Integer> right = new SinglePriorityQueue<>();
        source.splitByKey(key, left, right);
        System.out.println("source");
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println("left");
        System.out.println("  isEmpty {false}: " + left.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", sortedValues[0], left.peek()));
        System.out.println("  Contents: " + objectsToString(left));
        System.out.println("right");
        System.out.println("  isEmpty {false}: " + right.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", key, right.peek()));
        System.out.println("  Contents: " + objectsToString(right));
        System.out.println(LINE);
        System.out.println("target.combine(left, right)");
        final SinglePriorityQueue<Integer> target = new SinglePriorityQueue<>();
        target.combine(left, right);
        System.out.println("target");
        System.out.println("  isEmpty {false}: " + target.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", sortedValues[0], target.peek()));
        System.out.println("  Contents: " + objectsToString(target));
        System.out.println("left");
        System.out.println("  isEmpty {true}: " + left.isEmpty());
        System.out.println("  Contents: " + objectsToString(left));
        System.out.println("right");
        System.out.println("  isEmpty {true}: " + right.isEmpty());
        System.out.println("  Contents: " + objectsToString(right));
        System.out.println(LINE);
        System.out.println("Clear target");
        int i = 0;

        while (!target.isEmpty()) {
            System.out.println("  remove {" + sortedValues[i] + "}: " + target.remove());
            i++;
        }
        System.out.println();
        System.out.println(LINE);
        System.out.println("Test Priority Queue with strings");
        SinglePriorityQueue<String> stringQueue = new SinglePriorityQueue<>();

        for (String string : testStrings) {
            stringQueue.insert(string);
        }
        while (!stringQueue.isEmpty()) {
            System.out.println(stringQueue.remove());
        }
    }

    /**
     * Test {@code SingleList} - Basic functionality.
     */
    private static void testSingleList() {
        // Test objects.
        int sameValue = 75;
        int badValue = 999;
        // Test arrays.
        Integer[] testValues = getValues();
        int length = testValues.length;
        Integer[] sortedValues = Arrays.copyOf(testValues, testValues.length);
        Arrays.sort(sortedValues);
        Integer[] sameValues = new Integer[length];
        Arrays.fill(sameValues, sameValue);
        Integer[] reverseValues = new Integer[length];

        for (int i = 0; i < length; i++) {
            reverseValues[i] = testValues[length - 1 - i];
        }
        Integer[] uniqueValues1 = new Integer[length];

        for (int i = 0; i < length; i++) {
            uniqueValues1[i] = i;
        }
        Integer[] uniqueValues2 = Arrays.copyOf(uniqueValues1, length);
        // Test SingleLists.
        SingleList<Integer> source = new SingleList<>();
        SingleList<Integer> target = new SingleList<>();
        SingleList<Integer> same = new SingleList<>();
        SingleList<Integer> left = new SingleList<>();
        SingleList<Integer> right = new SingleList<>();

        // Tests.
        System.out.println(TEST_LINE);
        System.out.println("Testing SingleList");
        System.out.println(LINE);
        System.out.println("SingleList<Integer> source = new SingleList<>();");
        System.out.println("  isEmpty {true}: " + source.isEmpty());
        System.out.println(LINE);
        Integer[] appendValues = Arrays.copyOfRange(testValues, length - 2, length);
        System.out.println("Append objects: " + Arrays.toString(appendValues));
        for (Integer object : appendValues) {
            System.out.println("  append: " + object);
            source.append(object);
        }
        System.out.println("  isEmpty {false}: " + source.isEmpty());
        System.out.println("  peek {" + appendValues[0] + "}: " + source.peek());
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println(LINE);
        System.out.println("prepend: " + testValues[0]);
        source.prepend(testValues[0]);
        System.out.println("  isEmpty {false}: " + source.isEmpty());
        System.out.println("  peek {" + testValues[0] + "}: " + source.peek());
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println(LINE);
        Integer[] insertValues = Arrays.copyOfRange(testValues, 1, length - 2);
        System.out.println("Insert objects: " + Arrays.toString(appendValues));
        int i = 1;
        for (Integer object : insertValues) {
            System.out.println(String.format("  insert: (%d, %d)", i, object));
            source.insert(i, object);
            i++;
        }
        System.out.println("  isEmpty {false}: " + source.isEmpty());
        System.out.println(String.format("  peek {%d}: %d", testValues[0], source.peek()));
        System.out.println("  Contents: " + objectsToString(source));
        System.out.println(LINE);
        System.out.println(String.format("contains %d {false}: %b", badValue, source.contains(badValue)));
        int object = testValues[length / 2];
        System.out.println(String.format("contains %d {true}: %b", object, source.contains(object)));
        System.out.println(LINE);
        System.out.println(String.format("find %d {%s}: ", badValue, source.find(badValue)));
        System.out.println(String.format("find %d {%d}: %d", object, object, source.find(object)));
        System.out.println(LINE);
        System.out.println(String.format("get %d {%d}: %d", length / 2, object, source.get(length / 2)));
        System.out.println(LINE);
        System.out.println(String.format("index %d {%d}: %d", object, length / 2, source.index(object)));
        System.out.println(String.format("index %d {%d}: %d", badValue, -1, source.index(badValue)));
        System.out.println(LINE);
        System.out.println(String.format("max {%d}: %d", sortedValues[length - 1], source.max()));
        System.out.println(String.format("min {%d}: %d", sortedValues[0], source.min()));
        System.out.println(LINE);
        System.out.println("Contents: " + objectsToString(source));
        System.out.println(String.format("  count %d {%d}: %d", badValue, 0, source.count(badValue)));
        fillSingleList(same, sameValues);
        System.out.println("Contents: " + objectsToString(same));
        System.out.println(String.format("  count %d {%d}: %d", sameValue, length, same.count(sameValue)));
        System.out.println(LINE);
        System.out.println("Contents: " + objectsToString(same));
        same.clean();
        System.out.println(String.format("  clean {[%d]}: %s", sameValue, objectsToString(same)));
        System.out.println(LINE);
        same = new SingleList<>();
        fillSingleList(same, sameValues);
        System.out.println("Contents: " + objectsToString(same));
        System.out.println(String.format("  removeMany %d {%s}: %s", badValue, Arrays.toString(sameValues),
                objectsToString(same)));
        same.removeMany(sameValue);
        System.out.println(String.format("  removeMany %d {[]}: %s", sameValue, objectsToString(same)));
        System.out.println(LINE);
        System.out.println("Contents: " + objectsToString(source));
        System.out.println(String.format("  removeFront {%d}: %d", testValues[0], source.removeFront()));
        System.out.println(LINE);
        System.out.println("Contents: " + objectsToString(source));
        System.out.println(String.format("  remove %d {null}: %s", badValue, source.remove(badValue)));
        System.out.println(String.format("  remove %d {%d}: %d", testValues[length - 1], testValues[length - 1],
                source.remove(testValues[length - 1])));
        System.out.println("Contents: " + objectsToString(source));
        System.out.println(LINE);
        source = new SingleList<>();
        fillSingleList(source, testValues);
        System.out.println("Contents: " + objectsToString(source));
        source.reverse();
        System.out
                .println(String.format("  reverse {%s}: %s", Arrays.toString(reverseValues), objectsToString(source)));
        System.out.println(LINE);
        source = new SingleList<>();
        fillSingleList(source, testValues);
        System.out.println("Contents: " + objectsToString(source));
        source.split(left, right);
        System.out.println(String.format("  split {%s, %s}: %s, %s",
                Arrays.toString(Arrays.copyOfRange(testValues, 0, length / 2 + 1)),
                Arrays.toString(Arrays.copyOfRange(testValues, length / 2 + 1, length)), objectsToString(left),
                objectsToString(right)));
        System.out.println(LINE);
        source = new SingleList<>();
        left = new SingleList<>();
        right = new SingleList<>();
        fillSingleList(source, testValues);
        System.out.println("Contents: " + objectsToString(source));
        source.splitAlternate(left, right);
        Integer[] leftAlt = new Integer[length / 2 + 1];
        Integer[] rightAlt = new Integer[length - (length / 2 + 1)];
        i = 0;

        for (int j = 0; j < length / 2; j++) {
            leftAlt[j] = testValues[i++];
            rightAlt[j] = testValues[i++];
        }
        leftAlt[length / 2] = testValues[i];
        System.out.println(String.format("  splitAlternate {%s, %s}: %s, %s", Arrays.toString(leftAlt),
                Arrays.toString(rightAlt), objectsToString(left), objectsToString(right)));
        System.out.println(LINE);
        System.out.println(String.format("Contents: %s, %s", objectsToString(left), objectsToString(right)));
        source.combine(left, right);
        System.out.println(String.format("  combine {%s}: %s", objectsToString(source), objectsToString(source)));
        System.out.println(LINE);
        source = new SingleList<>();
        target = new SingleList<>();
        System.out.println(String.format("Contents: %s, %s", objectsToString(source), objectsToString(target)));
        System.out.println(String.format("  identical {%b}: %b", true, source.equals(target)));
        fillSingleList(source, testValues);
        fillSingleList(target, testValues);
        System.out.println(String.format("Contents: %s, %s", objectsToString(source), objectsToString(target)));
        System.out.println(String.format("  identical {%b}: %b", true, source.equals(target)));
        source = new SingleList<>();
        target = new SingleList<>();
        fillSingleList(source, testValues);
        fillSingleList(target, sortedValues);
        System.out.println(String.format("Contents: %s, %s", objectsToString(source), objectsToString(target)));
        System.out.println(String.format("  identical {%b}: %b", false, source.equals(target)));
        System.out.println(LINE);
        shuffleArray(uniqueValues1);
        shuffleArray(uniqueValues2);
        left = new SingleList<>();
        right = new SingleList<>();
        target = new SingleList<>();
        fillSingleList(left, uniqueValues1);
        fillSingleList(right, uniqueValues2);
        target.intersection(left, right);
        System.out.println(
                String.format("Contents: %s, %s", Arrays.toString(uniqueValues1), Arrays.toString(uniqueValues2)));
        System.out.println(
                String.format("  intersection {%s}: %s", Arrays.toString(uniqueValues1), objectsToString(target)));
        right = new SingleList<>();
        target = new SingleList<>();
        fillSingleList(left, uniqueValues1);
        fillSingleList(right, new Integer[] { badValue });
        target.intersection(left, right);
        System.out.println(String.format("Contents: %s, [%d]", Arrays.toString(uniqueValues1), badValue));
        System.out.println(String.format("  intersection {[]}: %s", objectsToString(target)));
        System.out.println(LINE);
        Integer[] leftUnique = Arrays.copyOfRange(uniqueValues1, 0, length / 2);
        Integer[] rightUnique = Arrays.copyOfRange(uniqueValues1, length / 2, length);
        left = new SingleList<>();
        right = new SingleList<>();
        target = new SingleList<>();
        fillSingleList(left, leftUnique);
        fillSingleList(right, rightUnique);
        target.union(left, right);
        System.out
                .println(String.format("Contents: %s, %s", Arrays.toString(leftUnique), Arrays.toString(rightUnique)));
        System.out.println(String.format("  union {%s}: %s", Arrays.toString(uniqueValues1), objectsToString(target)));
        System.out.println(LINE);
        System.out.println("SingleList<Character> characters = new SingleList<>();");
        String[] data = { "CP213", "David", "Laurier", "covid" };
        SingleList<String> strings = new SingleList<>();

        for (String ch : data) {
            System.out.println("  append: " + ch);
            strings.append(ch);
        }
        System.out.println("  Contents: " + objectsToString(strings));
        System.out.println();
        System.out.println(LINE);
        System.out.println("Test List with strings");
        SingleList<String> stringList = new SingleList<>();

        for (String string : testStrings) {
            stringList.append(string);
        }
        while (!stringList.isEmpty()) {
            System.out.println(stringList.removeFront());
        }
    }

    /**
     * Comprehensive testing for SingleList - Edge cases and boundary conditions.
     */
    private static void testSingleListComprehensive() {
        System.out.println(TEST_LINE);
        System.out.println("Testing SingleList - Comprehensive Edge Cases");
        System.out.println(LINE);

        // Test 1: Empty list operations
        System.out.println("EDGE CASE 1: Empty List Operations");
        SingleList<Integer> empty = new SingleList<>();
        System.out.println("  isEmpty {true}: " + empty.isEmpty());
        System.out.println("  getLength {0}: " + empty.getLength());
        System.out.println("  peek {null}: " + empty.peek());
        System.out.println("  removeFront {null}: " + empty.removeFront());
        System.out.println("  max {null}: " + empty.max());
        System.out.println("  min {null}: " + empty.min());
        System.out.println("  get(-1) {null}: " + empty.get(-1));
        System.out.println("  get(0) {null}: " + empty.get(0));
        System.out.println("  contains(5) {false}: " + empty.contains(5));
        System.out.println("  find(5) {null}: " + empty.find(5));
        System.out.println("  index(5) {-1}: " + empty.index(5));
        System.out.println("  count(5) {0}: " + empty.count(5));
        System.out.println(LINE);

        // Test 2: Single element list
        System.out.println("EDGE CASE 2: Single Element List");
        SingleList<Integer> single = new SingleList<>();
        single.append(42);
        System.out.println("  isEmpty {false}: " + single.isEmpty());
        System.out.println("  getLength {1}: " + single.getLength());
        System.out.println("  peek {42}: " + single.peek());
        System.out.println("  get(0) {42}: " + single.get(0));
        System.out.println("  get(-1) {null}: " + single.get(-1));
        System.out.println("  get(1) {null}: " + single.get(1));
        System.out.println("  contains(42) {true}: " + single.contains(42));
        System.out.println("  contains(99) {false}: " + single.contains(99));
        System.out.println("  find(42) {42}: " + single.find(42));
        System.out.println("  index(42) {0}: " + single.index(42));
        System.out.println("  max {42}: " + single.max());
        System.out.println("  min {42}: " + single.min());
        System.out.println("  removeFront {42}: " + single.removeFront());
        System.out.println("  isEmpty after removeFront {true}: " + single.isEmpty());
        System.out.println(LINE);

        // Test 3: Append to empty list
        System.out.println("EDGE CASE 3: Append to Empty List");
        SingleList<Integer> appendEmpty = new SingleList<>();
        appendEmpty.append(10);
        System.out.println("  getLength {1}: " + appendEmpty.getLength());
        System.out.println("  peek {10}: " + appendEmpty.peek());
        System.out.println("  get(0) {10}: " + appendEmpty.get(0));
        System.out.println(LINE);

        // Test 4: Prepend to empty list
        System.out.println("EDGE CASE 4: Prepend to Empty List");
        SingleList<Integer> prependEmpty = new SingleList<>();
        prependEmpty.prepend(20);
        System.out.println("  getLength {1}: " + prependEmpty.getLength());
        System.out.println("  peek {20}: " + prependEmpty.peek());
        System.out.println(LINE);

        // Test 5: Insert at various positions
        System.out.println("EDGE CASE 5: Insert at Various Positions");
        SingleList<Integer> insertTest = new SingleList<>();
        insertTest.append(1);
        insertTest.append(3);
        insertTest.insert(1, 2); // Insert at middle
        System.out.println("  insert(1, 2) - length {3}: " + insertTest.getLength());
        System.out.println("  get(1) {2}: " + insertTest.get(1));
        insertTest.insert(0, 0); // Insert at front
        System.out.println("  insert(0, 0) - get(0) {0}: " + insertTest.get(0));
        insertTest.insert(100, 4); // Insert beyond length (should append)
        System.out.println("  insert(100, 4) - last element {4}: " + insertTest.get(insertTest.getLength() - 1));
        insertTest.insert(-5, -1); // Insert at negative index (should insert at front)
        System.out.println("  insert(-5, -1) - get(0) {-1}: " + insertTest.get(0));
        System.out.println(LINE);

        // Test 6: Remove operations
        System.out.println("EDGE CASE 6: Remove Operations");
        SingleList<Integer> removeTest = new SingleList<>();
        removeTest.append(1);
        removeTest.append(2);
        removeTest.append(3);
        System.out.println("  remove(1) {1}: " + removeTest.remove(1));
        System.out.println("  remove(2) {2}: " + removeTest.remove(2));
        System.out.println("  remove(3) {3}: " + removeTest.remove(3));
        System.out.println("  remove(99) {null}: " + removeTest.remove(99));
        System.out.println("  isEmpty after all removes {true}: " + removeTest.isEmpty());
        System.out.println(LINE);

        // Test 7: RemoveMany operations
        System.out.println("EDGE CASE 7: RemoveMany Operations");
        SingleList<Integer> removeManyTest = new SingleList<>();
        removeManyTest.append(1);
        removeManyTest.append(2);
        removeManyTest.append(2);
        removeManyTest.append(3);
        removeManyTest.append(2);
        removeManyTest.append(4);
        removeManyTest.append(2);
        System.out.println("  Before removeMany(2): " + objectsToString(removeManyTest));
        removeManyTest.removeMany(2);
        System.out.println("  After removeMany(2) - length {3}: " + removeManyTest.getLength());
        System.out.println("  count(2) {0}: " + removeManyTest.count(2));
        System.out.println("  contains(2) {false}: " + removeManyTest.contains(2));
        System.out.println("  Contents: " + objectsToString(removeManyTest));
        System.out.println(LINE);

        // Test 8: Clean operations
        System.out.println("EDGE CASE 8: Clean Operations");
        SingleList<Integer> cleanTest = new SingleList<>();
        cleanTest.append(1);
        cleanTest.append(2);
        cleanTest.append(1);
        cleanTest.append(3);
        cleanTest.append(2);
        cleanTest.append(1);
        cleanTest.append(4);
        System.out.println("  Before clean: " + objectsToString(cleanTest));
        cleanTest.clean();
        System.out.println("  After clean - length {4}: " + cleanTest.getLength());
        System.out.println("  count(1) {1}: " + cleanTest.count(1));
        System.out.println("  count(2) {1}: " + cleanTest.count(2));
        System.out.println("  Contents: " + objectsToString(cleanTest));
        System.out.println(LINE);

        // Test 9: Reverse operations
        System.out.println("EDGE CASE 9: Reverse Operations");
        SingleList<Integer> reverseTest = new SingleList<>();
        reverseTest.append(1);
        reverseTest.append(2);
        reverseTest.append(3);
        System.out.println("  Before reverse: " + objectsToString(reverseTest));
        reverseTest.reverse();
        System.out.println("  After reverse - first {3}: " + reverseTest.get(0));
        System.out.println("  After reverse - last {1}: " + reverseTest.get(reverseTest.getLength() - 1));
        System.out.println("  Contents: " + objectsToString(reverseTest));
        System.out.println(LINE);

        // Test 10: Get operations with boundary conditions
        System.out.println("EDGE CASE 10: Get Operations - Boundary Conditions");
        SingleList<Integer> getTest = new SingleList<>();
        getTest.append(10);
        getTest.append(20);
        getTest.append(30);
        System.out.println("  get(-1) {null}: " + getTest.get(-1));
        System.out.println("  get(0) {10}: " + getTest.get(0));
        System.out.println("  get(2) {30}: " + getTest.get(2));
        System.out.println("  get(3) {null}: " + getTest.get(3));
        System.out.println("  get(100) {null}: " + getTest.get(100));
        System.out.println(LINE);

        // Test 11: Index operations
        System.out.println("EDGE CASE 11: Index Operations");
        SingleList<Integer> indexTest = new SingleList<>();
        indexTest.append(10);
        indexTest.append(20);
        indexTest.append(10);
        indexTest.append(30);
        System.out.println("  index(10) {0}: " + indexTest.index(10));
        System.out.println("  index(20) {1}: " + indexTest.index(20));
        System.out.println("  index(99) {-1}: " + indexTest.index(99));
        System.out.println(LINE);

        // Test 12: Equals operations
        System.out.println("EDGE CASE 12: Equals Operations");
        SingleList<Integer> equals1 = new SingleList<>();
        SingleList<Integer> equals2 = new SingleList<>();
        System.out.println("  equals - both empty {true}: " + equals1.equals(equals2));
        equals1.append(1);
        equals1.append(2);
        equals2.append(1);
        System.out.println("  equals - different lengths {false}: " + equals1.equals(equals2));
        equals2.append(3);
        System.out.println("  equals - different contents {false}: " + equals1.equals(equals2));
        equals2 = new SingleList<>();
        equals2.append(1);
        equals2.append(2);
        System.out.println("  equals - same contents {true}: " + equals1.equals(equals2));
        System.out.println(LINE);

        // Test 13: Split operations
        System.out.println("EDGE CASE 13: Split Operations");
        SingleList<Integer> splitTest = new SingleList<>();
        splitTest.append(1);
        splitTest.append(2);
        splitTest.append(3);
        splitTest.append(4);
        splitTest.append(5);
        SingleList<Integer> leftSplit = new SingleList<>();
        SingleList<Integer> rightSplit = new SingleList<>();
        splitTest.split(leftSplit, rightSplit);
        System.out.println("  split - source empty {true}: " + splitTest.isEmpty());
        System.out.println("  split - left length {3}: " + leftSplit.getLength());
        System.out.println("  split - right length {2}: " + rightSplit.getLength());
        System.out.println("  split - left first {1}: " + leftSplit.get(0));
        System.out.println("  split - right first {4}: " + rightSplit.get(0));
        System.out.println(LINE);

        // Test 14: SplitAlternate operations
        System.out.println("EDGE CASE 14: SplitAlternate Operations");
        SingleList<Integer> splitAltTest = new SingleList<>();
        splitAltTest.append(1);
        splitAltTest.append(2);
        splitAltTest.append(3);
        splitAltTest.append(4);
        splitAltTest.append(5);
        SingleList<Integer> leftAlt = new SingleList<>();
        SingleList<Integer> rightAlt = new SingleList<>();
        splitAltTest.splitAlternate(leftAlt, rightAlt);
        System.out.println("  splitAlternate - source empty {true}: " + splitAltTest.isEmpty());
        System.out.println("  splitAlternate - left length {3}: " + leftAlt.getLength());
        System.out.println("  splitAlternate - right length {2}: " + rightAlt.getLength());
        System.out.println("  splitAlternate - left first {1}: " + leftAlt.get(0));
        System.out.println("  splitAlternate - right first {2}: " + rightAlt.get(0));
        System.out.println(LINE);

        // Test 15: Combine operations
        System.out.println("EDGE CASE 15: Combine Operations");
        SingleList<Integer> combineTest = new SingleList<>();
        SingleList<Integer> leftCombine = new SingleList<>();
        SingleList<Integer> rightCombine = new SingleList<>();
        leftCombine.append(1);
        leftCombine.append(3);
        rightCombine.append(2);
        rightCombine.append(4);
        combineTest.combine(leftCombine, rightCombine);
        System.out.println("  combine - left empty {true}: " + leftCombine.isEmpty());
        System.out.println("  combine - right empty {true}: " + rightCombine.isEmpty());
        System.out.println("  combine - result length {4}: " + combineTest.getLength());
        System.out.println("  combine - alternating: " + objectsToString(combineTest));
        System.out.println(LINE);

        // Test 16: Intersection operations
        System.out.println("EDGE CASE 16: Intersection Operations");
        SingleList<Integer> interTest = new SingleList<>();
        SingleList<Integer> leftInter = new SingleList<>();
        SingleList<Integer> rightInter = new SingleList<>();
        leftInter.append(1);
        leftInter.append(2);
        leftInter.append(3);
        leftInter.append(4);
        rightInter.append(2);
        rightInter.append(4);
        rightInter.append(5);
        rightInter.append(6);
        interTest.intersection(leftInter, rightInter);
        System.out.println("  intersection - length {2}: " + interTest.getLength());
        System.out.println("  intersection - contains 2 {true}: " + interTest.contains(2));
        System.out.println("  intersection - contains 4 {true}: " + interTest.contains(4));
        System.out.println("  intersection - not contains 1 {false}: " + interTest.contains(1));
        System.out.println("  Contents: " + objectsToString(interTest));
        System.out.println(LINE);

        // Test 17: Union operations
        System.out.println("EDGE CASE 17: Union Operations");
        SingleList<Integer> unionTest = new SingleList<>();
        SingleList<Integer> leftUnion = new SingleList<>();
        SingleList<Integer> rightUnion = new SingleList<>();
        leftUnion.append(1);
        leftUnion.append(2);
        leftUnion.append(3);
        rightUnion.append(2);
        rightUnion.append(3);
        rightUnion.append(4);
        rightUnion.append(5);
        unionTest.union(leftUnion, rightUnion);
        System.out.println("  union - length {5}: " + unionTest.getLength());
        System.out.println("  union - contains all {true}: " + 
                (unionTest.contains(1) && unionTest.contains(2) && unionTest.contains(3) && 
                 unionTest.contains(4) && unionTest.contains(5)));
        System.out.println("  union - no duplicates, count(2) {1}: " + unionTest.count(2));
        System.out.println("  Contents: " + objectsToString(unionTest));
        System.out.println(LINE);

        // Test 18: Min/Max with duplicates
        System.out.println("EDGE CASE 18: Min/Max with Duplicates");
        SingleList<Integer> minMaxTest = new SingleList<>();
        minMaxTest.append(5);
        minMaxTest.append(1);
        minMaxTest.append(5);
        minMaxTest.append(10);
        minMaxTest.append(1);
        minMaxTest.append(10);
        System.out.println("  max with duplicates {10}: " + minMaxTest.max());
        System.out.println("  min with duplicates {1}: " + minMaxTest.min());
        System.out.println(LINE);

        // Test 19: Count operations
        System.out.println("EDGE CASE 19: Count Operations");
        SingleList<Integer> countTest = new SingleList<>();
        countTest.append(1);
        countTest.append(2);
        countTest.append(1);
        countTest.append(3);
        countTest.append(1);
        System.out.println("  count(1) {3}: " + countTest.count(1));
        System.out.println("  count(2) {1}: " + countTest.count(2));
        System.out.println("  count(99) {0}: " + countTest.count(99));
        System.out.println(LINE);

        // Test 20: String operations
        System.out.println("EDGE CASE 20: String Operations");
        SingleList<String> stringTest = new SingleList<>();
        stringTest.append("apple");
        stringTest.append("banana");
        stringTest.append("cherry");
        System.out.println("  contains('banana') {true}: " + stringTest.contains("banana"));
        System.out.println("  find('cherry') {cherry}: " + stringTest.find("cherry"));
        System.out.println("  max {cherry}: " + stringTest.max());
        System.out.println("  min {apple}: " + stringTest.min());
        System.out.println(LINE);
    }

    /**
     * Returns a comma-delimited string of the objects in a data structure from
     * front to rear.
     *
     * @param <T>           the {@code SingleNode} data type
     * @param dataStructure the linked structure containing the objects
     * @return a string with the objects of {@code dataStructure} listed from front
     *         to rear
     */
    private static <T> String objectsToString(SingleLink<T> dataStructure) {
        List<T> actual = new ArrayList<>();

        for (T object : dataStructure) {
            actual.add(object);
        }
        return actual.toString();
    }

}
