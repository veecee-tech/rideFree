# Generated by Django 3.2.12 on 2022-03-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20220302_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='pick_up_date',
        ),
        migrations.AlterField(
            model_name='orders',
            name='pick_up_time',
            field=models.DateTimeField(),
        ),
    ]