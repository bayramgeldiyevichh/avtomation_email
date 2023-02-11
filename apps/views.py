from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .serive import controlVideo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login, authenticate, logout as logout 
from django.contrib import messages
from .forms import CreateUserForm
from .forms import*
from .models import *

@login_required(login_url='signin')


def index(request):

    return render(request, 'index.html')

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


# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         if request.method == 'POST':
#             form = SignupForm(request.POST)
#             if form.is_valid():
                # save form in the memory not in database
                # user = form.save(commit=False)
                # user.is_active = False
                # user.save()
                # to get the domain of the current site
                # current_site = get_current_site(request)
                # mail_subject = 'Ýönekeý H.K-nyň Webinar saýty size hödürleýär'
                # message = render_to_string('acc_active_email.html', {
                    # 'user': user,
                    # 'domain': current_site.domain,
                    # 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    # 'token':account_activation_token.make_token(user),
        #         })
        #         to_email = form.cleaned_data.get('email')
        #         email = EmailMessage(
        #             mail_subject, message, to=[to_email]
        #         )
        #         email.send()
        #         return redirect('login')
        # else:
        #     form = SignupForm()
        # return render(request, 'signup.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                mail_subject = "Ýönekeý H.K-sy"
                message = render_to_string('acc_active_email.html', {

                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return redirect('signin')
            else:
                form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            email = authenticate(email=email, password=password)

            if email is not None:
                login(request,email)
                return redirect('index')
            else:
                messages.info(request, 'Ulanyjy email poctasy ýa-da paroly nädogry')
        context = {}
        return render(request, 'signin.html', context)



