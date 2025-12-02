package cp213;

/**
 * A linked priority queue structure. Items are inserted in priority order
 * (highest priority first, based on compareTo() method).
 * Items with higher priority (lower compareTo value) are removed first.
 * 
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-11-09
 * @param <T> the type of data stored in the priority queue (must be Comparable)
 */
public class SinglePriorityQueue<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Default constructor.
     */
    public SinglePriorityQueue() {
        super();
    }

    /**
     * Inserts an item into the priority queue in the correct position.
     * Items are ordered by priority (lower compareTo value = higher priority).
     * 
     * @param datum the item to insert
     */
    public void insert(final T datum) {
        // If queue is empty, just add the node
        if (this.front == null) {
            SingleNode<T> newNode = new SingleNode<T>(datum, null);
            this.front = newNode;
            this.rear = newNode;
            this.length++;
            return;
        }
        
        // Find the correct position to insert
        // We want to insert before the first node with lower priority (higher compareTo value)
        SingleNode<T> current = this.front;
        SingleNode<T> previous = null;
        
        // Find where to insert: before first node where datum.compareTo(current) > 0
        // This means we insert before nodes with lower priority
        while (current != null && datum.compareTo(current.getDatum()) > 0) {
            previous = current;
            current = current.getNext();
        }
        
        // Create new node pointing to the node that will follow it
        SingleNode<T> newNode = new SingleNode<T>(datum, current);
        
        // Insert the new node
        if (previous == null) {
            // Insert at front (highest priority)
            this.front = newNode;
        } else {
            // Insert in middle or at end
            previous.setNext(newNode);
            
            // If we're inserting at the end, update rear
            if (current == null) {
                this.rear = newNode;
            }
        }
        
        this.length++;
    }

    /**
     * Removes and returns the item with the highest priority (front of queue).
     * 
     * @return the item with highest priority, or null if queue is empty
     */
    public T remove() {
        T result = null;
        
        if (this.front != null) {
            // Get the data from front node (highest priority)
            result = this.front.getDatum();
            
            // Move front to next node
            this.front = this.front.getNext();
            this.length--;
            
            // If queue is now empty, clear rear
            if (this.front == null) {
                this.rear = null;
            }
        }
        
        return result;
    }

    /**
     * Combines the contents of {@code left} and {@code right} into {@code this}.
     * Moves nodes only - does not refer to data in any way, or call the high-level
     * methods. {@code left} and {@code right} are empty when done. Nodes are moved
     * alternately from {@code left} and {@code right} into {@code this}.
     * {@code this} may be empty. May call any appropriate {@code SingleLink} helper
     * methods available.
     *
     * @param left  the first {@code SinglePriorityQueue} to extract nodes from
     * @param right the second {@code SinglePriorityQueue} to extract nodes from
     */
    public void combine(final SinglePriorityQueue<T> left, final SinglePriorityQueue<T> right) {
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
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call the high-level methods.
     * {@code this} is empty when done. Nodes with values less than or equal to
     * {@code key} are moved to {@code left}, and nodes with values greater than
     * {@code key} are moved to {@code right}. {@code left} and {@code right} may
     * already contain data.
     *
     * @param key   the key value to split on
     * @param left  the first {@code SinglePriorityQueue} to move nodes to
     * @param right the second {@code SinglePriorityQueue} to move nodes to
     */
    public void splitByKey(final T key, final SinglePriorityQueue<T> left, final SinglePriorityQueue<T> right) {
        while (this.front != null) {
            T datum = this.front.getDatum();
            
            // Compare with key to determine which queue to move to
            if (datum.compareTo(key) <= 0) {
                // Move from this to rear of left (less than or equal to key)
                left.moveFrontToRear(this);
            } else {
                // Move from this to rear of right (greater than key)
                right.moveFrontToRear(this);
            }
        }
    }
}

