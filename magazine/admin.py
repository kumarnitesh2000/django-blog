from django.contrib import admin
from .models import Magazines,Casts,Comments,Box

admin.site.register(Magazines)
# Register your models here.
admin.site.register(Casts)
admin.site.register(Comments)
admin.site.register(Box)
