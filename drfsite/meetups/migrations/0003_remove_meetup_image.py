# Generated by Django 4.1.3 on 2022-12-04 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_remove_meetup_date_remove_meetup_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='image',
        ),
    ]