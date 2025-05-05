
/**
 * @author: Hogan Lin
 * @class: CS501 - Intro to Java
 * @description: Solutions for Assignment 5: Includes implementations and
 * comprehensive test cases for set operations, map manipulations, queue/stack
 * algorithms, and binary search tree (BST) problems.
 * @date: April 26, 2025
 */
import java.util.*;
import java.util.function.Predicate;

public class Assignment5 {

    /**
     * Problem 1: Finds elements common to both sets within a given tolerance.
     * For numbers within ±tolerance of each other, considers them "equal".
     *
     * @param set1 First set of doubles
     * @param set2 Second set of doubles
     * @param tolerance Allowed difference between numbers
     * @return Set of common elements within tolerance
     */
    public Set<Double> fuzzyIntersection(Set<Double> set1, Set<Double> set2, double tolerance) {
        Set<Double> result = new HashSet<>();

        for (Double num1 : set1) {
            for (Double num2 : set2) {
                // Check if within tolerance
                if (Math.abs(num1 - num2) <= tolerance) {
                    // Add to result if condition met
                    result.add(num1);
                    break;
                }
            }
        }
        return result;
    }

    /**
     * Problem 2: Partitions a set into two based on a predicate. Results should
     * be in a map with keys "true" and "false".
     *
     * @param originalSet The original set to partition
     * @param predicate The condition for partitioning
     * @return Map of partitioned sets based on predicate
     */
    public <T> Map<Boolean, Set<T>> partitionSet(Set<T> originalSet, Predicate<T> predicate) {
        Map<Boolean, Set<T>> result = new HashMap<>();
        result.put(true, new HashSet<>());
        result.put(false, new HashSet<>());

        for (T element : originalSet) {
            // Evaluate predicate and add element to the corresponding set
            result.get(predicate.test(element)).add(element);
        }

        return result;  // Return partitioned map
    }

    /**
     * Problem 3: Swap keys and values in a map. If duplicate values exist,
     * combine their keys into a set.
     *
     * @param map The input map to invert
     * @return Inverted map with values as keys and keys as sets
     */
    public <K, V> Map<V, Set<K>> invertMapWithSetValues(Map<K, V> map) {
        Map<V, Set<K>> result = new HashMap<>();

        for (Map.Entry<K, V> entry : map.entrySet()) {
            // For each value, get its corresponding set of keys, create if absent, and add the key
            result.computeIfAbsent(entry.getValue(), k -> new HashSet<>()).add(entry.getKey());
        }

        return result;
    }

    /**
     * Problem 4: Count word frequencies in a list. Case-insensitive.
     *
     * @param words List of words
     * @return Map of word frequencies
     */
    public Map<String, Integer> countWordFrequencies(List<String> words) {
        Map<String, Integer> result = new HashMap<>();

        for (String word : words) {
            String lower = word.toLowerCase();
            // Increment count for the word
            result.put(lower, result.getOrDefault(lower, 0) + 1);
        }

        return result;
    }

    /**
     * Problem 5: Reverse a queue using a stack.
     *
     * @param queue The queue to reverse
     */
    public <T> void reverseQueue(Queue<T> queue) {
        Stack<T> stack = new Stack<>();

        // Dequeue elements from the queue and push them onto the stack
        while (!queue.isEmpty()) {
            stack.push(queue.poll());
        }

        // Pop elements from the stack and enqueue them back into the queue
        while (!stack.isEmpty()) {
            queue.offer(stack.pop());
        }
    }

    /**
     * Problem 6: Find the first non-repeating character in a stream using a
     * queue.
     *
     * @param stream The input string stream
     * @return First non-repeating character or '#' if none
     */
    public char firstNonRepeatingChar(String stream) {
        Map<Character, Integer> count = new HashMap<>();
        Queue<Character> queue = new LinkedList<>();

        for (char c : stream.toCharArray()) {
            // Update character count
            count.put(c, count.getOrDefault(c, 0) + 1);
            // Add character to the queue
            queue.offer(c);

            // Remove characters from the front of the queue if they are repeating
            while (!queue.isEmpty() && count.get(queue.peek()) > 1) {
                queue.poll();
            }
        }

        return queue.isEmpty() ? '#' : queue.peek();
    }

