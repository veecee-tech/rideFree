# Generated by Django 3.2.12 on 2022-02-25 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
