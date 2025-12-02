package cp213;

import java.util.ArrayList;

/**
 * Implements a Binary Search Tree.
 *
 * @author Solomon Olufelo
 * @author David Brown
 * @version 2025-11-24
 * @param <T> the data structure data type
 */
public class BST<T extends Comparable<T>> {

    // Attributes.
    /**
     * Count of comparisons performed by tree.
     */
    protected int comparisons = 0;
    /**
     * Root node of the tree.
     */
    protected TreeNode<T> root = null;
    /**
     * Number of nodes in the tree.
     */
    protected int size = 0;

    /**
     * Auxiliary method for {@code equals}. Determines whether two subtrees are
     * identical in node data and height.
     *
     * @param source Node of this BST.
     * @param target Node of that BST.
     * @return true if source and target are identical in node data and height.
     */
    protected boolean equalsAux(final TreeNode<T> source, final TreeNode<T> target) {
	if (source == null && target == null) {
	    return true;
	}
	if (source == null || target == null) {
	    return false;
	}
	return source.getCountedItem().compareTo(target.getCountedItem()) == 0
		&& source.getCountedItem().getCount() == target.getCountedItem().getCount()
		&& source.getHeight() == target.getHeight() && equalsAux(source.getLeft(), target.getLeft())
		&& equalsAux(source.getRight(), target.getRight());
    }

