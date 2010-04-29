from django.conf.urls.defaults import *
from facebook.views import authenticate_view,logout_view,register

urlpatterns = patterns('',
    url(r'^authenticate/?$', view=authenticate_view,name='authenticate'),
    url(r'^logout/?$', view=logout_view,name='logout'),
    url(r'^register/?$', view=register,name='register'),
)
