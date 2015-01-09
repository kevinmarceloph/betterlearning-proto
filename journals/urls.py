from django.conf.urls import patterns, url

urlpatterns = patterns('journals.views',
    url(r'^$', 'view_home', name='view_home'),
    url(r'^journals/new/$', 'add_edit_journal', name='add_journal'),
    url(r'^journals/(?P<slug>[\w-]+)/edit/$', 'add_edit_journal', name='edit_journal'),
    url(r'^journals/(?P<slug>[\w-]+)/entries/new/$', 'add_edit_entry', name='add_entry'),
    url(r'^(?P<username>\w+)/$', 'view_profile', name='view_profile'),
    url(r'^(?P<username>\w+)/(?P<slug>[\w-]+)/$', 'view_journal', name='view_journal'),
    url(r'^(?P<username>\w+)/(?P<slug>[\w-]+)/(?P<id>\d+)/$', 'view_entry', name='view_entry'),
)
