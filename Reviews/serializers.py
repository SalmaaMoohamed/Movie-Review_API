from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Movie, Genre, ReviewFlag

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'title', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
