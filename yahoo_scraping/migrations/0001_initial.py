# Generated by Django 3.2.7 on 2021-09-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('open', models.FloatField(verbose_name='Open')),
                ('high', models.FloatField(verbose_name='High')),
                ('low', models.FloatField(verbose_name='Low')),
                ('close', models.FloatField(verbose_name='Close*')),
                ('adj_close', models.FloatField(verbose_name='Adj Close**')),
                ('volume', models.PositiveIntegerField(verbose_name='Volume')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]