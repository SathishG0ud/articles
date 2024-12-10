from django.shortcuts import render
from .models import Articles

# Create your views here.

def home(request):
    articles_data = Articles.objects.all()
    context = {'articles_data':articles_data}
    return render(request,'home.html',context)

def gen_article(request,pk):
    specific_articles = Articles.objects.get(id = pk)
    context = {'specific_articles':specific_articles}
    return render(request,'article1.html',context)

def about(request):
    return render(request,'about.html')