# Generated by Django 2.2.1 on 2019-06-07 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20190606_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Short_urls',
            new_name='ShortUrls',
        ),
        migrations.AlterModelOptions(
            name='shorturls',
            options={'ordering': ['-counter']},
        ),
    ]