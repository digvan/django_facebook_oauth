# Python
import urllib, simplejson

# Django
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Custom
from facebook.utils import get_facebook_profile
from facebook.models import FacebookUser

def authenticate_view(request):
    code = request.GET.get('code')
    args = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': request.build_absolute_uri(reverse('facebook.views.authenticate_view')),
        'scope': 'email,user_birthday,publish_stream',
    }
    
    if code != None:
        user = authenticate(token=code, request=request)
        
        if user != None:
            login(request, user)
            return_uri = request.session.get('fb_return_uri')
            if return_uri is None:
                return HttpResponseRedirect('/')
            else:
                del request.session['fb_return_uri']
                return HttpResponseRedirect(return_uri)
        
        else:
            return HttpResponseRedirect(reverse('facebook.views.register_view'))
    else:
        if request.GET.get('ignorereferer') != '1':
            referer = request.META.get('HTTP_REFERER')
            if not referer is None:
                request.session['fb_return_uri'] = referer
        
        return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))

def register_view(request):
    try:
        fb_profile = request.session['fb_profile']
    except KeyError:
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'])
        fb_user = FacebookUser(user=user, facebook_id=fb_profile['id'])
        fb_user.save()
        del request.session['fb_profile']
        return HttpResponseRedirect(reverse('facebook.views.authenticate_view') + '?ignorereferer=1')
    else:
        return render_to_response('member/register-facebook.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def test_view(request):
    profile = get_facebook_profile(request.user)
    return HttpResponse(simplejson.dumps(profile))