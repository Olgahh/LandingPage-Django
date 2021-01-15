from django.db import models
from django.contrib.auth.models import User
from django_lifecycle import LifecycleModelMixin, hook, AFTER_CREATE
from django.core.mail import EmailMessage
from django.core.mail import send_mail
# Create your models here.


class Organization(LifecycleModelMixin, models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(blank=True, null=True)
    email = models.EmailField(blank=False)
    basic_information = models.ForeignKey(
        'BasicInfo', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class BasicInfo(models.Model):
    title = models.CharField(max_length=120)
    about = models.TextField(blank=True)
    location = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12)
    details = models.ForeignKey('Detail', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Basic Info"


class Detail(models.Model):
    subtitle = models.CharField(max_length=120, blank=True)
    image = models.ImageField(blank=True, null=True)
    text = models.ForeignKey('Info', on_delete=models.CASCADE)


class Info(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Detailed Information"


class Profile(LifecycleModelMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    @hook(AFTER_CREATE)
    def send_user_mail(self):
        send_mail(
            f'Hello {user.username}',
            f'You have been successfully registered on {organization.name}',
            f'{organization.email}',
            [f'{user.email}', ]
        )
