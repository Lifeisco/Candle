from django.db import models
import sys
from PIL import Image

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    # thumbnail = models.ImageField(upload_to='thumbs/', null=True, blank=True)

    def __str__(self):
        return f'{self.item} - фото {self.image}'

'''    def make_thumbnail(self):
        output_size = (300, 600)
        thumbnail_img = Image.open(self.image)
        thumbnail_img.thumbnail(output_size)
        thumbnail_img.save(self.image.name + ".thumbnail", "PNG")'''


