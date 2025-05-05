# CS 515-A Final Project - Strava Lite
# Author: Hogan Lin
# Date: Apr 20th 2025
# Github: https://github.com/hogan-tech/CS-515-Final


import requests

BASE_URL = "http://127.0.0.1:5000"


def test_register_user() -> str:
    """Test user registration (POST /user)"""
    response = requests.post(
        f"{BASE_URL}/user", json={"name": "Hogan", "age": 28})
    assert response.status_code == 200
    user = response.json()
    print("Register User:", user)
    return user["id"]


def test_get_user(user_id: str) -> None:
    """Test retrieving user info (GET /user/<user_id>)"""
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == 200
    print("Get User:", response.json())


def test_list_users() -> None:
    """Test listing all users (GET /users)"""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    print("List Users:", response.json())


def test_remove_user(user_id: str) -> None:
    """Test deleting a user (DELETE /user/<user_id>)"""
    response = requests.delete(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == 200
    print(f"Remove User {user_id}: Success")


def test_add_workout(user_id: str) -> None:
    """Test adding a workout (PUT /workouts/<user_id>)"""
    workout = {"date": "2025-04-24", "time": "30min", "distance": "5km"}
    response = requests.put(f"{BASE_URL}/workouts/{user_id}", json=workout)
    assert response.status_code == 200
    print("Add Workout:", response.json())


def test_list_workouts(user_id: str) -> None:
    """Test listing workouts (GET /workouts/<user_id>)"""
    response = requests.get(f"{BASE_URL}/workouts/{user_id}")
    assert response.status_code == 200
    print("List Workouts:", response.json())


def test_follow_friend(user_id: str, follow_id: str) -> None:
    """Test following a friend (PUT /follow-list/<user_id>)"""
    response = requests.put(
        f"{BASE_URL}/follow-list/{user_id}", json={"follow_id": follow_id})
    assert response.status_code == 200
    print("Follow Friend:", response.json())


def test_show_friend_workouts(user_id: str, follow_id: str) -> None:
    """Test viewing a followed friend's workouts (GET /follow-list/<user_id>/<follow_id>)"""
    response = requests.get(f"{BASE_URL}/follow-list/{user_id}/{follow_id}")
    if response.status_code == 403:
        print("Show Friend Workouts: Forbidden (403)")
    else:
        assert response.status_code == 200
        print("Show Friend Workouts:", response.json())


if __name__ == "__main__":
    # Create two users
    user1 = test_register_user()
    user2 = test_register_user()

    # Verify user operations
    test_get_user(user1)
    test_list_users()

    # Add and verify workouts for user1
    test_add_workout(user1)
    test_list_workouts(user1)

    # Follow user2 from user1 and view their workouts
    test_follow_friend(user1, user2)
    test_show_friend_workouts(user1, user2)

    # Clean up: remove both users
    test_remove_user(user1)
    test_remove_user(user2)
