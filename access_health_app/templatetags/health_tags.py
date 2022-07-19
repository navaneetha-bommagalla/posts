
from django import template
from access_health_app.models import Comment
register = template.Library()



@register.filter
def child_comments(comment):
    sub_comments_list = []
    comments = Comment.objects.filter(parent=comment).order_by('commented_on')
    for each in comments:
        sub_comments_list.append(each)
        sub_comments_list.extend(child_comments(each))

    return sub_comments_list