from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from apps.permissions import IsOwnerOrReadOnly
from .pagination import ReviewPagination

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title', 'review_content']
    ordering_fields = ['rating', 'created_date']
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        # Check if user already reviewed this movie
        movie_title = serializer.validated_data.get('movie_title')
        existing_review = Review.objects.filter(
            user=self.request.user,
            movie_title__iexact=movie_title
        ).first()
        
        if existing_review:
            raise ValidationError("You have already reviewed this movie")
        
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by rating range
        rating_min = self.request.query_params.get('rating_min')
        rating_max = self.request.query_params.get('rating_max')
        
        if rating_min:
            queryset = queryset.filter(rating__gte=rating_min)
        if rating_max:
            queryset = queryset.filter(rating__lte=rating_max)
        
        # Filter by movie title (case-insensitive)
        movie_title = self.request.query_params.get('movie_title')
        if movie_title:
            queryset = queryset.filter(movie_title__icontains=movie_title)
        
        return queryset

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save()

class MovieReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    
    def get_queryset(self):
        movie_title = self.kwargs['movie_title']
        return Review.objects.filter(movie_title__iexact=movie_title)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response(
                {"message": f"No reviews found for movie: {kwargs['movie_title']}"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class TopRatedReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    
    def get_queryset(self):
        return Review.objects.filter(rating__gte=4).order_by('-rating', '-created_date')