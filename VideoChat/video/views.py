from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request , 'index.html')


def video(request ,room , created):
    return render(request , 'video.html')