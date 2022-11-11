from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'Tag','img','file','categoty')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        