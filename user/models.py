from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(unique=True, max_length=64, verbose_name='유저키')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        verbose_name = '유저 프로필'
        verbose_name_plural = '유저 프로필'

    def __str__(self):
        return self.user.username



#class ProfileHasTag(models.Model):
    