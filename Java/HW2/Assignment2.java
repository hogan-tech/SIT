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
    }
}
