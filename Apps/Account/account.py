#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther: gongxiaoma

import re
import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import UserInfo
from .forms import LoginUserForm
from .forms import RegistUserForm
from .forms import UserInfoForm
from .forms import ChangePasswordForm

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        login_form = LoginUserForm(request.POST)

        # 合法性验证，比如是否为空，也就是说cleaned_data是获取过滤后的数据。
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username', '')
            password = login_form.cleaned_data.get('password', '')
            next_url = request.POST.get("next_url")
            try:
                if UserInfo.objects.filter(username=username):
                    user = authenticate(username=username, password=password)
                    if user:
                        if user.is_active:
                            login(request, user)
                        if next_url and next_url != "/Account/logout/":
                            return redirect(next_url)
                        else:
                            return redirect('/Account/index')
                    else:
                        tips = '账号或密码错误，请确认'
                else:
                    tips = '账号不存在，请注册'
            except Exception as e:
                print(e)
    next_url = request.GET.get("next", '')
    login_form = LoginUserForm()
    return render(request, 'Account/login.html', locals())

@login_required(login_url='/Account/login')
def indexView(request):
    title = "OPSSEE | 首页"
    menuname = "index"
    username = request.user
    userinfolist = UserInfo.objects.filter(username=username)

    return render(request, 'index.html', locals())

def logoutView(request):
    logout(request)
    return redirect('/Account/login')

def registerView(request):
    if request.method == 'POST':
        register_form = RegistUserForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            username = register_form.cleaned_data.get('username', '')
            password = register_form.cleaned_data.get('password', '')
            email = register_form.cleaned_data.get('email', '')
            realname = register_form.cleaned_data.get('realname', '')
            qq = register_form.cleaned_data.get('qq', '')
            wechat = register_form.cleaned_data.get('wechat', '')
            mobile = register_form.cleaned_data.get('mobile', '')

            # create_user是django自带，有密码加密功能
            user = UserInfo.objects.create_user(username=username, password=password, email=email, realname=realname, qq=qq, wechat=wechat, mobile=mobile)
            user.save()
            tips = '注册成功，请登录'
        else:
            print(register_form.cleaned_data)
            tips = '注册失败，请检查'
            error_msg = register_form.errors
            print(error_msg)
    register_form = RegistUserForm()
    return render(request, 'Account/register.html', locals())

@login_required
def changepasswordView(request):
    title = "OPSSEE | 修改密码"
    username = request.user
    userinfolist = UserInfo.objects.filter(username=username)
    if request.method == 'POST':
        changepassword_form = ChangePasswordForm(request.POST)
        if changepassword_form.is_valid():
            old_password = changepassword_form.cleaned_data.get('password', '')
            new_password = changepassword_form.cleaned_data.get('new_password', '')
            if UserInfo.objects.filter(username=username):
                user = authenticate(username=username, password=old_password)
                if user:
                    user.set_password(new_password)
                    user.save()
                    tips = '密码修改成功,请重新登陆'
                else:
                    tips = '旧密码不正确，请确认'
            else:
                tips = '用户不存在'
        else:
            print(changepassword_form.cleaned_data)
            tips = "修改失败，请检查"
            error_msg = changepassword_form.errors
            print(error_msg)
    changepassword_form = ChangePasswordForm()
    return render(request, 'Account/changepassword.html', locals())

@login_required
def userinfoView(request):
    title = "OPSSEE | 修改用户信息"
    username = request.user
    userinfolist = UserInfo.objects.filter(username=username)
    if request.method == 'POST':
        userinfo_form = UserInfoForm(request.POST)
        if userinfo_form.is_valid():
            print(userinfo_form.cleaned_data)
            email = userinfo_form.cleaned_data.get('email', '')
            realname = userinfo_form.cleaned_data.get('realname', '')
            qq = userinfo_form.cleaned_data.get('qq', '')
            wechat = userinfo_form.cleaned_data.get('wechat', '')
            mobile = userinfo_form.cleaned_data.get('mobile', '')

            if UserInfo.objects.filter(username=username):
                UserInfo.objects.filter(username=username).update(realname=realname, email=email, wechat=wechat, mobile=mobile, qq=qq)
                tips = '用户信息修改成功'
            else:
                tips = '用户不存在'
        else:
            print(userinfo_form.cleaned_data)
            tips = "修改失败，请检查"
            error_msg = userinfo_form.errors
            print(error_msg)
    userinfo_form = UserInfoForm()
    return render(request, 'Account/userinfo.html', locals())

def forgotpasswordView(request):
    title = "OPSSEE | 忘记密码"
    button = '获取验证码'
    new_password = False
    if request.method == 'POST':
        username = request.POST.get('username', 'root')
        verificationcode = request.POST.get('verificationcode', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        user = UserInfo.objects.filter(username=username)

        if not user:
            tips = '用户' + username + '不存在'
        else:
            if not request.session.get('VerificationCode', ''):
                button = '重置密码'
                tips = '验证码已发送'
                new_password = True
                VerificationCode = str(random.randint(1000, 9999))
                request.session['VerificationCode'] = VerificationCode
                user[0].email_user('重置密码验证码', VerificationCode)
            elif verificationcode == request.session.get('VerificationCode'):
                if password != confirm_password:
                    tips = '两次密码不一致'
                    del request.session['VerificationCode']
                    return render(request, 'Account/forgotpassword.html', locals())
                dj_ps = make_password(password, None, 'pbkdf2_sha256')
                user[0].password = dj_ps
                user[0].save()
                del request.session['VerificationCode']
                tips = '密码已重置'
            else:
                tips = '验证码错误，请重新获取'
                new_password = False
                del request.session['VerificationCode']
    return render(request, 'Account/forgotpassword.html', locals())

@login_required
def taskView(request):
    title = "OPSSEE | 定时任务"
    menuname = "task"
    username = request.user
    userinfolist = UserInfo.objects.filter(username=username)
    return render(request, 'task.html', locals())

@login_required
def labelView(request):
    title = "OPSSEE | 标签管理"
    menuname = "label"
    username = request.user
    userinfolist = UserInfo.objects.filter(username=username)
    return render(request, 'label.html', locals())

