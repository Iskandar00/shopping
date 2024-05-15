from django import forms

from apps.comments.models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('product', 'user')
