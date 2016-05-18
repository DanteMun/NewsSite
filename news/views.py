from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.contrib import messages
# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, 'news/index.html', {
        'post_list':post_list,
        })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_list = Comment.objects.all()
    return render(request, 'news/post_detail.html', {
        'post':post,
        'comment_list':comment_list,
        })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save()

            messages.success(request, '새로운 뉴스가 등록되었습니다.')

            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'news/post_new.html', {
        'form':form,
        })

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, '새로운 댓글이 성공적으로 등록되었습니다.')
            return redirect(post)
    else:
        form = CommentForm()
    return render(request, 'news/comment_new.html', {
        'form':form,
        })