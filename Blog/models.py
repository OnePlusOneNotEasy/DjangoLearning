from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    subtract = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
