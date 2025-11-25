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
git clone https://github.com/YourUsername/Task-Manager.git
cd Task-Manager

### 2. Create and Activate Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On Linux/macOS:
source venv/bin/activate

### 3. Install Dependencies

Install the necessary Python packages:

```bash
pip install Django

### 4. Database Setup

Run migrations to create the database tables, including the Task model and the default Django authentication tables.

```bash
python manage.py migrate

### 5. Create Users (Admin & Employee)

You need at least one Superuser (Admin) and one regular user (Employee) for testing:

#### A. Create Superuser (Admin)

```bash
python manage.py createsuperuser
# Follow prompts to create username (e.g., 'admin') and password.

#### B. Create Regular User (Employee)

```bash
python manage.py createsuperuser # Yes, use this to create the regular user
# Follow prompts to create username (e.g., 'test_employee') and password.

### 6. Assign Roles (Groups)

You must now use the Django Admin interface to assign the roles:

1.  Start the server: 
    ```bash
    python manage.py runserver
    ```
2.  Go to `http://127.0.0.1:8000/admin` and log in with your Superuser.
3.  Navigate to the **Groups** section.
4.  Create two new groups: **`Admin`** and **`Employee`**.
5.  Navigate to the **Users** section.
6.  Edit the users you created:
    * Add the **`Admin`** group to the Superuser (`admin`).
    * Add the **`Employee`** group to the regular user (`test_employee`).

### 7. Run the Application

Start the development server:

```bash
python manage.py runserver
You can now access the application at `http://127.0.0.1:8000/accounts/login/`.

## 🔒 Testing and Workflow

| User | Login URL | Expected Redirection | Key Functionality |
| :--- | :--- | :--- | :--- |
| **Admin** | `/accounts/login/` | `/` (Admin Dashboard) | Full CRUD on all tasks. |
| **Employee** | `/accounts/login/` | `/` (Employee Dashboard) | View only assigned tasks; Update task status. |

## 📄 File Structure Highlights

| File/Path | Purpose |
| :--- | :--- |
| `tasks/models.py` | Defines the `Task` model and `STATUS_CHOICES`. |
| `accounts/models.py` | Contains helper functions (`is_admin`, `is_employee`) for role checking. |
| `accounts/decorators.py` | Defines the custom `@admin_required` decorator. |
| `tasks/views.py` | Contains all view logic, including role-based `home_view`, Admin CRUD, and Employee Update. |
| `tasks/urls.py` | Routes all custom paths, using the `/dashboard/tasks/` prefix for Admin views. |
| `templates/registration/login.html` | Custom login page template. |
| `tasks/templates/tasks/` | Contains all dashboard and task management templates. |

