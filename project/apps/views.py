from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# @login_required(login_url='login')



def index(request):

    return render(request, 'index.html')

def video(request):
    player = VideoEdit.objects.all()

    context = {
        'player': player,
    }

    return render(request, 'video.html', context)



def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                # save form in the memory not in database
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # to get the domain of the current site
                # current_site = get_current_site(request)
                mail_subject = 'Ýönekeý H.K-nyň Webinar saýty size hödürleýär'
                message = render_to_string('acc_active_email.html', {
                    # 'user': user,
                    # 'domain': current_site.domain,
                    # 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    # 'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return redirect('login')
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})


# login
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            email = authenticate(request, email=email, password=password)

            if email is not None:
                login(request, email)
                messages.success(request, f' welcome {username} !!')
                return redirect('index')
            else:
                messages.info(request, 'Ulanyjy email poctasy ýa-da paroly nädogry')
            
        return render(request, 'login.html')


#logout
# @login_required
def logout(request):
    django_logout(request)
    return redirect('index')


