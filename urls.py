from django.conf.urls.defaults import *
from facebook.views import login,logout,home

urlpatterns = patterns('',
    url(r'^login/?$', view=login,name='login'),
    url(r'^logout/?$', view=logout,name='logout'),
    url(r'^$', view=home,name='home'),
)
