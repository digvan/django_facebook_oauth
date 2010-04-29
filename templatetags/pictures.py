from django import template

from ldt_general.models import Status, ActivityType

register = template.Library()

@register.simple_tag
def facebook_profile_picture(fb_id):
	return "<img src=\"http://graph.facebook.com/%s/picture?type=%s\" />" % (fb_id, "square")
