from django.db import models

# Create your models here.

class FiringType(models.Model):
    COLOR_CHOICES = (
    ('gray-100','gray-100'),
    ('white', 'white'),
)

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True, max_length=255)
    color = models.CharField(max_length=255, choices=COLOR_CHOICES, null=True)
    

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name