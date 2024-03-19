from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    item_image = CloudinaryField('image', default='placeholder')
    allergens = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name