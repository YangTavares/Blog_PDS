from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('post_pic','post_text','title', 'text',)
	def clean_text(self):
		data = self.cleaned_data['text']
		if "fred@example.com" not in data:
			raise forms.ValidationError("You have forgotten about Fred!")
		
		# Always return a value to use as the new cleaned data, even if
		# this method didn't change it.
		return data

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ( 'text',)

class UserForm(forms.ModelForm):

	password=forms.CharField(max_length=250,widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ( 'username', 'email', 'password',)
	def clean_username(self):
		data = self.cleaned_data['username']
		if User.objects.filter(username=data).exists():
			raise forms.ValidationError("User already exists!")
		return data
	def clean_email(self):
		data = self.cleaned_data['email']
		if User.objects.filter(email=data).exists():
			raise forms.ValidationError("Email already exists!")
		return data
	
class UserExtendForm(forms.ModelForm):

	class Meta:
		model = UserExtend
		fields = ('profile_pic',)

#class UserLoginForm(forms.ModelForm):
#
#	password=forms.CharField(max_length=250,widget=forms.PasswordInput())
#	class Meta:
#		model = User
#		fields = ('username', 'password',)
#	
#	def clean(self):
#		username = self.cleaned_data.get('username')
#		password = self.cleaned_data.get('password')
#		user = authenticate(username=username, password=password)
#		if not user or not user.is_active:
#			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
#		return self.cleaned_data
#	def login(self, request):
#		username = self.cleaned_data.get('username')
#		password = self.cleaned_data.get('password')
#		user = authenticate(username=username, password=password)
#		return user
