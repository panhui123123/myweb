"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app01.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path(r'', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('user_list/', user_list),
    path('user_add/', user_add),
    path('user_edit/', user_edit),
    path('user_delete/', user_delete),
    path('text_check/', text_check),
    path('lottery/', lottery),
    path('signin/', signin),
    path('signout/', signout),
    path('ball/', ball),
    path('star/', star)
]
