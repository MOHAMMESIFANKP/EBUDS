# Generated by Django 4.2 on 2023-05-19 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('brand_image', models.ImageField(default='No image available', upload_to='photos/brand')),
                ('brand_address', models.TextField(max_length=200)),
                ('brand_discription', models.TextField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banners_image', models.ImageField(upload_to='photos/banner')),
                ('banner_name', models.CharField(max_length=200)),
                ('banner_discription', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
