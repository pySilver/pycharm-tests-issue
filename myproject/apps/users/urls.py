from django.conf.urls import patterns, url

from views import ListUsers

urlpatterns = patterns(
    '',
    url(r'^users', ListUsers.as_view(), name="users-list"),
)
