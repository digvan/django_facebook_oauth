# Django + Facebook Graph API authentication
This is a python app to use the new Graph API authentication with Django. It uses the standard authentication build into Django. 
## Basic setup
1. Put the files into a folder named 'facebook' in your Django project.
2. Add the facebook context processor to `TEMPLATE_CONTEXT_PROCESSORS` in settings.py: `"facebook.context_processors.facebook",`
3. Add the facebook authentication backend to settings.py `AUTHENTICATION_BACKENDS = ('facebook.backend.FacebookBackend')`
4. Add facebook app to `INSTALLED_APPS` in settings.py: `'facebook',
5. Add `FACEBOOK_APP_ID` and `FACEBOOK_APP_SECRET` to settings.py
6. Add this line to the urlpatterns in urls.py `(r'^facebook/', include('facebook.urls')),`
7. Run `python manage.py syncdb`
8. Add `{{ fb_user.facebook_id }}` to a template. It should show the logged in user's facebook id.
9. Test by going to '/facebook/authenticate' then to the template you added the facebook id to

## Template Tags Examples
To use the template tag to view the current user, add the following line to a template
`{% load pictures %}{% facebook_profile_picture fb_user.facebook_id %}`