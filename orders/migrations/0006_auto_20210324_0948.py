# Generated by Django 3.1.3 on 2021-03-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210314_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('requested', 'Requested'), ('pending', 'Pending'), ('finished', 'Finished')], default='requested', max_length=10),
        ),
    ]