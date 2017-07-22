from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()

    # request.GET['query']
    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
    })

def post_detail(request, pk):
    # pk = "100"
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
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

