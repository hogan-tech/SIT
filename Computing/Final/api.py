# CS 515-A Final Project - Strava Lite
# Author: Hogan Lin
# Date: Apr 20th 2025
# Github: https://github.com/hogan-tech/CS-515-Final

import uuid
from typing import Dict, Tuple, Optional, Any
from flask import request
from flask_restful import Resource
from constants import (
    STATUS_OK,
    STATUS_BAD_REQUEST,
    STATUS_NOT_FOUND,
    STATUS_FORBIDDEN
)


# A user object
User = Dict[str, Any]
# A workout object
Workout = Dict[str, str]
# Flask response structure
Response = Tuple[Dict[str, Any], int]


# Stores users indexed by their unique UUID string
users: Dict[str, User] = {}   


def get_user_or_404(user_id: str) -> Tuple[Optional[User], Optional[Response]]:
    """
    Helper to retrieve a user by UUID. Returns:
    - (user object, None) if found
    - (None, error response) if not found (404)
    
    :param user_id: Unique identifier for the user
    :return: Tuple of (User or None, Response or None)
    """
    if user_id not in users:
        return None, ({}, STATUS_NOT_FOUND)
    return users[user_id], None


class RegisterUser(Resource):
    def post(self) -> Response:
        """
        Registers a new user in the system.
        - POST /user
        - Request: { "name": str, "age": int }
        - Response: { "id": str, "name": str, "age": int }
        """
        data: Optional[Dict[str, Any]] = request.get_json()
        if not data or "name" not in data:  # Validate 'name' presence
            return {}, STATUS_BAD_REQUEST

        # Generate a unique UUID for the user
        user_id: str = str(uuid.uuid4())
        users[user_id] = {
            "id": user_id,
            "name": data["name"],
            "age": data.get("age", None),  # 'age' is optional
            "workouts": [],                # Initialize empty workout list
            "following": set()             # Initialize empty following set
        }
        user: User = users[user_id]
        return {"id": user["id"], "name": user["name"], "age": user["age"]}, STATUS_OK


class GetUser(Resource):
    def get(self, user_id: str) -> Response:
        """
        Retrieves a user's details.
        - GET /user/<user_id>
        - Request: {}
        - Response: { "id": str, "name": str, "age": int }
        """
        user, error = get_user_or_404(user_id)
        if error:
            return error  # Return 404 if user not found
        return {"id": user["id"], "name": user["name"], "age": user["age"]}, STATUS_OK


class RemoveUser(Resource):
    def delete(self, user_id: str) -> Response:
        """
        Removes a user from the system.
        - DELETE /user/<user_id>
        - Request: {}
        - Response: {}
        """
        _, error = get_user_or_404(user_id)
        if error:
            return error  # Return 404 if user not found
        del users[user_id]  # Delete user
        return {}, STATUS_OK


class ListUsers(Resource):
    def get(self) -> Response:
        """
        Lists all users in the system.
        - GET /users
        - Request: {}
        - Response: { "users": [{ "id": str, "name": str, "age": int }] }
        """
        return {
            "users": [
                {"id": u["id"], "name": u["name"], "age": u["age"]}
                for u in users.values()
            ]
        }, STATUS_OK


class AddWorkout(Resource):
    def put(self, user_id: str) -> Response:
        """
        Adds a workout to a specific user.
        - PUT /workouts/<user_id>
        - Request: { "date": str, "time": str, "distance": str }
        - Response: { "date": str, "time": str, "distance": str }
        """
        user, error = get_user_or_404(user_id)
        if error:
            return error

        data: Optional[Dict[str, Any]] = request.get_json()
        if not data or not all(k in data for k in ("date", "time", "distance")):
            return {}, STATUS_BAD_REQUEST  # Validate workout fields

        workout: Workout = {
            "date": data["date"],
            "time": data["time"],
            "distance": data["distance"]
        }
        user["workouts"].append(workout)  # Add workout to user's list
        return workout, STATUS_OK


class ListWorkouts(Resource):
    def get(self, user_id: str) -> Response:
        """
        Lists all workouts for a specific user.
        - GET /workouts/<user_id>
        - Request: {}
        - Response: { "workouts": [{ "date": str, "time": str, "distance": str }] }
        """
        user, error = get_user_or_404(user_id)
        if error:
            return error
        return {"workouts": user["workouts"]}, STATUS_OK


class FollowFriend(Resource):
    def put(self, user_id: str) -> Response:
        """
        Allows a user to follow another user.
        - PUT /follow-list/<user_id>
        - Request: { "follow_id": str }
        - Response: { "following": [str] }
        """
        user, error = get_user_or_404(user_id)
        if error:
            return error

        data: Optional[Dict[str, Any]] = request.get_json()
        follow_id: Optional[str] = data.get("follow_id") if data else None
        if not follow_id:
            return {}, STATUS_BAD_REQUEST  # Validate follow_id

        _, follow_error = get_user_or_404(follow_id)
        if follow_error:
            return follow_error  # Ensure followee exists

        user["following"].add(follow_id)  # Add followee to user's following set
        return {"following": list(user["following"])}, STATUS_OK


class ShowFriendWorkouts(Resource):
    def get(self, user_id: str, follow_id: str) -> Response:
        """
        Shows workouts of a followed friend.
        - GET /follow-list/<user_id>/<follow_id>
        - Request: {}
        - Response: { "workouts": [{ "date": str, "time": str, "distance": str }] }
        
        Returns:
        - 404 if either user does not exist
        - 403 if user_id does not follow follow_id
        """
        user, error = get_user_or_404(user_id)
        if error:
            return error

        follow_user, follow_error = get_user_or_404(follow_id)
        if follow_error:
            return follow_error

        if follow_id not in user["following"]:
            return {}, STATUS_FORBIDDEN  # Not following this user with 403 status code

        return {"workouts": follow_user["workouts"]}, STATUS_OK
