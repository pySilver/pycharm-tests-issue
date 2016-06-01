from django.conf.urls import patterns, url

from views import ListNotes

urlpatterns = patterns(
    '',
    url(r'^notes', ListNotes.as_view(), name="notes-list"),
)
