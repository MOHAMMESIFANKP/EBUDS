# Generated by Django 4.2 on 2023-06-01 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_coupon_rename_is_expired_usercoupon_used_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoupon',
            name='order',
        ),
    ]
