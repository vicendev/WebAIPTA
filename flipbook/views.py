from django.shortcuts import render

# Create your views here.

def flipbook(request):
    return render(request, 'flipbook/flipbook.html')
