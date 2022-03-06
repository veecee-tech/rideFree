# Generated by Django 3.2.12 on 2022-03-02 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20220228_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='pick_up_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='pick_up_time',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]