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


# Create your views here.
# reviews/views.py

class ReviewListView(ListView):
    model = Review
    template_name = "reviews/list.html"
    context_object_name = "reviews"

    #def get_queryset(self):
        #qs = super().get_queryset().select_related("user", "movie")
        #movie_id = self.request.GET.get("movie_id")
        #if movie_id:
            #qs = qs.filter(movie_id=movie_id)
        #return qs

def review_list(request):
    qs = Review.objects.all()
    q = request.GET.get('q', '')
    min_rate = request.GET.get('min_rate')
    max_rate = request.GET.get('max_rate')

    if q:
        qs = qs.filter(movie_title__icontains=q)
    if min_rate:
        qs = qs.filter(rating__gte=min_rate)
    if max_rate:
        qs = qs.filter(rating__lte=max_rate)

    return render(request, 'reviews/list.html', {'reviews': qs, 'q': q, 'min_rate': min_rate, 'max_rate': max_rate})

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["movies"] = Movie.objects.all()
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
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("reviews:detail", kwargs={"pk": self.object.pk})


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/update.html"

    def get_queryset(self):
        
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

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
