from django import forms
from .models import *

from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'text':forms.Textarea(attrs = {'class':'form-control mb-3','rows':'3'})
        }

class FormCreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title','body','tags']

        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control mb-3'}),
            'body':forms.Textarea(attrs = {'class':'form-control mb-3','rows':'3'}),
            'tags':forms.SelectMultiple(attrs = {'class':'form-control mb-3'}),
        }

class FormCreateTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'title'
        ]
        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control mb-3'}),
        }
