# Generated by Django 4.1.7 on 2023-03-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_category_options_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
