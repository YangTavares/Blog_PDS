from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

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
			return render(request, 'blog/user_login.html')
	else:
		return render(request, 'blog/user_login.html')

def user_new(request):
	if request.method == "POST":
		username = request.POST.get('username')
		email    = request.POST.get('email')
		password = request.POST.get('password')
		new_user = User.objects.create_user(username,email,password)
		new_user.save()	
		#form = UserForm(request.POST)
        #if form.is_valid():
        #    custom_user = form.save(commit=False)
        #    custom_user.save()
           # return redirect('post_detail', pk=post.pk)
    #else:
    #    form = UserForm()
	return render(request, 'blog/user_new.html')

def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
 	if request.method == "POST":
 		form = CommentForm(request.POST)	
 		if form.is_valid():
 			comment = form.save(commit=False)
 			comment.post_id = Post.objects.get(pk=pk)	
 			comment.author = request.user
 			comment.created_date = timezone.now()
 			comment.save()
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post_id=post)
	form = CommentForm()
	return render(request, 'blog/post_detail.html', {'post': post,'comments': comments,'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
           # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#def comment_new(request,post):
#	if request.method == "POST":
#		form = CommentForm(request.POST)	
#		if form.is_valid():
#			comment = form.save(commit=False)
#			comment.post_id = post	
#			comment.author = request.user
#			comment.created_date = timezone.now()
#			comment.save()
#	return render(request, 'blog/post_edit.html', {'form': form})
	
