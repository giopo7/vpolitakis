# Generated by Django 4.1.7 on 2023-03-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_firingtype_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firingtype',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='firingtype',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='firingtype',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='firingtype',
            name='image4',
        ),
        migrations.AddField(
            model_name='firingtype',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media'),
        ),
    ]
