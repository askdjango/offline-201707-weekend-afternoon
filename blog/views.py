from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html')

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x) + int(y) + int(z))

