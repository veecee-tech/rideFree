# Generated by Django 3.2.12 on 2022-02-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_book_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=None, editable=False),
        ),
    ]
