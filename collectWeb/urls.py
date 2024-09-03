"""collectWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
# from django.conf.urls import url
from . import login

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', login.loginPage),
    # url(r'^register$', login.registerPage),
    # url(r'^login/$', login.login),



    # path('', include('collectWeb.urls')),
    path('register/', login.register, name='registerPage'),
    path('', login.login, name='loginPage'),
    path('info_coll/', login.infoColl, name='infoColl'),
    path('user_func/', login.userFunc, name='userFunc'),
    path('admin_func/', login.adminFunc, name='adminFunc'),
    path('admin_func/admin_edit/', login.adminEdit, name='adminEdit'),
    path('user_func/mine/', login.mine, name='mine'),
    path('user_func/mine/user_psw/', login.user_psw, name='user_psw'),
    path('user_func/questionMMSE/', login.question, name='question'),
    # path('admin_func/add/', login.user_add, name='user_add'),
    path('admin_func/edit/', login.user_edit, name='user_edit'),
    # path('admin_func/edit/<int:user_id>/', login.user_edit, name='user_edit'),
    path('admin_func/detail/<str:user_id>/', login.user_detail, name='user_detail'),
    path('admin_func/delete/<str:user_id>/', login.user_delete, name='user_delete'),
    path('admin_func/reset/<str:user_id>/', login.user_reset, name='user_reset'),
    path('admin_func/upload_user_info/<str:username>/', login.upload_user_info, name='upload_user_info'),
    # path('admin_func/upload_user_info/test1/', login.upload_test, name='upload_test1_data'),
    # path('admin_func/upload_user_info/test2/', login.upload_test2, name='upload_test2'),


]


