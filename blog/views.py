import datetime
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post

def post_list(request):
    qs = Post.objects.all()

    # request.GET['query']
    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)

    date_list = []
    for i in range(365):
        date = datetime.datetime(2017, 1, 1) + datetime.timedelta(days=i)
        date_list.append(date)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
        'date_list': date_list,
    })


def post_new(request):
    if request.method == 'POST':
        # request.GET
        # request.POST  # POST인자, 파일 제외
        # request.FILES  # POST인자, 파일만
        form = PostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data  # {'title': ??, 'author': ??}
            post = form.save()
            # return redirect('blog:post_detail', post.id)
            return redirect(post)  # post.get_absolute_url()로 이동
        #else:
        #    form.errors
    else:
    # if request.method == 'GET':
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
            # request.GET
        # request.POST  # POST인자, 파일 제외
        # request.FILES  # POST인자, 파일만
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # form.cleaned_data  # {'title': ??, 'author': ??}
            post = form.save()
            return redirect('blog:post_detail', post.id)
        #else:
        #    form.errors
    else:
        # if request.method == 'GET':
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_detail(request, pk):
    # pk = "100"
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm_delete.html', {
        'post': post,
    })


def mysum(request, numbers):
    # "10/20/30/40/50/60".split("/")

    '''
    result = 0
    for number in numbers.split('/'):
        # 1)
#       if number:
#           result += int(number)

        # 2)
        result += int(number or 0)
    '''

    # 3) generator expression
    result = sum(
        int(number or 0)
        for number in numbers.split('/'))
    return HttpResponse(result)

