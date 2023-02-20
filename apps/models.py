from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    phone = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'
    
    def __str__(self):
        return self.email


#edit video
class VideoEdit(models.Model):
    img = models.ImageField(upload_to='media/', verbose_name='Surat')
    title = models.CharField(max_length=250, verbose_name='Wideonyň ady')
    video = models.FileField(upload_to='video', verbose_name='Wideo webinar')

    class Meta:
        verbose_name = 'Wideo'
        verbose_name_plural = 'Wideo'

    def __str__(self):
        return self.title


class ControlVideo(models.Model):
    user = models.ForeignKey(User, related_name='Ulanyjy', on_delete=models.CASCADE)
    video_name = models.ForeignKey(VideoEdit, related_name='wideo', on_delete=models.CASCADE)
    doly_wagty = models.CharField(max_length=200)
    gorulen_aralayk = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Wideony görenler'
        verbose_name_plural = 'Wideony görenler'

    def __str__(self):
        return self.user.username
