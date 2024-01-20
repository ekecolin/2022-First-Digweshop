from django.contrib import admin

# Register your models here.
#*zfrom django.contrib.auth.admin import UserAdmin
#*from .models import APIUser

#*admin.site.register(APIUser, UserAdmin)
from .models import *

admin.site.register(APIUser)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Order)