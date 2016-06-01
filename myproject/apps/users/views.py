# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class ListUsers(APIView):
    """View to list all users in the system."""
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = ['foo', 'bar', 'baz']
        return Response(usernames)
