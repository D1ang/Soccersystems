# Generated by Django 3.2.4 on 2021-11-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='description',
            field=models.CharField(max_length=85, null=True),
        ),
    ]
