# HW1 README
Hogan Lin hlin31@stevens.edu
I pledge my honor that I have abided by the Stevens Honor System.

## 1. What is the difference between print and return in Python?

`print` outputs a value to the console, while `return` gives a value back to the function caller.
Example:

```python
def example():
    print("Hello")  # Just prints "Hello"
    return "Hello"  # Returns "Hello" for further use
```

## 2. Are there any known bugs or issues with your program?
No known bugs or issues.

## 3. Describe an issue that you encountered and resolved when writing and testing your code.
Issue:
Initially, in temp.py, I forgot to convert the user input to a float, which caused a TypeError when performing arithmetic operations. The input was being treated as a string, which prevented the Fahrenheit-to-Celsius conversion.

Solution:
I fixed this issue by explicitly converting the input using float(input()), ensuring that arithmetic operations could be performed correctly.