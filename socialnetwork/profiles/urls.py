from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialnetwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'profiles.views.index'),
    url(r'^profiles/(?P<profile_id>\d+$)', 'profiles.views.show'),
)