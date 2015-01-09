from django.db import models


class JournalManager(models.Manager):
    def open(self):
        return self.get_queryset().filter(closed=None)

    def closed(self):
        return self.get_queryset().exclude(closed=None).order_by('-closed')
