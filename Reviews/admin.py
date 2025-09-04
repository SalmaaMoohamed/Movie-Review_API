from django.contrib import admin
from .models import Movie, Review, Genre, ReviewFlag, ReviewLike

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'genre', 'created_at']
    list_filter = ['genre', 'year', 'created_at']
    search_fields = ['title', 'synopsis']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at', 'movie__genre']
    search_fields = ['title', 'content', 'movie__title', 'user__username']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(ReviewFlag)
class ReviewFlagAdmin(admin.ModelAdmin):
    list_display = ['review', 'reporter', 'reason', 'created_at']
    list_filter = ['created_at']
    search_fields = ['reason', 'review__title']
    ordering = ['-created_at']

@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'created_at']
    list_filter = ['created_at']
    ordering = ['-created_at']