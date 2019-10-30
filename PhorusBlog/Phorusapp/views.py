from django.shortcuts import render


# Create your views here.
def post_list(request):
    return render(request, 'Phorusapp/post_list.html',{})
