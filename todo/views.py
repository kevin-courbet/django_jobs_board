"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpRequest
from datetime import datetime
from .models import Todo
from operator import itemgetter
from .forms import SignUpForm, TodoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    todos = Todo.objects.all()[:10]

    return render(
        request,
        'todo/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'todos': todos,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'todo/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'todo/about.html',
        {
            'title': 'About',
            'message': 'This website allows is a Global Business Consulting Jobs Board : Post, share and manage tasks.',
            'year': datetime.now().year,
        }
    )


def details(request, id):
    assert isinstance(request, HttpRequest)
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/details.html',
                  {
                      'todo': todo,
                      'year': datetime.now().year,
                  })


@login_required()
def add(request):
    assert isinstance(request, HttpRequest)
    if(request.method == 'POST'):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    return render(request, 'todo/add.html', {
        'user': request.user, 
        'form': form,
        'title': 'Add',
        'year': datetime.now().year,
        })


def signup(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'todo/signup.html', {
            'form': form,
            'title': 'Signup',
            'year': datetime.now().year,
            })
