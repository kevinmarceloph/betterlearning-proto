from django.db import models
from model_utils.models import TimeStampedModel

from .managers import JournalManager


class Topic(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.name


class Resource(TimeStampedModel):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100, blank=True)
    text = models.TextField(blank=True)

    topics = models.ManyToManyField(Topic, related_name='resources', blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.name


class Icon(TimeStampedModel):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.name


class Review(TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='reviews')
    resource = models.ForeignKey(Resource, related_name='reviews')

    rating = models.PositiveIntegerField(null=True, blank=True)
    text = models.TextField(blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'{} reviews {}: {} ({})'.format(self.user, self.resource, self.rating, self.text[:40])


class Journal(TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='journals')

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.ForeignKey(Icon, related_name='journals', null=True, blank=True)
    objectives = models.TextField(blank=True)
    description = models.TextField(blank=True)

    topics = models.ManyToManyField(Topic, related_name='journals', blank=True)
    resources = models.ManyToManyField(Resource, related_name='journals', blank=True)

    closed = models.DateTimeField(null=True, blank=True)

    objects = JournalManager()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.name


class Step(TimeStampedModel):
    journal = models.ForeignKey(Journal, related_name='steps')
    order = models.PositiveIntegerField(default=0)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    resource = models.ForeignKey(Resource, related_name='steps', null=True, blank=True)
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.name

class Entry(TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='entries', null=True, blank=True)
    journal = models.ForeignKey(Journal, related_name='entries')
    step = models.ForeignKey(Step, related_name='entries', null=True, blank=True)

    text = models.TextField(blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'#{}, {}: {}'.format(self.id, self.journal, self.text[:40])


class EntryPhoto(TimeStampedModel):
    entry = models.ForeignKey(Entry, related_name='photos')
    photo = models.ImageField(upload_to='journal/entry/photos')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'#{}: {}'.format(self.entry_id, self.photo.name)


class EntryFile(TimeStampedModel):
    entry = models.ForeignKey(Entry, related_name='files')
    file = models.FileField(upload_to='journal/entry/files')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'#{}: {}'.format(self.entry_id, self.file.name)


class EntryLink(TimeStampedModel):
    entry = models.ForeignKey(Entry, related_name='links')
    link = models.URLField(max_length=100)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'#{}: {}'.format(self.entry_id, self.link)
