# Generated by Django 3.2.12 on 2022-09-09 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('pick_up_time', models.TimeField()),
                ('pick_up_date', models.DateField()),
                ('address', models.TextField(max_length=50)),
                ('order_status', models.CharField(choices=[('pending', 'pending'), ('received', 'received'), ('completed', 'completed'), ('cancelled', 'cancelled')], default='pending', max_length=50)),
                ('payed', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.IntegerField()),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.destination')),
                ('rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rider', to=settings.AUTH_USER_MODEL)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.source')),
            ],
        ),
    ]
