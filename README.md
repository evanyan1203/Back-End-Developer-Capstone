# 🍋 Little Lemon Restaurant API (Capstone Project)

This project is the **Back-End Developer Capstone** for the Meta Back-End Developer Professional Certificate.  
It is a full-featured RESTful API built with **Django REST Framework**, demonstrating database modeling, authentication, and API design for a restaurant reservation system.

---

## 🚀 Features
- User authentication with **Django Token Authentication**
- CRUD API for managing:
  - Menu items
  - Table bookings
- Role-based access control (Staff vs Customer)
- Integrated database using SQLite (can be extended to PostgreSQL)
- Automated testing with Django's TestCase
- Admin panel for menu & booking management

---

## 🛠️ Tech Stack
- **Python** 3.10+
- **Django** 4.x
- **Django REST Framework**
- **SQLite** (default) / **PostgreSQL**
- **Git & GitHub**

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/evanyan1203/Back-End-Developer-Capstone.git
cd Back-End-Developer-Capstone

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run the server
python manage.py migrate
python manage.py runserver
