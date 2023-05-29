from .models import Comment, Recipe
from django import forms
from django.forms import ModelForm, TextInput
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe

        widgets = {
            'direction': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'excerpt': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Enter a short description of your recipe'
                }),
            'author': TextInput(attrs={'id': 'username', 'type': 'hidden'}),
        }

        fields = [
            'title',
            'excerpt',
            'author',
            'featured_image',
            'category',
            'servings',
            'ingredients',
            'direction',
            'status',
        ]
