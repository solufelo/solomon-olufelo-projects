package cp213;

/**
 * A single linked list structure of {@code T} objects. Extends the
 * {@code SingleLink} class.
 *
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-09-07
 * @param <T> the {@code SingleNode} data type
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Searches for the first occurrence of {@code key} in this SingleList. Private
     * helper methods - used only by other ADT methods.
     *
     * @param key the object to look for
     * @return a pointer to the node previous to the node containing {@code key}
     */
    private SingleNode<T> linearSearch(final T key) {
        SingleNode<T> previous = null;
        SingleNode<T> current = this.front;

        while (current != null) {
            if (current.getDatum().compareTo(key) == 0) {
                return previous;
            }
            previous = current;
            current = current.getNext();
        }
        return null;
    }

    /**
     * Appends data to the end of {@code this}
     *
     * @param datum the object to append
     */
    public void append(final T datum) {
        // Create new node with the datum (next is null since it's at the end)
        SingleNode<T> newNode = new SingleNode<T>(datum, null);

        // If list is empty, new node is front
        if (this.rear == null) {
            this.front = newNode;
        } else {
            // Link current rear to new node
            this.rear.setNext(newNode);
        }

        // Update rear and length
        this.rear = newNode;
        this.length++;
    }

    /**
     * Removes duplicates from {@code this}. The list contains one and only one of
     * each object formerly present in {@code this}. The first occurrence of each
     * object is preserved.
     */
    public void clean() {
        SingleNode<T> current = this.front;

        while (current != null) {
            T datum = current.getDatum();
            SingleNode<T> previous = current;
            SingleNode<T> check = current.getNext();

            // Remove all subsequent occurrences of this datum
            while (check != null) {
                if (check.getDatum().compareTo(datum) == 0) {
                    // Remove check node
                    previous.setNext(check.getNext());
                    this.length--;

                    // Update rear if we removed the last node
                    if (previous.getNext() == null) {
                        this.rear = previous;
                    }

                    check = previous.getNext();
                } else {
                    previous = check;
                    check = check.getNext();
                }
            }

            current = current.getNext();
        }
    }

    /**
     * Combines the contents of {@code left} and {@code right} into {@code this}.
     * Moves nodes only - does not refer to data in any way, or call the high-level
     * methods {@code insert} or {@code remove}. {@code left} and {@code right} are
     * empty when done. Nodes are moved alternately from {@code left} and
     * {@code right} into {@code this}. {@code this} may be empty. May call any
     * appropriate {@code SingleLink} helper methods available. {@code left} and
     * {@code right} are not necessarily the same length.
     *
     * @param left  the first {@code SingleList} to extract nodes from
     * @param right the second {@code SingleList} to extract nodes from
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {
        // Alternate between left and right until both are empty
        while (left.front != null || right.front != null) {
            // Move from left if available
            if (left.front != null) {
                this.moveFrontToRear(left);
            }
            // Move from right if available
            if (right.front != null) {
                this.moveFrontToRear(right);
            }
        }
    }

    /**
     * Determines if {@code this} contains {@code key}.
     *
     * @param key the key object to look for
     * @return {@code true} if {@code key} is in {@code this}, {@code false}
     *         otherwise
     */
    public boolean contains(final T key) {
        SingleNode<T> current = this.front;

        while (current != null) {
            if (current.getDatum().compareTo(key) == 0) {
                return true;
            }
            current = current.getNext();
        }

        return false;
    }

    /**
     * Finds the number of times {@code key} appears in {@code this}.
     *
     * @param key the object to look for
     * @return the number of times {@code key} appears in {@code this}
     */
    public int count(final T key) {
        int count = 0;
        SingleNode<T> current = this.front;

        while (current != null) {
            if (current.getDatum().compareTo(key) == 0) {
                count++;
            }
            current = current.getNext();
        }

        return count;
    }

    /**
     * Finds and returns the object in {@code this} that matches {@code key}.
     *
     * @param key the object to search for
     * @return the object that matches {@code key}, {@code null} otherwise
     */
    public T find(final T key) {
        SingleNode<T> current = this.front;

        while (current != null) {
            if (current.getDatum().compareTo(key) == 0) {
                return current.getDatum();
            }
            current = current.getNext();
        }

        return null;
    }

    /**
     * Get the {@code n}th object in {@code this}.
     *
     * @param n the index of the object to return
     * @return the nth object in {@code this} if {@code n} is a valid index,
     *         {@code null} otherwise
     */
    public T get(final int n) {
        if (n < 0 || n >= this.length) {
            return null;
        }

        SingleNode<T> current = this.front;
        for (int i = 0; i < n; i++) {
            current = current.getNext();
        }

        return current.getDatum();
    }

    /**
     * Determines whether two lists are identical.
     *
     * @param source the list to compare against {@code this}
     * @return {@code true} if {@code this} contains the same objects in the same
     *         order as {@code source}, {@code false} otherwise
     */
    public boolean equals(final SingleList<T> source) {
        // Check if lengths are different
        if (this.length != source.length) {
            return false;
        }

        SingleNode<T> current1 = this.front;
        SingleNode<T> current2 = source.front;

        // Compare each element
        while (current1 != null && current2 != null) {
            if (current1.getDatum().compareTo(current2.getDatum()) != 0) {
                return false;
            }
            current1 = current1.getNext();
            current2 = current2.getNext();
        }

        return true;
    }

    /**
     * Finds the first location of {@code key} in {@code this}.
     *
     * @param key the object to search for
     * @return the index of {@code key} in {@code this}, -1 otherwise
     */
    public int index(final T key) {
        SingleNode<T> current = this.front;
        int index = 0;

        while (current != null) {
            if (current.getDatum().compareTo(key) == 0) {
                return index;
            }
            current = current.getNext();
            index++;
        }

        return -1;
    }

    /**
     * Inserts object into {@code this} at index {@code i}. If {@code i} greater
     * than the length of {@code this}, append data to the rear of {@code this}.
     *
     * @param i     The index to insert the new data at.
     * @param datum The new object to insert into this SingleList.
     */
    public void insert(int i, final T datum) {
        // If index is beyond length, append
        if (i >= this.length) {
            this.append(datum);
            return;
        }

        // If inserting at front
        if (i <= 0) {
            // Create new node pointing to current front
            SingleNode<T> newNode = new SingleNode<T>(datum, this.front);
            this.front = newNode;
            // If list was empty, also set rear
            if (this.rear == null) {
                this.rear = newNode;
            }
            this.length++;
            return;
        }

        // Find the node at position i-1
        SingleNode<T> previous = this.front;
        for (int j = 0; j < i - 1; j++) {
            previous = previous.getNext();
        }

        // Create new node pointing to the node that will follow it
        SingleNode<T> newNode = new SingleNode<T>(datum, previous.getNext());
        previous.setNext(newNode);

        // Update rear if inserting at end
        if (newNode.getNext() == null) {
            this.rear = newNode;
        }

        this.length++;
    }

    /**
     * Creates an intersection of {@code left} and {@code right} into {@code this}.
     * Copies data to {@code this}. {@code left} and {@code right} are unchanged.
     * Values from {@code left} are copied in order first, then objects from
     * {@code right} are copied in order.
     * <p>
     * In an intersection, data copied to {@code this} must appear in both
     * {@code left} and {@code right}.
     *
     * @param left  the first {@code SingleList} to create an intersection from
     * @param right the second {@code SingleList} to create an intersection from
     */
    public void intersection(final SingleList<T> left, final SingleList<T> right) {
        // Clear this list first
        this.front = null;
        this.rear = null;
        this.length = 0;

        // Check each element in left to see if it's also in right
        SingleNode<T> current = left.front;

        while (current != null) {
            T datum = current.getDatum();

            // Check if this datum is in right
            if (right.contains(datum)) {
                // Check if we already added it (avoid duplicates)
                if (!this.contains(datum)) {
                    this.append(datum);
                }
            }

            current = current.getNext();
        }
    }

    /**
     * Finds the maximum object in {@code this}.
     *
     * @return the maximum object or {@code null} if {@code this} is empty
     */
    public T max() {
        if (this.front == null) {
            return null;
        }

        T max = this.front.getDatum();
        SingleNode<T> current = this.front.getNext();

        while (current != null) {
            if (current.getDatum().compareTo(max) > 0) {
                max = current.getDatum();
            }
            current = current.getNext();
        }

        return max;
    }

    /**
     * Finds the minimum object in {@code this}.
     *
     * @return the minimum object or {@code null} if {@code this} is empty
     */
    public T min() {
        if (this.front == null) {
            return null;
        }

        T min = this.front.getDatum();
        SingleNode<T> current = this.front.getNext();

        while (current != null) {
            if (current.getDatum().compareTo(min) < 0) {
                min = current.getDatum();
            }
            current = current.getNext();
        }

        return min;
    }

    /**
     * Inserts object into the front of {@code this}.
     *
     * @param datum the object to insert into the front of {@code this}
     */
    public void prepend(final T datum) {
        // Create new node pointing to current front
        SingleNode<T> newNode = new SingleNode<T>(datum, this.front);
        this.front = newNode;

        // If list was empty, also set rear
        if (this.rear == null) {
            this.rear = newNode;
        }

        this.length++;
    }

    /**
     * Finds, removes, and returns the object in {@code this} that matches
     * {@code key}.
     *
     * @param key the object to search for
     * @return the object matching {@code key}, {@code null} otherwise
     */
    public T remove(final T key) {
        SingleNode<T> previous = this.linearSearch(key);

        if (previous == null) {
            // Check if the first node contains the key
            if (this.front != null && this.front.getDatum().compareTo(key) == 0) {
                // Remove from front
                T result = this.front.getDatum();
                this.front = this.front.getNext();
                this.length--;

                // If list is now empty, clear rear
                if (this.front == null) {
                    this.rear = null;
                }

                return result;
            }
            // Item not found
            return null;
        }

        // Remove the node after previous
        SingleNode<T> nodeToRemove = previous.getNext();
        if (nodeToRemove != null) {
            T result = nodeToRemove.getDatum();
            previous.setNext(nodeToRemove.getNext());
            this.length--;

            // If we removed the last node, update rear
            if (previous.getNext() == null) {
                this.rear = previous;
            }

            return result;
        }

        return null;
    }

    /**
     * Removes and returns the object at the front of {@code this}.
     *
     * @return the object at the front of {@code this}, if empty return {@code null}
     */
    public T removeFront() {
        if (this.front == null) {
            return null;
        }

        T result = this.front.getDatum();
        this.front = this.front.getNext();
        this.length--;

        // If list is now empty, clear rear
        if (this.front == null) {
            this.rear = null;
        }

        return result;
    }

    /**
     * Finds and removes all objects in {@code this} that match {@code key}.
     *
     * @param key the object to search for
     */
    public void removeMany(final T key) {
        // Remove from front as long as front matches
        while (this.front != null && this.front.getDatum().compareTo(key) == 0) {
            this.front = this.front.getNext();
            this.length--;
        }

        // If list is now empty, clear rear
        if (this.front == null) {
            this.rear = null;
            return;
        }

        // Remove from middle and end
        SingleNode<T> previous = this.front;
        SingleNode<T> current = this.front.getNext();

        while (current != null) {
            if (current.getDatum().compareTo(key) == 0) {
                // Remove current node
                previous.setNext(current.getNext());
                this.length--;

                // Update rear if we removed the last node
                if (previous.getNext() == null) {
                    this.rear = previous;
                }

                current = previous.getNext();
            } else {
                previous = current;
                current = current.getNext();
            }
        }
    }

    /**
     * Reverses the order of the objects in {@code this}.
     */
    public void reverse() {
        if (this.front == null || this.front.getNext() == null) {
            return; // Empty or single node, nothing to reverse
        }

        SingleNode<T> previous = null;
        SingleNode<T> current = this.front;
        SingleNode<T> next = null;

        // Save the old front before reversing
        SingleNode<T> oldFront = this.front;

        // Reverse the links
        while (current != null) {
            next = current.getNext();
            current.setNext(previous);
            previous = current;
            current = next;
        }

        // Swap front and rear
        this.front = previous; // previous is now the old rear
        this.rear = oldFront;  // old front is now the rear
    }

    /**
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call high-level methods.
     * {@code this} is empty when done.The first half of {@code this} is moved to
     * {@code left}, and the last half of {@code this} is moved to {@code right}. If
     * the resulting lengths are not the same, left should have one more object than
     * right. Order is preserved. {@code left} and {@code right} may already contain
     * data.
     *
     * @param left  the first {@code SingleList} to move nodes to
     * @param right the second {@code SingleList} to move nodes to
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {
        if (this.front == null) {
            return; // Nothing to split
        }

        // Calculate split point: if odd length, left gets one more
        int splitPoint = (this.length + 1) / 2;

        // Move first half to left
        for (int i = 0; i < splitPoint; i++) {
            this.moveFrontToRear(left);
        }

        // Move remaining to right
        while (this.front != null) {
            this.moveFrontToRear(right);
        }
    }

    /**
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call the high-level methods
     * {@code insert} or {@code remove}. {@code this} is empty when done. Nodes are
     * moved alternately from {@code this} to the rear of {@code left} and
     * {@code right}. {@code left} and {@code right} may already contain data.
     * <p>
     * This is the opposite of the combine method.
     *
     * @param left  the first {@code SingleList} to move nodes to
     * @param right the second {@code SingleList} to move nodes to
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {
        boolean toLeft = true;

        while (this.front != null) {
            if (toLeft) {
                this.moveFrontToRear(left);
            } else {
                this.moveFrontToRear(right);
            }
            toLeft = !toLeft;
        }
    }

    /**
     * Creates an union of {@code left} and {@code right} into {@code this}. Copies
     * data to {@code this}. {@code left} and {@code right} are unchanged. Values
     * from {@code left} are copied in order first, then objects from {@code right}
     * are copied in order.
     * <p>
     * In an union, data copied to {@code this} must appear in one or both of
     * {@code left} and {@code right}.
     *
     * @param left  the first {@code SingleList} to create an union from
     * @param right the second {@code SingleList} to create an union from
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {
        // Clear this list first
        this.front = null;
        this.rear = null;
        this.length = 0;

        // Copy all unique elements from left
        SingleNode<T> current = left.front;
        while (current != null) {
            T datum = current.getDatum();
            if (!this.contains(datum)) {
                this.append(datum);
            }
            current = current.getNext();
        }

        // Copy all unique elements from right
        current = right.front;
        while (current != null) {
            T datum = current.getDatum();
            if (!this.contains(datum)) {
                this.append(datum);
            }
            current = current.getNext();
        }
    }
}
