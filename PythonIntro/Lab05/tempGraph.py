# Author: Hogan Lin
# Date: Oct 6th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program generates random hourly temperatures for three cities over a 12-hour
#              period. It then plots these temperatures using Matplotlib, displaying the temperature trends for
#              each city on the same graph. The graph includes labeled axes, a title, and a legend to distinguish
#              between the cities.

"""
This function generates random hourly temperatures for three cities, plots the data, 
and displays a line graph comparing the temperature trends.
"""
import matplotlib.pyplot as plt
import random

time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

city1 = "Denton"
city2 = "Allentown"
city3 = "Raritan"

city1List = []
city2List = []
city3List = []

for i in range(12):
    city1List.append(random.randint(10, 30))
    city2List.append(random.randint(10, 30))
    city3List.append(random.randint(10, 30))

plt.plot(time, city1List, label=city1)
plt.plot(time, city2List, label=city2)
plt.plot(time, city3List, label=city3)

plt.title("Hourly Temperatures")
plt.xlabel("Hours")
plt.ylabel("Temperatures")

plt.legend([city1, city2, city3])

plt.show()
