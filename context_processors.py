from facebook.models import FacebookUser

def facebook(request):
	try:
		fb_user = FacebookUser.objects.get(user = request.user.id)
	except FacebookUser.DoesNotExist:
		fb_user = None
	return { 'fb_user': fb_user }