# CS 515-A Final Project - Strava Lite
# Author: Hogan Lin
# Date: Apr 20th 2025
# Github: https://github.com/hogan-tech/CS-515-Final

from flask import Flask
from flask_restful import Api
from routes import initialize_routes  # Import route setup function

# Create Flask app and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

# Initialize all API routes
initialize_routes(api)

# Run server (localhost:5000)
if __name__ == "__main__":
    app.run(debug=True)
