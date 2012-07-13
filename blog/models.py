from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib import admin

class Blog(models.Model):
	title = models.CharField(max_length=32)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	isPrivate= models.BooleanField(default=False)
	class Meta(models.Model):
		ordering = ['date']
	def displayText(self):
		return mark_safe(self.text)
	def __unicode__(self):
		return u'%s' % ( self.title)	
class Comment(models.Model):
	text = models.TextField(null=False)
	date = models.DateTimeField(auto_now_add=True)
	user = models.CharField(max_length=20)
	belongs_to_blog = models.ForeignKey('Blog')

class Image(models.Model):
	image_field = models.ImageField(upload_to='uploads/')
	belongs_to_blog = models.ForeignKey('Blog')
	title = models.CharField(max_length=32)
	def __unicode__(self):
		return u'%s' % ( self.title)	

