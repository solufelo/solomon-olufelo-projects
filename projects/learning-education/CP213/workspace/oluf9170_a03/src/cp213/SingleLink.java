package cp213;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Abstract parent class for linked data structures (Stack, Queue, List).
 * Provides common functionality and helper methods for linked structures.
 * 
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-11-09
 * @param <T> the type of data stored in the linked structure
 */
public abstract class SingleLink<T> implements Iterable<T> {

    // Attributes
    /**
     * Pointer to the first node in the linked structure.
     */
    protected SingleNode<T> front = null;
    
    /**
     * Pointer to the last node in the linked structure.
     */
    protected SingleNode<T> rear = null;
    
    /**
     * Count of items in the linked structure.
     */
    protected int length = 0;

    /**
     * Default constructor.
     */
    public SingleLink() {
        // Initialize empty structure
        this.front = null;
        this.rear = null;
        this.length = 0;
    }

    /**
     * Appends the entire contents of source to the rear of this.
     * After appending, source becomes empty.
     * 
     * @param source the linked structure to append
     */
    protected void append(final SingleLink<T> source) {
        if (source.front != null) {
            // If this is empty, just take source's nodes
            if (this.front == null) {
                this.front = source.front;
            } else {
                // Connect source to the end of this
                this.rear.setNext(source.front);
            }
            
            // Update rear pointer and length
            this.rear = source.rear;
            this.length += source.length;
            
            // Empty source
            source.front = null;
            source.rear = null;
            source.length = 0;
        }
    }

    /**
     * Moves the front node from source to the front of this.
     * 
     * @param source the linked structure to move from
     */
    protected void moveFrontToFront(final SingleLink<T> source) {
        if (source.front != null) {
            // Save the node to move
            final SingleNode<T> node = source.front;
            
            // Remove from source
            source.length--;
            source.front = source.front.getNext();
            
            // If source is now empty, clear rear
            if (source.front == null) {
                source.rear = null;
            }
            
            // Add to front of this
            node.setNext(this.front);
            
            // If this was empty, node is also rear
            if (this.rear == null) {
                this.rear = node;
            }
            
            // Make node the new front
            this.front = node;
            this.length++;
        }
    }

    /**
     * Moves the front node from source to the rear of this.
     * 
     * @param source the linked structure to move from
     */
    protected void moveFrontToRear(final SingleLink<T> source) {
        if (source.front != null) {
            // Save the node to move
            final SingleNode<T> node = source.front;
            
            // Remove from source
            source.length--;
            source.front = source.front.getNext();
            
            // If source is now empty, clear rear
            if (source.front == null) {
                source.rear = null;
            }
            
            // This node becomes the new end
            node.setNext(null);
            
            // Add to rear of this
            if (this.rear == null) {
                // If this was empty, node is front
                this.front = node;
            } else {
                // Link current rear to node
                this.rear.setNext(node);
            }
            
            // Make node the new rear
            this.rear = node;
            this.length++;
        }
    }

    /**
     * Returns the number of items in the linked structure.
     * 
     * @return the number of items
     */
    public final int getLength() {
        return this.length;
    }

    /**
     * Returns whether the linked structure is empty.
     * 
     * @return true if empty, false otherwise
     */
    public final boolean isEmpty() {
        return this.front == null;
    }

    /**
     * Returns the data at the front of the linked structure without removing it.
     * 
     * @return the data at the front, or null if empty
     */
    public final T peek() {
        if (this.front != null) {
            return this.front.getDatum();
        }
        return null;
    }

    /**
     * Returns an iterator for the linked structure.
     * 
     * @return an iterator
     */
    @Override
    public final Iterator<T> iterator() {
        return new SingleLinkIterator();
    }

    /**
     * Returns a string representation of the linked structure.
     * 
     * @return a string in the format "front > A > B > C > null"
     */
    @Override
    public String toString() {
        String string = "front > ";
        SingleNode<T> curr = this.front;
        
        while (curr != null) {
            string += curr.getDatum() + " > ";
            curr = curr.getNext();
        }
        string += "null";
        return string;
    }

    /**
     * Iterator for SingleLink structures.
     * Allows iteration through the linked structure using enhanced for-loops.
     */
    private class SingleLinkIterator implements Iterator<T> {
        /**
         * Current node being examined.
         */
        private SingleNode<T> current = SingleLink.this.front;

        /**
         * Returns whether there is a next element.
         * 
         * @return true if there is a next element, false otherwise
         */
        @Override
        public boolean hasNext() {
            return this.current != null;
        }

        /**
         * Returns the next element and advances the iterator.
         * 
         * @return the next element
         * @throws NoSuchElementException if there is no next element
         */
        @Override
        public T next() {
            if (this.current == null) {
                throw new NoSuchElementException();
            }
            
            T result = this.current.getDatum();
            this.current = this.current.getNext();
            return result;
        }
    }
}

