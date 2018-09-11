from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile,Yaarbelli,Post
from .forms import PostForm





# Create your views here.

def user_login(request):
	context = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username, password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect(reverse('user_home'))
		else:
			context["error"] = "Provide valid credentials !!"
			return render(request,'loginlogout.html',context)
	else:
		return	render(request,'loginlogout.html',context)


def home(request,pk = None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user
	follower = Yaarbelli.objects.filter(follower__pk=user.pk)
	following = Yaarbelli.objects.filter(following__pk=user.pk)
	posts = Post.objects.filter(user=user.pk)


	args = { 'user':user,'follower':follower,'following':following,'posts':posts}


	return render(request, "home.html",args)



def alluserpost(request):
	posts = Post.objects.all().order_by('-created')	
	args = {'posts':posts}

	return render(request,"alluserpost.html",args)




def user_logout(request):
	logout(request)
	return render(request,'loginlogout.html')
   

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    loginuser = User.objects.get(pk = request.user.pk)
    try:
     	Yaarbelli.objects.get(follower=loginuser,following=friend)
     	if operation == 'remove':
     		table = Yaarbelli.objects.get(follower=loginuser,following=friend)
     		table.delete()
     
    except: 	
	    if operation == 'add':
	    	table = Yaarbelli(
	    		follower = loginuser,
	    		following = friend
	    		)
	    	table.save()
        
    return follower(request,pk)
    


def following(request, pk):
	following = Yaarbelli.objects.filter(follower__pk=pk).exclude(following__pk=request.user.pk)

	followbyloginuser = Yaarbelli.objects.filter(following__pk=request.user.pk)


	temp=list(map(lambda x:x.follower,list(followbyloginuser)))
	for i  in followbyloginuser:
		print(i.follower,"\n")
	print(temp)
	return render(request,'following.html',{'following':following,'temp':temp})


def follower(request,pk):
	follower = Yaarbelli.objects.filter(following__pk=pk).exclude(follower__pk=request.user.pk)
	following = Yaarbelli.objects.filter(follower__pk=pk)
	followbyloginuser = Yaarbelli.objects.filter(follower__pk=request.user.pk)
	temp=list(map(lambda x:x.following,list(followbyloginuser)))

	return render(request,'follower.html',{'follower':follower,'following':following,'temp':temp})
       

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect('user_home')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html',{form: form})



def addpost(request):
	if request.method == "POST":
		addform = PostForm(request.POST,request.FILES)
		if addform.is_valid():
			Post_item = addform.save(commit=False)
			Post_item.save()
			return redirect('user_home')	
	else:
		addform = PostForm()
	return render(request,'forms/addpostform.html',{'addform':addform})		

def search(request):
	q = request.GET.get('q')
	if q:
		users = User.objects.filter(username__icontains=q)
		return render(request,'search.html',{'users':users,'query':q})
	return HttpResponse('Please submit a search term')		



	#fedfdfdfdfdfdfdfdfdfdfdfdfd