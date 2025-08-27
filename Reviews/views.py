from django.shortcuts import render
from .models import Review

# Create your views here.
# reviews/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review, Movie
from .forms import ReviewForm  

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
