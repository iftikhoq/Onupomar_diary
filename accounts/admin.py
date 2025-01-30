from django.contrib import admin
from .models import UserAccount, UserAddress, Borrow

admin.site.register(UserAccount)
admin.site.register(UserAddress)
admin.site.register(Borrow)