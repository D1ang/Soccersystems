# Generated by Django 3.1.3 on 2020-11-18 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201118_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitem',
            options={'ordering': ['product_group', 'description', 'size']},
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='name',
            new_name='description',
        ),
    ]