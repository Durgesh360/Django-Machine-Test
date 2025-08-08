# Django-Machine-Test

# Django REST API for Client & Project Management

This is a Django REST Framework (DRF) based API system for managing Clients, Projects, and Users. Users can only access the projects they are assigned to. Admins can create clients and assign projects to specific users.

---

## 📦 Features

- Projects are assigned to users
- Each user sees only their assigned projects
- Clients can have multiple projects
- MySQL database support

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

### 2. Create & Activate a Virtual Environment

### 3. Install Requirements

pip install -r requirements.txt

### 4. Configure MySQL Database

### 5. Run Migrations

python manage.py makemigrations
python manage.py migrate

### 6. Create Superuser

python manage.py createsuperuser

### 7. Run Development Server

python manage.py runserver

---

##  For Postman

### 1. Login at: `http://127.0.0.1:8000/admin/`

### 2. Get the auth-token using the /token/ endpoint

Pass the { "username": "" , "password" : ""} in body and Retrieve the Token

### 3. Pass the token inside the header for every request 

As Authorization : Token <token_id>

---

* Login at: `http://127.0.0.1:8000/admin/`
* Only authenticated users can create or view projects.

---

## 🔗 Key API Endpoints

| Method | Endpoint                 | Description                                       |
| ------ | ------------------------ | ------------------------------------------------- |
| GET    | `/token/`                | View the Auth-token for specific user             |
| GET    | `/clients/`              | View all client details                           |
| POST   | `/clients/:id/`          | Create new clients                                |
| GET    | `/projects/`             | View all projects assigned to logged-in user      |
| POST   | `/clients/:id/projects/` | Create a project for a client with assigned users |
| GET    | `/clients/:id/`          | View client details and its projects              |
| PUT    | `/clients/:id/`          | Update client details                             |
| PATCH  | `/clients/:id/`          | Partially Update client details                   |
| DELETE | `/clients/:id/`          | Delete the specific client                        |

---
