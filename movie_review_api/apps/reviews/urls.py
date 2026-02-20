from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewListCreateView.as_view(), name='review-list'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('movie/<str:movie_title>/', views.MovieReviewsView.as_view(), name='movie-reviews'),
    path('top-rated/', views.TopRatedReviewsView.as_view(), name='top-rated-reviews'),
]
