# Django + Facebook Graph API authentication
This is a python app to use the new Graph API authentication with Django. It uses the standard authentication build into Django. 
## Basic setup
1. Put the files into a folder named 'Facebook' in your Django project.
2. Add the facebook context processor
`
TEMPLATE_CONTEXT_PROCESSORS = (
	"lets-do-this.facebook.context_processors.facebook",
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
)
`
1. Install app by adding 'facebook' to INSTALLED_APPS in settings.py
2. Add APP_ID and APP_SECRET to settings.py
3. Run manage.py syncdb
## Template Tags Examples
To use the template tag to view the current user, add the following line to a template `{% load lets-do-this.facebook.backend.FacebookBackend %}{% facebook_profile_picture fb_user.facebook_id %}`