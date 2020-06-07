#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther: gongxiaoma

from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'账 号',
                               max_length=128,
                               error_messages={'required': u'用户不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'请输入用户', 'oninvalid': "this.setCustomValidity('用户不能为空');", 'oninput': "setCustomValidity('');"}))
    password = forms.CharField(label=u'密 码',
                               max_length=256,
                               error_messages={'required': u'密码不能为空'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': u'请输入密码', 'oninvalid': "this.setCustomValidity('密码不能为空');", 'oninput': "setCustomValidity('');"}))


class RegistUserForm(forms.ModelForm):
    class Meta:
        fields = ('username', 'password', 'email', 'realname', 'qq', 'wechat', 'mobile')
