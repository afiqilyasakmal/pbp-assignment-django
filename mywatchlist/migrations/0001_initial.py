# Generated by Django 4.1 on 2022-09-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistFilmKu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_watched', models.BooleanField()),
                ('film_title', models.TextField()),
                ('film_rating', models.IntegerField()),
                ('film_release_date', models.TextField()),
                ('film_review', models.TextField()),
            ],
        ),
    ]