from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, null=True, related_name="posted_by", on_delete=models.CASCADE)


    def likes_count(self):
        return Like.objects.filter(post=self).count()


    def dislikes_count(self):
        return DisLike.objects.filter(post=self).count()



class Like(models.Model):

    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, null=True, related_name='liked_by', on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)


class DisLike(models.Model):

    post = models.ForeignKey(Post, related_name="dislikes", on_delete=models.CASCADE)
    # users = models.ManyToManyField(User, related_name='disliked_users')
    disliked_by = models.ForeignKey(User, null=True, related_name='disliked_by', on_delete=models.CASCADE)
    disliked_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment = models.TextField()
    commented_by = models.ForeignKey(
        User, related_name="commented_user", blank=True, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, blank=True, null=True, related_name="post_comments", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", blank=True, null=True,
                               related_name="comment_parent", on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

