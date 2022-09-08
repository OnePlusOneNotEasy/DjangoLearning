from django.db import models
from django.urls import reverse

# Create your models here.
class Fruit(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    GOOD = 'G'
    BAD = 'B'
    SUMMARY_CHOICES = [(GOOD, 'good'),(BAD, 'bad')]
    summary = models.TextField(choices=SUMMARY_CHOICES, default=GOOD)
    buy = models.BooleanField(default=False) # null=True, default=True

    def get_absolute_url(self):
        # return reverse('fruits-show', kwargs={'my_id':self.id})
        # return f"/fruits/{self.id}/"
        return reverse('fruit:fruits-detail', kwargs={'my_id':self.id})
