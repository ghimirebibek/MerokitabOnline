# Generated by Django 3.0.4 on 2020-10-15 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201014_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
