# reviews/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from django.db import models
from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewListView,
    ReviewViewSet,
)

app_name = "reviews"

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path("", ReviewListView.as_view(), name="list"),
    path("<int:pk>/", ReviewDetailView.as_view(), name="detail"),
    path("create/", ReviewCreateView.as_view(), name="create"),
    path("<int:pk>/update/", ReviewUpdateView.as_view(), name="update"),
    path("search/", ReviewListView.as_view(), name="search"),
    path("filter/", ReviewListView.as_view(), name="filter"),
    path('', include(router.urls)),
    path('api/', include('reviews.urls')),

]
