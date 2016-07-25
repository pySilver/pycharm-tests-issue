# -*- coding: utf-8 -*-
from django.test import TestCase
from ..models import Note, MyNoteException


class NotesTests(TestCase):
    def test_note_create(self):
        note = Note()
        note.title = "Sample note"
        note.body = "note body goes here"
        note.save()

        self.assertIsNotNone(note.pk)
        self.assertEqual(note.title, "Sample note")
        self.assertEqual(note.title, "NOT A VALID NOTE BODY")

    def test_is_note_completed(self):
        note = Note()
        self.assertRaisesMessage(MyNoteException, "Note is not yet completed!", note.is_completed)
