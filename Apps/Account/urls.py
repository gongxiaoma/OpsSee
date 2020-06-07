"""OpsSee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Apps.Account.account import loginView
from Apps.Account.account import indexView
from Apps.Account.account import logoutView
from Apps.Account.account import registerView
from Apps.Account.account import changepasswordView
from Apps.Account.account import userinfoView
from Apps.Account.account import forgotpasswordView
from Apps.Account.account import taskView
from Apps.Account.account import labelView
from django.conf.urls import url

urlpatterns = [
    url(r'^login/', loginView, name='login'),
    url(r'^index/', indexView, name='index'),
    url(r'^logout/', logoutView, name='logout'),
    url(r'^register/', registerView, name='register'),
    url(r'^changepassword/', changepasswordView, name='changepassword'),
    url(r'^userinfo/', userinfoView, name='userinfo'),
    url(r'^forgotpassword/', forgotpasswordView, name='forgotpassword'),
    url(r'^task/', taskView, name='taskView'),
    url(r'^label/', labelView, name='labelView'),
]
