package cp213;

/**
 * Implements an AVL (Adelson-Velsky Landis) tree. Extends BST.
 *
 * @author Solomon Olufelo
 * @author David Brown
 * @version 2025-11-24
 * @param <T> the data structure data type
 */
public class AVL<T extends Comparable<T>> extends BST<T> {

    /**
     * Returns the balance data of node. If greater than 1, then left heavy, if less
     * than -1, then right heavy. If in the range -1 to 1 inclusive, the node is
     * balanced. Used to determine whether to rotate a node upon insertion.
     *
     * @param node The TreeNode to analyze for balance.
     * @return A balance number.
     */
    private int balance(final TreeNode<T> node) {
	return nodeHeight(node.getLeft()) - nodeHeight(node.getRight());
    }

    /**
     * Rebalances the current node if its children are not balanced.
     *
     * @param node the node to rebalance
     * @return replacement for the rebalanced node
     */
    private TreeNode<T> rebalance(TreeNode<T> node) {
	int balance = balance(node);
	if (balance > 1) {
	    if (balance(node.getLeft()) < 0) {
		node.setLeft(rotateLeft(node.getLeft()));
	    }
	    return rotateRight(node);
	} else if (balance < -1) {
	    if (balance(node.getRight()) > 0) {
		node.setRight(rotateRight(node.getRight()));
	    }
	    return rotateLeft(node);
	}
	return node;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> node) {
	TreeNode<T> right = node.getRight();
	node.setRight(right.getLeft());
	right.setLeft(node);
	node.updateHeight();
	right.updateHeight();
	return right;
    }

    /**
     * Performs a right rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> node) {
	TreeNode<T> left = node.getLeft();
	node.setLeft(left.getRight());
	left.setRight(node);
	node.updateHeight();
	left.updateHeight();
	return left;
    }

    /**
     * Auxiliary method for insert. Inserts data into this AVL. Same as BST
     * insertion with addition of rebalance of nodes.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data to be inserted into the node.
     * @return The inserted node.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> countedItem) {
	if (node == null) {
	    node = new TreeNode<T>(countedItem);
	    node.getCountedItem().incrementCount();
	    this.size++;
	} else {
	    final int result = node.getCountedItem().compareTo(countedItem);
	    if (result > 0) {
		node.setLeft(insertAux(node.getLeft(), countedItem));
	    } else if (result < 0) {
		node.setRight(insertAux(node.getRight(), countedItem));
	    } else {
		node.getCountedItem().incrementCount();
	    }
	}
	node.updateHeight();
	return rebalance(node);
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree. An AVL must meet the BST validation conditions, and additionally be
     * balanced in all its subtrees - i.e. the difference in height between any two
     * children must be no greater than 1.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
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
	int lh = nodeHeight(node.getLeft());
	int rh = nodeHeight(node.getRight());
	if (node.getHeight() != Math.max(lh, rh) + 1) {
	    return false;
	}
	if (Math.abs(lh - rh) > 1) {
	    return false;
	}
	return isValidAux(node.getLeft(), minNode, node) && isValidAux(node.getRight(), node, maxNode);
    }

    /**
     * Determines whether two AVLs are identical.
     *
     * @param target The AVL to compare this AVL against.
     * @return true if this AVL and target contain nodes that match in position,
     *         data, count, and height, false otherwise.
     */
    public boolean equals(final AVL<T> target) {
	return super.equals(target);
    }

    /**
     * Auxiliary method for remove. Removes data from this BST. Same as BST removal
     * with addition of rebalance of nodes.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data removed from the tree.
     * @return The replacement node.
     */
    @Override
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
		node.updateHeight();
		return rebalance(node);
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
		    return rebalance(leftMax);
		}
	    }
	}
	return rebalance(node);
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
	return rebalance(node);
    }

}
