# CS 515-A Final Project - Strava Lite
# Author: Hogan Lin
# Date: Apr 20th 2025
# Github: https://github.com/hogan-tech/CS-515-Final

from constants import USER_ROUTE, USERS_ROUTE, WORKOUTS_ROUTE, FOLLOW_ROUTE
from api import (
    RegisterUser, GetUser, RemoveUser, ListUsers,
    AddWorkout, ListWorkouts, FollowFriend, ShowFriendWorkouts
)

def initialize_routes(api):
    # User routes
    api.add_resource(RegisterUser, USER_ROUTE)  # POST /user
    api.add_resource(GetUser, f"{USER_ROUTE}/<string:user_id>")  # GET /user/<user_id>
    api.add_resource(RemoveUser, f"{USER_ROUTE}/<string:user_id>")  # DELETE /user/<user_id>
    api.add_resource(ListUsers, USERS_ROUTE)  # GET /users

    # Workout routes
    api.add_resource(AddWorkout, f"{WORKOUTS_ROUTE}/<string:user_id>")  # PUT /workouts/<user_id>
    api.add_resource(ListWorkouts, f"{WORKOUTS_ROUTE}/<string:user_id>")  # GET /workouts/<user_id>

    # Follow routes
    api.add_resource(FollowFriend, f"{FOLLOW_ROUTE}/<string:user_id>")  # PUT /follow-list/<user_id>
    api.add_resource(ShowFriendWorkouts, f"{FOLLOW_ROUTE}/<string:user_id>/<string:follow_id>")  # GET /follow-list/<user_id>/<follow_id>
