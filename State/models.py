# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=30)



# Create your models here.
