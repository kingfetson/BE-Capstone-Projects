from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('login/', views.LoginView.as_view(), name='auth_login'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('profile/reviews/', views.UserReviewsView.as_view(), name='user_reviews'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
