
/**
* @author: Hogan Lin
* @class: CS501 Intro to Java
* @description: Implementation of various array and matrix operations, including solving quadratic equations, 
*               array manipulations (reversal, removing duplicates, moving zeros, finding the second largest element), 
*               and matrix transformations (transposing and rotating). Additionally, implements functions to extract 
*               a spiral path from a matrix and check for the presence of a 2D subarray within a 3D array.
* @date: February 28, 2025
* @githubRepo: https://github.com/hogan-tech/SIT/tree/main/Java
**/
import java.util.Arrays;

public class Assignment2 {
    /**
     * Solves the quadratic equation ax^2 + bx + c = 0 using the quadratic formula.
     * 
     * @param a Coefficient of x^2 (must be nonzero)
     * @param b Coefficient of x
     * @param c Constant term
     * @return A double array containing the two roots of the equation, rounded to
     *         three decimal places.
     *         If the equation has no real roots, returns {Double.NaN, Double.NaN}.
     */
    public static double[] quadraticEquation(double a, double b, double c) {
        // Calculate the discriminant (b^2 - 4ac) to determine the nature of the roots.
        double discriminant = b * b - 4 * a * c;

        // If the discriminant is negative, the equation has no real roots.
        if (discriminant < 0) {
            return new double[] { Double.NaN, Double.NaN }; // Returning NaN for both roots.
        }

        // Compute the square root of the discriminant.
        double sqrtD = Math.sqrt(discriminant);

        // Compute the two roots using the quadratic formula: (-b ± sqrt(D)) / (2a)
        double root1 = (-b + sqrtD) / (2 * a);
        double root2 = (-b - sqrtD) / (2 * a);

        // Round the roots to three decimal places before returning.
        return new double[] {
                Math.round(root1 * 1000.0) / 1000.0,
                Math.round(root2 * 1000.0) / 1000.0
        };
    }

    /**
     * Given an array, find the max, min, average, and sum.
     * Return the answers in an array of size 4 in the order above.
     * 
     * @param arr Input array
     * @return Array containing max, min, average, and sum
     */
    public static double[] arrayOperations(double[] arr) {
        // Handle edge case: empty array
        if (arr.length == 0) {
            return new double[] { Double.NaN, Double.NaN, Double.NaN, 0 };
        }

        // Initialize max with the smallest possible value and min with the largest
        // possible value.
        double max = Double.MIN_VALUE, min = Double.MAX_VALUE, sum = 0;

        // Iterate through the array to compute max, min, and sum.
        for (double num : arr) {
            max = Math.max(max, num); // Update max if the current number is larger.
            min = Math.min(min, num); // Update min if the current number is smaller.
            sum += num; // Accumulate the sum of all elements.
        }

        // Return an array containing max, min, average (sum / count), and sum.
        return new double[] { max, min, sum / arr.length, sum };
    }

    /**
     * Reverse the elements in arr in-place.
     * 
     * @param arr Input array
     */
    public static void reverseArray(int[] arr) {
        // Initialize two pointers: left starts at the beginning, right starts at the
        // end.
        int left = 0, right = arr.length - 1;

        // Swap elements from the start and end until the pointers meet in the middle.
        while (left < right) {
            // Swap the elements at positions 'left' and 'right'.
            int temp = arr[left];
            arr[left++] = arr[right]; // Move left pointer to the right.
            arr[right--] = temp; // Move right pointer to the left.
        }
    }

    /**
     * Remove all duplicates from an array. The result should
     * have a length corresponding to the number of unique elements.
     * 
     * @param arr Input array
     * @return Array with unique elements
     */

    // Reference: https://www.geeksforgeeks.org/stream-distinct-java/
    public static int[] removeDuplicates(int[] arr) {
        // Convert the array into a stream, apply 'distinct()' to remove duplicates, and
        // convert back to an array.
        return java.util.Arrays.stream(arr).distinct().toArray();
    }

