from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Commentform class.
    """
    class Meta:
        model = Comment
        fields = ('body',)
