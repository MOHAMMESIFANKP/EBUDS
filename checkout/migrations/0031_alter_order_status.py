# Generated by Django 4.2 on 2023-05-31 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0030_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Processing', 'Processing'), ('Pending', 'Pending'), ('Shipped', 'Shipped')], default='Pending', max_length=150),
        ),
    ]
