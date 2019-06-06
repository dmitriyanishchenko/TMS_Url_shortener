# Generated by Django 2.2.1 on 2019-06-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20190604_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.URLField()),
                ('short_url', models.URLField(blank=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('counter_click', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='ShortUrl',
        ),
    ]
