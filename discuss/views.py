from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from discuss.models import Post, Comment
import markdown


def list(request):
    context = {
        "posts": Post.objects.all().order_by('-create_date')
    }
    return render(request, 'discuss/list.html', context)


def discuss(request, pid):
    if not Post.objects.filter(id=pid).exists():
        return HttpResponseNotFound()
    post = Post.objects.get(id=pid)
    context = {
        'post': post,
        'comments': post.comment.all().order_by('-create_date')
    }

    return render(request, 'discuss/single.html', context)


def post(request):
    return render(request, 'discuss/create.html', {})


def api_post(request):
    data = request.POST
    content = markdown.markdown(data['content'], extensions=['fenced_code'])

    post = Post.objects.create(user=request.user,
                               title=data['title'], content=content)
    return redirect('/discuss/{}'.format(post.id))


def api_comment(request, pid):
    if not Post.objects.filter(id=pid).exists():
        return HttpResponseNotFound()
    post = Post.objects.get(id=pid)
    data = request.POST

    content = markdown.markdown(data['content'], extensions=['fenced_code'])
    Comment.objects.create(user=request.user, post=post,
                           content=content)

    return redirect('/discuss/{}'.format(pid))
