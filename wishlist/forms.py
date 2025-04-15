from django import forms
from .models import Wishlist, WishlistItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'description', 'priority', 'is_private', 'estimated_cost', 'target_date']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }

class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['name', 'description', 'price', 'url', 'image', 'status', 'priority', 'notes']