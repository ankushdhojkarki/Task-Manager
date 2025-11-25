# Task Manager 📅

**Task Manager** is a secure, role-based web application built with **Django** for managing and tracking tasks assigned to a team. It enforces distinct views and permissions for administrative staff and standard employees, providing a complete, ready-to-use solution for small team workflow management.

## ✨ Features

This project implements robust role-based access control (RBAC) and full CRUD functionality based on user roles:

### 👑 Admin Features (Full CRUD)
* **Complete Control:** Admins can **Create, Read, Update, and Delete** any task in the system.
* **Task Assignment:** Admins are responsible for **Assigning** tasks to specific employees.
* **Security:** Admin views are protected using the custom `@admin_required` decorator.
* **Validation:** Includes **Deadline Validation** to prevent setting task deadlines to past dates.

### 💼 Employee Features (View & Update)
* **Restricted View:** Employees can **only see tasks** that are explicitly assigned to them.
* **Status Update:** Employees can update the status of their assigned tasks (`Pending`, `In Progress`, `Completed`).
* **Security:** Employee task access is restricted in the views using Django's query filtering (`assigned_to=request.user`).

## 🛠️ Technology Stack

* **Backend Framework:** Django (Python)
* **Database:** SQLite (default for development)
* **Authentication:** Django built-in `django.contrib.auth`

---

## 🚀 Setup and Installation

Follow these steps to get the Task Manager project running locally.

### Prerequisites

* Python 3.8+
* Git

### 1. Clone the Repository

```bash
git clone [https://github.com/YourUsername/Task-Manager.git](https://github.com/YourUsername/Task-Manager.git)
cd Task-Manager

2. Create and Activate Virtual EnvironmentBash# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On Linux/macOS:
source venv/bin/activate
3. Install DependenciesInstall the necessary Python packages:Bashpip install Django
(If you used a requirements.txt file, use pip install -r requirements.txt)4. Database SetupRun migrations to create the database tables, including the Task model and the default Django authentication tables.Bashpython manage.py migrate
5. Create Users (Admin & Employee)You need at least one Superuser (Admin) and one regular user (Employee) for testing:A. Create Superuser (Admin)Bashpython manage.py createsuperuser
# Follow prompts to create username (e.g., 'admin') and password.
B. Create Regular User (Employee)Bashpython manage.py createsuperuser # Yes, use this to create the regular user
# Follow prompts to create username (e.g., 'test_employee') and password.
6. Assign Roles (Groups)You must now use the Django Admin interface to assign the roles:Start the server: python manage.py runserverGo to http://127.0.0.1:8000/admin and log in with your Superuser.Navigate to the Groups section.Create two new groups: Admin and Employee.Navigate to the Users section.Edit the users you created:Add the Admin group to the Superuser (admin).Add the Employee group to the regular user (test_employee).7. Run the ApplicationStart the development server:Bashpython manage.py runserver
You can now access the application at http://127.0.0.1:8000/accounts/login/.🔒 Testing and WorkflowUserLogin URLExpected RedirectionKey FunctionalityAdmin/accounts/login// (Admin Dashboard)Full CRUD on all tasks.Employee/accounts/login// (Employee Dashboard)View only assigned tasks; Update task status.
