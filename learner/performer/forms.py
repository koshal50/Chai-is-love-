from .models import chaiVariety,Store
from django import forms
from .models import ContactMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CHaiReview

class ChaiVarietyForm(forms.Form):
    chaiVariety = forms.ModelChoiceField(
        queryset=chaiVariety.objects.all(),label="Select Chai Variety")

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ChaiReviewForm(forms.ModelForm):
    class Meta:
        model = CHaiReview
        fields = ['rating', 'comment']  # Removed 'user' since we set it in view
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Share your experience with this chai...',
                'class': 'form-control'
            }),
            'rating': forms.Select(
                choices=[(i, f'{i} ★') for i in range(1, 6)],
                attrs={'class': 'form-control'}
            )
        }
        labels = {
            'rating': 'Rating (1-5 stars)',
            'comment': 'Your Review'
        }