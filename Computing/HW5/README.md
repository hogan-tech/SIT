# HW5 README
Hogan Lin hlin31@stevens.edu
I pledge my honor that I have abided by the Stevens Honor System.

## 1. Are there any known bugs or issues with your program?
No known bugs or issues.

## 2. Describe an issue that you encountered and resolved when writing and testing your code.
Issue:
While writing `pequod()`, my initial regex pattern `r'white whale'` only matched exact occurrences, ignoring extra spaces. This caused mismatches when the text contained variations like "white   whale".

Solution:
I modified the regex to `r'white\s*whale'` to allow flexible spacing between words, ensuring correct matches.
