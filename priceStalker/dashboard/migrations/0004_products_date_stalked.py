# Generated by Django 2.1 on 2020-02-26 02:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date_stalked',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
