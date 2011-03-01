# Django
from django.conf.urls.defaults import *

# Custom
from facebook.views import authenticate_view, logout_view, register_view, test_view

urlpatterns = patterns('',
    url(r'^authenticate/?$', view=authenticate_view, name='authenticate'),
    url(r'^logout/?$', view=logout_view, name='logout'),
    url(r'^register/?$', view=register_view, name='register'),
    url(r'^test/?$', view=test_view, name='test'),
)