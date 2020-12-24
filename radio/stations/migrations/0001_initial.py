# Generated by Django 3.0.8 on 2020-12-23 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('frequency', models.FloatField()),
            ],
            options={
                'verbose_name': 'радиостанции',
                'verbose_name_plural': 'радиостанции',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40)),
                ('album', models.CharField(max_length=40)),
                ('ganre', models.CharField(max_length=30)),
                ('duration', models.DurationField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traks', to='stations.Singer')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traks', to='stations.Station')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Трек',
                'ordering': ('name',),
            },
        ),
    ]