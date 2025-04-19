
/**
 * Author: Hogan Lin
 * Date: Apr 9th 2025
 * Github: https://github.com/hogan-tech/SIT
 * Description: This class implements a Treap, a randomized binary search tree with heap properties.
 */

import java.util.Random;
import java.util.Stack;

/**
 * Treap class implementing a randomized binary search tree (BST) with heap
 * properties.
 * 
 * @param <E> the type of elements maintained by this treap, must be comparable
 */
public class Treap<E extends Comparable<E>> {

    /**
     * Node class representing each node in the Treap.
     * 
     * @param <E> the type of data stored, must be comparable
     */
    private static class Node<E> {
        public E data;
        public int priority;
        public Node<E> left;
        public Node<E> right;

        /**
         * Constructs a node with specified data and priority.
         *
         * @param data     the key for BST ordering
         * @param priority the priority for heap ordering
         * @throws NullPointerException if data is null
         */
        public Node(E data, int priority) {
            if (data == null)
                throw new NullPointerException("Data cannot be null");
            this.data = data;
            this.priority = priority;
            this.left = null;
            this.right = null;
        }

        /**
         * Performs a right rotation around this node.
         *
         * @return the new root after rotation
         */
        public Node<E> rotateRight() {
            Node<E> newRoot = this.left;
            this.left = newRoot.right;
            newRoot.right = this;
            return newRoot;
        }

        /**
         * Performs a left rotation around this node.
         *
         * @return the new root after rotation
         */
        public Node<E> rotateLeft() {
            Node<E> newRoot = this.right;
            this.right = newRoot.left;
            newRoot.left = this;
            return newRoot;
        }

        /**
         * Returns a string representation of the node.
         *
         * @return string representation in format (key=x, priority=y)
         */
        public String toString() {
            return "(key=" + data + ", priority=" + priority + ")";
        }
    }

    private Random priorityGenerator;
    private Node<E> root;

    /**
     * Constructs an empty Treap with a random seed.
     * http://docs.oracle.com/javase/8/docs/api/java/util/Random.html
     * 
     */
    public Treap() {
        this.priorityGenerator = new Random();
        this.root = null;
    }

    /**
     * Constructs an empty Treap with a fixed seed for reproducibility.
     *
     * @param seed seed for the random number generator
     */
    public Treap(long seed) {
        this.priorityGenerator = new Random(seed);
        this.root = null;
    }

    /**
     * Adds a key with a randomly generated priority.
     *
     * @param key the key to insert
     * @return true if added successfully, false if key already exists
     */
    public boolean add(E key) {
        int priority = priorityGenerator.nextInt();
        return add(key, priority);
    }

    /**
     * Adds a key with a specified priority, Overide.
     *
     * @param key      the key to insert
     * @param priority the priority for heap ordering
     * @return true if added successfully, false if key already exists
     */
    public boolean add(E key, int priority) {
        Node<E> newNode = new Node<>(key, priority);
        if (root == null) {
            root = newNode;
            return true;
        }

        Stack<Node<E>> path = new Stack<>();
        Node<E> current = root;
        while (true) {
            path.push(current);
            int cmp = key.compareTo(current.data);
            if (cmp == 0)
                return false;
            else if (cmp < 0) {
                if (current.left == null) {
                    current.left = newNode;
                    break;
                }
                current = current.left;
            } else {
                if (current.right == null) {
                    current.right = newNode;
                    break;
                }
                current = current.right;
            }
        }
        reheap(path, newNode);
        return true;
    }

    /**
     * Bubbles up the inserted node to maintain the heap invariant.
     *
     * @param path the path from root to inserted node
     * @param node the newly inserted node
     */
    private void reheap(Stack<Node<E>> path, Node<E> node) {
        while (!path.isEmpty()) {
            Node<E> parent = path.pop();
            if (node.priority > parent.priority) {
                if (node == parent.left) {
                    node = parent.rotateRight();
                } else {
                    node = parent.rotateLeft();
                }
                if (path.isEmpty()) {
                    root = node;
                } else {
                    Node<E> grandparent = path.peek();
                    if (grandparent.left == parent)
                        grandparent.left = node;
                    else
                        grandparent.right = node;
                }
            } else {
                break;
            }
        }
    }

    /**
     * Deletes the node with the specified key from the Treap.
     *
     * @param key the key to delete
     * @return true if deleted, false if not found
     */
    public boolean delete(E key) {
        root = delete(root, key);
        return deletionResult;
    }

    private boolean deletionResult = false;

    /**
     * Recursively deletes a node and maintains heap invariant.
     *
     * @param root subtree root
     * @param key  key to be deleted
     * @return updated subtree root
     */
    private Node<E> delete(Node<E> root, E key) {
        if (root == null)
            return null;
        int cmp = key.compareTo(root.data);
        if (cmp < 0) {
            root.left = delete(root.left, key);
        } else if (cmp > 0) {
            root.right = delete(root.right, key);
        } else {
            deletionResult = true;
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;
            else {
                if (root.left.priority > root.right.priority) {
                    root = root.rotateRight();
                    root.right = delete(root.right, key);
                } else {
                    root = root.rotateLeft();
                    root.left = delete(root.left, key);
                }
            }
        }
        return root;
    }

    /**
     * Recursively finds if a key exists in a subtree.
     *
     * @param root subtree root
     * @param key  key to find
     * @return true if found, false otherwise
     */
    private boolean find(Node<E> root, E key) {
        if (root == null)
            return false;
        int cmp = key.compareTo(root.data);
        if (cmp == 0)
            return true;
        else if (cmp < 0)
            return find(root.left, key);
        else
            return find(root.right, key);
    }

    /**
     * Finds if a key exists in the Treap.
     *
     * @param key the key to search for
     * @return true if found, false otherwise
     */
    public boolean find(E key) {
        return find(root, key);
    }

    /**
     * Returns a string representation of the Treap (preorder traversal).
     *
     * @return string representation of the Treap
     */
    public String toString() {
        return toString(root);
    }

    /**
     * Returns a string representation of the Treap using preorder traversal.
     * Indents each node according to its depth.
     *
     * @return formatted string representation of the tree
     */
    private String toString(Node<E> node) {
        StringBuilder sb = new StringBuilder();
        preOrderString(root, sb, 0);
        return sb.toString();
    }

    /**
     * Helper method to build a string of the Treap using preorder traversal.
     * Adds indentation based on depth to visualize tree structure.
     *
     * @param node  the current node being processed
     * @param sb    the StringBuilder accumulating the tree representation
     * @param depth the depth of the current node to determine indentation
     */

    private void preOrderString(Node<E> node, StringBuilder sb, int depth) {
        if (node == null) {
            sb.append(" ".repeat(depth)).append("null\n");
            return;
        }
        sb.append(" ".repeat(depth)).append(node.toString()).append("\n");
        preOrderString(node.left, sb, depth + 1);
        preOrderString(node.right, sb, depth + 1);
    }

    /**
     * Main method for testing Treap implementation.
     *
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        Treap<Integer> testTree = new Treap<>();
        testTree.add(4, 19);
        testTree.add(2, 31);
        testTree.add(6, 70);
        testTree.add(1, 84);
        testTree.add(3, 12);
        testTree.add(5, 83);
        testTree.add(7, 26);

        System.out.println(testTree);
        System.out.println("Delete 6: " + testTree.delete(6));
        System.out.println(testTree);
        System.out.println("Find 3: " + testTree.find(3));
    }
}
