# Generated by Django 3.2.12 on 2022-02-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_book_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='source',
            field=models.CharField(choices=[('ss', 'ss')], max_length=50),
        ),
    ]
