# importing render and redirect
from django.shortcuts import render, redirect
# auth from
from django.contrib.auth.forms import UserCreationForm
# mesages
from django.contrib import messages
# authenticate
from django.contrib.auth import authenticate, login, logout
# decorators
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group
# importing jango httpresponse
from django.http import HttpResponse
#importing models form models files
from .models import *
#importing the forms files
from .forms import blogForm, CreateUserForm
#filters
from .filters import BlogFilter
#decorator
from .decorators import unauthencated_user, allowed_user, admin_only


# Create your views here.

@unauthencated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account is created for '+ username)
            return redirect('login')

    context={'form':form}
    return render(request, 'myapp/register.html', context)

@unauthencated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context={}
    return render(request, 'myapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    
    #importing blogs objects from Blog model
    blog = Blog.objects.all().order_by('-id')
    
    user= request.user
    #django-filter library
    myFilter = BlogFilter(request.GET, queryset=blog)
    blog = myFilter.qs
     
    # Count method to get the total data
    total_blog = blog.count()
    # dictionary to pass the data
    context = {'posts':blog,
    'user':user,
    'total_blog': total_blog,
    'myFilter': myFilter,}
    # return and render to the urls
    return render(request, 'myapp/index.html', context)

# @login_required(login_url='login')
# @allowed_user(allowed_roles=['admin'])
# def authorPage(request):
#     #importing authors objects from Author model
    
#     context={}
#     return render(request, 'myapp/author.html', context)

@login_required(login_url='login')
#@allowed_user(allowed_roles=['authors','admin'])
def userPage(request):
    # using primary key to get the data form one user
    author= request.user.author
    context={'author':author}
    return render(request, 'myapp/user.html', context)

def blogPage(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context={'blog':blog}
    return render(request, 'myapp/blogpage.html',context)

@login_required(login_url='login')
#@allowed_user(allowed_roles=['authors','admin'])
def createBlog(request, id):
    text = "Create Blog"
    author = Author.objects.get(id=id)
    if not (request.user.author.id == author.id):
        return HttpResponse("It is not yours ! You are not permitted !")
    else:
        # initial is user to prefill the form
        form = blogForm(initial={'author':author})
        # if the request is post
        if request.method == 'POST':
            # set the data to the form
            form = blogForm(request.POST)
            # check the data if valid
            if form.is_valid():
                # save the data
                form.save()
                # redirect to the home page
                return redirect('/')


        context={'form': form,'text':text}
        return render(request, 'myapp/create.html', context)

#@user_is_author
@login_required(login_url='login')
#@allowed_user(allowed_roles=['authors','admin'])
def updateBlog(request, blog_id):
    text = "Update blog"
    author= request.user.author
    blog = Blog.objects.get(id=blog_id)
    if not (author == blog.author):
        return HttpResponse("It is not yours ! You are not permitted !")
    else:
        form = blogForm(instance=blog)
        if request.method == "POST":
            form = blogForm(request.POST, instance=blog,)
            if form.is_valid():
                form.save()
                return redirect('/')

        context={'form': form, 'blog': blog, 'author':author, 'text':text}
        return render(request, 'myapp/create.html', context)

@login_required(login_url='login')
#@allowed_user(allowed_roles=['authors', 'admin'])
def deleteBlog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    author= request.user.author
    blog = Blog.objects.get(id=blog_id)
    if not (request.user.author == blog.author):
        return HttpResponse("It is not yours ! You are not permitted !")
    else:
        if request.method == "POST":
            blog.delete()
            return redirect('/')
        context={'blog': blog}
        return render(request, 'myapp/delete.html', context)

def about(request):
    return render(request, 'myapp/about.html')