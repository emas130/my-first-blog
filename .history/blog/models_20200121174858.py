from django.db import models

# Create your models here.
class Blog(models.Model):
   title = models.CharField(max_length = 100)
   slug  = models.SlugField()
   body  = models.TextField()
   date  = models.DateTiemeField(auto_now_add = True)