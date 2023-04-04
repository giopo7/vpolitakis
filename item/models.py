from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta():
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    SHAPE_CHOICES = (
    ('Amphora','Amphora'),
    ('Stirrup_Jar', 'Stirrup Jar'),
    ('Jug','Jug'),
    ('Cup','Cup'),
    ('Mug','Mug'),
    ('Rhyton','Rhyton'),
    ('Figure','Figure'),
    ('Strainer','Strainer'),
    ('Spouted_Jar','Spouted Jar'),
    ('Ewer','Ewer'),
    ('Flask','Flask'),
)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True, null=True, max_length=255)
    image1 = models.ImageField(upload_to='media', blank=True, null=True, max_length=255)
    image2 = models.ImageField(upload_to='media', blank=True, null=True, max_length=255)
    image3 = models.ImageField(upload_to='media', blank=True, null=True, max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    shape = models.CharField(max_length=255, choices=SHAPE_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def Meta():
        ordering=('created_at',)

    def __str__(self):
        return self.name

