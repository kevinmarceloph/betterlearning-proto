from django import forms
from django.utils.text import slugify

from .models import Journal, Entry


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('name', 'icon', 'objectives', 'description', 'topics')

    def save(self, user):
        instance = super(JournalForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.user = user
        instance.save()

        return instance


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('text',)

    def save(self, journal):
        instance = super(EntryForm, self).save(commit=False)
        instance.journal = journal
        instance.user = journal.user
        instance.save()

        return instance
