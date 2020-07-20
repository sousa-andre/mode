from django import forms

from forum.models import Comment


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
