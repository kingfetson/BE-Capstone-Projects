🍽️ Recipe Management API

A fully functional RESTful API built with Django and Django REST Framework for managing recipes, categories, and ingredients.

This project was developed as part of the ALX Backend Capstone Project.

🚀 Features
✅ Week 1 – Core API Development

Custom Django app: recipes

Models:

Category

Ingredient

Recipe

RecipeIngredient (through table)

Model relationships:

One-to-Many (Recipe → Category)

Many-to-Many (Recipe ↔ Ingredient)

ForeignKey (Recipe → User)

CRUD operations using ModelViewSet

API routing using DefaultRouter

Custom permissions (IsOwnerOrReadOnly)

✅ Week 2 – Advanced API Features

🔐 JWT Authentication (SimpleJWT)

🔎 Filtering (by category)

🔍 Search (title, description, category, ingredients)

📄 Pagination

🧪 API Tests

🔒 Permission controls

🛠️ Tech Stack

Python 3.12+

Django 6+

Django REST Framework

djangorestframework-simplejwt

django-filter

SQLite (Development)

📂 Project Structure
Recipe_Management_API/
│
├── recipes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── tests.py
│   └── urls.py
│
├── Recipe_Management_API/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── README.md
🧱 Database Models
Category

name

Ingredient

name

Recipe

title

description

instructions

prep_time

cook_time

servings

created_at

author (ForeignKey → User)

category (ForeignKey → Category)

ingredients (ManyToMany → Ingredient through RecipeIngredient)

🔐 Authentication (JWT)

Authentication is implemented using SimpleJWT.

Obtain Token
POST /api/token/

Example body:

{
  "username": "your_username",
  "password": "your_password"
}

Response:

{
  "refresh": "refresh_token",
  "access": "access_token"
}
Use Token

Include in request header:

Authorization: Bearer <access_token>
🔎 Filtering

Filter recipes by category ID:

GET /api/recipes/?category=1
🔍 Search

Search across:

title

description

category name

ingredient name

Example:

GET /api/recipes/?search=chicken
📄 Pagination

Pagination is enabled using PageNumberPagination.

Example response:

{
  "count": 20,
  "next": "http://127.0.0.1:8000/api/recipes/?page=2",
  "previous": null,
  "results": [...]
}

Default page size: 5

🔒 Permissions

IsAuthenticatedOrReadOnly

Custom IsOwnerOrReadOnly

Rules:

Anyone can view recipes

Only authenticated users can create recipes

Only the recipe owner can update/delete

🧪 Running Tests

Run:

python manage.py test

Tests cover:

Authentication

Recipe creation

Permission enforcement

Filtering

Search

Pagination structure

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd Recipe_Management_API
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Visit:

http://127.0.0.1:8000/api/
📡 API Endpoints
Method	Endpoint	Description
GET	/api/categories/	List categories
POST	/api/categories/	Create category
GET	/api/ingredients/	List ingredients
POST	/api/ingredients/	Create ingredient
GET	/api/recipes/	List recipes
POST	/api/recipes/	Create recipe
GET	/api/recipes/{id}/	Retrieve recipe
PUT	/api/recipes/{id}/	Update recipe
DELETE	/api/recipes/{id}/	Delete recipe
POST	/api/token/	Obtain JWT token
POST	/api/token/refresh/	Refresh token
📈 Learning Outcomes

Through Weeks 1 & 2, this project demonstrates:

Building relational models in Django

Implementing RESTful APIs with DRF

Applying authentication & permissions

Implementing search, filtering & pagination

Writing API tests

Structuring production-ready backend code

📌 Project Status

✅ Week 1 Complete
✅ Week 2 Complete
🚀 Ready for Week 3 (Advanced features & production deployment)

If you'd like, I can now:

🔥 Upgrade this into a GitHub-polished README with badges

📄 Generate a submission summary for ALX

🚀 Help you start Week 3 professionally

🌍 Add deployment instructions (Render / Railway / Docker)

