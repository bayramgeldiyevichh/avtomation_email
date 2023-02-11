from django.contrib import admin
from .models import *
from .forms import *
  
admin.site.register(User)
admin.site.register(VideoEdit)
admin.site.register(ControlVideo)
