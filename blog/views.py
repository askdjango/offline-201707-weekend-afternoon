from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html')

def mysum(request, numbers):
    # "10/20/30/40/50/60".split("/")
    result = 0
    for number in numbers.split('/'):
        result += int(number)
    return HttpResponse(result)

