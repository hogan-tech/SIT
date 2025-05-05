# Strava Lite - CS 515-A Final Project

Hogan Lin  
hlin31@stevens.edu  
[GitHub Repository](https://github.com/hogan-tech/CS-515-Final)

## Description

**Strava Lite** is a lightweight RESTful API server designed to help users **track their runs** and **connect with friends**. Built using **Flask** and **Flask-RESTful**, this project simulates core functionalities of fitness apps like Strava, including:

- User management (registration, retrieval, deletion)
- Workout tracking (adding, listing workouts)
- Social features (following friends, viewing their workouts)

This project adheres to the specifications of the **CS 515-A Final Project** and implements both **core features** and **extra credit social features**.

---

## Features

- **User Registration**: Register new users with a unique UUID and store basic information (name, age).
- **User Retrieval**: Fetch user information via UUID.
- **User Deletion**: Remove a user by UUID.
- **Workout Tracking**: Add and list workouts with details such as date, time, and distance.
- **Friend Following (Extra Credit)**: Users can follow friends and view their workouts if permission is granted.
- **Error Handling**: Standardized HTTP status codes (200, 400, 404, 403) for consistent responses.

---

## API Overview

| Endpoint                             | Method | Description                      | Status Codes  |
| ------------------------------------ | ------ | -------------------------------- | ------------- |
| `/user`                              | POST   | Register a new user              | 200, 400      |
| `/user/<user_id>`                    | GET    | Retrieve user details            | 200, 404      |
| `/user/<user_id>`                    | DELETE | Remove a user                    | 200, 404      |
| `/users`                             | GET    | List all users                   | 200           |
| `/workouts/<user_id>`                | PUT    | Add a workout for a user         | 200, 400, 404 |
| `/workouts/<user_id>`                | GET    | List workouts for a user         | 200, 404      |
| `/follow-list/<user_id>`             | PUT    | Follow another user              | 200, 400, 404 |
| `/follow-list/<user_id>/<follow_id>` | GET    | View workouts of a followed user | 200, 403, 404 |

---

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/hogan-tech/CS-515-Final.git
   cd CS-515-Final
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed, then:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   ```bash
   python app.py
   ```
   The server will start on `http://127.0.0.1:5000`.

---

## Testing Instructions

The project includes an automated **test script** (`test.py`) that validates all key endpoints:

```bash
python test.py
```

The test flow includes:

- User creation and retrieval
- Adding workouts
- Following a friend and viewing their workouts
- Cleaning up (deleting users)

Ensure the server is running before executing tests.


---

## Dependencies

- **Flask==2.3.2**: Web framework for Python.
- **Flask-RESTful==0.3.9**: Extension for building REST APIs easily with Flask.
- **requests==2.32.3**: For testing API endpoints in `test.py`.

---

## Acknowledgments

- Based on the **CS 515-A Flask lecture materials**.
- Inspired by core functionalities of fitness tracking applications.
