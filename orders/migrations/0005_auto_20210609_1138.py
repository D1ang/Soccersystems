# Generated by Django 3.2.4 on 2021-06-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_id',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]
