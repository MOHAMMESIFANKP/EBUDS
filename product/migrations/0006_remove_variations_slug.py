# Generated by Django 4.2 on 2023-05-25 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_variations_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variations',
            name='slug',
        ),
    ]
