# Author: Hogan Lin
# Date: Sept 23th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Use random module and get random integer from 0 ~ 450, use if elif else to check every condition.

import random

distance = random.randint(0, 450)

# Determine the outcome based on the distance and display the appropriate message
if distance > 400:
    print(f"The ball flew {distance} feet and the batter scored a home run! That's one point for our team!")
elif 135 <= distance <= 400:
    print(f"The ball flew {distance} feet and the batter made it to third base!")
elif 10 <= distance <= 134:
    print(f"The ball flew {distance} feet and the batter made it to second base!")
elif 1 <= distance <= 9:
    print(f"The ball flew {distance} feet because the batter bunted, and made it to first base!")
else:  # distance == 0
    print("The batter has made a strike! Oh no!")