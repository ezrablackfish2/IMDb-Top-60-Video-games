# Generated by Django 4.2.3 on 2023-09-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='year',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
