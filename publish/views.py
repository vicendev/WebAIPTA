from django.shortcuts import render
from publish.models import PDFPublish

# Create your views here.

def flipbook(request):
    documents = PDFPublish.objects.all()
    return render(request, 'publish/index.html', {'documents': documents})

def publish(request):
    documents = PDFPublish.objects.all()
    return render(request, 'publish/publish.html', {'documents': documents})