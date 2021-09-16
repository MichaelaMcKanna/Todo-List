from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.template import context

def todo_list(request):
    # the client sends us a requestand we return a response when the view is called
    todos = Todo.objects.all()
    # if printed this would show a Query set of all items on the todo list
    context = {
        "todo_list": todos
        #allows us to access our todos from our html file 
    }
    return render(request, "todo/todo_list.html", context)

# CRUD Create, Retrieve, Update, Delete, List

def todo_details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_details.html", context)
    # assign the new view to a url

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        #saves the form
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo/todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo/todo_update.html", context)

def todo_delete(request, id): #we want id to be a parameter so tha we can delete a specific id
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")
