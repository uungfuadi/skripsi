# Generated by Django 4.2.3 on 2023-07-16 00:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0002_inspirasi_alter_product_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profil',
        ),
        migrations.DeleteModel(
            name='Statis',
        ),
        migrations.AlterField(
            model_name='inspirasi',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
