# Generated by Django 4.2.3 on 2023-07-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_castvideo_castvideo_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='role',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]