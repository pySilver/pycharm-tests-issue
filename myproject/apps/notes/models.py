# -*- coding: utf-8 -*-
from django.db import models


class Note(models.Model):

    title = models.CharField(max_length=32)

    body = models.TextField()

