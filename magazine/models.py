from django.urls import reverse
from django.db import models
import datetime
from taggit.managers import TaggableManager
from urllib.parse import quote
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
def makeslugs(date):
    year=date.year
    day=date.day
    month=date.month
    s=f'-{year}-{month}-{day}'
    return s


class Magazines(models.Model):
    author=models.ForeignKey('accounts.UserModel',on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    subscribed_user=models.ManyToManyField(User,blank=True,verbose_name="subscribed")

    is_monetize=models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Casts(models.Model):
    publish=models.DateTimeField(default=datetime.datetime.now())
    publish_by=models.ForeignKey('accounts.UserModel',on_delete=models.CASCADE,related_name="published_by",blank=True,null=True)
    magazine=models.ForeignKey(Magazines,on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    content=models.TextField(max_length=1000,blank=True,null=True)
    thumbnail=models.ImageField(upload_to="media/",null=True,blank=True)
    upvotes=models.ManyToManyField('accounts.UserModel',blank=True,verbose_name="liked")
    slug=models.SlugField(max_length=100,blank=True,null=True,unique=True)
    time=models.PositiveSmallIntegerField(default=0)
    tag=TaggableManager()
    def __str__(self):
        return self.title
    #Then override models save method:
    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            #self.slug = slugify(makeslugs(self.title,self.publish)) #Or whatever you want the slug to use
            self.slug=slugify(self.title)+makeslugs(self.publish)
        super(Casts, self).save(*args, **kwargs)
    def get_absolute_url(self):
        slug=slugify(self.title)+makeslugs(self.publish)
        return reverse('magazine:cast',kwargs={'slug':slug})

class Comments(models.Model):
    comment_by=models.ForeignKey('accounts.UserModel',on_delete=models.CASCADE)
    comment=models.CharField(max_length=100,null=True,blank=True)
    commented_cast=models.ForeignKey(Casts,on_delete=models.CASCADE,blank=True,null=True)
    is_pos=models.BooleanField(default=True)
    upvotes=models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.comment} by {self.comment_by}'



class Box(models.Model):
    cast=models.ForeignKey(Casts,on_delete=models.CASCADE,null=True,blank=True)
    file=models.FileField(upload_to='media/')
    text=models.TextField(max_length=1000)

    def __str__(self):
        return self.text.split(" ")[0]

