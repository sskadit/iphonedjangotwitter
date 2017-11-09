from django.db import models

# Create your models here.



class AppleTrendingHastags(models.Model):
	text = models.CharField(max_length=100000,null=True,blank=True)
	source = models.CharField(max_length=100000,null=True,blank=True)
	author = models.CharField(max_length=100000,null=True,blank=True)
	name = models.CharField(max_length=100000,null=True,blank=True)
	time_zone = models.CharField(max_length=100000,null=True,blank=True)
	user_language = models.CharField(max_length=100000,null=True,blank=True)
	followers = models.CharField(max_length=100000,null=True,blank=True)
	user_description = models.CharField(max_length=100000,null=True,blank=True)
	geo_enabled = models.CharField(max_length=100000,null=True,blank=True)
	friends = models.CharField(max_length=100000,null=True,blank=True)
	retweets = models.CharField(max_length=100000,null=True,blank=True)
	location = models.CharField(max_length=100000,null=True,blank=True)
	user_id = models.CharField(max_length=100000,null=True,blank=True)
	coordinates = models.CharField(max_length=100000,null=True,blank=True)
	place = models.CharField(max_length=100000,null=True,blank=True)
	possible_senstive = models.CharField(max_length=100000,null=True,blank=True)
	status_created = models.CharField(max_length=100000,null=True,blank=True)
	link = models.CharField(max_length=1000,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '%s,%s' % (self.text,self.author)




class IphoneX(models.Model):
	text = models.CharField(max_length=100000,null=True,blank=True)
	source = models.CharField(max_length=100000,null=True,blank=True)
	author = models.CharField(max_length=100000,null=True,blank=True)
	name = models.CharField(max_length=100000,null=True,blank=True)
	time_zone = models.CharField(max_length=100000,null=True,blank=True)
	user_language = models.CharField(max_length=100000,null=True,blank=True)
	followers = models.CharField(max_length=100000,null=True,blank=True)
	user_description = models.CharField(max_length=100000,null=True,blank=True)
	geo_enabled = models.CharField(max_length=100000,null=True,blank=True)
	friends = models.CharField(max_length=100000,null=True,blank=True)
	retweets = models.CharField(max_length=100000,null=True,blank=True)
	location = models.CharField(max_length=100000,null=True,blank=True)
	user_id = models.CharField(max_length=100000,null=True,blank=True)
	coordinates = models.CharField(max_length=100000,null=True,blank=True)
	place = models.CharField(max_length=100000,null=True,blank=True)
	possible_senstive = models.CharField(max_length=100000,null=True,blank=True)
	status_created = models.CharField(max_length=100000,null=True,blank=True)
	link = models.CharField(max_length=1000,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '%s,%s' % (self.text,self.author)


