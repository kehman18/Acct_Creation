# Account Creation System

## Project Overview

This project is an **account creation and management system** built using **Flask** and **SQLAlchemy**. It provides user authentication features such as **sign-up**, **login**, and **logout**, with a database storing user information. The project is structured to be modular, with separate routes for authentication, views, and database models.

## Project Structure

```bash
acct_creation/
│
└───registration/
    └───organizational_project/   # Root folder for the project
        ├───static/               # Static assets (JS, CSS)
        │   └───index.js          # Front-end interactivity
        ├───templates/            # HTML templates for the web pages
        │   ├───home.html
        │   ├───sign_up.html
        │   ├───login.html
        │   └───base.html
        ├───__init__.py           # Flask app factory and database initialization
        ├───auth.py               # Authentication routes (login, sign-up, logout)
        ├───main.py               # Entry point of the application
        ├───models.py             # SQLAlchemy models (User, Notes)
        └───views.py              # View routes (home, dashboard)
```

## Features

- **User Registration**: Users can create an account by providing an email, name, and password.
- **User Login**: Registered users can log in using their email and password.
- **Logout**: Users can securely log out of their accounts.
- **SQLAlchemy Integration**: User data is stored in a SQLite database using SQLAlchemy.
- **Templating**: HTML templates for rendering web pages (using Flask's `render_template`).

## Installation

### Prerequisites

- **Python 3.6+**: Make sure Python is installed.
- **pip**: Install `pip` if it's not already installed.

### Steps to Install

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/kehman18/acct_creation.git
   cd acct_creation/registration/organizational_project
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv        # For Windows: py -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the necessary Python packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Initialize the SQLite database using the `create_database()` function from `__init__.py`:

   ```bash
   python
   >>> from organizational_project import create_app
   >>> app = create_app()
   >>> with app.app_context():
   >>>     from organizational_project import db
   >>>     db.create_all()
   ```

5. **Run the Application**:
   Start the Flask development server:

   ```bash
   flask --app main run --debug --port 5000   #you can choose to use any other port.
   ```

6. **Open in Browser**:
   Navigate to `http://127.0.0.1:5000` in your browser to view the application.

## Usage

### Register a New User

1. Navigate to the **Sign Up** page at `http://127.0.0.1:5000/sign-up`.
2. Fill in your **email**, **name**, and **password** to create an account.

### Log In

1. Go to the **Login** page at `http://127.0.0.1:5000/login`.
2. Enter your registered **email** and **password** to log in.

### Log Out

1. After logging in, you can securely log out by visiting `http://127.0.0.1:5000/logout`.

## File Descriptions

- **main.py**: Entry point of the application, runs the Flask server.
- **auth.py**: Handles routes related to user authentication, including sign-up, login, and logout.
- **views.py**: Handles general routes such as the home page and dashboard.
- **models.py**: Defines the database models using SQLAlchemy, including the `User` and `Note` models.
- \***\*init**.py\*\*: Initializes the Flask application, sets up the database, and registers blueprints.
- **static/index.js**: Contains any JavaScript for front-end interactivity.
- **templates/**: HTML templates for rendering pages such as home, login, sign-up, and logout.

## Requirements

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Jinja2

Install them with:

```bash
pip install flask flask-sqlalchemy flask-login jinja2
```

## Future Features (Optional)

- Password reset functionality.
- User profile management.
- Enhanced security features such as two-factor authentication.

## Contact

For any issues or inquiries, feel free to reach out:

- **Email**: kehindeadekola96@gmail.com
- **Portfolio**: [https://rehobothjnr.pythonanywhere.com]
- **LinkedIn**: [https://www.linkedin.com/in/adekola-p/]
