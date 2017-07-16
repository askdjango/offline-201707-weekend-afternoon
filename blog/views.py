from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()

    # request.GET['query']
    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
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

