# Generated by Django 4.2 on 2023-05-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='variations',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
