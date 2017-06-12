from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from itertools import chain
from operator import attrgetter

def users_chat(request,pk):
	if request.method == "POST":
		damoa_text = request.POST.get('message')
		sender = request.user
		receiver = User.objects.get(pk=pk)
		new_damoa = Damoa(sender=sender, receiver=receiver, text=damoa_text)
		new_damoa.save()
	senders = Damoa.objects.filter(sender__pk=pk)
	receivers = Damoa.objects.filter(receiver__pk=pk)
	sender_receiver_messages = sorted(chain(senders,receivers),key=attrgetter('created_date'))
	if sender_receiver_messages:
		return render(request, 'blog/users_chat.html',{'receiver_pk':pk, 'sender_messages':sender_receiver_messages})
	else:
		return render(request, 'blog/users_chat.html',{'receiver_pk':pk})

def search_db(request):
	if request.method == "POST":
		if request.POST.get('search_option')=="blog_user":
			name = request.POST.get('username')
			usernames = User.objects.filter(username__contains=name)
			if usernames.exists():
				found_flag=1
			else:
				found_flag=0
			return render(request, 'blog/search_db.html', {'usernames':usernames, 'found_flag':found_flag})
		elif request.POST.get('search_option')=="user_message":
			name = request.POST.get('username')
			damoa_message = Damoa.objects.filter(text__contains=name, receiver=request.user) | Damoa.objects.filter(text__contains=name, sender=request.user)

			if damoa_message.exists():
				found_flag=1
			else:
				found_flag=0
			return render(request, 'blog/search_db.html', {'damoa_message':damoa_message, 'found_flag':found_flag})
		elif request.POST.get('search_option')=="blog_post" or True:
			text = request.POST.get('username')
			blog_post = Post.objects.filter(text__contains=text)

			if blog_post.exists():
				found_flag=1
			else:
				found_flag=0
			return render(request, 'blog/search_db.html', {'blog_post':blog_post, 'found_flag':found_flag})
	found_flag=1
	return render(request, 'blog/search_db.html')

def user_logout(request):
	logout(request)
	return render(request, 'blog/user_logout.html')

def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		login_user = authenticate(username = username,password = password)
		if login_user is not None:
			login(request, login_user)
			return render(request, 'blog/post_list.html')
		else:
			invalid_user = "yes"
			return render(request, 'blog/user_login.html',{'invalid_user':invalid_user})
	else:
		return render(request, 'blog/user_login.html')


def user_new(request):
	exist_flag = 0
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES,prefix='form')
		extendform = UserExtendForm(request.POST, request.FILES,prefix='extendform')
		if form.is_valid() and extendform.is_valid():
			new_user = form.save()
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			user_extend = extendform.save(commit=False)
			user_extend.soul = new_user
			user_extend.profile_pic.name = str(new_user.pk)+'.png'
			user_extend.save()
	else:
		form = UserForm(prefix='form')
		extendform = UserExtendForm(prefix='extendform')
	return render(request, 'blog/user_new.html', {'exist_flag':exist_flag, 'form':form,'extendform':extendform})

def post_list(request):
	posts = Post.objects.filter()
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	if request.method == "POST":
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post_id = Post.objects.get(pk=pk)
			comment.author = request.user
			comment.created_date = timezone.now()
			comment.save()
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post_id=post.id)
	form = CommentForm()
	return render(request, 'blog/post_detail.html', {'post': post,'comments': comments,'form': form})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.post_pic.name = str(post.pk)+'.png'
			post.save()
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.post_pic.name = str(post.pk)+'.png'
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

