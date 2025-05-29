# MyIoTApp: IoT Dashboard and Services Platform

## Overview
MyIoTApp is a Django-based web application designed to manage and showcase IoT projects. Developed by Md Shaifulla Zibon, a student of Electrical and Electronic Engineering (EEE) at the European University of Bangladesh, this platform serves as a practice and demonstration tool for IoT solutions. It includes features such as an admin dashboard for monitoring devices, user management, and service pages for smart home automation, agriculture solutions, and more.

The application is divided into several Django apps:
- **admins**: Admin dashboard for managing IoT devices and users.
- **dashboard**: Core dashboard functionality.
- **home**: Public-facing pages like About Us and Services.
- **users**: User dashboard for viewing device statuses.

## Features
- **Admin Dashboard**: Monitor active and inactive IoT devices, view analytics, and manage users.
- **User Dashboard**: Displays device statistics (active, inactive, total devices) and recent user activity.
- **About Us Page**: Information about the developer and the purpose of the project.
- **Services Page**: Showcases IoT services like smart home automation, smart agriculture, surveillance, and custom IoT solutions.
- **Responsive Design**: Includes a sidebar with navigation, a dark/light mode toggle, and reminders section.
- **Static Assets**: Custom CSS, JavaScript, and images for styling and functionality.

## Project Structure
```
myiotapp/
├── iotapp/
│   ├── admins/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── dashboard/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── active_link.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── home/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── iotapp/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── users/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   │   ├── css/
│   │   │   └── dashboard.css
│   │   ├── js/
│   │   │   └── dashboard.js
│   │   └── images/
│   │       ├── logo.png
│   │       ├── Md-Shaifulla-Zibon.jpg
│   │       ├── zibon.jpg
│   │       ├── profile-2.jpg
│   │       ├── profile-3.jpg
│   │       ├── profile-4.jpg
│   │       └── plus.png
│   ├── templates/
│   │   ├── admins/
│   │   │   └── base_dashboard.html
│   │   ├── base/
│   │   ├── dashboard/
│   │   ├── home/
│   │   │   ├── about.html
│   │   │   ├── base.html
│   │   │   └── services.html
│   │   ├── sales/
│   │   └── users/
│   │       ├── base_dashboard.html
│   │       └── users_dashboard.html
│   ├── db.sqlite3
│   └── manage.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Prerequisites
- Python 3.8 or higher
- Django 4.x
- A virtual environment (recommended)
- SQLite (default database, can be replaced with PostgreSQL or MySQL)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/zibontaroka/MyIoTApp.git
   cd MyIoTApp
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```

6. **Create a Superuser (Admin Account)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - Access the app at `http://127.0.0.1:8000/`.
   - Admin dashboard: `http://127.0.0.1:8000/admin/` (login with superuser credentials).

## Usage
- **Home Page**: Visit the root URL (`/`) to explore the "About Us" and "Services" pages.
- **Admin Dashboard**: Navigate to `/admins/` (requires login) to monitor IoT devices and manage users.
- **User Dashboard**: Access `/users/` (requires login) to view device statistics and recent activity.
- **Dark/Light Mode**: Toggle between dark and light themes using the button in the top-right corner of the dashboard.
- **Reminders**: View and add reminders in the right sidebar of the dashboard.

## Technologies Used
- **Django**: Backend framework for handling requests, routing, and templating.
- **HTML/CSS/JavaScript**: Frontend for responsive design and interactivity.
- **Material Icons**: For icons used in the dashboard.
- **SQLite**: Default database for development.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Developed by Md Shaifulla Zibon as part of an academic project.
- Thanks to the Django community for excellent documentation and resources.
- Inspired by the need to explore and demonstrate IoT technologies.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 🧠 Author  
**Md Shaifulla Zibon**  
Electrical and Electronics Engineering  
European University of Bangladesh  
GitHub: [@zibontaroka](https://github.com/zibontaroka)
