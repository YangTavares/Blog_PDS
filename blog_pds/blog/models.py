from django.db import models
from django.utils import timezone

class UserExtend(models.Model):
	soul = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	profile_pic = models.ImageField()

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	post_pic = models.ImageField(upload_to='post_pic',default='')
	post_text = models.TextField(default='')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
	        default=timezone.now)
	published_date = models.DateTimeField(
	        blank=True, null=True)
	keyword= models.TextField(default='',blank=True,null=True)
	views = models.IntegerField(default=0,blank=True,null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
class Comment(models.Model):
	post_id = models.ForeignKey(Post, related_name='post_id')
	author = models.CharField(max_length=200, default='')
	c_email = models.CharField(max_length=200, default='')
	text = models.TextField()
	created_date = models.DateTimeField(
	        default=timezone.now)
class Denounce(models.Model):
	denounce_comment = models.OneToOneField(Comment)
	is_okay = models.CharField(max_length=200,default='no')
	@classmethod
	def create_denounce(cls, denounce_comment):
		denounce = cls(denounce_comment=denounce_comment)
		# do something with the book
		denounce.save()
		return denounce
class Damoa(models.Model):
	sender = models.ForeignKey('auth.User', related_name='test1') 
	receiver = models.ForeignKey('auth.User', related_name='test2')
	text = models.TextField(blank=True)
	created_date = models.DateTimeField(
	        default=timezone.now)
