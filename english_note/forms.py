from django import forms
from django.db.models import fields
from .models import Sentence

class englishNoteForm(forms.ModelForm):

    class Meta:
        model = Sentence
        fields = '__all__'