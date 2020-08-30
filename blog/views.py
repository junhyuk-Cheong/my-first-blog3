from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def map(request):
    return render(request, 'blog/map.html',{})

def home(request):
    return render(request, 'blog/home.html',{})

def pathfinding(request):
    return render(request, 'blog/pathfinding1.html',{})

# Create your views here.
