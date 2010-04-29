from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import login, logout, authenticate
from facebook.models import *
import urllib, cgi, simplejson
		
def authenticate_view(request):
	code = request.GET.get("code",None)
	args = dict(client_id=settings.APP_ID, callback="http://" + Site.objects.get(id=settings.SITE_ID).domain + '/authenticate/')
	if code != None:
		user = authenticate(token=code, request=request)
		if user != None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/register/')
	else:
		return HttpResponseRedirect("https://graph.facebook.com/oauth/authorize?" + urllib.urlencode(args))


def register(request):
	if request.method == "POST":
		user = User.objects.create_user(request.POST["username"], request.POST["email"])
		fb_user = FacebookUser(user = user, facebook_id = request.session['fb_id'])
		fb_user.save()
		return HttpResponseRedirect('/authenticate/')
	else:
		return render_to_response("anonymous/register.html")
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')