from django.shortcuts import render, redirect
from .models import Blogers, Blogs
from .forms import BlogerForm, BlogForm

#LOG IN / SIGN IN
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


#LOG IN / SIGN IN
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    context['form']=form
    return render(request,'registration/sign_up.html',context)


# blogers
def blogers_list(request):
    blogers = Blogers.objects.all()
    return render(request, 'app/blogers/blogers.html', {'blogers': blogers})


def bloger_detail(request, pk):
    bloger = Blogers.objects.get(id=pk)
    return render(request, 'app/blogers/bloger_detail.html', {'bloger': bloger})


# login
# @login_required
def bloger_create(request):
    if request.method == 'POST':
        form = BlogerForm(request.POST)
        if form.is_valid():
            bloger = form.save()
            return redirect('bloger_detail', pk=bloger.pk)
    else:
        form = BlogerForm()
    return render(request, 'app/blogers/bloger_form.html', {'form': form})


def bloger_edit(request, pk):
    bloger = Blogers.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogerForm(request.POST, instance=bloger)
        if form.is_valid():
            bloger = form.save()
            return redirect('bloger_detail', pk=bloger.pk)
    else:
        form = BlogerForm(instance=bloger)
    return render(request, 'app/blogers/bloger_form.html', {'form': form})


def bloger_delete(request, pk):
    Blogers.objects.get(id=pk).delete()
    return redirect('home')



# blogs
def blogs_list(request):
    blogs = Blogs.objects.all()
    return render(request, 'app/blogs/blogs.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = Blogs.objects.get(id=pk)
    return render(request, 'app/blogs/blog_detail.html', {'blog': blog})


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'app/blogs/blog_form.html', {'form': form})


def blog_edit(request, pk):
    blog = Blogs.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'app/blogs/blog_form.html', {'form': form})


def blog_delete(request, pk):
    Blogs.objects.get(id=pk).delete()
    return redirect('blogs_list')
