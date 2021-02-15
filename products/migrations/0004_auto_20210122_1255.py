# Generated by Django 3.1.3 on 2021-01-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productgroup_sort'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='productitem',
            name='slug',
            field=models.SlugField(max_length=4, primary_key=True, serialize=False, unique=True),
        ),
    ]