# Generated by Django 2.1 on 2020-03-15 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20200314_0437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmarks',
            options={'verbose_name_plural': 'Bookmarks'},
        ),
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='prices',
            options={'verbose_name_plural': 'Prices'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='scrapers',
            options={'verbose_name_plural': 'Scrapers'},
        ),
    ]
