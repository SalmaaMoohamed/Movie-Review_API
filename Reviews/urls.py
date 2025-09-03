# reviews/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewViewSet,
)

app_name = "reviews"

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', ReviewListView.as_view(), name='list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='detail'),
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='update'),
    path('', include(router.urls)),
]
