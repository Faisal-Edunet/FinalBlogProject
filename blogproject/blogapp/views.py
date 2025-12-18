from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogapp/blog_list.html',context)

@login_required(login_url='login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)   # no instance → new object
        if form.is_valid():
            form.save()   # creates a new Student record
            return redirect('blogapp:blog_list')
        else:
            return HttpResponse('Invalid Data')
    else:
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, 'blogapp/add_blog.html',context)


@login_required(login_url='login')
def update_blog(request, id):
    a = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST,instance=a)   # no instance → new object
        if form.is_valid():
            form.save()   # creates a new Student record
            return redirect('blogapp:blog_list')
        else:
            return HttpResponse('Invalid Data')
    else:
        form = BlogForm(instance=a)
        context = {
            'form': form
        }
        return render(request, 'blogapp/update_blog.html',context)
 
@login_required(login_url='login')   
def delete_blog(request, id):
    a = get_object_or_404(Blog, id=id)
    a.delete()
    return redirect('blogapp:blog_list')