    /**
     * Move all zeros to the end of the array while maintaining the order of other
     * elements.
     * 
     * @param arr Input array
     */
    public static void moveZeros(int[] arr) {
        int index = 0; // Pointer to track the position of the next nonzero element.

        // First pass: Move all nonzero elements forward in their original order.
        for (int num : arr) {
            if (num != 0) {
                arr[index++] = num; // Place the nonzero element at the next available position.
            }
        }

        // Second pass: Fill the remaining positions with zeros.
        while (index < arr.length) {
            arr[index++] = 0; // Assign zeros to the remaining positions in the array.
        }
    }

    /**
     * Find the second-largest element in an array without sorting.
     * 
     * @param arr Input array
     * @return Second largest element
     */
    public static int findSecondLargest(int[] arr) {
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE; // Initialize largest and second largest.

        // Iterate through the array to find the two largest unique values.
        for (int num : arr) {
            if (num > first) {
                // If current number is greater than first largest, update first and shift the
                // previous first to second.
                second = first;
                first = num;
            } else if (num > second && num != first) {
                // If current number is greater than second largest and not equal to first,
                // update second.
                second = num;
            }
        }

        // Return second largest element; if no valid second largest is found, it
        // remains Integer.MIN_VALUE.
        return second;
    }

    /**
     * Transpose a square matrix (swaps rows and columns in-place).
     * 
     * @param matrix Input square matrix
     */
    public static void transposeMatrix(int[][] matrix) {
        int n = matrix.length; // Get the dimension of the square matrix.

        // Iterate over the upper triangle of the matrix (excluding the diagonal).
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Swap matrix[i][j] with matrix[j][i] to perform the transpose operation.
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }

