import java.util.Arrays;

public class Assignment2 {
    /**
     * Given the coefficients of a quadratic equation, find the
     * array of roots of the equation. Round to three decimal
     * places and return the roots in an array of size 2. If
     * imaginary, set roots to Double.NaN (Not a Number).
     * 
     * @param a Coefficient of x^2
     * @param b Coefficient of x
     * @param c Constant term
     * @return Array containing the two roots
     */
    public static double[] quadraticEquation(double a, double b, double c) {
        double discriminant = b * b - 4 * a * c;
        if (discriminant < 0) {
            return new double[] { Double.NaN, Double.NaN };
        }
        double sqrtD = Math.sqrt(discriminant);
        double root1 = (-b + sqrtD) / (2 * a);
        double root2 = (-b - sqrtD) / (2 * a);
        return new double[] { Math.round(root1 * 1000.0) / 1000.0, Math.round(root2 * 1000.0) / 1000.0 };
    }

    /**
     * Given an array, find the max, min, average, and sum.
     * Return the answers in an array of size 4 in the order above.
     * 
     * @param arr Input array
     * @return Array containing max, min, average, and sum
     */
    public static double[] arrayOperations(double[] arr) {
        double max = Double.MIN_VALUE, min = Double.MAX_VALUE, sum = 0;
        for (double num : arr) {
            max = Math.max(max, num);
            min = Math.min(min, num);
            sum += num;
        }
        return new double[] { max, min, sum / arr.length, sum };
    }

    /**
     * Reverse the elements in arr in-place.
     * 
     * @param arr Input array
     */
    public static void reverseArray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left++] = arr[right];
            arr[right--] = temp;
        }
    }

    /**
     * Remove all duplicates from an array. The result should
     * have a length corresponding to the number of unique elements.
     * 
     * @param arr Input array
     * @return Array with unique elements
     */
    public static int[] removeDuplicates(int[] arr) {
        return java.util.Arrays.stream(arr).distinct().toArray();
    }

    /**
     * Move all zeros to the end of the array while maintaining the order of other
     * elements.
     * 
     * @param arr Input array
     */
    public static void moveZeros(int[] arr) {
        int index = 0;
        for (int num : arr) {
            if (num != 0)
                arr[index++] = num;
        }
        while (index < arr.length) {
            arr[index++] = 0;
        }
    }

    /**
     * Find the second-largest element in an array without sorting.
     * 
     * @param arr Input array
     * @return Second largest element
     */
    public static int findSecondLargest(int[] arr) {
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
        for (int num : arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second && num != first) {
                second = num;
            }
        }
        return second;
    }

    /**
     * Transpose a square matrix (swaps rows and columns in-place).
     * 
     * @param matrix Input square matrix
     */
    public static void transposeMatrix(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
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
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        return rotated;
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
        for (int[][] layer : array) {
            if (isSubarrayPresent(layer, subarray)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Helper function to check if a 2D subarray is present in a 2D array.
     * 
     * @param matrix   The larger 2D matrix
     * @param subarray The 2D subarray to search for
     * @return True if subarray is found, false otherwise
     */
    private static boolean isSubarrayPresent(int[][] matrix, int[][] subarray) {
        int m = matrix.length, n = matrix[0].length;
        int sm = subarray.length, sn = subarray[0].length;

        for (int i = 0; i <= m - sm; i++) {
            for (int j = 0; j <= n - sn; j++) {
                if (matchesSubarray(matrix, subarray, i, j)) {
                    return true;
                }
            }
        }
        return false;
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
        for (int i = 0; i < subarray.length; i++) {
            for (int j = 0; j < subarray[i].length; j++) {
                if (matrix[row + i][col + j] != subarray[i][j]) {
                    return false;
                }
            }
        }
        return true;
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

        // Test containsSubarray
        int[][][] array3D = {
                {
                        { 1, 2, 3 },
                        { 4, 5, 6 },
                        { 7, 8, 9 }
                },
                {
                        { 10, 11, 12 },
                        { 13, 14, 15 },
                        { 16, 17, 18 }
                }
        };

        int[][] subarray = {
                { 4, 5 },
                { 7, 8 }
        };

        System.out.println("Contains subarray: " + containsSubarray(array3D, subarray));
    }
}
