# Author: Hogan Lin
# Date: Sept 23th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Use if-elif-else to handle the condition to show the roman value, and use integer to get the input

num = int(
    input("Please enter a number between 1 and 9 to convert to a roman numeral: "))
# I
if num == 1:
    print("The Roman numeral for 1 is: \u2160")  
# II
elif num == 2:
    print("The Roman numeral for 2 is: \u2161")  
# III
elif num == 3:
    print("The Roman numeral for 3 is: \u2162")  
# IV
elif num == 4:
    print("The Roman numeral for 4 is: \u2163")  
# V
elif num == 5:
    print("The Roman numeral for 5 is: \u2164")  
# VI
elif num == 6:
    print("The Roman numeral for 6 is: \u2165")  
# VII
elif num == 7:
    print("The Roman numeral for 7 is: \u2166")  
# VIII
elif num == 8:
    print("The Roman numeral for 8 is: \u2167")  
# IX
elif num == 9:
    print("The Roman numeral for 9 is: \u2168")
else:
    print(num, "is outside the allowed range of 1-9.")
