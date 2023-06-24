from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='images', blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): return self.title

class TodoPhoto(models.Model):
    image = models.ImageField(upload_to='images')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)