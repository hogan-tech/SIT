
/**
 * Author: Hogan Lin
 * Date: Apr 23th 2025
 * Github: https://github.com/hogan-tech/SIT
 * Description: This program implements the Anagrams class which computes the list of words
 *              in a given dictionary that has the most number of anagrams.
 */
import java.io.*;
import java.util.*;

public class Anagrams {

    // Array of the first 26 prime numbers corresponding to each letter a-z
    private final Integer[] primes = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
        47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    };

    // Maps each letter a-z to a unique prime number
    private final Map<Character, Integer> letterTable;

    // Maps the hash code (product of primes) to a list of words (anagrams)
    private Map<Long, ArrayList<String>> anagramTable;

    /**
     * Default constructor for Anagrams class. Initializes the letterTable and
     * anagramTable.
     */
    public Anagrams() {
        letterTable = new HashMap<>();
        // Initialize the letter to prime mapping
        anagramTable = new HashMap<>();
        // Initialize the anagram hash table
        buildLetterTable();
        // Populate letterTable with a-z mapped to primes
    }

    /**
     * Constructor for testing or specific initialization purposes. Allows
     * passing in pre-defined anagramTable and letterTable.
     *
     * @param anagramTable Predefined anagramTable
     * @param letterTable Predefined letterTable
     */
    public Anagrams(Map<Long, ArrayList<String>> anagramTable, Map<Character, Integer> letterTable) {
        this.anagramTable = anagramTable;
        this.letterTable = letterTable;
    }

    /**
     * Builds the letterTable mapping each letter 'a'-'z' to a corresponding
     * prime number. This is crucial for ensuring that different permutations
     * (anagrams) of the same letters produce the same hash code.
     */
    private void buildLetterTable() {
        char c = 'a';
        for (Integer prime : primes) {
            letterTable.put(c, prime);
            // Assign each letter its corresponding prime number
            c++;
        }
    }

    /**
     * Computes the hash code for a given word using the product of prime
     * numbers corresponding to each letter in the word. This ensures all
     * anagrams of a word yield the same hash code.
     *
     * @param s The input word.
     * @return The computed hash code as a Long.
     */
    private Long myHashCode(String s) {
        long hash = 1;
        for (char c : s.toCharArray()) {
            // Multiply the primes for each character
            hash *= letterTable.get(c);
        }
        return hash;
    }

    /**
     * Adds a word to the anagramTable by computing its hash code and appending
     * it to the corresponding list.
     *
     * @param s The word to add.
     */
    private void addWord(String s) {
        // Compute the hash for the word
        Long hash = myHashCode(s);
        ArrayList<String> anagrams = anagramTable.getOrDefault(hash, new ArrayList<>());
        anagrams.add(s);
        anagramTable.put(hash, anagrams);
    }

    /**
     * Processes a file containing words (one word per line), reads each word,
     * and adds it to the anagramTable.
     *
     * @param s The filename.
     * @throws IOException If an I/O error occurs during file reading.
     */
    private void processFile(String s) throws IOException {
        FileInputStream fstream = new FileInputStream(s);
        try (BufferedReader br = new BufferedReader(new InputStreamReader(fstream))) {
            String strLine;
            while ((strLine = br.readLine()) != null) {
                // Add each word to the anagram table
                this.addWord(strLine.trim().toLowerCase());
            }
        }
    }

    /**
     * Retrieves a list of entries (hash code and corresponding word list) that
     * contain the maximum number of anagrams. This method scans the entire
     * anagramTable to find the entries with the longest anagram lists.
     *
     * @return A list of Map.Entry containing hash codes and corresponding
     * anagram lists.
     */
    private ArrayList<Map.Entry<Long, ArrayList<String>>> getMaxEntries() {
        ArrayList<Map.Entry<Long, ArrayList<String>>> maxEntries = new ArrayList<>();
        int maxSize = 0;
        for (Map.Entry<Long, ArrayList<String>> entry : anagramTable.entrySet()) {
            int size = entry.getValue().size();
            if (size > maxSize) {
                // Update maximum size
                maxSize = size;
                maxEntries.clear();
                maxEntries.add(entry);
            } else if (size == maxSize) {
                // Add entries with equal max size
                maxEntries.add(entry);
            }
        }
        return maxEntries;
    }

    /**
     * Main method for testing the Anagrams class. Reads a dictionary file,
     * builds the anagramTable, finds the words with the most anagrams, and
     * prints the results along with the execution time.
     *
     * @param args Command-line arguments.
     */
    @SuppressWarnings("CallToPrintStackTrace")
    public static void main(String[] args) {
        Anagrams a = new Anagrams();
        final long startTime = System.nanoTime();
        try {
            // Process the dictionary file
            a.processFile("words_alpha.txt");
        } catch (IOException e1) {
            e1.printStackTrace();
            return;
        }
        ArrayList<Map.Entry<Long, ArrayList<String>>> maxEntries = a.getMaxEntries();
        final long estimatedTime = System.nanoTime() - startTime;
        // Convert time to seconds
        final double seconds = ((double) estimatedTime / 1_000_000_000);
        System.out.println("Elapsed Time : " + seconds);
        for (Map.Entry<Long, ArrayList<String>> entry : maxEntries) {
            System.out.println("Key of max anagrams : " + entry.getKey());
            System.out.println("List of max anagrams : " + entry.getValue());
            System.out.println("Length of list of max anagrams : " + entry.getValue().size());
        }
    }

    /**
     * Getter for the anagramTable.
     *
     * @return The current anagramTable.
     */
    public Map<Long, ArrayList<String>> getAnagramTable() {
        return anagramTable;
    }

    /**
     * Setter for the anagramTable.
     *
     * @param anagramTable The new anagramTable to set.
     */
    public void setAnagramTable(Map<Long, ArrayList<String>> anagramTable) {
        this.anagramTable = anagramTable;
    }
}
