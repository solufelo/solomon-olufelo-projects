package cp213;

/**
 * A linked stack structure. Items are added and removed from the front.
 * Implements a Last-In-First-Out (LIFO) data structure.
 * 
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-11-09
 * @param <T> the type of data stored in the stack
 */
public class SingleStack<T> extends SingleLink<T> {

    /**
     * Default constructor.
     */
    public SingleStack() {
        super();
    }

    /**
     * Adds an item to the top of the stack (front).
     * 
     * @param datum the item to add
     */
    public void push(final T datum) {
        // Create new node pointing to current front
        SingleNode<T> newNode = new SingleNode<T>(datum, this.front);
        
        // If stack was empty, new node is also rear
        if (this.rear == null) {
            this.rear = newNode;
        }
        
        // Update front and length
        this.front = newNode;
        this.length++;
    }

    /**
     * Removes and returns the item from the top of the stack (front).
     * 
     * @return the item removed from the top, or null if stack is empty
     */
    public T pop() {
        T result = null;
        
        if (this.front != null) {
            // Get the data from front node
            result = this.front.getDatum();
            
            // Move front to next node
            this.front = this.front.getNext();
            this.length--;
            
            // If stack is now empty, clear rear
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
     * @param left  the first {@code SingleStack} to extract nodes from
     * @param right the second {@code SingleStack} to extract nodes from
     */
    public void combine(final SingleStack<T> left, final SingleStack<T> right) {
        // Alternate between left and right until both are empty
        while (left.front != null || right.front != null) {
            // Move from left if available
            if (left.front != null) {
                this.moveFrontToFront(left);
            }
            // Move from right if available
            if (right.front != null) {
                this.moveFrontToFront(right);
            }
        }
    }

    /**
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call the high-level methods.
     * {@code this} is empty when done. Nodes are moved alternately from
     * {@code this} to the front of {@code left} and {@code right}.
     * {@code left} and {@code right} may already contain data.
     * <p>
     * This is the opposite of the combine method.
     *
     * @param left  the first {@code SingleStack} to move nodes to
     * @param right the second {@code SingleStack} to move nodes to
     */
    public void splitAlternate(final SingleStack<T> left, final SingleStack<T> right) {
        boolean toLeft = true;

        while (this.front != null) {
            if (toLeft) {
                // Move from this to front of left
                left.moveFrontToFront(this);
            } else {
                // Move from this to front of right
                right.moveFrontToFront(this);
            }
            toLeft = !toLeft;
        }
    }
}