Your backend portfolio is becoming very strong 💪

GitHub-polished README with badges

Love it 🔥 Festus, we’re leveling this up to portfolio-grade GitHub quality.

Below is a fully polished README with badges, clean sections, and professional formatting.

You can paste this directly into your README.md.

🍽️ Recipe Management API












A production-ready RESTful API built using Django and Django REST Framework for managing recipes, categories, and ingredients.

Developed as part of the ALX Backend Capstone Project.

🚀 Features
✅ Week 1 – Core API Development

Relational database modeling

CRUD operations via ModelViewSet

RESTful routing using DefaultRouter

Custom permissions (IsOwnerOrReadOnly)

Clean serializer architecture

📦 Models

Category

Ingredient

Recipe

RecipeIngredient (through model)

🔗 Relationships

One-to-Many → Recipe → Category

Many-to-Many → Recipe ↔ Ingredient

ForeignKey → Recipe → User

✅ Week 2 – Advanced API Features

🔐 JWT Authentication (SimpleJWT)

🔎 Filtering

🔍 Search across related models

📄 Pagination

🧪 API Testing

🔒 Permission enforcement

🛠️ Tech Stack

Python 3.12+

Django 6+

Django REST Framework

SimpleJWT

django-filter

SQLite (Development)

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Recipe_Management_API.git
cd Recipe_Management_API
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Open:

http://127.0.0.1:8000/api/
🔐 Authentication (JWT)

Authentication uses SimpleJWT.

🔑 Obtain Access Token
POST /api/token/

Example:

{
  "username": "your_username",
  "password": "your_password"
}

Response:

{
  "refresh": "refresh_token",
  "access": "access_token"
}
🔄 Refresh Token
POST /api/token/refresh/
📌 Use Token

Add header:

Authorization: Bearer <access_token>
🔎 Filtering

Filter recipes by category:

GET /api/recipes/?category=1
🔍 Search

Search across:

Title

Description

Category name

Ingredient name

GET /api/recipes/?search=chicken
📄 Pagination

Pagination enabled using PageNumberPagination.

Example response:

{
  "count": 12,
  "next": "http://127.0.0.1:8000/api/recipes/?page=2",
  "previous": null,
  "results": [...]
}

Default page size: 5

🔒 Permissions
Action	Permission
View recipes	Public
Create recipe	Authenticated user
Update/Delete	Recipe owner only

Implemented using:

IsAuthenticatedOrReadOnly

Custom IsOwnerOrReadOnly

🧪 Running Tests
python manage.py test

Covers:

Authentication

Permissions

Recipe creation

Filtering

Search

Pagination structure

📡 API Endpoints
Method	Endpoint	Description
GET	/api/categories/	List categories
POST	/api/categories/	Create category
GET	/api/ingredients/	List ingredients
POST	/api/ingredients/	Create ingredient
GET	/api/recipes/	List recipes
POST	/api/recipes/	Create recipe
GET	/api/recipes/{id}/	Retrieve recipe
PUT	/api/recipes/{id}/	Update recipe
DELETE	/api/recipes/{id}/	Delete recipe
POST	/api/token/	Obtain JWT
POST	/api/token/refresh/	Refresh JWT
📁 Project Structure
Recipe_Management_API/
│
├── recipes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── tests.py
│
├── Recipe_Management_API/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── README.md
🎯 Learning Outcomes

This project demonstrates:

RESTful API design

Relational database modeling

JWT authentication implementation

Advanced query filtering

Secure permission handling

Automated testing

Clean Django architecture

📌 Project Status

✅ Week 1 Complete
✅ Week 2 Complete
🚀 Ready for Week 3 (Advanced features & Deployment)

📄 License

This project is licensed under the MIT License.

If you want next-level polish, I can:

🔥 Add CI/CD badge (GitHub Actions)

🌍 Add Deployment (Render / Railway)

🐳 Add Docker setup

📘 Add OpenAPI / Swagger documentation

🎓 Create a professional ALX submission summary