# Generated by Django 3.2.4 on 2021-06-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210412_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]