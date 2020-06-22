from django.shortcuts import HttpResponseRedirect, reverse, render


def jump(request):
    return HttpResponseRedirect('/Account/login')