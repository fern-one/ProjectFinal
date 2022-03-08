from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def shopall(request):
    return render(request,'cactus.html')

def story(request):
    return render(request,'story.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

