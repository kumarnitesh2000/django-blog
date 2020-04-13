
from django.urls import path
from . import views
app_name='magazine'
urlpatterns = [

    path('',views.land,name='land'),
    path('profile/<str:username>/',views.all_casts,name="home"),
    path('cast/<slug:slug>/',views.cast,name='cast')

]
