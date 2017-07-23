from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.id])

