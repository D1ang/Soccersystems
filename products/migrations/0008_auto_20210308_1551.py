# Generated by Django 3.1.3 on 2021-03-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productitem_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='product_id',
            field=models.IntegerField(max_length=8),
        ),
    ]
