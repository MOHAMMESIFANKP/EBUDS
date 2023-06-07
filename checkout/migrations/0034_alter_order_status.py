# Generated by Django 4.2 on 2023-06-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0033_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled')], default='Pending', max_length=150),
        ),
    ]
