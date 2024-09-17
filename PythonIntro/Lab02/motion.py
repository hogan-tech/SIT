# Author: Hogan Lin
# Date: Sep 15, 2024
# Description: Given a duration of time, this program computes
# the velocity, average velocity, and displacement of an object.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Initialize the radius:
time = 10.0

# Calculate the properties of the object:
velocity = 0
averageVelocity = 0
displacement = 0

velocity = initialVelocity + acceleration * time
averageVelocity = initialVelocity + 0.5 * acceleration * time
displacement = initialVelocity * time + 0.5 * acceleration * time * time

# Print the results:
print("time =", time)
print("velocity".ljust(18), "=", velocity)
print("average velocity".ljust(18), "=", averageVelocity)
print("displacement".ljust(18), "=", displacement)

# I use string.ljust() to align the string.
# Learn from this stack overflow post
# https://stackoverflow.com/questions/57156557/how-can-i-change-align-columns-vertically-in-python