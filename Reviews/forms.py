# reviews/forms.py  
from django import forms  
from .models import Review, Movie, Genre

class MovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Style form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': f'id_{field_name}'
            })
        
        # Special styling for specific fields
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter the movie title'
        })
        
        if 'synopsis' in self.fields:
            self.fields['synopsis'].widget.attrs.update({
                'placeholder': 'Brief description of the movie...',
                'rows': 4
            })

    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre', 'synopsis', 'poster_url']
        widgets = {
            'synopsis': forms.Textarea(attrs={'rows': 4}),
            'poster_url': forms.URLInput(attrs={'placeholder': 'https://example.com/poster.jpg'})
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year and (year < 1888 or year > 2030):
            raise forms.ValidationError('Please enter a valid year between 1888 and 2030.')
        return year

class ReviewForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Style form fields
        for field_name, field in self.fields.items():
            if field_name != 'rating':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'id': f'id_{field_name}'
                })
        
        # Movie field with search capability
        self.fields['movie'].widget = forms.Select(attrs={
            'class': 'form-control movie-select',
            'id': 'id_movie'
        })
        self.fields['movie'].empty_label = "Select a movie or add new one"
        
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter a catchy title for your review'
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Share your detailed thoughts about the movie...',
            'rows': 6
        })
        self.fields['rating'].widget = forms.HiddenInput(attrs={
            'id': 'id_rating'
        })

    class Meta:  
        model = Review  
        fields = ["movie", "title", "content", "rating"]
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not rating or rating < 1 or rating > 5:
            raise forms.ValidationError('Please select a rating between 1 and 5 stars.')
        return rating