    /**
     * Rotate a matrix 90 degrees clockwise.
     * 
     * @param matrix Input matrix
     * @return Rotated matrix
     */
    public static int[][] rotate90Clockwise(int[][] matrix) {
        int n = matrix.length; // Get the dimension of the square matrix.
        int[][] rotated = new int[n][n]; // Create a new matrix to store the rotated result.

        // Iterate through the matrix and map each element to its new position.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j]; // Rotate and assign to the new position.
            }
        }

        return rotated; // Return the rotated matrix.
    }

    /**
     * Return a 1D array path that traverses the matrix in a clockwise spiral
     * starting from the top left.
     * Ex:
     * { {1, 2, 3},
     * {4, 5, 6},
     * {7, 8, 9}
     * } -> {1, 2, 3, 6, 9, 8, 7, 4, 5}
     * 
     * @param matrix The input matrix
     * @return The spiral path
     */

    public static int[] spiralPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0)
            return new int[0];

        int rows = matrix.length, cols = matrix[0].length;
        int[] result = new int[rows * cols];
        int index = 0;

        int top = 0, bottom = rows - 1, left = 0, right = cols - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right
            for (int i = left; i <= right; i++) {
                result[index++] = matrix[top][i];
            }
            top++;

            // Traverse from top to bottom
            for (int i = top; i <= bottom; i++) {
                result[index++] = matrix[i][right];
            }
            right--;

            // Traverse from right to left (if not already traversed)
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result[index++] = matrix[bottom][i];
                }
                bottom--;
            }

            // Traverse from bottom to top (if not already traversed)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result[index++] = matrix[i][left];
                }
                left++;
            }
        }
        return result;
    }

    /**
     * Given a 3D array, check if it contains a given 2D subarray.
     * 
     * @param array    The 3D array
     * @param subarray The 2D subarray
     * @return True if the subarray is found in any layer of the 3D array, false
     *         otherwise
     */
    public static boolean containsSubarray(int[][][] array, int[][] subarray) {
        // Iterate through each 2D layer in the 3D array.
        for (int[][] layer : array) {
            // Check if the subarray is present in the current 2D layer.
            if (isSubarrayPresent(layer, subarray)) {
                return true; // Return true immediately if found.
            }
        }
        return false; // Return false if no match is found in any layer.
    }

    /**
     * Helper function to check if a 2D subarray is present in a 2D array.
     * 
     * @param matrix   The larger 2D matrix
     * @param subarray The 2D subarray to search for
     * @return True if subarray is found, false otherwise
     */
    private static boolean isSubarrayPresent(int[][] matrix, int[][] subarray) {
        int m = matrix.length, n = matrix[0].length; // Dimensions of the main matrix
        int sm = subarray.length, sn = subarray[0].length; // Dimensions of the subarray

        // Iterate over all possible starting positions where the subarray could fit
        for (int i = 0; i <= m - sm; i++) {
            for (int j = 0; j <= n - sn; j++) {
                // Check if the subarray matches at the current position (i, j)
                if (matchesSubarray(matrix, subarray, i, j)) {
                    return true; // Return true immediately if a match is found
                }
            }
        }
        return false; // Return false if no match is found
    }

    /**
     * Helper function to check if subarray matches starting at (row, col)
     * 
     * @param matrix   The larger matrix
     * @param subarray The subarray to match
     * @param row      Starting row index
     * @param col      Starting column index
     * @return True if subarray matches, false otherwise
     */
    private static boolean matchesSubarray(int[][] matrix, int[][] subarray, int row, int col) {
        // Iterate through the subarray and compare each element with the corresponding
        // element in the matrix.
        for (int i = 0; i < subarray.length; i++) {
            for (int j = 0; j < subarray[i].length; j++) {
                // If any element does not match, return false immediately.
                if (matrix[row + i][col + j] != subarray[i][j]) {
                    return false;
                }
            }
        }
        return true; // If all elements match, return true.
    }

    public static void main(String[] args) {
        // Test quadraticEquation
        System.out.println("Quadratic roots: " + Arrays.toString(quadraticEquation(1, -3, 2)));

        // Test arrayOperations
        System.out.println("Array operations: " + Arrays.toString(arrayOperations(new double[] { 1, 2, 3, 4, 5 })));

        // Test reverseArray
        int[] arr = { 1, 2, 3, 4, 5 };
        reverseArray(arr);
        System.out.println("Reversed array: " + Arrays.toString(arr));

        // Test removeDuplicates
        System.out
                .println("Remove duplicates: " + Arrays.toString(removeDuplicates(new int[] { 1, 2, 2, 3, 4, 4, 5 })));

        // Test moveZeros
        int[] zerosArr = { 0, 1, 0, 3, 12 };
        moveZeros(zerosArr);
        System.out.println("Move zeros: " + Arrays.toString(zerosArr));

        // Test findSecondLargest
        System.out.println("Second largest: " + findSecondLargest(new int[] { 10, 20, 4, 45, 99 }));

        // Test spiralPath
        int[][] spiralMatrix = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
        };
        System.out.println("Spiral Path: " + Arrays.toString(spiralPath(spiralMatrix)));
        // Test transposeMatrix
        int[][] matrix = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
        };
        System.out.println("Original matrix: ");
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }

        transposeMatrix(matrix);

        System.out.println("Transposed matrix: ");
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }

        // Base on Slack Homework channel, use the same test case to check logic
        // Test containsSubarray (Example 1 - Should return true)
        int[][][] array3D_1 = {
                {
                        { 1, 2, 3, 4 },
                        { 2, 4, 6, 8 },
                        { 3, 6, 9, 12 }
                },
                {
                        { 2, 4, 6, 8 },
                        { 4, 8, 12, 16 },
                        { 6, 12, 18, 24 }
                }
        };

        int[][] subarray_1 = {
                { 4, 6, 8 },
                { 8, 12, 16 }
        };

        System.out.println("Contains subarray (expected true): " + containsSubarray(array3D_1, subarray_1));

        // Test containsSubarray (Example 2 - Should return false)
        int[][][] array3D_2 = {
                {
                        { 2, 4, 6 },
                        { 4, 8, 12 },
                        { 6, 12, 18 }
                },
                {
                        { 3, 6, 9 },
                        { 6, 12, 18 },
                        { 9, 18, 27 }
                },
                {
                        { 4, 8, 12 },
                        { 8, 16, 24 },
                        { 12, 24, 36 }
                }
        };

        int[][] subarray_2 = {
                { 12, 18 },
                { 16, 24 }
        };

        System.out.println("Contains subarray (expected false): " + containsSubarray(array3D_2, subarray_2));

    }
}
