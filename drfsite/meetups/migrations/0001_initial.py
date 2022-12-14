# Generated by Django 4.1.3 on 2022-12-04 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeetUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(null=True, upload_to='images/%Y/%m/%d/')),
                ('organizer_email', models.EmailField(max_length=254)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.location')),
                ('participants', models.ManyToManyField(blank=True, to='meetups.participant')),
            ],
        ),
    ]
