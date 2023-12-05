import datetime

import django.utils.timezone
from django.db import models


class Category(models.Model):
    title = models.CharField("Title", max_length=100, default='')
    description = models.TextField("Description", default="")


class TypeOfEvent(models.Model):
    name = models.CharField('Name', max_length=20, default='close')


class Event(models.Model):
    title = models.CharField('Title', max_length=50, default='')
    anons = models.CharField('Anons', max_length=100, default='')
    date = models.DateTimeField('Date', default=django.utils.timezone.now())
    creator_id = models.ForeignKey('auth.User', models.SET(1))
    category = models.ForeignKey('events.Category', models.SET(1))
    source = models.CharField("Source", max_length=200, default='')
    typeOfEvent = models.ForeignKey('events.TypeOfEvent', models.SET(1))

    def __str__(self):
        return self.title
