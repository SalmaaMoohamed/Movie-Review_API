from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie
from .forms import ReviewForm
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from django.contrib import messages
from django.db.models import Q


# Create your views here.
# reviews/views.py

class ReviewListView(ListView):
    model = Review
    template_name = "reviews/list.html"
    context_object_name = "reviews"
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset().select_related("user", "movie", "movie__genre")
        
        # Search functionality
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(movie__title__icontains=q) |
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )
        
        # Rating filters
        min_rate = self.request.GET.get('min_rate')
        if min_rate:
            qs = qs.filter(rating__gte=min_rate)
            
        max_rate = self.request.GET.get('max_rate')
        if max_rate:
            qs = qs.filter(rating__lte=max_rate)
            
        # User filter
        user = self.request.GET.get('user')
        if user:
            qs = qs.filter(user__username=user)
        
        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all().order_by('title')
        return context


class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/detail.html"
    context_object_name = "review"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Your review for "{self.object.movie.title}" has been published!')
        return response

    def get_success_url(self):
        return reverse_lazy("reviews:detail", kwargs={"pk": self.object.pk})


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/update.html"
    context_object_name = "review"

    def get_queryset(self):
        
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Your review for "{self.object.movie.title}" has been updated!')
        return response
    def get_success_url(self):
        return reverse_lazy("reviews:detail", kwargs={"pk": self.object.pk})
    


# API ViewSet for Reviews 
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # مثال إضافي: تخصيص create ليظهر 201 مباشرة وبالتأكد من validity
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # مثال إضافي: تخصيص retrieve ليظهر 404 عند غير موجود
    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Review, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    # مثال إضافي: تخصيص destroy ليعيد 204 على النجاح
    def destroy(self, request, pk=None):
        obj = get_object_or_404(Review, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
