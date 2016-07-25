# -*- coding: utf-8 -*-
from django.db import models


class MyNoteException(BaseException):
    pass


class Note(models.Model):

    title = models.CharField(max_length=32)

    body = models.TextField()

    def is_completed(self):
        if not self.pk:
            raise MyNoteException("Note is not yet completed!")

        return True
