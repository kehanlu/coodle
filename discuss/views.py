from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from discuss.models import Post, Comment
import markdown as md


def post_list(request):
    context = {
        "posts": Post.objects.all().order_by('-create_date')
    }
    return render(request, 'discuss/list.html', context)


def discuss(request, pid):
    if not Post.objects.filter(id=pid).exists():
        return HttpResponseNotFound()
    post = Post.objects.get(id=pid)
    post.content = md.markdown(post.content, extensions=['fenced_code'])

    comments_query = post.comment.all().order_by('-create_date')
    comments = list()
    for comment in comments_query:
        comment.content = md.markdown(
            comment.content, extensions=['fenced_code'])
        comments.append(comment)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'discuss/single.html', context)


def post(request):
    return render(request, 'discuss/create.html', {})


def api_post(request):
    data = request.POST

    post = Post.objects.create(user=request.user,
                               title=data['title'], content=data['content'])
    return redirect('/discuss/{}'.format(post.id))


def api_comment(request, pid):
    if not Post.objects.filter(id=pid).exists():
        return HttpResponseNotFound()
    post = Post.objects.get(id=pid)
    data = request.POST
    Comment.objects.create(user=request.user, post=post,
                           content=data['content'])

    return redirect('/discuss/{}'.format(pid))
