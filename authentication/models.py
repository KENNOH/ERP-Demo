import imp
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.first_name + " - " + self.user.last_name

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'



@receiver(post_save,sender=User)
def update_profile(sender,instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
