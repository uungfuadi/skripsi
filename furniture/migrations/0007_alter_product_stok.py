# Generated by Django 4.2.3 on 2023-07-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0006_remove_product_jumlah_product_stok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stok',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
