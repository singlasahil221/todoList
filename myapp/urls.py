"""upgrad_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from myapp.views import *
from myapp.background_task_file import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('sign-up/',register),
    path('new-task/', new_task),
    path('my-task/', my_task),
    path('my-task/<int:pk>/', my_task_part),
    path('task/', TodosView.as_view()),
    path('task/<int:todo_id>/',  TodosView.as_view()),

    path('register/', RegistrationView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

task_notifier(repeat=10,repeat_until=None)
task_report(repeat=10,repeat_until=None)