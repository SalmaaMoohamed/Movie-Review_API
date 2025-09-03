# reviews/forms.py  
from django import forms  
from .models import Review  

class ReviewForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Style form fields
        self.fields['movie'].widget.attrs.update({
            'class': 'form-control',
            'id': 'id_movie'
        })
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'id_title',
            'placeholder': 'Enter a catchy title for your review'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control textarea',
            'id': 'id_content',
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