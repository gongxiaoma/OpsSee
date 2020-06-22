#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther: gongxiaoma

import re
from django import forms
from .models import UserInfo
from django.core.exceptions import ValidationError


class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'账 号',
                               max_length=128,
                               error_messages={'required': u'用户不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入用户'}))
    password = forms.CharField(label=u'密 码',
                               max_length=256,
                               error_messages={'required': u'密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请输入密码'}))

class RegistUserForm(forms.ModelForm):
    # 重写初始函数
    def __init__(self, *args, **kwargs):
        super(RegistUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    # 添加模型外表单字段
    confirm_password = forms.CharField(label=u'密 码',
                               max_length=128,
                               error_messages={'required': u'重试密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请再次输入密码'}))

    # 关联UserInfo模型
    class Meta:
        model = UserInfo
        fields = ('username', 'password', 'email', 'realname', 'qq', 'wechat', 'mobile')

        # 设置html的label标签
        labels = {
            'username': '用 户',
            'password': '密 码',
            'email': '邮 箱',
            'realname': '姓 名',
            'qq': 'QQ 号',
            'wechat': '微 信',
            'mobile': '手 机'
        }

        # 设置样式与修改必填项默认提示为自定义提示
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入用户'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请输入密码'}),
            'email': forms.TextInput(attrs={'class': ' form-control', 'placeholder': u'请输入邮箱'}),
            'realname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入姓名'}),
            'qq': forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入QQ号码'}),
            'wechat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入微信号码'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入手机号码'}),
        }

        # 定义字段类型,一般模型的字段会自动转换成表单的字段
        # field_classes = {
        #     'name': forms.CharField
        # }
        # 帮助提示信息
        # help_texts = {
        #     'username': '用户'
        # }

        # 自定义每个字段的错误信息
        error_messages = {
            'username': {'required': '请输入账号',
                        'invalid': '请检查用户格式是否正确'},
            'password': {'required': '请输入密码',
                         'invalid': '请检查密码格式是否正确'},
            'email': {'required': '请输入邮箱',
                         'invalid': '请检查邮箱格式是否正确'},
            'realname': {'required': '请输入真姓名',
                         'invalid': '请检查姓名格式是否正确'},
            'qq': {'required': '请输入QQ号码',
                         'invalid': '请检查QQ号码格式是否正确'},
            'wechat': {'required': '请输入微信号码',
                         'invalid': '请检查微信号码格式是否正确'},
            'mobile': {'required': '请输入手机',
                         'invalid': '请检查手机号码是否正确'}
        }

    # 校验表单：用户是否已经存在
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserInfo.objects.filter(username=username):
            raise ValidationError("%s用户已经存在" % username)
        else:
            return username

    # 校验表单：邮箱是否已经存在
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserInfo.objects.filter(email=email):
            raise ValidationError("%s邮箱已经存在" % email)
        else:
            return email

    # 校验表单：手机号码是否符合格式
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.findall('^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1})|(17[0-9]{1}))+\d{8})$', mobile):
            raise ValidationError("手机号码格式错误！")
        else:
            return mobile

    # 校验表单：QQ号码是否符合格式
    # def clean_qq(self):
    #     qq = self.cleaned_data.get('qq')
    #     if not re.findall('^[1-9][0-9]{4,19}$', qq):
    #         raise ValidationError("QQ号码格式错误！")
    #     else:
    #         return qq

    # 校验密码：两次密码是否相同
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', '两次密码不一致')
            #raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data

class UserInfoForm(forms.ModelForm):
    # 重写初始函数
    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = False

    # 关联UserInfo模型
    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'realname', 'qq', 'wechat', 'mobile')

        # 设置html的label标签
        labels = {
            'username': '用户名称',
            'email': '邮箱地址',
            'realname': '真实姓名',
            'qq': 'QQ号码',
            'wechat': '微信号码',
            'mobile': '手机号码'
        }

        # 定义字段类型,一般模型的字段会自动转换成表单的字段
        # field_classes = {
        #     'name': forms.CharField
        # }
        # 帮助提示信息
        # help_texts = {
        #     'username': '用户'
        # }

        # 自定义每个字段的错误信息
        error_messages = {
            'username': {'invalid': '请检查用户格式是否正确'},
            'email': {'required': '请输入邮箱',
                      'invalid': '请检查邮箱格式是否正确'},
            'realname': {'required': '请输入真姓名',
                         'invalid': '请检查姓名格式是否正确'},
            'qq': {'required': '请输入QQ号码',
                   'invalid': '请检查QQ号码格式是否正确'},
            'wechat': {'required': '请输入微信号码',
                       'invalid': '请检查微信号码格式是否正确'},
            'mobile': {'required': '请输入手机',
                       'invalid': '请检查手机号码是否正确'}
        }

    # 校验表单：邮箱是否已经存在
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserInfo.objects.filter(email=email):
            raise ValidationError("%s邮箱已经存在" % email)
        else:
            return email

    # 校验表单：手机号码是否符合格式
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.findall('^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1})|(17[0-9]{1}))+\d{8})$', mobile):
            raise ValidationError("手机号码格式错误！")
        else:
            return mobile

    # 校验表单：QQ号码是否符合格式
    # def clean_qq(self):
    #     qq = self.cleaned_data.get('qq')
    #     if not re.findall('^[1-9][0-9]{4,19}$', qq):
    #         raise ValidationError("QQ号码格式错误！")
    #     else:
    #         return qq

class ChangePasswordForm(forms.Form):
    password = forms.CharField(label=u'密码',
                               max_length=256,
                               error_messages={'required': u'密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请输入密码'}))
    new_password = forms.CharField(label=u'新密码',
                               max_length=256,
                               error_messages={'required': u'密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请输入密码'}))

    confirm_password = forms.CharField(label=u'再次密码',
                               max_length=256,
                               error_messages={'required': u'密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请再次输入密码'}))

    # 校验密码：两次密码是否相同
    def clean(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            self.add_error('confirm_password', '两次密码不一致')
            #raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data




