/**
 * Author: Hogan Lin
 * Date: February 27, 2025
 * Github: https://github.com/hogan-tech/SIT/tree/main/DSA
 * Description: 
 * PairInt represents a coordinate pair (x, y) for a cell in the maze.
 * Used to trace and return paths.
 */

package Maze;

import java.util.ArrayList;
import java.util.Stack;

/**
 * Class that solves maze problems with backtracking.
 * 
 * @author Koffman and Wolfgang
 **/
public class Maze implements GridColors {

    /** The maze */
    private TwoDimGrid maze;

    public Maze(TwoDimGrid m) {
        maze = m;
    }

    /** Wrapper method. */
    public boolean findMazePath() {
        return findMazePath(0, 0); // (0, 0) is the start point.
    }

    /**
     * Attempts to find a path through point (x, y).
     * 
     * @pre Possible path cells are in BACKGROUND color;
     *      barrier cells are in ABNORMAL color.
     * @post If a path is found, all cells on it are set to the
     *       PATH color; all cells that were visited but are
     *       not on the path are in the TEMPORARY color.
     * @param x The x-coordinate of current point
     * @param y The y-coordinate of current point
     * @return If a path through (x, y) is found, true;
     *         otherwise, false
     */

    /**
     * Problem 1: Recursive backtracking to find a path.
     * This method explores all possible directions from the current (x, y) cell
     * and tries to reach the bottom-right cell (exit) following only NON_BACKGROUND
     * cells.
     * It uses color marking to track visited cells and valid paths.
     *
     * @param x the column index
     * @param y the row index
     * @return true if a path to the exit is found; false otherwise
     */
    public boolean findMazePath(int x, int y) {
        // Check if the cell is out of maze bounds
        if (x < 0 || y < 0 || x >= maze.getNCols() || y >= maze.getNRows())
            return false;

        // Check if the cell is not a valid path cell
        if (!maze.getColor(x, y).equals(NON_BACKGROUND))
            return false;

        // If it's the exit cell, color it as PATH and return true
        if (x == maze.getNCols() - 1 && y == maze.getNRows() - 1) {
            maze.recolor(x, y, PATH);
            return true;
        }

        // Assume current cell is part of a valid path
        maze.recolor(x, y, PATH);

        // Recursively try all 4 neighboring cells
        if (findMazePath(x + 1, y) || findMazePath(x - 1, y) ||
                findMazePath(x, y + 1) || findMazePath(x, y - 1)) {
            return true;
        }

        // If no path found, mark cell as TEMPORARY and backtrack
        maze.recolor(x, y, TEMPORARY);
        return false;
    }

    /**
     * Problem 2: Find all possible paths from (x, y) to the exit cell.
     * Uses a helper method with stack-based trace to backtrack through all valid
     * paths.
     *
     * @param x the starting column index
     * @param y the starting row index
     * @return a list of all valid paths, each represented as a list of PairInt
     */
    public ArrayList<ArrayList<PairInt>> findAllMazePaths(int x, int y) {
        ArrayList<ArrayList<PairInt>> result = new ArrayList<>();
        Stack<PairInt> trace = new Stack<>();
        findMazePathStackBased(x, y, result, trace);
        if (result.isEmpty()) {
            result.add(new ArrayList<>()); // Return [[]] if no paths found
        }
        return result;
    }

    /**
     * Helper method for Problem 2: recursively explores all paths.
     * Uses backtracking to explore each direction and stores each successful path.
     *
     * @param x      current column index
     * @param y      current row index
     * @param result list to store all successful paths
     * @param trace  stack to trace the current path being explored
     */
    private void findMazePathStackBased(int x, int y,
            ArrayList<ArrayList<PairInt>> result, Stack<PairInt> trace) {

        // Check if current cell is out of bounds
        if (x < 0 || y < 0 || x >= maze.getNCols() || y >= maze.getNRows())
            return;

        // Only proceed if cell is NON_BACKGROUND (i.e., valid path cell)
        if (!maze.getColor(x, y).equals(NON_BACKGROUND))
            return;

        // Add current cell to path trace
        trace.push(new PairInt(x, y));
        maze.recolor(x, y, PATH); // Temporarily mark as visited

        // If current cell is the exit, store a copy of the path
        if (x == maze.getNCols() - 1 && y == maze.getNRows() - 1) {
            result.add(new ArrayList<>(trace));
        } else {
            // Explore all 4 directions
            findMazePathStackBased(x + 1, y, result, trace);
            findMazePathStackBased(x - 1, y, result, trace);
            findMazePathStackBased(x, y + 1, result, trace);
            findMazePathStackBased(x, y - 1, result, trace);
        }

        // Backtrack: remove current cell from trace and restore its color
        trace.pop();
        maze.recolor(x, y, NON_BACKGROUND);
    }

    /**
     * Problem 3: Return the shortest path from all valid paths.
     * Utilizes findAllMazePaths to compare and select the path with minimum length.
     *
     * @param x starting column index
     * @param y starting row index
     * @return the shortest path as a list of PairInt; empty if no path exists
     */
    public ArrayList<PairInt> findMazePathMin(int x, int y) {
        ArrayList<ArrayList<PairInt>> allPaths = findAllMazePaths(x, y);
        ArrayList<PairInt> minPath = new ArrayList<>();
        int minLength = Integer.MAX_VALUE;

        for (ArrayList<PairInt> path : allPaths) {
            if (!path.isEmpty() && path.size() < minLength) {
                minLength = path.size();
                minPath = path;
            }
        }
        return minPath;
    }

    /* <exercise chapter="5" section="6" type="programming" number="2"> */
    public void resetTemp() {
        maze.recolor(TEMPORARY, BACKGROUND);
    }
    /* </exercise> */

    /* <exercise chapter="5" section="6" type="programming" number="3"> */
    public void restore() {
        resetTemp();
        maze.recolor(PATH, BACKGROUND);
        maze.recolor(NON_BACKGROUND, BACKGROUND);
    }
    /* </exercise> */
}
/* </listing> */
