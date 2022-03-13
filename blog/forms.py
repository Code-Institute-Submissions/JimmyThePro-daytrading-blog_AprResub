from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Commentform class.
    """
    class Meta:
        """
        Meta class.
        """
        model = Comment
        fields = ('body',)
