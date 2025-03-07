# HW Sorting Algorithms
Hogan Lin hlin31@stevens.edu
I pledge my honor that I have abided by the Stevens Honor System.

## 1. Are there any known bugs or issues with your program?
No known bugs or issues.

## 2. Describe an issue that you encountered and resolved when writing and testing your code.
Issue:
Initially, I forgot to reset the counter between sorting runs, leading to incorrect values in summary.txt. The comparisons and swaps accumulated across tests, making the data unreliable.

Solution:
I fixed this by ensuring that a fresh `Counter` object is created for each sorting test case, preventing data leakage between runs.
