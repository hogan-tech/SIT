/**
 * Author: Hogan Lin
 * Date: February 27, 2025
 * Github: https://github.com/hogan-tech/SIT/tree/main/DSA
 * Description: 
 * PairInt represents a coordinate pair (x, y) for a cell in the maze.
 * Used to trace and return paths.
 */

package Maze;

public class PairInt {
    private int x; // X-coordinate of the cell
    private int y; // Y-coordinate of the cell

    /**
     * Constructor to create a pair with given coordinates.
     * 
     * @param x the x-coordinate
     * @param y the y-coordinate
     */
    public PairInt(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Returns the x-coordinate.
     * 
     * @return x value
     */
    public int getX() {
        return x;
    }

    /**
     * Returns the y-coordinate.
     * 
     * @return y value
     */
    public int getY() {
        return y;
    }

    /**
     * Sets the x-coordinate.
     * 
     * @param x new x value
     */
    public void setX(int x) {
        this.x = x;
    }

    /**
     * Sets the y-coordinate.
     * 
     * @param y new y value
     */
    public void setY(int y) {
        this.y = y;
    }

    /**
     * Returns a deep copy of this PairInt.
     * 
     * @return new PairInt with the same coordinates
     */
    public PairInt copy() {
        return new PairInt(x, y);
    }

    /**
     * Compares this pair with another object for equality.
     * 
     * @param obj the object to compare
     * @return true if obj is a PairInt with same x and y
     */
    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof PairInt))
            return false;
        PairInt other = (PairInt) obj;
        return this.x == other.x && this.y == other.y;
    }

    /**
     * Returns string representation of the coordinate.
     * 
     * @return string in format (x, y)
     */
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
