# Generated by Django 3.1.2 on 2021-01-17 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210116_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_image_url',
        ),
    ]
