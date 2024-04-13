from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from .models import CreateRoom
from .models import Message
from .forms import sign_up_form
from django.http import JsonResponse


# Create your views here.


def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html',{})
	else:
		return redirect('login')

def user_login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		return redirect('login')
	return render(request,'login.html',{})

def user_logout(request):	
	logout(request)
	return redirect('login')

def user_register(request):
	if request.method=='POST':
		form=sign_up_form(request.POST)
		if form.is_valid:
			form.save()
			return redirect('login')
	else:
		form=sign_up_form()
	return render(request,'register.html',{'form':form})



def work(request,slug):
	return render(request,'work.html',{'slug':'','username':'','roomname':''})

def send(request):
	if request.user.is_authenticated:
		message=request.POST['message']
		username=request.POST['username']
		slug=request.POST['room_slug']
		roomname=request.POST['room_name']
		Message.objects.create(username=username,value=message,slug=slug)
		return HttpResponse()
	else:
		return redirect('login')

def user_work(request,slug,username,roomname):
	if request.user.is_authenticated:

		try :
			CreateRoom.objects.get(slug=slug)
		except:
			CreateRoom.objects.create(slug=slug,name=roomname)
		#all_messages=Message.objects.filter(slug=slug)
		return render(request,'work.html',{#'all_messages':all_messages,
			'username':username,'room':CreateRoom.objects.get(slug=slug)})
	else:
		return redirect('login')

def getmessages(request,room):
	if request.user.is_authenticated:
		all_messages=Message.objects.filter(slug=room)
		return JsonResponse({'all_messages':list(all_messages.values())})
	else:
		return redirect('login')


