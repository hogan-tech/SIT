# HW README
Hogan Lin `hlin31@stevens.edu`
I pledge my honor that I have abided by the Stevens Honor System.

## 1. Are there any known bugs or issues with your program?
No known bugs or issues.

## 2. Describe an issue that you encountered and resolved when writing and testing your code.
### Issue:
When implementing `letters.py`, I initially used `input().lower()` but forgot to strip whitespace. This led to errors when users accidentally entered spaces before or after their letters.

### Solution:
I fixed this by adding `.strip()` to ensure the input was correctly processed.
