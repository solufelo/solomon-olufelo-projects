package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author Solomon Olufelo
 * @author David Brown
 * @version 2025-11-24
 * @param <T> the data structure data type
 */
public class PopularityTree<T extends Comparable<T>> extends BST<T> {

    /**
     * Used to store the item found during retrieval.
     */
    private CountedItem<T> found = null;

    /**
     * Auxiliary method for valid. May force node rotation if the retrieval count of
     * the located node data is incremented.
     *
     * @param node The node to examine for key.
     * @param key  The data to search for. Count is updated to count in matching
     *             node data if key is found.
     * @return The updated node.
     */
    private TreeNode<T> retrieveAux(TreeNode<T> node, final CountedItem<T> key) {
	if (node == null) {
	    return null;
	}
	this.comparisons++;
	int result = node.getCountedItem().compareTo(key);
	if (result > 0) {
	    node.setLeft(retrieveAux(node.getLeft(), key));
	    if (node.getLeft() != null && node.getLeft().getCountedItem().getCount() > node.getCountedItem().getCount()) {
		node = rotateRight(node);
	    }
	} else if (result < 0) {
	    node.setRight(retrieveAux(node.getRight(), key));
	    if (node.getRight() != null && node.getRight().getCountedItem().getCount() > node.getCountedItem().getCount()) {
		node = rotateLeft(node);
	    }
	} else {
	    node.getCountedItem().incrementCount();
	    this.found = node.getCountedItem();
	}
	node.updateHeight();
	return node;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param parent The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> parent) {
	TreeNode<T> right = parent.getRight();
	parent.setRight(right.getLeft());
	right.setLeft(parent);
	parent.updateHeight();
	right.updateHeight();
	return right;
    }

    /**
     * Performs a right rotation around {@code node}.
     *
     * @param parent The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> parent) {
	TreeNode<T> left = parent.getLeft();
	parent.setLeft(left.getRight());
	left.setRight(parent);
	parent.updateHeight();
	left.updateHeight();
	return left;
    }

    /**
     * Replaces BST insertAux - does not increment count on repeated insertion.
     * Counts are incremented only on retrieve.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> countedItem) {
	if (node == null) {
	    node = new TreeNode<T>(countedItem);
	    this.size++;
	} else {
	    final int result = node.getCountedItem().compareTo(countedItem);
	    if (result > 0) {
		node.setLeft(insertAux(node.getLeft(), countedItem));
	    } else if (result < 0) {
		node.setRight(insertAux(node.getRight(), countedItem));
	    } else {
		// Do nothing (no count increment)
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree. An Popularity Tree must meet the BST validation conditions, and
     * additionally the counts of any node data must be greater than or equal to the
     * counts of its children.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
	if (node == null) {
	    return true;
	}
	if (!super.isValidAux(node, minNode, maxNode)) {
	    return false;
	}
	if (node.getLeft() != null && node.getLeft().getCountedItem().getCount() > node.getCountedItem().getCount()) {
	    return false;
	}
	if (node.getRight() != null && node.getRight().getCountedItem().getCount() > node.getCountedItem().getCount()) {
	    return false;
	}
	return true;
    }

    /**
     * Determines whether two PopularityTrees are identical.
     *
     * @param target The PopularityTree to compare this PopularityTree against.
     * @return true if this PopularityTree and target contain nodes that match in
     *         position, data, count, and height, false otherwise.
     */
    public boolean equals(final PopularityTree<T> target) {
	return super.equals(target);
    }

    /**
     * Very similar to the BST retrieve, but increments the data count here instead
     * of in the insertion.
     *
     * @param key The key to search for.
     */
    @Override
    public CountedItem<T> retrieve(CountedItem<T> key) {
	this.found = null;
	this.root = retrieveAux(this.root, key);
	return this.found;
    }

}
