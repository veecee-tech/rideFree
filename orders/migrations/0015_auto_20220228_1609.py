# Generated by Django 3.2.12 on 2022-02-28 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0014_auto_20220228_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('pending', 'pending'), ('received', 'received'), ('completed', 'completed')], default='pending', max_length=50)),
                ('payed', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.IntegerField()),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.destination')),
                ('rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rider', to=settings.AUTH_USER_MODEL)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.source')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]