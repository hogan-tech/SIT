# Author: Hogan Lin
# Date: Sept 23th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Get the two random from 1 ~ 10 and 11 ~ 20, use for loop to calculate the odd sum.


import random

num1 = random.randint(1, 10)
num2 = random.randint(11, 20)

# Initialize sum variable
oddSum = 0

# For loop to calculate sum of odd numbers
for i in range(num1, num2 + 1):
    # Check if the number is odd
    if i % 2 != 0:  
        oddSum += i

print(
    f"The first random number was {num1}, the second random number was {num2}, and the sum is {oddSum}.")
