
/**
 * Author: Hogan Lin
 * Date: Nov 25th 2024
 * Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
 * Description: This program implements a BinaryNumber class that supports various binary operations.
 */

import java.util.Arrays;

public class BinaryNumber {
    private int[] data;
    private boolean overflow;

    /**
     * Constructor for creating a binary number with all zeros.
     * 
     * @param length Length of the binary number.
     */
    public BinaryNumber(int length) {
        if (length <= 0) {
            throw new IllegalArgumentException("Length must be greater than zero.");
        }
        data = new int[length];
        overflow = false;
    }

    /**
     * Constructor for creating a binary number from a string.
     * 
     * @param str Binary string representation.
     */
    public BinaryNumber(String str) {
        if (str == null || str.isEmpty() || !str.matches("[01]+")) {
            throw new IllegalArgumentException("Invalid binary string.");
        }
        data = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            data[i] = Character.getNumericValue(str.charAt(str.length() - 1 - i)); // Little-endian representation
        }
        overflow = false;
    }

    /**
     * Returns the length of the binary number.
     * 
     * @return Length of the binary number.
     */
    public int getLength() {
        return data.length;
    }

    /**
     * Returns the digit at a specific index.
     * 
     * @param index The position of the digit to retrieve.
     * @return The binary digit at the given index.
     */
    public int getDigit(int index) {
        if (index < 0 || index >= data.length) {
            System.out.println("Index out of bounds.");
            return -1; // Indicating an error
        }
        return data[index];
    }

    /**
     * Converts the binary number to decimal.
     * 
     * @return Decimal equivalent of the binary number.
     */
    public int toDecimal() {
        int decimalValue = 0;
        for (int i = 0; i < data.length; i++) {
            decimalValue += data[i] * Math.pow(2, i);
        }
        return decimalValue;
    }

    /**
     * Shifts the binary number to the right by the specified amount.
     * 
     * @param amount Number of positions to shift.
     */
    public void shiftR(int amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Shift amount must be non-negative.");
        }
        data = Arrays.copyOf(data, data.length + amount);
    }

    /**
     * Adds another binary number to this one.
     * 
     * @param aBinaryNumber The binary number to be added.
     */
    public void add(BinaryNumber aBinaryNumber) {
        if (this.getLength() != aBinaryNumber.getLength()) {
            System.out.println("Binary numbers must be of the same length.");
            return;
        }
        int carry = 0;
        for (int i = 0; i < data.length; i++) {
            int sum = data[i] + aBinaryNumber.getDigit(i) + carry;
            data[i] = sum % 2;
            carry = sum / 2;
        }
        if (carry == 1) {
            overflow = true;
            data = Arrays.copyOf(data, data.length + 1);
            data[data.length - 1] = 1;
        }
    }

    /**
     * Clears the overflow flag.
     */
    public void clearOverflow() {
        overflow = false;
    }

    /**
     * Returns the string representation of the binary number.
     * 
     * @return Binary number as a string.
     */
    @Override
    public String toString() {
        if (overflow) {
            return "Overflow";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = data.length - 1; i >= 0; i--) {
            sb.append(data[i]);
        }
        return sb.toString();
    }

    /**
     * Main function for testing BinaryNumber operations.
     * 
     * @param args Command-line arguments.
     */
    public static void main(String[] args) {
        BinaryNumber num1 = new BinaryNumber("01101");
        BinaryNumber num2 = new BinaryNumber("00111");
        System.out.println("Binary Number 1: " + num1);
        System.out.println("Binary Number 2: " + num2);
        num1.add(num2);
        System.out.println("Sum: " + num1);
        System.out.println("Decimal Value: " + num1.toDecimal());
    }
}
