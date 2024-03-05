#!/bin/bash

# Check for env
if [ ! -d "env" ]; then
python3 -m venv env
fi

# Activate virtual environment
source env/bin/activate
pip install -r requirements.txt

# Navigate to project directory
cd fts
# Apply migrations
python manage.py migrate
# Create super user
python manage.py createsuperuser
# Populate the DB with dummy data
python manage.py loaddata dummy_data.json
# Run server
python manage.py runserver

