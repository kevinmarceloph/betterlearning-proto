from django.contrib import admin

from .models import Topic, Resource, Journal, Step, Entry, EntryPhoto, EntryFile, EntryLink

admin.site.register(Topic)
admin.site.register(Resource)
admin.site.register(Journal)
admin.site.register(Step)
admin.site.register(Entry)
admin.site.register(EntryPhoto)
admin.site.register(EntryFile)
admin.site.register(EntryLink)
