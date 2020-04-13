from django.contrib import admin
from .models import UserModel,Notifications,Activity
# Register your models here.
admin.site.register(UserModel)
admin.site.register(Notifications)
admin.site.register(Activity)