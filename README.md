# 🎬 Movie Review API — Backend Capstone Project

![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/DRF-3.14.0-red?style=for-the-badge&logo=django)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=json-web-tokens)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-In_Development-yellow?style=for-the-badge)

---

## 🎓 What is the Capstone Project?

The **Capstone Project** is your opportunity to bring together **all the skills you've learned** over the past few months—along with new ones you'll pick up along the way—to build a project from scratch.

This is your chance to:
- ✨ **Showcase your learning** and prove you can apply your knowledge
- 🚀 **Create something real** that solves a practical problem
- 💪 **Build something you'll be proud of**—a project that reflects the effort and dedication you've put into this journey

> *"It's not about building the next Facebook or Twitter. It's about choosing an idea that interests you, making a plan, and putting in the effort to bring it to life, step by step."*

---

## 🧩 Bringing It All Together

Throughout this program, we've covered a lot of ground. Now it's time to **tie everything together** into a single, structured project.

The **Movie Review API** represents the culmination of this learning journey—a production-ready backend application built with **Django** and **Django REST Framework** that allows users to create, manage, and discover movie reviews.

---

## 📋 Project Overview

The **Movie Review API** is a comprehensive backend solution that enables users to:

- 🔐 **Securely authenticate** using JWT tokens
- 📝 **Create, read, update, and delete** movie reviews
- 👤 **Manage user profiles** and view personal review history
- 🔍 **Search and filter** reviews by movie title or rating
- 📄 **Access paginated results** for optimal performance

---

## 🛠️ Breaking Down the Capstone Journey

The Capstone Project is divided into **five structured parts** to help you stay on track and avoid feeling overwhelmed. Here's how this project maps to each stage:

### 🟢 **Capstone Part 1: Idea & Planning Phase**
> *Choose a project idea and create a simple plan.*

**✅ What was done:**
- Selected the **Movie Review API** concept
- Defined core features and scope
- Created project documentation and timeline
- Identified target users and use cases

### 🟡 **Capstone Part 2: Design Phase**
> *Create an ERD diagram and design the database schema.*

**✅ What was done:**
- Designed **Entity Relationship Diagram (ERD)** using dbdiagram
- Identified database entities: Users, Reviews
- Established relationships and constraints
- Planned API endpoints following RESTful principles

**📊 Database Schema:**
```
User (1) ────╼ writes ╾──── (∞) Review
  │                              │
  ├─ id (PK)                     ├─ id (PK)
  ├─ email (Unique)               ├─ movie_title
  ├─ username                     ├─ review_content
  ├─ password                     ├─ rating (1-5)
  └─ bio                          ├─ created_date
                                  ├─ updated_date
                                  └─ user_id (FK)
```

### 🔵 **Capstone Part 3: Start Building**
> *Set up your project and begin development.*

**✅ What was done:**
- Initialized Django project with proper structure
- Created custom User model extending AbstractUser
- Implemented Review model with validation
- Applied database migrations
- Configured Django Admin interface
- Set up environment variables for security

### 🟣 **Capstone Part 4: Continue Building**
> *Expand your project, refine features, and improve functionality.*

**✅ What was done:**
- Implemented **JWT authentication** system
- Built **CRUD endpoints** for reviews and users
- Added **permission controls** (users can only edit their own reviews)
- Implemented **search and filtering** capabilities
- Added **pagination** for efficient data retrieval
- Created **sorting options** by rating and date
- Integrated **Swagger documentation**

### 🔴 **Capstone Part 5: Finalize & Submit**
> *Polish your project, test it, and submit your final version.*

**🚧 In Progress:**
- Writing comprehensive tests
- Performance optimization
- Production deployment preparation
- Final documentation polish
- Submission package preparation

---

## 🎯 What We're Expecting

Let's be clear: **we're not expecting you to build the next Facebook or Twitter.**

All we want is for you to:
- ✅ **Choose an idea that interests you**
- ✅ **Make a plan for how you'll build it**
- ✅ **Put in the effort to bring it to life, step by step**

This project reflects exactly that philosophy—a practical, well-planned, and carefully executed backend system that demonstrates mastery of core concepts.

---

## 🚀 Why This Project Structure Works

Building a project from scratch can feel intimidating. That's why the capstone is broken down into **smaller, achievable steps**:

