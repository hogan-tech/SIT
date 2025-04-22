import java.util.*;

/**
 * @author: Hogan Lin
 * @class: CS501 - Intro to Java
 * @description: Solutions for Assignment 4: recursion, collections, and
 *               generics.
 * @date: April 15, 2025
 **/
public class Assignment4 {

    /**
     * Problem 1: Recursive Palindrome Checker.
     * Checks if a string is a palindrome, ignoring case, non-alphanumeric
     * characters, and whitespace.
     * Reference:
     * https://www.geeksforgeeks.org/problems/form-a-palindrome2544/
     *
     * @param s The input string to check
     * @return True if s is a palindrome, false otherwise
     */
    public boolean isPalindrome(String s) {
        // Kick off the recursive helper with pointers at both ends of the string
        return isPalindromeHelper(s, 0, s.length() - 1);
    }

    /**
     * Recursive helper that advances left and right pointers towards the center,
     * skipping non-alphanumeric characters and comparing characters
     * case-insensitively.
     *
     * @param s     The input string
     * @param left  The current left index
     * @param right The current right index
     * @return true if the substring s[left..right] is a palindrome; false otherwise
     */
    private boolean isPalindromeHelper(String s, int left, int right) {
        // Move left forward past any non-alphanumeric characters
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
            left++;
        }
        // Move right backward past any non-alphanumeric characters
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
            right--;
        }
        // If pointers have crossed, we’ve checked all relevant chars – it’s a
        // palindrome
        if (left >= right) {
            return true;
        }
        // Compare characters case-insensitively
        if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
            return false; // Mismatch found
        }
        // Recurse inward
        return isPalindromeHelper(s, left + 1, right - 1);
    }

    /**
     * Problem 2: Map Merging.
     * Merges two maps of String to Integer. If a key exists in both, sums their
     * values.
     *
     * @param map1 First map
     * @param map2 Second map
     * @return A new map containing merged entries
     */
    public Map<String, Integer> mergeMaps(Map<String, Integer> map1, Map<String, Integer> map2) {
        // Start with a shallow copy of map1 so we don’t modify the original
        Map<String, Integer> merged = new HashMap<>(map1);

        // For each entry in map2, add it into 'merged'.
        // If the key already exists, Integer::sum will add the two values together.
        for (Map.Entry<String, Integer> entry : map2.entrySet()) {
            merged.merge(
                    entry.getKey(),
                    entry.getValue(),
                    Integer::sum);
        }

        return merged;
    }

    /**
     * Problem 3: Set Symmetric Difference.
     * Returns elements in either set1 or set2 but not both.
     *
     * @param set1 First set
     * @param set2 Second set
     * @param <T>  Type of elements
     * @return A new set containing the symmetric difference
     */
    public <T> Set<T> symmetricDifference(Set<T> set1, Set<T> set2) {
        // Start by copying all elements from set1 into the result
        Set<T> result = new HashSet<>(set1);

        // For each element in set2:
        for (T elem : set2) {
            if (!result.add(elem)) {
                result.remove(elem);
            }
        }

        // 'result' contains elements only from one of the sets, notboth.
        return result;
    }

    /**
     * Problem 4: Deep List Reversal.
     * Recursively reverses a list and all nested sublists.
     *
     * @param list The list to reverse
     * @return A new list that is the deep reverse of the input
     */
    @SuppressWarnings("unchecked")
    public static List<Object> deepReverse(List<Object> list) {
        // Prepare a new list to hold the reversed elements
        List<Object> reversed = new ArrayList<>();

        // Create a ListIterator positioned at the end of the list
        ListIterator<Object> it = list.listIterator(list.size());

        // Walk backwards through the list
        while (it.hasPrevious()) {
            Object elem = it.previous();

            // If the current element is itself a List, recurse to deep-reverse it
            if (elem instanceof List) {
                reversed.add(deepReverse((List<Object>) elem));
            } else {
                // Otherwise, just add the element as is
                reversed.add(elem);
            }
        }

        return reversed;
    }

    /**
     * Problem 5: Generic MyStack with recursive reverse.
     * Implements a stack using a List and provides methods to push, pop, and
     * reverse.
     */
    public static class MyStack<T> {
        private List<T> elements = new ArrayList<>();

        /**
         * Pushes an element onto the stack.
         *
         * @param element The element to push
         */
        public void push(T element) {
            elements.add(element);
        }

        /**
         * Pops the top element from the stack.
         *
         * @return The popped element, or null if empty
         */
        public T pop() {
            return elements.isEmpty() ? null : elements.remove(elements.size() - 1);
        }

        /**
         * Recursively reverses the elements of the stack.
         */
        public void reverse() {
            if (elements.isEmpty())
                return;
            T bottom = removeBottom();
            reverse();
            elements.add(bottom);
        }

        /**
         * Helper to remove and return the bottom element of the stack.
         *
         * @return The bottom element
         */
        private T removeBottom() {
            T top = pop();
            if (elements.isEmpty()) {
                // This was the bottom element
                return top;
            } else {
                T bottom = removeBottom();
                elements.add(top);
                return bottom;
            }
        }
    }

    /**
     * Problem 6: Power Set using recursion.
     * Returns all subsets of the original set.
     *
     * @param originalSet The input set
     * @param <T>         Type of elements
     * @return A set of all subsets
     */
    public <T> Set<Set<T>> powerSet(Set<T> originalSet) {
        // This will hold all subsets
        Set<Set<T>> sets = new HashSet<>();

        // Base case: the power set of the empty set is a set containing the empty set
        if (originalSet.isEmpty()) {
            sets.add(new HashSet<>()); // add the empty subset
            return sets;
        }

        // Convert originalSet to a List so we can easily split off one element
        List<T> list = new ArrayList<>(originalSet);
        // 'head' is the first element, 'rest' is everything else
        T head = list.get(0);
        Set<T> rest = new HashSet<>(list.subList(1, list.size()));

        // Recursively compute the power set of the smaller set 'rest'
        for (Set<T> subset : powerSet(rest)) {
            // 1) All subsets that do not include 'head'
            sets.add(new HashSet<>(subset));

            // 2) All subsets that do include 'head'
            Set<T> withHead = new HashSet<>(subset);
            withHead.add(head);
            sets.add(withHead);
        }

        return sets;
    }

    /**
     * Problem 7: Find pairs summing to target.
     * Returns unique pairs (as sets) that sum to the target.
     *
     * @param list   List of Double values
     * @param target Target sum
     * @return A set of unique pairs
     */
    public Set<Set<Double>> findPairs(List<Double> list, Double target) {
        // Holds the resulting pairs (each pair is itself a Set<Double>)
        Set<Set<Double>> result = new HashSet<>();

        // Tracks which numbers we've already processed, to avoid duplicate pairs
        Set<Double> seen = new HashSet<>();

        // Count occurrences of each number in the list (needed for handling num ==
        // complement)
        Map<Double, Integer> count = new HashMap<>();
        for (Double num : list) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Iterate through each number to find its complement
        for (Double num : list) {
            Double complement = target - num;

            // Check if the complement exists in the list
            if (count.containsKey(complement)) {
                // If num and complement are the same value, ensure it occurs at least twice
                if (num.equals(complement) && count.get(num) < 2) {
                    continue; // not enough occurrences to form a valid pair
                }

                // Only add the pair if neither element has been "seen" yet,
                // which prevents adding the same pair twice in different orders
                if (!seen.contains(num) && !seen.contains(complement)) {
                    Set<Double> pair = new HashSet<>();
                    pair.add(num);
                    pair.add(complement);
                    result.add(pair);
                }
            }

            // Mark this number as processed
            seen.add(num);
        }

        return result;
    }

    /**
     * Problem 8: Balanced Parentheses Checker using recursion and a stack.
     * Valid pairs: (), [], {}, <>.
     *
     * @param s Input string containing parentheses
     * @return True if balanced, false otherwise
     */
    public boolean isBalanced(String s) {
        // Kick off recursion starting at index 0 with an empty stack
        return isBalancedHelper(s, 0, new ArrayDeque<>());
    }

    /**
     * Recursive helper that processes one character at a time and maintains a stack
     * of opening brackets. At the end of the string, the stack must be empty.
     *
     * @param s     the input bracket string
     * @param index current character position
     * @param stack stack holding unmatched opening brackets
     * @return true if the substring from index to end is balanced with the current
     *         stack
     */
    private boolean isBalancedHelper(String s, int index, Deque<Character> stack) {
        // Base case: reached end of string → valid only if no unclosed brackets remain
        if (index == s.length()) {
            return stack.isEmpty();
        }

        char c = s.charAt(index);

        // If it's an opening bracket, push onto stack
        if (c == '(' || c == '[' || c == '{' || c == '<') {
            stack.push(c);

        }
        // If it's a closing bracket, ensure it matches the most recent opening
        else if (c == ')' || c == ']' || c == '}' || c == '>') {
            // Cannot close if nothing is open
            if (stack.isEmpty()) {
                return false;
            }
            char open = stack.pop();
            // If the popped bracket doesn't match, it's unbalanced
            if (!matches(open, c)) {
                return false;
            }
        }
        // Recurse to next character
        return isBalancedHelper(s, index + 1, stack);
    }

    /**
     * Checks if the given opening and closing brackets form a matching pair.
     *
     * @param open  the opening bracket character
     * @param close the closing bracket character
     * @return true if open and close are one of (), [], {}, or <>; false otherwise
     */
    private boolean matches(char open, char close) {
        return (open == '(' && close == ')')
                || (open == '[' && close == ']')
                || (open == '{' && close == '}')
                || (open == '<' && close == '>');
    }

    /**
     * Problem 9: Recursive Maze Solver.
     * Determines if there's a path from (x, y) to bottom-right in a 0/1 grid.
     *
     * @param maze    2D grid (0 = path, 1 = wall)
     * @param x       Current row
     * @param y       Current column
     * @param visited Visited cells tracker
     * @return True if path exists, false otherwise
     */
    public boolean solveMaze(int[][] maze, int x, int y, boolean[][] visited) {
        int rows = maze.length;
        int cols = maze[0].length;
        // bounds or wall or visited
        if (x < 0 || y < 0 || x >= rows || y >= cols || maze[x][y] == 1 || visited[x][y]) {
            return false;
        }
        // reached goal
        if (x == rows - 1 && y == cols - 1) {
            return true;
        }
        visited[x][y] = true;
        // explore neighbors
        if (solveMaze(maze, x + 1, y, visited)
                || solveMaze(maze, x - 1, y, visited)
                || solveMaze(maze, x, y + 1, visited)
                || solveMaze(maze, x, y - 1, visited)) {
            return true;
        }
        return false;
    }

    /**
     * Problem 10: Recursive Tree Mirroring.
     * Swaps left and right subtrees at every node.
     *
     * @param root The root of the binary tree
     * @param <T>  Type of node data
     */
    public <T> void mirrorTree(Node<T> root) {
        // Base case: if we've reached a null node, nothing to mirror
        if (root == null) {
            return;
        }

        // Swap the left and right child references
        Node<T> temp = root.left;
        root.left = root.right;
        root.right = temp;

        // Recursively mirror the left subtree (which was originally the right subtree)
        mirrorTree(root.left);
        // Recursively mirror the right subtree (which was originally the left subtree)
        mirrorTree(root.right);
    }

    /**
     * Simple binary tree node class.
     *
     * @param <T> the type of data stored in this node
     */
    public static class Node<T> {
        T data; // the value or payload stored in this node
        Node<T> left; // reference to the left child subtree
        Node<T> right; // reference to the right child subtree

        /**
         * Constructs a new Node with the given data and no children.
         *
         * @param data the value to store in this node
         */
        public Node(T data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    // Simple test utilities
    private static void test(String input, boolean result, boolean expected) {
        System.out.printf("Input: %-30s Result: %-5b Expected: %-5b [%s]\n", input, result, expected,
                (result == expected ? "PASS" : "FAIL"));
    }

    private static void testMapEntry(String key, Integer value, int expected) {
        System.out.printf("Key: %-5s Value: %-5d Expected: %-5d [%s]\n", key, value, expected,
                (value == expected ? "PASS" : "FAIL"));
    }

    private static <T> void testSet(Set<T> result, Set<T> expected) {
        System.out.printf("Result Set: %-15s Expected Set: %-15s [%s]\n", result, expected,
                (result.equals(expected) ? "PASS" : "FAIL"));
    }

    public static void main(String[] args) {
        Assignment4 a = new Assignment4();
        System.out.println("Problem 1: Recursive Palindrome Checker");
        test("A man, a plan, a canal: Panama", a.isPalindrome("A man, a plan, a canal: Panama"), true);
        test("Hello, world!", a.isPalindrome("Hello, world!"), false);
        System.out.println();

        System.out.println("\nProblem 2: Map Merging");
        Map<String, Integer> m1 = new HashMap<>();
        m1.put("a", 1);
        m1.put("b", 2);
        Map<String, Integer> m2 = new HashMap<>();
        m2.put("b", 3);
        m2.put("c", 4);
        Map<String, Integer> merged = a.mergeMaps(m1, m2);
        testMapEntry("a", merged.get("a"), 1);
        testMapEntry("b", merged.get("b"), 5);
        testMapEntry("c", merged.get("c"), 4);
        System.out.println();

        System.out.println("\nProblem 3: Set Symmetric Difference");
        Set<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3));
        Set<Integer> s2 = new HashSet<>(Arrays.asList(2, 3, 4));
        Set<Integer> diff = a.symmetricDifference(s1, s2);
        testSet(diff, new HashSet<>(Arrays.asList(1, 4)));
        System.out.println();

        System.out.println("\nProblem 4: Deep List Reversal");
        List<Object> nested = Arrays.asList(1, Arrays.asList(2, 3), 4);
        List<Object> rev = Assignment4.deepReverse(nested);
        System.out.printf("Deep Reverse: %-25s Expected: [4, [3, 2], 1]", rev);
        System.out.println();

        System.out.println("\nProblem 5: MyStack.reverse()");
        MyStack<Integer> st = new MyStack<>();
        for (int i = 1; i <= 4; i++)
            st.push(i);
        st.reverse();
        List<Integer> popped = new ArrayList<>();
        Integer val;
        while ((val = st.pop()) != null)
            popped.add(val);
        System.out.printf("Stack reverse: %-25s Expected: [1, 2, 3, 4]", popped);
        System.out.println();

        System.out.println("\nProblem 6: Power Set");
        Set<String> empty = new HashSet<>();
        System.out.println("Power set of empty: " + a.powerSet(empty));
        Set<String> oneTwo = new HashSet<>(Arrays.asList("x", "y"));
        System.out.println("Power set of [x,y]: " + a.powerSet(oneTwo));
        System.out.println();

        System.out.println("\nProblem 7: Find Pairs Summing to Target");
        List<Double> nums = Arrays.asList(1.0, 2.0, 3.0, 4.0, 2.0);
        System.out.println("Pairs to 5.0: " + a.findPairs(nums, 5.0));
        System.out.println();

        System.out.println("\nProblem 8: Balanced Parentheses Checker");
        test("([]){}<>", a.isBalanced("([]){}<>"), true);
        test("([)]", a.isBalanced("([)]"), false);
        System.out.println();

        System.out.println("\nProblem 9: Recursive Maze Solver");
        int[][] openMaze = { { 0, 1, 0 }, { 0, 0, 0 }, { 1, 0, 0 } };
        boolean[][] vis1 = new boolean[3][3];
        System.out.printf("Open Maze: %-5b Expected: true\n", a.solveMaze(openMaze, 0, 0, vis1));
        int[][] blocked = { { 0, 1, 1 }, { 1, 1, 0 }, { 1, 0, 0 } };
        boolean[][] vis2 = new boolean[3][3];
        System.out.printf("Blocked Maze: %-5b Expected: false\n", a.solveMaze(blocked, 0, 0, vis2));
        System.out.println();

        System.out.println("\nProblem 10: Recursive Tree Mirroring");
        Node<Integer> root = new Node<>(1);
        root.left = new Node<>(2);
        root.right = new Node<>(3);
        a.mirrorTree(root);
        System.out.printf("Mirror root.left: %-5d Expected: 3\n", root.left.data);
        System.out.printf("Mirror root.right: %-5d Expected: 2\n", root.right.data);
    }
}
