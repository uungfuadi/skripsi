# Generated by Django 4.2.3 on 2023-07-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0005_alter_product_jumlah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='jumlah',
        ),
        migrations.AddField(
            model_name='product',
            name='stok',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
