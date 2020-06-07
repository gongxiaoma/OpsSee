from django.contrib import admin
from .models import UserInfo
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(UserAdmin):
    list_display = ['username', 'email', 'realname', 'qq', 'wechat', 'mobile']
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (_('Personal info'), { 'fields': ('realname', 'email', 'qq', 'wechat', 'mobile')})


