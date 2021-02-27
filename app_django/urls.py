from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    #LOG IN / SIGN IN
    path('accounts/sign_up/', views.sign_up, name="sign-up"),
    
    # blogers
    path('blogers', views.blogers_list, name='blogers'),
    path('blogers/<int:pk>', views.bloger_detail, name='bloger_detail'),
    path('blogers/new', views.bloger_create, name='bloger_create'),
    path('blogers/<int:pk>/edit', views.bloger_edit, name='bloger_edit'),
    path('blogers/<int:pk>/delete', views.bloger_delete, name='bloger_delete'),
    
    # blogs
    path('blogs', views.blogs_list, name='blogs_list'),
    path('blogs/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blogs/new', views.blog_create, name='blog_create'),
    path('blogs/<int:pk>/edit', views.blog_edit, name='blog_edit'),
    path('blogs/<int:pk>/delete', views.blog_delete, name='blog_delete'),

]