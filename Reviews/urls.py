# reviews/urls.py
from django.urls import path
from django.db import models
from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewListView,
)

app_name = "reviews"

urlpatterns = [
    path("", ReviewListView.as_view(), name="list"),
    path("<int:pk>/", ReviewDetailView.as_view(), name="detail"),
    path("create/", ReviewCreateView.as_view(), name="create"),
    path("<int:pk>/update/", ReviewUpdateView.as_view(), name="update"),
    path("search/", ReviewListView.as_view(), name="search"),
    path("filter/", ReviewListView.as_view(), name="filter"),
]