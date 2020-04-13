from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .forms import LoginForm,RegisterForm,ImageForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from . import models
def loginuser(request):
    if request.method=='POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)

                    return HttpResponse("done")
                else:
                    return HttpResponse('disabled')
            else:
                return HttpResponse('no data ')
    else:
        form=LoginForm()

    return JsonResponse({"code":200})




def reg_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            print("True")
            cd=form.cleaned_data
            email=cd['email']
            username=cd['username']
            new_user=form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponse("successfuly registerd")
        else:
            return HttpResponse("not valid form")

    else:
        form=RegisterForm()
    return JsonResponse({"data":"not done ."})

def imageupload(request):
    username=str(request.user.username)
    user=User.objects.get(username=username)
    usermodel=models.UserModel.objects.get(user=user)
    form = ImageForm(request.POST or None,request.FILES or None,  instance=usermodel)

    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return JsonResponse("success")
    return HttpResponse("not done")