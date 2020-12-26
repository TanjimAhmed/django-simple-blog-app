#importing path from main urls
from django.urls import path
#importing views
from . import views




urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user/', views.userPage, name='userPage'),

    path('blog/<str:blog_id>/', views.blogPage, name='blogPage'),
    path('create/<str:id>/', views.createBlog, name='create_blog'),
    path('update/<str:blog_id>/', views.updateBlog, name='update_blog'),
    path('delete/<str:blog_id>/', views.deleteBlog, name='delete_blog'),
]
