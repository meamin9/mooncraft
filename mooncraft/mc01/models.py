# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GameUrl(models.Model):
    res_url = models.CharField(max_length=255)
