from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'text':forms.Textarea(attrs = {'class':'form-control mb-3','rows':'3'})
        }
