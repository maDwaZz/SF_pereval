# Generated by Django 4.2.5 on 2023-09-13 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(blank=True, max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(blank=True, max_length=255)),
                ('connect', models.TextField(blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('level_winter', models.CharField(blank=True, max_length=10)),
                ('level_spring', models.CharField(blank=True, max_length=10)),
                ('level_summer', models.CharField(blank=True, max_length=10)),
                ('level_autumn', models.CharField(blank=True, max_length=10)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pereval_added',
            },
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.perevaladded')),
            ],
            options={
                'db_table': 'pereval_images',
            },
        ),
    ]
