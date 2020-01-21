from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('gallery', include('gallery.urls')),
    path('', views.home),
]

urlpatterns += staticfiles_urlpatterns()