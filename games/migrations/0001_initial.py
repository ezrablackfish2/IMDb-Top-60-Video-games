# Generated by Django 4.2.3 on 2023-07-15 13:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Goof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ParentsGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cover', models.ImageField(blank=True, default=None, null=True, upload_to='covers/')),
                ('title', models.CharField(default=None, max_length=40, null=True)),
                ('award', models.CharField(default=None, max_length=40, null=True)),
                ('video', models.FileField(blank=True, default=None, null=True, upload_to='videos/')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/')),
                ('storyline', models.CharField(default=None, max_length=200, null=True)),
                ('genre', models.CharField(default=None, max_length=20, null=True)),
                ('crazy_credits', models.CharField(default=None, max_length=40, null=True)),
                ('soundtrack', models.CharField(default=None, max_length=20, null=True)),
                ('country_of_origin', models.CharField(default=None, max_length=20, null=True)),
                ('language', models.CharField(default=None, max_length=20, null=True)),
                ('company', models.CharField(default=None, max_length=20, null=True)),
                ('box_office', models.CharField(default=None, max_length=20, null=True)),
                ('runtime', models.TimeField(default=None, null=True)),
                ('color', models.CharField(default=None, max_length=10, null=True)),
                ('soundmix', models.CharField(default=None, max_length=10, null=True)),
                ('nickname', models.CharField(default=None, max_length=20, null=True)),
                ('release_date', models.DateField(default=None, null=True)),
                ('imdb_rating', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('popularity', models.IntegerField(default=None, null=True)),
                ('metascore', models.PositiveIntegerField(default=None, null=True)),
                ('cast', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casts', to='games.cast')),
                ('director', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directors', to='games.director')),
                ('frequent_questions', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FAQs', to='games.frequentlyaskedquestion')),
                ('goof', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goofs', to='games.goof')),
                ('parents_guide', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parental_guides', to='games.parentsguide')),
                ('picks', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.videogame')),
                ('quote', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='games.quote')),
                ('relation', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='games.relation')),
                ('review', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='games.review')),
                ('trivia', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Trivias', to='games.trivia')),
                ('writer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writers', to='games.writer')),
            ],
        ),
    ]