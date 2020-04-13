from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . forms import LoginForm
app_name='accounts'
urlpatterns = [

    path('image/',views.imageupload,name="image"),
    path('login/',views.loginuser,name="login"),
    path('register/',views.reg_user,name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/loggedout.html",extra_context={'form':LoginForm()}), name="logout")
    #path('logout/',
         #auth_views.LogoutView.as_view(),
         #name="logout")

]
