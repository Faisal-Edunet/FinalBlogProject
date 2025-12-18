from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Author
from .forms import AuthorForm
# Create your views here.

def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'authorapp/author_list.html',context)

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)   # no instance → new object
        if form.is_valid():
            form.save()   # creates a new Student record
            return redirect('authorapp:author_list')
        else:
            return HttpResponse('Invalid Data')
    else:
        form = AuthorForm()
        context = {
            'form': form
        }
        return render(request, 'authorapp/add_author.html',context)

def update_author(request, id):
    a = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST,instance=a)   # no instance → new object
        if form.is_valid():
            form.save()   # creates a new Student record
            return redirect('authorapp:author_list')
        else:
            return HttpResponse('Invalid Data')
    else:
        form = AuthorForm(instance=a)
        context = {
            'form': form
        }
        return render(request, 'authorapp/update_author.html',context)
    
def delete_author(request, id):
    a = get_object_or_404(Author, id=id)
    a.delete()
    return redirect('authorapp:author_list')
