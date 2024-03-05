# Car Management Application - Django

## Introduction

The Car Management Application is a web-based system developed using Django, a high-level Python web framework. This application is designed to help users manage car-related data such as brands, colours, and ownership records. It provides functionalities for adding, viewing, editing, and deleting car-related information.

## Features:

**Brand Management:**

Users can create new car brands.
Brand information includes the brand name, the number of new cars, used cars, and total cars associated with each brand.
Brands can be viewed and managed through the application interface.

**Colour Management:**

- Authorized users can add new colours for cars.
- Colour information includes the colour name and can be viewed and managed through the application interface.

**Car Management:**

- Authorized users can add new cars to the system, providing details such as brand, model, colour, condition (new/used), etc.
- Existing cars can be edited or deleted as needed.
- Cars can be filtered based on various criteria such as brand, model, and condition.

**Ownership Record Management:**

- Authorized users can add ownership records for cars, specifying the duration for which each car was owned by a particular owner.
- The application ensures that overlapping ownership periods are not allowed.
- Ownership records can be edited or deleted as required.

**User Registration and Management:**

- New users can register through the application.
- User registration requires admin approval before the account becomes active.
- Admin can view a list of registered users and approve or delete user accounts as needed.

## Technologies Used:

**Django Framework:** Used for backend development, providing a robust structure for building web applications.
**HTML/CSS/JavaScript:** Used for frontend development, providing the user interface and interactivity.
**Bootstrap:** Used for styling and layout of the application's frontend components.
**SQLite Database:** Used for storing application data, providing a lightweight and easy-to-use database solution.
**Font Awesome:** Used for adding icons to enhance the visual appeal of the application.

## Dependencies

- Django==4.2.10
- django-filter==23.5

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
5. **Create super user**
    ```bash
   python manage.py createsuperuser
6. **Load dummy data**
    ```bash
   python manage.py loaddata dummy_data.json
7. **Run the app**
    ```bash
   python manage.py runserver


## Conclusion:

The Car Management Application provides a comprehensive solution for managing car-related data efficiently. With features for brand, colour, car, and ownership record management, along with user registration and management functionalities, it offers a user-friendly interface for users to interact with car-related information effectively.

## Application Screenshot

![Cars](https://github.com/cyrilyoh/django-test/fts/static/img/cars_ss.png)