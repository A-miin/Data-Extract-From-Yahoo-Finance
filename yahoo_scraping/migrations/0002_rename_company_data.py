# Generated by Django 3.2.7 on 2021-09-29 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo_scraping', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Data',
        ),
    ]