| Part | Focus | What You Accomplish |
|------|-------|---------------------|
| **Part 1** | Planning | Clear vision and scope |
| **Part 2** | Design | Solid foundation and blueprint |
| **Part 3** | Building | Working prototype |
| **Part 4** | Expanding | Feature-rich application |
| **Part 5** | Polishing | Production-ready product |

Each part guides you through a different stage of the project, making sure you **stay focused and don't get stuck**.

---

## 💪 You're Not Alone

You're not in this alone—**we've taught you everything you need** to successfully complete this project.

This project demonstrates:
- 🔧 **Django fundamentals** — Models, views, URLs, templates
- 📊 **Database design** — Relationships, migrations, queries
- 🌐 **API development** — REST principles, serializers, endpoints
- 🔐 **Authentication** — User management, JWT, permissions
- 📝 **Documentation** — Clear, comprehensive, and useful

---

## 🧠 Key Takeaways

Through building this project, you'll:
- ✓ **Connect theoretical knowledge** to practical application
- ✓ **Experience the full development lifecycle** from idea to deployment
- ✓ **Build portfolio-worthy work** that showcases your skills
- ✓ **Gain confidence** in your ability to create real software

---

## 🌟 Final Thought

This capstone project is both a learning experience and a personal milestone. It reflects growth, persistence, and the ability to turn ideas into working software—**step by step**.

Now, it's time to trust yourself and start building.

**We know you can do it.** 💪

---

## 📁 Project Structure

```
movie_review_api/
├── apps/
│   ├── users/           # User authentication & profiles
│   └── reviews/         # Review management
├── movie_review_api/     # Project configuration
├── static/               # Static files
├── media/                # User uploads
└── requirements.txt      # Dependencies
```

---

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Django 4.2.7 |
| **API Layer** | Django REST Framework 3.14.0 |
| **Auth** | JWT (djangorestframework-simplejwt) |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Documentation** | Swagger UI, ReDoc |
| **Version Control** | Git & GitHub |

---

## 📚 Core Features

| Feature | Status | Description |
|---------|--------|-------------|
| User Registration | ✅ Complete | Create new user accounts |
| JWT Authentication | ✅ Complete | Secure token-based auth |
| Create Reviews | ✅ Complete | Post reviews with ratings |
| Read Reviews | ✅ Complete | Browse all reviews |
| Update Reviews | ✅ Complete | Edit your own reviews |
| Delete Reviews | ✅ Complete | Remove your reviews |
| Search & Filter | ✅ Complete | Find reviews by movie/rating |
| Pagination | ✅ Complete | Efficient data loading |
| API Documentation | ✅ Complete | Interactive Swagger docs |
| Testing | 🚧 In Progress | Unit and integration tests |
| Deployment | 🚧 In Progress | Heroku deployment |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/kingfetson/movie-review-api.git
cd movie-review-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 📖 API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/auth/register/` | Register new user | ❌ |
| POST | `/api/auth/login/` | Login user | ❌ |
| GET | `/api/auth/profile/` | Get user profile | ✅ |
| GET | `/api/reviews/` | List all reviews | ❌ |
| POST | `/api/reviews/` | Create review | ✅ |
| GET | `/api/reviews/{id}/` | Review details | ❌ |
| PUT | `/api/reviews/{id}/` | Update review | ✅* |
| DELETE | `/api/reviews/{id}/` | Delete review | ✅* |

*\*Owner only*

---

## 📊 Current Status

| Phase | Status | Progress |
|-------|--------|----------|
| **Part 1: Planning** | ✅ Complete | 100% |
| **Part 2: Design** | ✅ Complete | 100% |
| **Part 3: Building** | ✅ Complete | 100% |
| **Part 4: Expanding** | 🟡 In Progress | 85% |
| **Part 5: Finalizing** | 🟡 In Progress | 40% |

---

## 🙏 Acknowledgments

- The Django and Django REST Framework communities
- My mentors and peers for their guidance
- Everyone who believes in learning by building

---

<div align="center">
  
**⭐ If this project inspires you, give it a star! ⭐**

[Report Bug](https://github.com/kingfetson/movie-review-api/issues) · [Request Feature](https://github.com/kingfetson/movie-review-api/issues)

**Built with ❤️ as part of the Backend Capstone Journey**

</div>