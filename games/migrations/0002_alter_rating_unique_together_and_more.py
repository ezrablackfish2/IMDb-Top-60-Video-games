# Generated by Django 4.2.3 on 2023-07-18 07:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('game', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('game', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('game', 'user')},
        ),
    ]