package cp213;

/**
 * A linked queue structure. Items are added to the rear and removed from the front.
 * Implements a First-In-First-Out (FIFO) data structure.
 * 
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-11-09
 * @param <T> the type of data stored in the queue
 */
public class SingleQueue<T> extends SingleLink<T> {

    /**
     * Default constructor.
     */
    public SingleQueue() {
        super();
    }

    /**
     * Adds an item to the rear of the queue.
     * 
     * @param datum the item to add
     */
    public void enqueue(final T datum) {
        // Create new node with the datum (next is null since it's at the end)
        SingleNode<T> newNode = new SingleNode<T>(datum, null);
        
        // If queue is empty, new node is front
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
     * Adds an item to the rear of the queue (alias for enqueue).
     * 
     * @param datum the item to add
     */
    public void insert(final T datum) {
        this.enqueue(datum);
    }

    /**
     * Removes and returns the item from the front of the queue.
     * 
     * @return the item removed from the front, or null if queue is empty
     */
    public T dequeue() {
        T result = null;
        
        if (this.front != null) {
            // Get the data from front node
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
     * Removes and returns the item from the front of the queue (alias for dequeue).
     * 
     * @return the item removed from the front, or null if queue is empty
     */
    public T remove() {
        return this.dequeue();
    }

    /**
     * Combines the contents of {@code left} and {@code right} into {@code this}.
     * Moves nodes only - does not refer to data in any way, or call the high-level
     * methods. {@code left} and {@code right} are empty when done. Nodes are moved
     * alternately from {@code left} and {@code right} into {@code this}.
     * {@code this} may be empty. May call any appropriate {@code SingleLink} helper
     * methods available.
     *
     * @param left  the first {@code SingleQueue} to extract nodes from
     * @param right the second {@code SingleQueue} to extract nodes from
     */
    public void combine(final SingleQueue<T> left, final SingleQueue<T> right) {
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
     * {@code this} is empty when done. Nodes are moved alternately from
     * {@code this} to the rear of {@code left} and {@code right}.
     * {@code left} and {@code right} may already contain data.
     * <p>
     * This is the opposite of the combine method.
     *
     * @param left  the first {@code SingleQueue} to move nodes to
     * @param right the second {@code SingleQueue} to move nodes to
     */
    public void splitAlternate(final SingleQueue<T> left, final SingleQueue<T> right) {
        boolean toLeft = true;

        while (this.front != null) {
            if (toLeft) {
                // Move from this to rear of left
                left.moveFrontToRear(this);
            } else {
                // Move from this to rear of right
                right.moveFrontToRear(this);
            }
            toLeft = !toLeft;
        }
    }
}

