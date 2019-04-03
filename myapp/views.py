from django.http import Http404
# Create your views here.

from datetime import datetime, timedelta

# Django
from django.shortcuts import render
from django.contrib.auth.models import User

# REST Framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, serializers


# Todo App
from myapp.serializers import UserSerializer, TodoSerializer, RegistrationSerializer
from myapp.models import Todo

# payload registeration
# {
# "username":"<username>",
# "email" : "<email>"
# "password":"<password>"
# }



# # payload todo
# {
#    "user_username":"sahil",
#    "scheduled_at":"2019-11-25T19:43:37+0100",
#    "task_title" : "Mandee birthday"
# }



class RegistrationView(APIView):
    """ Allow registration of new users. """
    permission_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        # Check format and unique constraint
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        u = User.objects.create(username=data['username'],email = data['email'])
        u.set_password(data['password'])
        u.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodosView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, todo_id=None):
        """ Get all todos """
        try:
            if todo_id is not None:
                todos = Todo.objects.filter(owner=request.user.id, id = todo_id)
            else:
                todos = Todo.objects.filter(owner=request.user.id)
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
        except : 
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        """ Adding a new todo. """
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            owner = request.user
            t = Todo(owner=owner, description=data['description'], scheduled_at = data['scheduled_at'], is_completed=False)
            t.save()
            request.data['id'] = t.pk # return id
            return Response(request.data, status=status.HTTP_201_CREATED)

    def put(self, request, todo_id):
        """ Update a todo """
        serializer = TodoSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            desc = data['description']
            is_completed = data['is_completed']
            t = Todo(id=todo_id, owner=request.user, scheduled_at = data['scheduled_at'], description=desc,is_completed=is_completed)
            t.save()
            return Response(status=status.HTTP_200_OK)


def register(request):
    return render(request,"registeration.html",{})

def my_task(request):
    return render(request,"my_task.html",{})

def my_task_part(request,pk):
    return render(request,"my_task_part.html",{})

def new_task(request):
    return render(request,"new_task.html",{})