# Python
import urllib, simplejson

# Custom
from facebook.models import FacebookUser

def get_facebook_profile(user):
    try:
        fb_user = FacebookUser.objects.get(user=user)
        user_json = urllib.urlopen('https://graph.facebook.com/me?' + urllib.urlencode(dict(access_token=fb_user.access_token)))
        profile = simplejson.load(user_json)
        return profile
    except:
        return None