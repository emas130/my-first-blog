from django.http import HttpResponse
from django.shortcuts import render

def about(request):
   # Adres strony który funkcja wywołuje
   return render(request, 'about.html')

def blog(request):
   #return HttpResponse('To jest blog')
   return render(request, 'blog.html')

def home(request):
   return render(request, 'home.html')

def gallery(request):
   return render(request, 'gallery.html')