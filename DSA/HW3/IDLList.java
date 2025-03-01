/**
 * Author: Hogan Lin
 * Date: February 28, 2025
 * Github: https://github.com/hogan-tech/SIT/tree/main/DSA
 * Description: 
 * This program implements an Indexed Doubly Linked List (IDLList) in Java. 
 * IDLList is an enhanced version of a standard doubly linked list that supports 
 * fast O(1) access to elements using an index maintained via an internal ArrayList. 
 */

package DSA.HW3;

import java.util.ArrayList;
import java.util.NoSuchElementException;

public class IDLList<E> {

    /**
     * Inner class representing a node in the doubly linked list.
     */
    private static class Node<E> {
        private E data;
        private Node<E> next;
        private Node<E> prev;
        // Constructor for a node with data only
        @SuppressWarnings("unused")
        Node(E elem) {
            this.data = elem;
            this.next = null;
            this.prev = null;
        }
        
        // Constructor for a node with data, previous, and next references
        Node(E elem, Node<E> prev, Node<E> next) {
            this.data = elem;
            this.prev = prev;
            this.next = next;
        }
    }

    // Reference to the head of the list
    private Node<E> head;

    // Reference to the tail of the list
    private Node<E> tail;

    // The current size of the list
    private int size;

    // ArrayList for fast index-based access to nodes
    private ArrayList<Node<E>> indices;

    /**
     * Constructor - Creates an empty Indexed Doubly Linked List
     */
    public IDLList() {
        size = 0;
        head = null;
        tail = null;
        indices = new ArrayList<>();
    }

    /**
     * Adds an element at the specified index.
     * 
     * @param index Position where the element should be inserted.
     * @param elem  Element to be inserted.
     * @return true if successfully added.
     */
    public boolean add(int index, E elem) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }

        if (index == 0) {
            return add(elem);
        } else if (index == size) {
            return append(elem);
        } else {
            // Retrieve next node at index position
            Node<E> nextNode = indices.get(index);
            Node<E> prevNode = nextNode.prev;
            Node<E> newNode = new Node<>(elem, prevNode, nextNode);
            prevNode.next = newNode;
            nextNode.prev = newNode;
            indices.add(index, newNode);
            size += 1;
            return true;
        }
    }

    /**
     * Adds an element at the head of the list.
     * 
     * @param elem Element to be inserted.
     * @return true if successfully added.
     */
    public boolean add(E elem) {
        if (elem == null) {
            throw new IllegalArgumentException();
        }

        Node<E> newNode = new Node<>(elem, null, head);

        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            head.prev = newNode;
            head = newNode;
        }

        indices.add(0, newNode);
        size += 1;
        return true;
    }

    /**
     * Adds an element at the tail of the list.
     * 
     * @param elem Element to be inserted.
     * @return true if successfully added.
     */
    public boolean append(E elem) {
        if (elem == null) {
            throw new IllegalArgumentException();
        }

        Node<E> newNode = new Node<>(elem, tail, null);

        if (tail == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }

        indices.add(newNode);
        size += 1;
        return true;
    }

    /**
     * Retrieves an element at a given index.
     * 
     * @param index Position of the element.
     * @return Element at the given index.
     */
    public E get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        return indices.get(index).data;
    }

    /**
     * Retrieves the head element.
     * 
     * @return Head element.
     */
    public E getHead() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        return head.data;
    }

    /**
     * Retrieves the last element.
     * 
     * @return Last element.
     */
    public E getLast() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        return tail.data;
    }

    /**
     * Returns the size of the list.
     * 
     * @return Number of elements in the list.
     */
    public int size() {
        return size;
    }

    /**
     * Removes and returns the head element.
     * 
     * @return Removed element.
     */
    public E remove() {
        if (size == 0) {
            throw new NoSuchElementException();
        }

        E data = head.data;

        if (size == 1) {
            head = null;
            tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }

        indices.remove(0);
        size -= 1;
        return data;
    }

    /**
     * Removes and returns the last element.
     * 
     * @return Removed element.
     */
    public E removeLast() {
        if (size == 0) {
            throw new NoSuchElementException();
        }

        E data = tail.data;

        if (size == 1) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }

        indices.remove(size - 1);
        size -= 1;
        return data;
    }

    /**
     * Removes and returns the element at a specified index.
     * 
     * @param index Position of the element to be removed.
     * @return Removed element.
     */
    public E removeAt(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }

        if (index == 0) {
            return remove();
        } else if (index == size - 1) {
            return removeLast();
        } else {
            Node<E> nodeToRemove = indices.get(index);
            Node<E> prevNode = nodeToRemove.prev;
            Node<E> nextNode = nodeToRemove.next;
            prevNode.next = nextNode;
            nextNode.prev = prevNode;
            indices.remove(index);
            size -= 1;
            return nodeToRemove.data;
        }
    }

    /**
     * Removes the first occurrence of an element.
     * 
     * @param elem Element to be removed.
     * @return true if the element was removed, false otherwise.
     */
    public boolean remove(E elem) {
        for (int i = 0; i < size; i++) {
            if (indices.get(i).data.equals(elem)) {
                removeAt(i);
                return true;
            }
        }
        return false;
    }

    /**
     * Returns a string representation of the list.
     * 
     * @return List contents as a string.
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        Node<E> current = head;
        while (current != null) {
            sb.append(current.data);
            if (current.next != null) {
                sb.append(" <-> ");
            }
            current = current.next;
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        IDLList<Integer> list = new IDLList<>();

        System.out.println("Adding elements...");
        list.add(10);
        list.add(20);
        list.append(30);
        list.add(1, 15);
        list.append(40);
        list.add(0, 5);

        System.out.println("List after insertions: " + list);
        System.out.println("Size: " + list.size());

        System.out.println("Head: " + list.getHead());
        System.out.println("Tail: " + list.getLast());
        System.out.println("Element at index 2: " + list.get(2));

        System.out.println("\nRemoving elements...");
        list.remove();
        list.removeLast();
        list.removeAt(1);

        System.out.println("List after removals: " + list);
        System.out.println("Size: " + list.size());

        System.out.println("\nRemoving a specific element (15): " + list.remove(Integer.valueOf(15)));
        System.out.println("Final list: " + list);

        // Testing edge cases
        try {
            list.get(10);
        } catch (Exception e) {
            System.out.println("Caught error: " + e.getMessage());
        }

        try {
            list.removeAt(10);
        } catch (Exception e) {
            System.out.println("Caught error: " + e.getMessage());
        }
    }
}
