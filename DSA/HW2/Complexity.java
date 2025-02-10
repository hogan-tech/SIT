/**
 * Author: Hogan Lin
 * Date: February 6, 2025
 * Github: https://github.com/hogan-tech/SIT/tree/main/DSA
 * Description: This class implements methods with different time complexities
 * and prints the number of operations performed.
 */

public class Complexity {

    /**
     * Method with O(n^2) complexity.
     * Prints the number of operations performed.
     * 
     * @param num The input size.
     */
    public static void method1(int num) {
        int counter = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                System.out.println("Operation " + (++counter));
            }
        }
    }

    /**
     * Method with O(n^3) complexity.
     * Prints the number of operations performed.
     * 
     * @param num The input size.
     */
    public static void method2(int num) {
        int counter = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                for (int k = 0; k < num; k++) {
                    System.out.println("Operation " + (++counter));
                }
            }
        }
    }

    /**
     * Method with O(log n) complexity.
     * Prints the number of operations performed.
     * 
     * @param num The input size.
     */
    public static void method3(int num) {
        int counter = 0;
        for (int i = 1; i < num; i *= 2) {
            System.out.println("Operation " + (++counter));
        }
    }

    /**
     * Method with O(n log n) complexity.
     * Prints the number of operations performed.
     * 
     * @param num The input size.
     */
    public static void method4(int num) {
        int counter = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 1; j < num; j *= 2) {
                System.out.println("Operation " + (++counter));
            }
        }
    }

    /**
     * Method with O(log log n) complexity.
     * Prints the number of operations performed.
     * 
     * @param num The input size.
     */
    public static void method5(int num) {
        int counter = 0;
        for (int i = 2; i < num; i = (int) Math.pow(i, 2)) {
            System.out.println("Operation " + (++counter));
        }
    }

    /**
     * Optional method with O(2^n) complexity.
     * Recursively counts the number of operations performed.
     * 
     * @param num The input size.
     * @return The number of operations performed.
     */
    public static int method6(int num) {
        if (num <= 0)
            return 1;
        return 1 + method6(num - 1) + method6(num - 1);
    }

    public static void main(String[] args) {
        int n = 5;

        System.out.println("Method1 (O(n^2)):");
        method1(n);

        System.out.println("\nMethod2 (O(n^3)):");
        method2(n);

        System.out.println("\nMethod3 (O(log n)):");
        method3(n);

        System.out.println("\nMethod4 (O(n log n)):");
        method4(n);

        System.out.println("\nMethod5 (O(log log n)):");
        method5(n);

        System.out.println("\nMethod6 (O(2^n)):");
        System.out.println("Operations: " + method6(n));
    }
}
