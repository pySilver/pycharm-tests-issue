# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class ListNotes(APIView):
    """View to list all notes in the system."""
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        notes = ['note one', 'note two', 'note 42']
        return Response(notes)
