from django.db import models

# Create your models here.
    
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True) #blank 추가함 ##교안에 추가하기!!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True,null=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE, related_name = 'comments')
    writer = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
