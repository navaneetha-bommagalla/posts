from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_description"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


    def clean_comment(self):
        if self.cleaned_data.get('comment') == '<p>&nbsp;</p>':
            raise forms.ValidationError('This field is required')
        else:
            return self.cleaned_data.get('comment')
