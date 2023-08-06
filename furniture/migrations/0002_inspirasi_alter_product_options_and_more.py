# Generated by Django 4.2.3 on 2023-07-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspirasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
            options={
                'verbose_name_plural': 'Inspirasi',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Produk'},
        ),
        migrations.RemoveField(
            model_name='kategori',
            name='banner_dua',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gambar_dua',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gambar_empat',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gambar_lima',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gambar_satu',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gambar_tiga',
        ),
    ]