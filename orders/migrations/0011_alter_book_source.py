# Generated by Django 3.2.12 on 2022-02-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20220228_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='source',
            field=models.CharField(choices=[('kpakngu', 'kpakngu')], max_length=50),
        ),
    ]