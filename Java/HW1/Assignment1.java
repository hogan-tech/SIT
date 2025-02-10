/**
 * Author: Hogan Lin
 * Date: February 6, 2025
 * Github: https://github.com/hogan-tech/SIT/tree/main/Java
 * Course: CS 501-A
 * Description: Implementation of various utility functions, including numerical
 * operations, string manipulations, and validation checks.
 */

public class Assignment1 {

    /**
     * Returns the second largest number among the three given integers.
     * 
     * @param a First integer
     * @param b Second integer
     * @param c Third integer
     * @return The second largest integer
     */
    public int secondLargest(int a, int b, int c) {
        return a + b + c - Math.max(a, Math.max(b, c)) - Math.min(a, Math.min(b, c));
    }

    /**
     * Determines if a given number is prime.
     * 
     * @param num The number to check
     * @return True if the number is prime, false otherwise
     */
    public boolean isPrime(int num) {
        if (num < 2)
            return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }

    /**
     * Checks if a given string is a palindrome.
     * 
     * @param sequence The string to check
     * @return True if the string is a palindrome, false otherwise
     */
    public boolean isPalindrome(String sequence) {
        String reversed = new StringBuilder(sequence).reverse().toString();
        return sequence.equals(reversed);
    }

    /**
     * Returns the sum of the digits of a given integer.
     * 
     * @param num The number to process
     * @return Sum of its digits
     */
    public int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += Math.abs(num % 10);
            num /= 10;
        }
        return sum;
    }

    /**
     * Returns the number of digits in a given integer.
     * 
     * @param num The number to process
     * @return Number of digits in num
     */
    public int countDigits(int num) {
        return String.valueOf(Math.abs(num)).length();
    }

    /**
     * Checks if a given integer is a palindrome.
     * 
     * @param num The number to check
     * @return True if num is a palindrome, false otherwise
     */
    public boolean isPalindrome(int num) {
        return isPalindrome(String.valueOf(num));
    }

    /**
     * Returns the reversed integer of a given number, keeping the sign.
     * 
     * @param num The number to reverse
     * @return The reversed integer
     */
    public int reverseNumber(int num) {
        int sign = num < 0 ? -1 : 1;
        int reversed = Integer.parseInt(new StringBuilder(String.valueOf(Math.abs(num))).reverse().toString());
        return sign * reversed;
    }

    /**
     * Converts a Roman numeral string to an integer.
     * 
     * @param romanNumeral The Roman numeral string
     * @return The integer equivalent
     */
    public int romanNumeralToInt(String romanNumeral) {
        java.util.Map<Character, Integer> map = java.util.Map.of(
                'I',
                1,
                'V',
                5,
                'X',
                10,
                'L',
                50,
                'C',
                100,
                'D',
                500,
                'M',
                1000);
        int sum = 0;
        for (int i = 0; i < romanNumeral.length(); i++) {
            int current = map.get(romanNumeral.charAt(i));
            if (i < romanNumeral.length() - 1 && current < map.get(romanNumeral.charAt(i + 1))) {
                sum -= current;
            } else {
                sum += current;
            }
        }
        return sum;
    }

    /**
     * Validates if a given string is a valid phone number.
     * 
     * @param phoneNumber The phone number string
     * @return True if it matches the expected formats, false otherwise
     */
    public boolean validPhoneNumber(String phoneNumber) {
        return phoneNumber.matches("\\(\\d{3}\\)\\d{3}-\\d{4}|\\d{3}-\\d{3}-\\d{4}|\\d{10}");
    }

    /**
     * Calculates the Euclidean distance between two points in a 2D plane.
     * 
     * @param x1 X-coordinate of the first point
     * @param y1 Y-coordinate of the first point
     * @param x2 X-coordinate of the second point
     * @param y2 Y-coordinate of the second point
     * @return The Euclidean distance
     */
    public double euclideanDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    public static void main(String[] args) {
        Assignment1 test = new Assignment1();
        System.out.println(" 1. Second largest of 5, 8, 3: " + test.secondLargest(5, 8, 3));
        System.out.println(" 2. Is 13 prime? " + test.isPrime(13));
        System.out.println(" 3. Is 'madam' palindrome? " + test.isPalindrome("madam"));
        System.out.println(" 4. Sum of digits in 1234: " + test.sumOfDigits(1234));
        System.out.println(" 5. Number of digits in 12345: " + test.countDigits(12345));
        System.out.println(" 6. Is 12321 palindrome? " + test.isPalindrome(12321));
        System.out.println(" 7. Reverse of 12345: " + test.reverseNumber(12345));
        System.out.println(" 8. Roman numeral 'XIV' to integer: " + test.romanNumeralToInt("XIV"));
        System.out.println(" 9. Is '(123)456-7890' a valid phone number? " + test.validPhoneNumber("(123)456-7890"));
        System.out.println("10. Euclidean distance between (1,2) and (4,6): " + test.euclideanDistance(1, 2, 4, 6));
    }
}



