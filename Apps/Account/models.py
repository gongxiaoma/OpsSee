#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auther: gongxiaoma

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    realname = models.CharField('姓名', max_length=16)
    qq = models.CharField('QQ号码', max_length=16)
    wechat = models.CharField('微信号码', max_length=100)
    mobile = models.CharField('手机号码', max_length=11)

    # 设置返回值
    def __str__(self):
        return self.username
