from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import Post, Comment, Like, DisLike
from .forms import PostForm, CommentForm


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save()
            if request.user.is_authenticated:
                user = User.objects.filter(id=request.user.id).last()
                instance.posted_by = user
                instance.save()

            return JsonResponse({'error': False, 'message': 'Posted Successfully'})
        else:
            errors = form.errors
            return JsonResponse({'error': True, 'errors': errors})
    else:
        return render(request, 'post_create.html')


def like_post(request, post_id):
    post = Post.objects.filter(id=post_id).last()
    if request.user.is_authenticated:
        if DisLike.objects.filter(post=post, disliked_by=request.user):
            DisLike.objects.filter(post=post, disliked_by=request.user).last().delete()
        Like.objects.get_or_create(post=post, liked_by=request.user)
    else:
        Like.objects.get_or_create(post=post)
    return JsonResponse({'message': "Liked"})



def dislike_post(request, post_id):
    post = Post.objects.filter(id=post_id).last()
    if request.user.is_authenticated:
        if Like.objects.filter(post=post, liked_by=request.user):
            Like.objects.filter(post=post, liked_by=request.user).last().delete()
        DisLike.objects.get_or_create(post=post, disliked_by=request.user)
    else:
        DisLike.objects.get_or_create(post=post)
    return JsonResponse({'message': "DisLiked"})


def post_detail(request, post_id):
    post = Post.objects.filter(id=post_id).last()
    comments = Comment.objects.filter(
        post=post, parent__isnull=True).order_by('commented_on')
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


def comment_create(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        post = Post.objects.get(id=post_id)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.POST.get('parent_comment'):
                parent = request.POST.get('parent_comment')
                comment_parent = Comment.objects.get(id=parent)
                comment.parent = comment_parent

            comment.post = post
            comment.save()
            if request.user.is_authenticated:
                user = User.objects.filter(id=request.user.id).last()
                comment.commented_by = user
                comment.save()

            data = {
                "error": False,
                "message": "Success"
            }
        else:
            data = {'error': True, 'errors': form.errors}
        return JsonResponse(data)


def post_delete(post_id):
    post = Post.objects.filter(id=post_id).last()
    post.delete()
    return redirect("/posts")