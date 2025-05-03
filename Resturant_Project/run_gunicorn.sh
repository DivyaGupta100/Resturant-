#!/bin/bash
gunicorn -c gunicorn_config.py flask_api:app
