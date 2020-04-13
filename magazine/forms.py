from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=('is_pos','upvotes','commented_cast','comment_by')
