"""admin_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse

def test01(request):
    return HttpResponse("test01")

def test02(request):
    return HttpResponse("test02")

def test03(request):
    return HttpResponse("test03")

def list_view(request):
    return HttpResponse("list_view")

def add_view(request):
    return HttpResponse("add_view")

def change_view(request,id):
    return HttpResponse("change_view")

def delete_view(request,id):
    return HttpResponse("delete_view")

def get_urls_2():
    temp = []
    temp.append(url(r"^$",list_view))
    temp.append(url(r"^add/$", add_view))
    temp.append(url(r"^(\d+)/change/$", change_view))
    temp.append(url(r"^(\d+)/delete/$", delete_view))
    return temp

def get_urls():
    print(admin.site._registry)
    temp = []
    for model,admin_class_obj in admin.site._registry.items():
        #用类变量提取app名字
        app_name = model._meta.app_label
        model_name = model._meta.model_name
        #提取表名字
        temp.append(url(r'^{0}/{1}/'.format(app_name,model_name),(get_urls_2(),None,None),))
    return temp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^liang/', (get_urls(),None,None)),
]
#超级用户
#账号 liang  邮箱 123456@qq.com 密码 qq151523 创建命令 python manage.py createsuperuser

