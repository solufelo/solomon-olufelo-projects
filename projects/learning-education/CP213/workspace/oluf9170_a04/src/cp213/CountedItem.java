package cp213;

/**
 * Stores a item and an occurrence count for that item. The item must be
 * Comparable so that it can be compared and sorted against other datas of the
 * same type.
 *
 * @author David Brown
 * @version 2025-09-07
 *
 * @param <T> data type to store
 */
public class CountedItem<T extends Comparable<T>> implements Comparable<CountedItem<T>> {

    // Attributes.
    private int count = 0; // item count
    private T item = null; // item

    /**
     * Copy constructor.
     *
     * @param source Another CountedItem object.
     */
    public CountedItem(final CountedItem<T> source) {
	this.item = source.item;
	this.count = source.count;
    }

    /**
     * Constructor for key version of object. (item count defaults to 0)
     *
     * @param item The object to be counted.
     */
    public CountedItem(final T item) {
	this.item = item;
    }

    /**
     * Constructor.
     *
     * @param item  The object to be counted.
     * @param count The object count.
     */
    public CountedItem(final T item, final int count) {
	this.item = item;
	this.count = count;
    }

    /**
     * Comparison method for objects. Compares only the stored objects, counts are
     * ignored. Returns:
     * <ul>
     * <li>0 if this equals target</li>
     * <li>&lt; 0 if this precedes target</li>
     * <li>&gt; 0 if this follows target</li>
     * </ul>
     *
     * @param target CountedItem object to compare against.
     * @return Comparison result.
     */
    @Override
    public int compareTo(CountedItem<T> target) {
	return this.item.compareTo(target.item);
    }

    /**
     * Decrements the item count.
     */
    public void decrementCount() {
	this.count--;
    }

    /**
     * Returns this item count.
     *
     * @return this item count.
     */
    public int getCount() {
	return this.count;
    }

    /**
     * Returns this item.
     *
     * @return this item.
     */
    public T getItem() {
	return this.item;
    }

    /**
     * Returns a copy of the current object.
     *
     * @return the current object
     */
    public CountedItem<T> copy() {
	return new CountedItem<T>(this.item, this.count);
    }

    /**
     * Increments the item count.
     */
    public void incrementCount() {
	this.count++;
    }

    /**
     * Sets the item count.
     *
     * @param count the new item count.
     */
    public void setCount(final int count) {
	this.count = count;
	return;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString()
     */
    @Override
    public String toString() {
	return String.format("{%s: %d}", this.item.toString(), this.count);
    }

}
