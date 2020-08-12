"""interface URL Configuration

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
from django.contrib import admin
from django.urls import path
from usersRegister import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.greeting, name='index'),
    path('control', views.createRegister, name='control'),
    path('sing_up', views.login_screen, name='sing_up'),
    path('register', views.register_screen, name='register'),
    path('view', views.select, name='view'),
    path('index/', views.back, name='index'),
    path('edit', views.update, name='edit'),
]
