from django.shortcuts import render
from . models import Blog


# Create your views here.
def blog(request):
   blogel = Blog.objects.all().order_by('date')
   #return HttpResponse('To jest blog')
   return render(request, 'blog/blog.html')
