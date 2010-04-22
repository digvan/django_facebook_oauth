from django.db import models
from django.core.exceptions import *
#import logging

#LOG_FILENAME = 'facebook.log'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
#LOGGER = logging.getLogger('DBLog')

class FacebookUser(models.Model):
	facebook_id = models.CharField(max_length=150,unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(blank=True,null=True)
	name = models.CharField(max_length=150)
	profile_url = models.CharField(max_length=350,blank=True,null=True)
	access_token = models.CharField(max_length=150,blank=True,null=True)