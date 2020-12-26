from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *


def unauthencated_user(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapped_func

#decorator pk = kwargs['blog_id']
# def user_is_author(view_func):
#     def check_and_call(request, *args, **kwargs):
#         user = request.user
#         #print user.id
#         pk = kwargs['blog_id']
        
#         author = Author.objects.get(pk=pk)
#         if not (author.id == request.user.id): 
#             return HttpResponse("It is not yours ! You are not permitted !")
#         return view_func(request, *args, **kwargs)
#     return check_and_call

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not allowed to visit this page')
        return wrapped_func
    return decorator

def admin_only(view_func):
    def wrapped_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'authors':
            return redirect('userPage')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapped_func