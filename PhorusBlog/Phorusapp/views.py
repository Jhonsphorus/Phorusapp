from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post1


# Create your views here.
#def post_list(request):
    #return render(request, 'Phorusapp/post_list.html',{})

def post_list(request):
    #posts = Post1.objects.filter(title__contains='Semicolon')
    posts = Post1.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Phorusapp/post_list.html', {'posts':posts})
    # 'posts' is the name we are giving to the variable posts in  views.py, it is the 'posts' that 
    #  will be representing the variable posts in template(in html)
    # The post can be any name e.g. {'johnson':posts}

def post_detail(request,pk):
    post = get_object_or_404(Post1, pk=pk)
    return render(request, 'Phorusapp/post_detail.html', {'post': post})

def contact(request):
    return render(request, 'Phorusapp/contact.html',{})

def akin(request):
    return render(request, 'Phorusapp/akin.html',{})

def greeting(request):
    return HttpResponse("Greetings from Johnson Adebayo")