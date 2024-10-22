# BucketList API
A bucket list is a list of things that one has not done before but wants to do before dying.This is an API for an online bucket list using the Django Rest Framework.This API creates a foundation of an app that will help you track things you want to do before you die. Users can create, view, update, and delete bucket list items.

## Features

- User registration and authentication (using JWT).
- Create, update, and delete bucket list items.
- View all bucket lists for the authenticated user.
- Token-based authentication for API access.
  
## Technologies Used

- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For building the API.
  
## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8+
- Git

### Steps

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/Zamzamke/bucketlist_project.git
    cd bucketlist_project
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply the migrations to set up the database:
    ```
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```
    python manage.py runserver
    ```

7. Access the API at `http://127.0.0.1:8000/api/`.


## API Endpoints

| Method | Endpoint               | Description                           |
|--------|------------------------|---------------------------------------|
| POST   | `/api/token/`           | Obtain JWT token                      |
| POST   | `/api/token/refresh/`   | Refresh the JWT token                 
|POST   | `/api-auth/login/`       | Login with username and password |
| GET    | `/api/bucketlists/`     | List all bucket lists (authenticated) |
| POST   | `/api/bucketlists/`     | Create a new bucket list              |
| GET    | `/api/bucketlists/<id>/`| Retrieve a specific bucket list       |
| PUT    | `/api/bucketlists/<id>/`| Update a specific bucket list         |
| DELETE | `/api/bucketlists/<id>/`| Delete a specific bucket list         |



