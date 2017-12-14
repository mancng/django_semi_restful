# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *

def index(request):
    all_courses = Course.objects.all()
    return render(request, "courses/index.html", {"all_courses" : all_courses})

def course(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "courses/delete.html", {'course': course})

def add(request):
    if request.method == "POST":
        Course.objects.create(name=request.POST['name'], content=request.POST['description'])
        print request.POST['name']
        return redirect('/courses')
    else:
        return redirect('/courses')

def delete_course(request, course_id):
    del_course = Course.objects.get(id=course_id)
    del_course.delete()
    return redirect('/courses')