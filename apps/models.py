from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

#Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, username, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            mobile = mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, username, mobile, **extra_fields)

    
    def create_superuser(self, email, password, username, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, username, mobile, **extra_fields)


#Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile']

    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'



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
