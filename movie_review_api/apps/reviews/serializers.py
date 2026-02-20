from rest_framework import serializers
from .models import Review
from apps.users.serializers import UserProfileSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user_details = UserProfileSerializer(source='user', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = (
            'id', 'movie_title', 'review_content', 'rating', 
            'user', 'user_details', 'created_date', 'updated_date'
        )
        read_only_fields = ('created_date', 'updated_date')
    
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

class ReviewDetailSerializer(ReviewSerializer):
    class Meta(ReviewSerializer.Meta):
        fields = ReviewSerializer.Meta.fields + ('updated_date',)
