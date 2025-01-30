from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review_text", "rating"]
        widgets = {
            'review_text': forms.Textarea(attrs={'cols': 40, 'rows': 1})  
        }

