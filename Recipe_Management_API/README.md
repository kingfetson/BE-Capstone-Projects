
# 🍽️ Recipe Management API

A production-ready RESTful API built with Django and Django REST Framework for comprehensive recipe management, featuring categories, ingredients, and user authentication.

**Developed as part of the ALX Backend Capstone Project**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6+-green.svg)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.15+-red.svg)](https://www.django-rest-framework.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-orange.svg)](https://jwt.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

### 📦 Core Functionality
- **Relational Data Models** with proper database relationships
- **Full CRUD Operations** via Django REST Framework ViewSets
- **Custom Permission Classes** for granular access control
- **Through Model Relationships** for complex many-to-many connections

### 🔧 Advanced Capabilities
- **JWT Authentication** using SimpleJWT for secure API access
- **Smart Filtering** by category, ingredients, and custom parameters
- **Global Search** across recipe titles, descriptions, and ingredients
- **Pagination** with configurable page sizes
- **Comprehensive Test Suite** covering all API endpoints

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Django 6+ & Django REST Framework |
| **Authentication** | SimpleJWT |
| **Database** | SQLite (development) |
| **Filtering** | django-filter |
| **Testing** | Django TestCase |
| **Python** | 3.12+ |

---

## 📊 Database Schema

### Models and Relationships

```
Category
  ├── name (CharField)
  └── (One-to-Many with Recipe)

Ingredient
  └── name (CharField)

Recipe
  ├── title (CharField)
  ├── description (TextField)
  ├── instructions (TextField)
  ├── prep_time (IntegerField)
  ├── cook_time (IntegerField)
  ├── servings (IntegerField)
  ├── created_at (DateTimeField)
  ├── author (ForeignKey → User)
  ├── category (ForeignKey → Category)
  └── ingredients (ManyToMany through RecipeIngredient)

RecipeIngredient (Through Model)
  ├── recipe (ForeignKey → Recipe)
  ├── ingredient (ForeignKey → Ingredient)
  └── quantity (CharField)
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.12 or higher
- pip package manager
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Recipe_Management_API.git
   cd Recipe_Management_API
   ```

2. **Set up virtual environment if you're using Codespace**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python manage.py migrate
   ```

5. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```

6. **Launch development server**
   ```bash
   python manage.py runserver
   ```

Access the API at: `http://127.0.0.1:8000/api/`

---

## 🔐 Authentication System

### Obtaining Tokens

**Get Access Token**
```http
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

**Response**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Authentication
Include the access token in request headers:
```http
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

**Refresh Token**
```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "your_refresh_token"
}
```

---

## 🔍 API Usage Examples

### Filtering Recipes
```http
GET /api/recipes/?category=1
```

### Searching
```http
GET /api/recipes/?search=chicken
```
*Searches across titles, descriptions, category names, and ingredient names*

### Paginated Response
```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/recipes/?page=3",
  "previous": "http://127.0.0.1:8000/api/recipes/?page=1",
  "results": [...]
}
```
*Default page size: 5 items*

---

## 📋 Complete API Reference

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/categories/` | List all categories | Public |
| POST | `/api/categories/` | Create category | Required |
| GET | `/api/ingredients/` | List all ingredients | Public |
| POST | `/api/ingredients/` | Create ingredient | Required |
| GET | `/api/recipes/` | List recipes (paginated) | Public |
| POST | `/api/recipes/` | Create recipe | Required |
| GET | `/api/recipes/{id}/` | Retrieve recipe details | Public |
| PUT | `/api/recipes/{id}/` | Update recipe | Owner only |
| DELETE | `/api/recipes/{id}/` | Delete recipe | Owner only |
| POST | `/api/token/` | Obtain JWT tokens | Public |
| POST | `/api/token/refresh/` | Refresh access token | Public |

---

## 🔒 Permission Matrix

| Action | Unauthenticated | Authenticated | Recipe Owner |
|--------|-----------------|---------------|--------------|
| View Recipes | ✅ | ✅ | ✅ |
| Create Recipe | ❌ | ✅ | ✅ |
| Update Recipe | ❌ | ❌ | ✅ |
| Delete Recipe | ❌ | ❌ | ✅ |
| View Categories | ✅ | ✅ | ✅ |
| Create Category | ❌ | ✅ | ✅ |

---

## 🧪 Testing

Run the complete test suite:
```bash
python manage.py test
```

**Test Coverage Includes:**
- JWT authentication flow
- Permission enforcement
- Recipe CRUD operations
- Search functionality
- Filtering mechanisms
- Pagination structure
- Edge cases and error handling

---

## 📁 Project Structure

```
Recipe_Management_API/
├── recipes/                      # Main application
│   ├── models.py                 # Database models
│   ├── serializers.py            # API serializers
│   ├── views.py                  # View logic
│   ├── permissions.py            # Custom permissions
│   ├── tests.py                  # Test suite
│   └── urls.py                   # App routes
│
├── Recipe_Management_API/         # Project configuration
│   ├── settings.py               # Django settings
│   └── urls.py                   # Main URL config
│
├── manage.py                      # Django CLI
├── requirements.txt               # Dependencies
└── README.md                      # Documentation
```

---

## 📈 Development Progress

| Phase | Status | Features |
|-------|--------|----------|
| **Week 1** | ✅ Complete | Core models, CRUD operations, permissions |
| **Week 2** | ✅ Complete | JWT auth, filtering, search, pagination, testing |
| **Week 3** | 🚀 Ready | Deployment, optimization, documentation |

---

## 🎯 Learning Outcomes

This project demonstrates proficiency in:

- **RESTful Architecture** - Designing intuitive API endpoints
- **Database Modeling** - Implementing complex relationships
- **Security** - JWT authentication and permission layers
- **Query Optimization** - Efficient filtering and search
- **Testing** - Comprehensive test coverage
- **Documentation** - Clear, professional API documentation

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact & Support

- **Project Link**: [[https://github.com/kingfetson/BE-Capstone-Projects/Recipe_Management_API](https://github.com/kingfetson/BE-Capstone-Projects/Recipe_Management_API)
- **Issues**: [https://github.com/kingfetson/BE-Capstone-Projects/Recipe_Management_API/issues](https://github.com/kingfetson/BE-Capstone-Projects/Recipe_Management_API/issues)

---

<p align="center">
  <sub>Built with ❤️ as part of the ALX Backend Engineering Program</sub>
</p>
