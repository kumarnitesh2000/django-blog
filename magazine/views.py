from django.shortcuts import render,redirect
from accounts.forms import LoginForm,RegisterForm
from .models import Magazines,Casts,Comments
from accounts.models import UserModel
from django.contrib.auth.models import User
from . forms import CommentForm
from django.http import JsonResponse
def land(request):

    return render(request,'magazine/landing.html',context={'form':LoginForm(),'reg_form':RegisterForm()})
def cast(request,slug):
    if request.method=='POST':
        title=request.POST['cast']
        cast=Casts.objects.get(title=title)
        u = User.objects.get(username=str(request.user))
        user = UserModel.objects.get(user=u)
        comment=Comments(is_pos=True,upvotes=0,commented_cast=cast,comment_by=user,comment=request.POST['comment'])
        comment.save()
        return redirect('magazine:cast',slug=slug)
    u = User.objects.get(username=str(request.user))
    user = UserModel.objects.get(user=u)
    Cast=Casts.objects.get(slug=slug)

    return render(request,"magazine/cast.html",context={"cast":Cast,'form':CommentForm,'user':user})


def all_casts(request,username):
    user=User.objects.get(username=username)
    usermodel=UserModel.objects.get(user=user.id)
    magazines=usermodel.my_subscribed_magazine.all()
    #magazine is the 1 subscribed magazine.
    if len(magazines)>0:
        magazine=magazines[0]
        print("subscribed mah=gazine ",magazine)
    #author of the magazine
        author=magazine.author.__str__()
        print("author ",author)
    #total magazine subscribers
        total_subscribers=len(magazines)
        print("total subscribers ",total_subscribers)
    #3 notifications
    else:
        author=""
        magazine=[]
        total_subscribers=0
    print("done")
    three_activity=usermodel.activity_set.all()[:3]
    three_activit=[]
    for i in three_activity:
        three_activit.append(i.activity)
    print("activities ",three_activit)
    #3 notifications
    three_notification=usermodel.notifications_set.all()[:3]
    print("notifications ",three_notification)
    #3 casts from subscribed magazines .
    #magazines from the subscribed channel
    subscribed_magazine=user.magazines_set.all()
    print("magazine subscribed  ",subscribed_magazine)
    casts=[]
    for magazin in subscribed_magazine:
        if magazin.casts_set.all():
            casts.append(magazin.casts_set.all())
    if len(casts)>3:
        casts=casts[:3]
    else:
        casts=casts[:len(casts)]
    castr = []
    print("done")
    if len(casts)>0:
        for cast1 in casts[0]:
            castr.append(cast1)
        print(castr)

    context={'author':author,'totsub':total_subscribers,'magazine':magazine,'threeact':three_activit,
             'threenot':three_notification,'webcasts':casts,'casts':castr}
    return render(request, "magazine/all.html",context)