    /**
     * Problem 7: Merge k sorted lists into one sorted list using a priority
     * queue (min-heap).
     *
     * @param lists List of sorted integer lists
     * @return Merged sorted list
     */
    public List<Integer> mergeKSortedLists(List<List<Integer>> lists) {
        List<Integer> result = new ArrayList<>();
        // Min-heap: [value, list index, element index]
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for (int i = 0; i < lists.size(); i++) {
            if (!lists.get(i).isEmpty()) {
                // Add [value, list index, element index]
                pq.offer(new int[]{lists.get(i).get(0), i, 0});
            }
        }

        while (!pq.isEmpty()) {
            // Extract the smallest element
            int[] curr = pq.poll();
            // Add value to the result list
            result.add(curr[0]);
            // If more elements remain in the same list, add the next element to the heap
            int listIndex = curr[1], elemIndex = curr[2];
            if (elemIndex + 1 < lists.get(listIndex).size()) {
                pq.offer(new int[]{lists.get(listIndex).get(elemIndex + 1), listIndex, elemIndex + 1});
            }
        }

        return result;
    }

    /**
     * Problem 8: Find the top k frequent elements using a priority queue.
     *
     * @param nums Array of integers
     * @param k Number of top frequent elements
     * @return List of top k frequent elements
     */
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            // Update frequency
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(Map.Entry.comparingByValue());

        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            // Add entry to the heap
            pq.offer(entry);
            // If heap exceeds k, remove the least frequent element
            if (pq.size() > k) {
                pq.poll();
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!pq.isEmpty()) {
            // Extract top k frequent elements
            result.add(pq.poll().getKey());
        }

