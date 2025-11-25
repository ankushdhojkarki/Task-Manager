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

### 2. Create and Activate Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On Linux/macOS:
source venv/bin/activate
