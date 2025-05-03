#!/bin/bash
# Script to run the Flask API with Gunicorn for production

# Activate virtual environment
source myenv/Scripts/activate

# Run Gunicorn server binding to all interfaces on port 8000
gunicorn -w 4 -b 0.0.0.0:8000 Resturant_Project.flask_api:app
