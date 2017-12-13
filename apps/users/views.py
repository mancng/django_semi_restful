# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {"users": users})

def user(request, user_id):
    user = User.objects.get(id = user_id)
    return render(request, 'users/single.html', {'user': user})

def add(request):
    return render(request, 'users/add.html')

def add_user(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/')
    else:
        return redirect('/')

def edit(request, user_id):
    user = User.objects.get(id = user_id)
    return render(request, 'users/edit.html', {'user': user})

def edit_user(request, user_id):
    if request.method == "POST":
        update_user = User.objects.get(id=user_id)
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']
        update_user.email = request.POST['email']
        update_user.save()
    return redirect('/')

def delete(request, user_id):
    delete_user = User.objects.get(id = user_id)
    delete_user.delete()
    return redirect('/')