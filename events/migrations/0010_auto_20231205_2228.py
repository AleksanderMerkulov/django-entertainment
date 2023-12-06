# Generated by Django 3.1.14 on 2023-12-05 12:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20231202_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('description', models.TextField(default='', verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='close', max_length=20, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='source',
            field=models.CharField(default='', max_length=200, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 12, 27, 37, 340196, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='events.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='typeOfEvent',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='events.typeofevent'),
            preserve_default=False,
        ),
    ]