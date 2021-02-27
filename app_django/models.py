from django.db import models

# Create your models here.
class Blogers(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    def __str__(self):
        return self.name

class Blogs(models.Model):
    bloger = models.ForeignKey(Blogers, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

