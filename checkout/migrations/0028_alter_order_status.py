# Generated by Django 4.2 on 2023-05-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0027_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Shipped', 'Shipped')], default='Pending', max_length=150),
        ),
    ]