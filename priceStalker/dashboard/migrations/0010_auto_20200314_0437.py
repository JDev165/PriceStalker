# Generated by Django 2.1 on 2020-03-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200306_0419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrapers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_url', models.CharField(max_length=100)),
                ('price_element_selector', models.CharField(max_length=50)),
                ('image_element_selector', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='keywords',
            name='product',
        ),
        migrations.DeleteModel(
            name='Keywords',
        ),
    ]