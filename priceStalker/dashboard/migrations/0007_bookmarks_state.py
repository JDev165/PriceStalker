# Generated by Django 2.1 on 2020-03-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarks',
            name='state',
            field=models.BooleanField(default=0),
        ),
    ]