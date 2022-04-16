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
        body = forms.CharField(required=True, max_length=250)
        model = Comment
        fields = ('body',)
