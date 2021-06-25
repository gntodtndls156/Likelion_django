from django.shortcuts import render
from .models import Post
# Create your views here.
def Home(request):
    posts = Post.objects.all()
    return render(request, 'Home.html', {'posts': posts})