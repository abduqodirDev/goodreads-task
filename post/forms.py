from django import forms
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category', 'tag')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
