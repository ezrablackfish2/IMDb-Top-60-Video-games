# Generated by Django 4.2.3 on 2023-07-31 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_rename_alsoknownas_cast_officialsite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cast',
            old_name='reatives',
            new_name='relatives',
        ),
    ]
