# Generated by Django 3.1 on 2024-06-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, upload_to='photos/products'),
        ),
    ]
