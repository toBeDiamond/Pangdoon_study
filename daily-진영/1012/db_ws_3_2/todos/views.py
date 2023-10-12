from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm
from accounts.models import User

def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, 'todos/index.html', context)
    else:
        return redirect('accounts:login')

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                user = User.objects.get(username=request.user.username)
                todo.author = user
                form.save()
                return redirect('todos:index')
        else:
            form = TodoForm()
        context = {
            'form': form,
        }
        return render(request, 'todos/create.html', context)
    else:
        return redirect('accounts:login')

@require_POST
def toggle(request, pk):
    if request.user.is_authenticated:
        todo = Todo.objects.get(pk=pk)
        todo.completed = not todo.completed
        todo.save()
        return redirect('todos:index')
    else:
        return redirect('accounts:login')

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('accounts:login')