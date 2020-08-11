import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template  import Template, Context, loader
from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
import json
from django.http import JsonResponse

from .models import Users, Sign
from .forms import registerForm

def greeting(request):
    index_ext = loader.get_template('templates/index.html')
    # a dictionary is necessary with loader template
    doc = index_ext.render({})
    return HttpResponse(doc)
    
@csrf_exempt
def login_screen(request):
    index_ext = loader.get_template('templates/sing_in.html')
    # a dictionary is necessary with loader template
    doc = index_ext.render({})
    return HttpResponse(doc)

@csrf_exempt
def register_screen(request):
    index_ext = loader.get_template('templates/register.html')
    # a dictionary is necessary with loader template
    doc = index_ext.render({})
    return HttpResponse(doc)

def prueba(request):
    index_ext = loader.get_template('templates/prueba.html')
    # a dictionary is necessary with loader template
    doc = index_ext.render({})
    return HttpResponse(doc)


@csrf_exempt
def createRegister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        register = Users()
        register.Name = name
        register.Username = username
        register.Phone = phone
        register.Email = email
        register.Password = password
        register.save()

        print(name)
        print(username)
        index_ext = loader.get_template('templates/index.html')
        # a dictionary is necessary with loader template
        doc = index_ext.render({})
        return HttpResponse(doc)

@csrf_exempt
def select(request):
    users = Users.objects.all()
    context = {'users' : users}
    index_ext = loader.get_template('templates/view.html')
    # a dictionary is necessary with loader template
    doc = index_ext.render(context)
    return HttpResponse(doc)


@csrf_exempt
def update(request):
    id = request.POST.get('id')
    users = Users.objects.get(id = id)
    print(id)
    print(users)
    if request.method =='GET':
        register = Users(instance = users)
    else:
        name = request.POST.get('name')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        register = Users()
    register.Name = name
    register.Username = username
    register.Phone = phone
    register.Email = email
    register.Password = password
    register.save()
    index_ext = loader.get_template('templates/register.html')
    # a dictionary is necessary with loader template
    doc = index_ext.render({})
    return HttpResponse(doc)
