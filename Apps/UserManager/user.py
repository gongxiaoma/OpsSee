#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther: gongxiaoma


from django.shortcuts import render
from Apps.Account.models import UserInfo

# Create your views here.
def userView(request):
    title = "OPSSEE | 用户管理"
    menuname = "index"
    username = request.user
    userinfolist = UserInfo.objects.filter(username=username)

    return render(request, 'UserManager/user.html', locals())