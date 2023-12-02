import datetime

import django.utils.timezone
from django.db import models


class Event(models.Model):
    title = models.CharField('Title', max_length=50, default='')
    anons = models.CharField('Anons', max_length=100, default='')
    date = models.DateTimeField('Date', default=django.utils.timezone.now())
    creator_id = models.ForeignKey('auth.User', models.SET(1))

    def __str__(self):
        return self.title
