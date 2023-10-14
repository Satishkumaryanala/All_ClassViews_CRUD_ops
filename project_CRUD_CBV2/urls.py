"""
URL configuration for project_CRUD_CBV2 project.

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
from django.urls import path,re_path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',Home.as_view(),name='Home'),
    path('Temp_CBV/',TemplateView.as_view(template_name='app/Temp_CBV.html'),name='Temp_CBV'),
    path('Temp_Context/',Temp_Context.as_view(),name='Temp_Context'),
    path('Temp_Form/',Temp_Form.as_view(),name='Temp_Form'),
    path('Temp_FormView/',Temp_FormView.as_view(),name='Temp_FormView'),
    path('School_ListView/',School_ListView.as_view(),name='School_ListView'),
    path('School_CreateView/',School_CreateView.as_view(),name='School_CreateView'),
    path('Student_CreateView/',Student_CreateView.as_view(),name='Student_CreateView'),
    path('Student_ListView/',Student_ListView.as_view(),name='Student_ListView'),

    re_path('^deleteSchool(?P<pk>\d+)/',School_DeleteView.as_view(),name='School_DeleteView'),
    re_path('^updateSchool(?P<pk>\d+)/',School_UpdateView.as_view(),name='School_UpdateView'),
    re_path('^STDetails(?P<pk>\d+)/',Student_Detail.as_view(),name='Student_Detail'),
    re_path('(?P<pk>\d+)/',School_Detail.as_view(),name='School_Detail'),

]
