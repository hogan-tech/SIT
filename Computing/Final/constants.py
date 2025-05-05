# CS 515-A Final Project - Strava Lite
# Author: Hogan Lin
# Date: Apr 20th 2025
# Github: https://github.com/hogan-tech/CS-515-Final


# Success
STATUS_OK = 200
# Missing or invalid request data
STATUS_BAD_REQUEST = 400
# Resource not found
STATUS_NOT_FOUND = 404
# Action not allowed (e.g., not following a user)
STATUS_FORBIDDEN = 403

# Single user operations
USER_ROUTE = "/user"
# List all users
USERS_ROUTE = "/users"
# Workout operations
WORKOUTS_ROUTE = "/workouts"
# Follow-related operations
FOLLOW_ROUTE = "/follow-list"
