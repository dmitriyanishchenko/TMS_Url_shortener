# Generated by Django 2.2.1 on 2019-06-09 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20190607_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturls',
            name='long_url',
            field=models.URLField(),
        ),
    ]