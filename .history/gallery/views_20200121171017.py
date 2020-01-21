from django.shortcuts import render
from django.http import HttpResponse

def gallery(request):
   #return HttpResponse('To jest blog')
   return render(request, 'gallery/gallery.html')
