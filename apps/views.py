from django.contrib import messages
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .serive import controlVideo
from django.contrib.auth import login, authenticate, logout as logout 
from django.contrib import messages
from .forms import*
from .models import *
from django.contrib.auth.hashers import make_password


def signup(request):
    if request.user.is_authenticated:
        return redirect('video')
    else:
        if request.method == 'POST':
            user = User.objects.create(
                username=request.POST['username'], 
                email=request.POST['email'], 
                phone=request.POST['phone'], 
                password=make_password(request.POST['password']))
            # user.save()
            emailSubject = "Ýönekeý H.K-y"
            message = "Salam! Siz biziň saýtymyza üstünlikli kabul edildiňiz!"
            email = EmailMessage(
            emailSubject,
            message,
            to=[user.email]
            )
            email.send()
            if request.method == 'POST':
                email = request.POST.get('email')
                password = request.POST.get('password')

                user = authenticate(email=email, password=password)
                login(request,user)
            return redirect('video')
        else:
            return render(request, 'index.html')


# def signin(request):
#     if request.user.is_authenticated:
#         return redirect('video')
#     else:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             user = authenticate(email=email, password=password)

#             if user is not None:
#                 login(request,user)
#                 return redirect('video')
#         context = {}
#         return render(request, 'base.html', context)


def video(request):
    if request.method == "POST":
        userId = request.POST.get("userId")
        videoId = request.POST.get("videoId")
        fullTime = request.POST.get("fullTime")
        stopTime = request.POST.get("stopTime")
        controlVideo(videoId, userId, fullTime, stopTime)
    player = VideoEdit.objects.all()

    context = {
        'player': player,
    }

    return render(request, 'video.html', context)










