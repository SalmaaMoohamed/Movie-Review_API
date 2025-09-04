# Movie-Review_API
My ALX Capstone Project from ALX Back-End Development Program

## Features
- User authentication (register, login, logout)
- User profile management
- Movie database with genres
- Review creation and management
- Rating system (1-5 stars)
- Search and filter functionality
- Responsive design
- Admin interface
## Overview
## Setup Instructions
A comprehensive movie review platform built with Django and Django REST Framework. Users can register, browse movies, write reviews, and rate films on a 5-star scale.
### 1. Clone the repository
```bash
git clone <repository-url>
cd Movie-Review_API
```
### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create superuser (optional)
```bash
python manage.py createsuperuser
```
### 6. Run the development server
```bash
python manage.py runserver
```
### 7. Access the application
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
- API endpoints: http://127.0.0.1:8000/api/
## Project Structure
```
Movie-Review_API/
├── Movies/                 # Main project settings
├── Accounts/              # User authentication app
├── Reviews/               # Movie reviews app
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS)
├── media/                # User uploaded files
├── venv/                 # Virtual environment
└── requirements.txt      # Python dependencies
```
## API Endpoints
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create a new review
- `GET /api/reviews/{id}/` - Get specific review
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review
## Color Scheme
- Primary: #042E58 (Dark Blue)
- Secondary: #2DE787 (Green)
- Accent: #7261DD (Purple)
- Warning: #DDB100 (Gold)
## Technologies Used
- Django 5.2.4
- Django REST Framework
- SQLite (default database)
- HTML5, CSS3, JavaScript
- Bootstrap-inspired responsive design