# Generated by Django 4.2.3 on 2023-09-04 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genra', to='games.videogame')),
            ],
        ),
    ]