    /**
     * Auxiliary method for insert. Inserts data into this BST.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data to be inserted into the tree.
     * @return The inserted node.
     */
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> countedItem) {

	if (node == null) {
	    // Base case - add a new node containing the data.
	    node = new TreeNode<T>(countedItem);
	    node.getCountedItem().incrementCount();
	    this.size++;
	} else {
	    // Compare the node data against the insert data.
	    final int result = node.getCountedItem().compareTo(countedItem);

	    if (result > 0) {
		// General case - check the left subtree.
		node.setLeft(this.insertAux(node.getLeft(), countedItem));
	    } else if (result < 0) {
		// General case - check the right subtree.
		node.setRight(this.insertAux(node.getRight(), countedItem));
	    } else {
		// Base case - data is already in the tree, increment its count
		node.getCountedItem().incrementCount();
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree.
     *
     * @param node    The root of the subtree to test for validity.
     * @param minNode The node of the minimum data in the current subtree.
     * @param maxNode The node of the maximum data in the current subtree.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
	if (node == null) {
	    return true;
	}
	if (minNode != null && node.getCountedItem().compareTo(minNode.getCountedItem()) <= 0) {
	    return false;
	}
	if (maxNode != null && node.getCountedItem().compareTo(maxNode.getCountedItem()) >= 0) {
	    return false;
	}
	int leftHeight = nodeHeight(node.getLeft());
	int rightHeight = nodeHeight(node.getRight());

	if (node.getHeight() != Math.max(leftHeight, rightHeight) + 1) {
	    return false;
	}
	return isValidAux(node.getLeft(), minNode, node) && isValidAux(node.getRight(), node, maxNode);
    }

    /**
     * Returns the height of a given TreeNode. Required for when TreeNode is null.
     *
     * @param node The TreeNode to determine the height of.
     * @return The height attribute of node, 0 if node is null.
     */
    protected int nodeHeight(final TreeNode<T> node) {
	return node != null ? node.getHeight() : 0;
    }

    /**
     * Auxiliary method for remove. Removes data from this BST.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data to be removed from the tree.
     * @return The replacement node.
     */
    protected TreeNode<T> removeAux(TreeNode<T> node, final CountedItem<T> countedItem) {
	if (node == null) {
	    return null;
	}
	int result = node.getCountedItem().compareTo(countedItem);
	if (result > 0) {
	    node.setLeft(removeAux(node.getLeft(), countedItem));
	    node.updateHeight();
	} else if (result < 0) {
	    node.setRight(removeAux(node.getRight(), countedItem));
	    node.updateHeight();
	} else {
	    if (node.getCountedItem().getCount() > 1) {
		node.getCountedItem().decrementCount();
	    } else {
		this.size--;
		if (node.getLeft() == null) {
		    return node.getRight();
		} else if (node.getRight() == null) {
		    return node.getLeft();
		} else {
		    TreeNode<T> leftMax = node.getLeft();
		    while (leftMax.getRight() != null) {
			leftMax = leftMax.getRight();
		    }
		    TreeNode<T> newLeft = removeMax(node.getLeft());
		    leftMax.setLeft(newLeft);
		    leftMax.setRight(node.getRight());
		    leftMax.updateHeight();
		    return leftMax;
		}
	    }
	}
	return node;
    }

    /**
     * Helper method to remove the node with the maximum value from a subtree.
     *
     * @param node The root of the subtree.
     * @return The root of the modified subtree.
     */
    private TreeNode<T> removeMax(TreeNode<T> node) {
	if (node.getRight() == null) {
	    return node.getLeft();
	}
	node.setRight(removeMax(node.getRight()));
	node.updateHeight();
	return node;
    }

    /**
     * Determines if this BST contains key.
     *
     * @param key The key to search for.
     * @return true if this contains key, false otherwise.
     */
    public boolean contains(final CountedItem<T> key) {
	TreeNode<T> curr = this.root;
	while (curr != null) {
	    int cmp = curr.getCountedItem().compareTo(key);
	    if (cmp == 0) {
		return true;
	    } else if (cmp > 0) {
		curr = curr.getLeft();
	    } else {
		curr = curr.getRight();
	    }
	}
	return false;
    }

    /**
     * Determines whether two trees are identical.
     *
     * @param target The tree to compare this BST against.
     * @return true if this and target contain nodes that match in position, data,
     *         count, and height, false otherwise.
     */
    public boolean equals(final BST<T> target) {
	boolean isEqual = false;

	if (this.size == target.size) {
	    isEqual = this.equalsAux(this.root, target.root);
	}
	return isEqual;
    }

    /**
     * Get number of comparisons executed by the retrieve method.
     *
     * @return comparisons
     */
    public int getComparisons() {
	return this.comparisons;
    }

    /**
     * Returns the height of the root node of this tree.
     *
     * @return height of root node, 0 if the root node is null.
     */
    public int getHeight() {
	return this.root != null ? this.root.getHeight() : 0;
    }

    /**
     * Returns the number of nodes in the tree.
     *
     * @return number of nodes in this tree.
     */
    public int getSize() {
	return this.size;
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in
     * order from smallest to largest.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return The contents of this tree as a list of data.
     */
    public ArrayList<CountedItem<T>> inOrder() {
	return this.root.inOrder();
    }

    /**
     * Inserts data into this tree.
     *
     * @param countedItem Data to store.
     */
    public void insert(final CountedItem<T> countedItem) {
	this.root = this.insertAux(this.root, countedItem);
	return;
    }

    /**
     * Determines if this tree is empty.
     *
     * @return true if this tree is empty, false otherwise.
     */
    public boolean isEmpty() {
	return this.root == null;
    }

    /**
     * Determines if this tree is a valid BST; i.e. a node's left child data is
     * smaller than its data, and its right child data is greater than its data, and
     * a node's height is equal to the maximum of the heights of its two children
     * (empty child nodes have a height of 0), plus 1.
     *
     * @return true if this tree is a valid BST, false otherwise.
     */
    public boolean isValid() {
	return this.isValidAux(this.root, null, null);
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in node
     * level order starting from the root node. Helps determine the structure of the
     * tree.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return this tree data as a list of data.
     */
    public ArrayList<CountedItem<T>> levelOrder() {
	return this.root.levelOrder();
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in node
     * preorder.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return The contents of this tree as a list of data.
     */
    public ArrayList<CountedItem<T>> preOrder() {
	return this.root.preOrder();
    }

    /**
     * Removes data from the tree. Decrements the node count, and if the count is 0,
     * removes the node entirely.
     *
     * @param countedItem Data to decrement or remove.
     */
    public void remove(final CountedItem<T> countedItem) {
	this.root = this.removeAux(this.root, countedItem);
	return;
    }

    /**
     * Resets the comparison count to 0.
     */
    public void resetComparisons() {
	this.comparisons = 0;
	return;
    }

    /**
     * Retrieves a copy of data matching key (key should have data count of 0).
     * Returning a complete CountedItem gives access to the data and its count.
     *
     * @param key The key to look for.
     * @return The complete CountedItem that matches key, null otherwise.
     */
    public CountedItem<T> retrieve(final CountedItem<T> key) {
	TreeNode<T> curr = this.root;
	while (curr != null) {
	    this.comparisons++;
	    int cmp = curr.getCountedItem().compareTo(key);
	    if (cmp == 0) {
		return curr.getCountedItem();
	    } else if (cmp > 0) {
		curr = curr.getLeft();
	    } else {
		curr = curr.getRight();
	    }
	}
	return null;
    }
}
