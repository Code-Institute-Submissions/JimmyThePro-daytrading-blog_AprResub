from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Commentform class.
    """
    body = forms.CharField(required=True, max_length=250)

    class Meta:
        """
        Meta class.
        """
        model = Comment
        fields = ('body',)
