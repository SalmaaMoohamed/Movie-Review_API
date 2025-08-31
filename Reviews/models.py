from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from .models import Movie
from .models import Review
from .models import Genre



# Create your models here.





class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(null=True, blank=True)
    imdb_id = models.CharField(max_length=20, blank=True, null=True, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name="movies")
    poster_url = models.URLField(blank=True, null=True)
    synopsis = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.year or 'N/A'})"
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],) # 1 to 5 stars
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "movie")  
        ordering = ["-created_at"]

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"
    

class ReviewFlag(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="flags")
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_flags")
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review Flag"
        verbose_name_plural = "Review Flags"

    def __str__(self):
        return f"Flag on {self.review.id} by {self.reporter.username}"
    
class ReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_likes")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "review")  
        verbose_name = "Review Like"
        verbose_name_plural = "Review Likes"

    def __str__(self):
        return f"{self.user.username} likes Review {self.review.id}"
