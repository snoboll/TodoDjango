from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Todo

def index(request):
    todos = Todo.objects.order_by('due_at')
    template = loader.get_template("todos/index.html")
    context = {
        'todos': todos
        }
    print(todos)
    return HttpResponse(template.render(context, request))

def todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    template = loader.get_template("todos/todo.html")
    context = {
        "todo":todo
    }

    return HttpResponse(template.render(context, request))