# 🎬 Movie Review API — Backend Capstone Project

![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/DRF-3.14.0-red?style=for-the-badge&logo=django)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=json-web-tokens)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-4169E1?style=for-the-badge&logo=postgresql)
![Heroku](https://img.shields.io/badge/Heroku-Deployed-430098?style=for-the-badge&logo=heroku)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Swagger](https://img.shields.io/badge/Swagger-Documented-85EA2D?style=for-the-badge&logo=swagger)

> *A comprehensive backend solution for managing movie reviews, built with Django REST Framework*

## 📋 Table of Contents

- [🎬 Movie Review API — Backend Capstone Project](#-movie-review-api--backend-capstone-project)
  - [📋 Table of Contents](#-table-of-contents)
  - [📌 Overview](#-overview)
  - [🎯 Key Features](#-key-features)
  - [🏗️ Project Architecture](#️-project-architecture)
  - [📊 Database Schema](#-database-schema)
  - [🔧 Tech Stack](#-tech-stack)
  - [📚 API Documentation](#-api-documentation)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Environment Variables](#environment-variables)
    - [Running the Project](#running-the-project)
  - [📖 API Usage Examples](#-api-usage-examples)
  - [🧪 Testing](#-testing)
  - [📈 Project Status](#-project-status)
  - - [✅ Completed Features](#-completed-features)
  - [🚧 In Progress](#-in-progress)
  - [🎯 Stretch Goals (Optional)](#-stretch-goals-optional)
  - [🤝 Contributing](#-contributing)
  - [📝 License](#-license)
  - [👨‍💻 Author](#-author)
  - [🙏 Acknowledgments](#-acknowledgments)

---

## 📌 Overview

The **Movie Review API** is a production-ready backend application built with **Django** and **Django REST Framework**. This project serves as my **Backend Capstone Project**, demonstrating the practical application of backend development concepts including database design, API architecture, authentication, and deployment.

Users can **create, manage, and discover movie reviews** while the system enforces proper authentication, authorization, and data validation following RESTful best practices.

**Live Demo:** [https://your-movie-review-api.herokuapp.com](https://your-movie-review-api.herokuapp.com)  
**API Documentation:** [https://your-movie-review-api.herokuapp.com/swagger](https://your-movie-review-api.herokuapp.com/swagger)

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **🔐 JWT Authentication** | Secure token-based authentication system |
| **📝 Full CRUD Operations** | Create, read, update, and delete reviews |
| **👤 User Management** | Registration, login, profile management |
| **🔍 Advanced Filtering** | Search by movie title, filter by rating |
| **📄 Pagination** | Efficient handling of large datasets |
| **📊 Sorting** | Sort reviews by date, rating, or popularity |
| **🔒 Permission Controls** | Users can only modify their own reviews |
| **📚 API Documentation** | Interactive Swagger/ReDoc documentation |
| **⚡ Optimized Queries** | Database indexing for fast searches |

---

## 🏗️ Project Architecture

```
movie_review_api/
├── apps/
│   ├── users/                 # User management app
│   │   ├── models.py          # Custom User model
│   │   ├── serializers.py     # User data serialization
│   │   ├── views.py           # Authentication endpoints
│   │   └── permissions.py     # Custom permissions
│   └── reviews/               # Review management app
│       ├── models.py          # Review model with validation
│       ├── serializers.py     # Review data serialization
│       ├── views.py           # CRUD endpoints
│       └── pagination.py      # Custom pagination classes
├── movie_review_api/           # Project configuration
│   ├── settings.py            # Environment-based settings
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # WSGI configuration
├── static/                     # Static files
├── media/                      # User uploaded files
└── requirements.txt            # Project dependencies
```

---

## 📊 Database Schema

```mermaid
erDiagram
    User ||--o{ Review : writes
    Review {
        int id PK
        string movie_title
        text review_content
        int rating
        datetime created_date
        datetime updated_date
        int user_id FK
    }
    User {
        int id PK
        string email UK
        string username
        string password
        string bio
        string avatar
        datetime date_joined
    }
```

**Key Relationships:**
- One user can write many reviews
- One review belongs to exactly one user
- Unique constraint: One review per user per movie

---

## 🔧 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend Framework** | Django 4.2.7, Django REST Framework 3.14.0 |
| **Database** | SQLite (dev), PostgreSQL 13 (prod) |
| **Authentication** | JWT (djangorestframework-simplejwt) |
| **API Documentation** | Swagger UI, ReDoc (drf-yasg) |
| **Deployment** | Heroku, Gunicorn, WhiteNoise |
| **Development** | Python 3.11, pip, virtualenv |
| **Testing** | Django TestCase, Postman |
| **Version Control** | Git, GitHub |
| **Security** | CORS headers, environment variables |

---

## 📚 API Documentation

Interactive API documentation is available at:
- **Swagger UI:** `/swagger/`
- **ReDoc:** `/redoc/`

### Core Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | ❌ |
| POST | `/api/auth/login/` | Login user | ❌ |
| GET | `/api/auth/profile/` | Get user profile | ✅ |
| GET | `/api/reviews/` | List all reviews | ❌ |
| POST | `/api/reviews/` | Create new review | ✅ |
| GET | `/api/reviews/{id}/` | Get review details | ❌ |
| PUT | `/api/reviews/{id}/` | Update review | ✅ (Owner) |
| DELETE | `/api/reviews/{id}/` | Delete review | ✅ (Owner) |
| GET | `/api/reviews/movie/{title}/` | Get movie reviews | ❌ |
| GET | `/api/reviews/top-rated/` | Get top-rated reviews | ❌ |

### Query Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `?search=` | Search by movie title or content | `?search=inception` |
| `?rating_min=` | Minimum rating filter | `?rating_min=4` |
| `?rating_max=` | Maximum rating filter | `?rating_max=5` |
| `?ordering=` | Sort results | `?ordering=-created_date` |
| `?page=` | Page number | `?page=2` |
| `?page_size=` | Items per page | `?page_size=20` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git
- PostgreSQL (optional, for production)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/movie-review-api.git
cd movie-review-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

# For PostgreSQL (production)
# DATABASE_URL=postgresql://user:password@localhost:5432/movie_review_db
```

### Running the Project

```bash
# Start the development server
python manage.py runserver

# Access the API
open http://localhost:8000/api/

# View API documentation
open http://localhost:8000/swagger/
```

---

## 📖 API Usage Examples

### 1. User Registration

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "movie_fan",
    "email": "fan@example.com",
    "password": "SecurePass123",
    "password2": "SecurePass123"
  }'
```

**Response:**
```json
{
  "user": {
    "id": 1,
    "username": "movie_fan",
    "email": "fan@example.com",
    "bio": "",
    "date_joined": "2024-01-15T10:30:00Z"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. Create a Review

```bash
curl -X POST http://localhost:8000/api/reviews/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "movie_title": "Inception",
    "review_content": "A mind-bending masterpiece!",
    "rating": 5
  }'
```

### 3. Filter Reviews

```bash
# Get 4+ star reviews for Inception
curl "http://localhost:8000/api/reviews/?movie_title=Inception&rating_min=4&ordering=-created_date"
```

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.reviews.tests
python manage.py test apps.users.tests

# Run with coverage
coverage run --source='apps' manage.py test
coverage report
coverage html  # Generate HTML report
```

---

## 📈 Project Status

### ✅ Completed Features

- [x] Project initialization and configuration
- [x] Custom user model implementation
- [x] Review model with validation
- [x] JWT authentication system
- [x] CRUD operations for reviews
- [x] User registration and login
- [x] Permission controls (owner-only edits)
- [x] Search and filtering capabilities
- [x] Pagination implementation
- [x] API documentation with Swagger
- [x] Database indexing for performance

### 🚧 In Progress

- [ ] Unit tests coverage
- [ ] Production deployment
- [ ] Rate limiting implementation
- [ ] Email verification

### 🎯 Stretch Goals (Optional)

- [ ] TMDB API integration for movie details
- [ ] Review "liking" functionality
- [ ] User profiles with avatar uploads
- [ ] Comment system on reviews
- [ ] Movie recommendation engine

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows PEP 8 guidelines and includes appropriate tests.

---
# Create new venv
python -m venv venv
source venv/bin/activate


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Fetson Kinyua**
- GitHub: [@kingfetson](https://github.com/kingfetson)
- Portfolio: [fetson.dev](https://fetson.dev)

---

## 🙏 Acknowledgments

- Django and Django REST Framework communities
- My mentors and peers for their valuable feedback
- The open-source community for amazing tools and libraries

---

<div align="center">
  
**⭐ Star this repo if you find it helpful! ⭐**

[Report Bug](https://github.com/kingfetson/movie-review-api/issues) · [Request Feature](https://github.com/kingfetson/movie-review-api/issues)

</div>