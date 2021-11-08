# Generated by Django 3.2.4 on 2021-11-04 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(max_length=8, null=True)),
                ('description', models.CharField(max_length=80, null=True)),
                ('fileMaker_id', models.IntegerField()),
                ('quantity', models.IntegerField(default=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ordered', models.BooleanField(default=False)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(max_length=15)),
                ('date', models.DateField(auto_now_add=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('request', 'Request'), ('production', 'Production'), ('backorder', 'Backorder'), ('sent', 'Sent')], default='request', max_length=10)),
                ('ordered', models.BooleanField(default=False)),
                ('total', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, max_length=250, null=True)),
                ('items', models.ManyToManyField(to='orders.OrderItem')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
