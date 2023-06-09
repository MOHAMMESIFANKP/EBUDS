# Generated by Django 4.2 on 2023-05-26 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_variations_quantity'),
        ('carts', '0004_remove_cart_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='variation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.variations'),
            preserve_default=False,
        ),
    ]
