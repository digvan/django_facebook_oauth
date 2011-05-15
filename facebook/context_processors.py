# Custom
from facebook.models import FacebookUser

def facebook(request):
    fb_user = None
    try:
        if request.user.is_authenticated():
            fb_user = FacebookUser.objects.get(user=request.user.id)
    except FacebookUser.DoesNotExist:
        pass
    return { 'fb_user': fb_user }