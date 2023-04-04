from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta():
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', max_length=255)
    collab = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE, default=None)
    description = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

    # PROJECT_CATEGORIES = (
    #     ('Experimental', 'Experimental'),
    #     ('Seminars', 'Seminars'),
    #     ('Theories', 'Theories'),
    #     ('Activities', 'Activities'),
    #     ('Collaborations', 'Collaborations'),
    # )