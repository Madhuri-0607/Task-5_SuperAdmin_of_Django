# 🛍️ SuperAdmin of Django – Product Store
## 📌 Project Overview

This project is built with Django as part of an internship task.
It extends the previous Task 2 (FileHub / File Upload system) and adds SuperAdmin features to manage the application.

The SuperAdmin has higher control over the system compared to normal admin users, enabling advanced monitoring and management.

## 🚀 Features

✅ User authentication (login/register)

✅ Role-based access (User, Admin, SuperAdmin)

✅ Product filtering by price and size

✅ Dynamic price range filter

✅ SuperAdmin dashboard for full control

✅ Ability to manage users, admins, and products

✅ Extended from Task2 while preserving original functionality

## 🛠️ Tech Stack

Backend: Django (Python)

Database: SQLite (default) / PostgreSQL (optional)

Frontend: Django Templates (HTML, CSS, Bootstrap)

## 📂 Project Structure  
Task5/  
│── manage.py  
│── db.sqlite3  
│── requirements.txt  
│── shop/               # Django app (models, views, urls)  
│── templates/          # HTML files  
│── static/             # CSS, JS, Images  
│── Task2 code base preserved  

## ⚡ Installation & Setup

### Clone the repository:

git clone https://github.com/your-username/Task5-SuperAdmin.git
cd Task5


### Create a virtual environment and activate it:

python -m venv venv  
source venv/bin/activate    # On Mac/Linux  
venv\Scripts\activate       # On Windows  


## Install dependencies:

pip install -r requirements.txt


## Run migrations:

python manage.py makemigrations  
python manage.py migrate  


## Create SuperAdmin user:

python manage.py createsuperuser


## Start the server:

python manage.py runserver


### Open in browser:
👉 http://127.0.0.1:8000

### 🔑 Default Credentials 

SuperAdmin Username: admin  

Password: admin123


## 📸 Screenshots
🏬 [Product Store](screenshots/product-store.png) – Filter Products

⚙️ [Django Admin](screenshots/admin-panel.png) – SuperAdmin Panel

📊 [Manage Products](screenshots/manage-products.png) – SuperAdmin View
