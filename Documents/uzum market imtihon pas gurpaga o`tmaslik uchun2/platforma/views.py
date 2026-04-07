
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from. models import Post
# templates

def home(request):
    narsalar = Post.objects.all()
    return render(request, 'home.html', {"narsalar":narsalar})


def bos(request):
    narsalar = Post.objects.all()
    return render(request, 'bos.html', )

def acaunt(request):
    narsalar = Post.objects.all()
    return render(request, 'acaunt.html' )





