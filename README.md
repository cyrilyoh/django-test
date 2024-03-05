# Car Database - Django

## Introduction

This Car Management System aims to streamline the process of managing cars and their associated data.

## Dependencies

- Django==4.2.10

## Steps to run the app using bash script

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
2. Run the bash script
   ```bash
   ./start.sh

## Steps to run the app without using bash script

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
2. **Install reuirements.txt**
    ```bash
   pip install -r requirements.txt
3. **Navigate to project folder**
    ```bash
   cd fts
4. **Apply Migrations**
    ```bash
   python manage.py runserver
5. **Load dummy data**
    ```bash
   python manage.py loaddata dummy_data.json
6. **Run the app**
    ```bash
   python manage.py runserver


Bootstrap 4 is utilized as CDN. Therefore, for an improved user interface, ensure the internet connectivity when running the project.