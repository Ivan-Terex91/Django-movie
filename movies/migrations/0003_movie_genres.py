# Generated by Django 3.1.4 on 2020-12-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201226_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre', verbose_name='Жанры'),
        ),
    ]
