# Generated by Django 3.1.14 on 2023-11-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
    ]