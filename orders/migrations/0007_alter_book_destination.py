# Generated by Django 3.2.12 on 2022-02-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_book_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='destination',
            field=models.CharField(choices=[('bosso', 'bosso')], max_length=50),
        ),
    ]