        // Reverse to get highest frequency first
        Collections.reverse(result);
        return result;
    }

    /**
     * Problem 9: Validate if a binary tree is a BST.
     *
     * @param root Root node of the tree
     * @return True if valid BST, false otherwise
     */
    public boolean isValidBST(Node<Integer> root) {
        return validateBST(root, null, null);
    }

    private boolean validateBST(Node<Integer> node, Integer min, Integer max) {
        if (node == null) {
            return true;
        }

        // Check current node's value against min and max constraints
        if ((min != null && node.data <= min) || (max != null && node.data >= max)) {
            return false;
        }

        // Recursively validate left and right subtrees with updated bounds
        return validateBST(node.left, min, node.data) && validateBST(node.right, node.data, max);
    }

    /**
     * Problem 10: Find the kth smallest element in a BST.
     *
     * @param root Root node of the tree
     * @param k The kth position
     * @return The kth smallest element
     */
    public int kthSmallest(Node<Integer> root, int k) {
        Stack<Node<Integer>> stack = new Stack<>();
        Node<Integer> current = root;

        // Iterative in-order traversal
        while (current != null || !stack.isEmpty()) {
            // Traverse left subtree
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            k--;
            if (k == 0) {
                // Found the kth smallest element
                return current.data;
            }

            current = current.right;
        }

        return -1;
    }

    // Node class for BST problems
    public static class Node<T> {

        T data;
        Node<T> left;
        Node<T> right;

        Node(T data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    public static void main(String[] args) {
        Assignment5 test = new Assignment5();

        // Problem 1: fuzzyIntersection
        Set<Double> set1 = new HashSet<>(Arrays.asList(1.0, 2.5, 3.0));
        Set<Double> set2 = new HashSet<>(Arrays.asList(2.4, 3.5));
        System.out.println("1a. Fuzzy Intersection (tolerance=0.5): " + test.fuzzyIntersection(set1, set2, 0.5));
        System.out.println("1b. Fuzzy Intersection (empty sets): " + test.fuzzyIntersection(new HashSet<>(), set2, 0.5));
        System.out.println("1c. Fuzzy Intersection (tolerance=0): " + test.fuzzyIntersection(set1, set2, 0.0));
        System.out.println("1d. Fuzzy Intersection (large tolerance=10): " + test.fuzzyIntersection(set1, set2, 10));
        System.out.println();
        // Problem 2: partitionSet
        Set<Integer> numbers = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        System.out.println("2a. Partition Set (x % 2 == 0): " + test.partitionSet(numbers, x -> x % 2 == 0));
        System.out.println("2b. Partition Set (predicate always true): " + test.partitionSet(numbers, x -> true));
        System.out.println("2c. Partition Set (predicate always false): " + test.partitionSet(numbers, x -> false));
        System.out.println();
        // Problem 3: invertMapWithSetValues
        Map<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 2);
        map.put("c", 1);
        System.out.println("3a. Invert Map with Set Values: " + test.invertMapWithSetValues(map));
        Map<String, Integer> emptyMap = new HashMap<>();
        Map<String, Integer> uniqueMap = Map.of("x", 10, "y", 20, "z", 30);
        Map<String, Integer> identicalMap = Map.of("a", 1, "b", 1, "c", 1);
        System.out.println("3b. Invert Map (empty): " + test.invertMapWithSetValues(emptyMap));
        System.out.println("3c. Invert Map (unique values): " + test.invertMapWithSetValues(uniqueMap));
        System.out.println("3d. Invert Map (identical values): " + test.invertMapWithSetValues(identicalMap));
        System.out.println();
        // Problem 4: countWordFrequencies
        List<String> words = Arrays.asList("apple", "banana", "Apple", "APPLE", "banana", "Cherry");
        System.out.println("4a. Word Frequencies: " + test.countWordFrequencies(words));
        System.out.println("4b. Word Frequencies (empty list): " + test.countWordFrequencies(new ArrayList<>()));
        List<String> punctuatedWords = Arrays.asList("Hello", "hello", "Hello!", "HELLO");
        System.out.println("4c. Word Frequencies (case insensitive, punctuation sensitive): " + test.countWordFrequencies(punctuatedWords));
        System.out.println();
        // Problem 5: reverseQueue
        Queue<Integer> queue = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5));
        test.reverseQueue(queue);
        System.out.println("5a. Reversed Queue: " + queue);
        Queue<Integer> emptyQueue = new LinkedList<>();
        Queue<Integer> singleQueue = new LinkedList<>(Collections.singletonList(42));
        test.reverseQueue(emptyQueue);
        System.out.println("5b. Reversed Empty Queue: " + emptyQueue);
        test.reverseQueue(singleQueue);
        System.out.println("5c. Reversed Single Element Queue: " + singleQueue);
        System.out.println();
        // Problem 6: firstNonRepeatingChar
        String stream = "aabcbd";
        System.out.println("6a. First Non-Repeating Char in 'aabcbd': " + test.firstNonRepeatingChar(stream));
        System.out.println("6b. First Non-Repeating (all repeating): " + test.firstNonRepeatingChar("aabbcc"));
        System.out.println("6c. First Non-Repeating (unique at end): " + test.firstNonRepeatingChar("aabbc"));
        System.out.println("6d. First Non-Repeating (empty stream): " + test.firstNonRepeatingChar(""));
        System.out.println();
        // Problem 7: mergeKSortedLists
        List<List<Integer>> lists = Arrays.asList(
                Arrays.asList(1, 4, 5),
                Arrays.asList(1, 3, 4),
                Arrays.asList(2, 6)
        );
        System.out.println("7a. Merge K Sorted Lists: " + test.mergeKSortedLists(lists));
        System.out.println("7b. Merge K Sorted (empty lists): " + test.mergeKSortedLists(new ArrayList<>()));
        List<List<Integer>> singleList = Arrays.asList(Arrays.asList(1, 2, 3));
        System.out.println("7c. Merge K Sorted (single list): " + test.mergeKSortedLists(singleList));
        List<List<Integer>> negativeLists = Arrays.asList(
                Arrays.asList(-3, -1, 0),
                Arrays.asList(-2, 2),
                Arrays.asList(-5, 5)
        );
        System.out.println("7d. Merge K Sorted (negative numbers): " + test.mergeKSortedLists(negativeLists));
        System.out.println();
        // Problem 8: topKFrequent
        int[] nums = {1, 1, 1, 2, 2, 3};
        System.out.println("8a. Top 2 Frequent Elements: " + test.topKFrequent(nums, 2));
        System.out.println("8b. Top 0 Frequent: " + test.topKFrequent(nums, 0));
        System.out.println("8c. Top 10 Frequent (k > unique): " + test.topKFrequent(nums, 10));
        System.out.println("8d. Top Frequent (empty array): " + test.topKFrequent(new int[]{}, 2));
        System.out.println();
        // Problem 9: isValidBST
        Node<Integer> bst = new Node<>(5);
        bst.left = new Node<>(3);
        bst.right = new Node<>(7);
        bst.left.left = new Node<>(2);
        bst.left.right = new Node<>(4);
        System.out.println("9a. Is Valid BST: " + test.isValidBST(bst));
        Node<Integer> invalidBST = new Node<>(5);
        invalidBST.left = new Node<>(3);
        invalidBST.right = new Node<>(8);
        invalidBST.left.right = new Node<>(6); // Invalid
        System.out.println("9b. Is Valid BST (invalid): " + test.isValidBST(invalidBST));
        System.out.println("9c. Is Valid BST (single node): " + test.isValidBST(new Node<>(10)));
        System.out.println("9d. Is Valid BST (empty): " + test.isValidBST(null));
        System.out.println();
        // Problem 10: kthSmallest
        System.out.println("10a. 3rd Smallest in BST: " + test.kthSmallest(bst, 3));
        System.out.println("10b. kth Smallest (k=1): " + test.kthSmallest(bst, 1));
        System.out.println("10c. kth Smallest (k=10 > nodes): " + test.kthSmallest(bst, 10));
        System.out.println("10d. kth Smallest (k=5, largest): " + test.kthSmallest(bst, 5));
    }
}
