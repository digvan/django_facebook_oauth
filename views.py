# Python
import urllib, simplejson

# Django
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import login, logout, authenticate

# Custom
from facebook.utils import get_facebook_profile
from facebook.models import FacebookUser
        
def authenticate_view(request):
    code = request.GET.get('code', None)
    args = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': request.build_absolute_uri(reverse('facebook.views.authenticate_view')),
        'scope': 'email,user_birthday,publish_stream',
    }
    
    if code != None:
        user = authenticate(token=code, request=request)
        
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(reverse('facebook.views.register_view'))
    else:
        return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))

def register_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'])
        fb_user = FacebookUser(user=user, facebook_id=request.session['fb_id'])
        fb_user.save()
        return HttpResponseRedirect(reverse('facebook.views.authenticate_view'))
    else:
        return render_to_response('member/register-facebook.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def test_view(request):
    profile = get_facebook_profile(request.user)
    return HttpResponse(simplejson.dumps(profile))