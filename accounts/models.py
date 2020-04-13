
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='media/',blank=True)
    my_subscribed_magazine=models.ManyToManyField('magazine.Magazines',blank=True,null=True)


    def ascii(self):
        userha=self.user.username
        return ord(userha[0].upper())

    def __str__(self):
        return str(self.user)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        UserModel.objects.create(user=instance)

#post_save.connect(create_profile,sender=User)
CHOICES=(
    ('Someone Liked Your WebCast .','LK'),
    ('Someone Viewed Your WebCast .','VC'),
    ('Someone Commented On Your WebCast .','VM'),
    ('Someone Subscribed Your Magazine .','SM'),
    ('New Cast From Your SubScribed Magazine .','LA')
)


class Notifications(models.Model):
    notify_to=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    notify=models.CharField(max_length=40,choices=CHOICES)

    def __str__(self):
        return self.notify

ACHOICES=(
    ('You Liked Someone"s WebCast .','LK'),
    ('You Viewed Someone"s WebCast .','VC'),
    ('You Commented On Someone"s WebCast .','VM'),
    ('You Subscribed Someone"s Magazine .','SM'),
    ('You Created a New WebCast .','LA')
)


class Activity(models.Model):
    act_of=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    activity=models.CharField(max_length=55,choices=ACHOICES)

    def __str__(self):
        return self.activity
