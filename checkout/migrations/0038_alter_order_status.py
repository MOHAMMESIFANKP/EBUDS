# Generated by Django 4.2 on 2023-06-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0037_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Processing', 'Processing'), ('Cancelled', 'Cancelled'), ('Shipped', 'Shipped'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
