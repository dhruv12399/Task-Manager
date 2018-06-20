# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Task, Activity 
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .serializers import TaskSerializer
from rest_framework import generics

# Create your views here.

def signup(request):
	# print request.POST
	form = UserCreationForm()
	if request.method == 'POST':
		# print "in posts"
		form = UserCreationForm(request.POST)
		# print form
		if form.is_valid():
			# print "hello"
			form.save()

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect(reverse('manager_task:home'))

	
	return render(request, 'manager_task/signup.jinja', {'form': form})

@login_required
def home(request):
	tasklist = request.user.task_set.all()
	act = Activity.objects.all()[::-1]
	act = act[0:25]
	return render(request, 'manager_task/home.jinja', {'tasklist': tasklist, 'act':act})

@login_required
def add_new_task(request):
	
	if request.method=='POST':
		form_task = TaskForm(request.POST)
		if form_task.is_valid():
			form_instance = form_task.save(commit=False)
			form_instance.user = request.user
			form_instance.save()
			new_obj = Task.objects.get(id=form_instance.id)
			# print new_obj
			a = Activity(ac_type = 1, task = new_obj)
			a.save()
	
		return HttpResponseRedirect(reverse('manager_task:home'))

	else:
		form_task = TaskForm()
		return render(request, 'manager_task/addnewtask.jinja', {'form': form_task})

@login_required
def change_status(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	if task.completed == False:
		task.completed = True
		a = Activity(ac_type = 2, task = task)
		a.save()
	else:
		task.completed = False
		a = Activity(ac_type = 5, task = task)
		a.save()

	
	
	task.save();
	return HttpResponseRedirect(reverse('manager_task:home'))

@login_required
def delete_task(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	
	a = Activity(ac_type = 3, task = task)
	a.save()
	task.is_deleted = 1
	task.save()
	# task.delete()
	return HttpResponseRedirect(reverse('manager_task:home'))

@login_required
def edit_task(request, task_id):

	task = get_object_or_404(Task, pk = task_id)
	existing_name = task.task_name
	existing_deadline = task.complete_by

	if request.method=='POST':
		print "in posts"
		form_task = TaskForm(request.POST, instance = task)
		print request.POST
		if form_task.is_valid():
			print "is valid"
			form_instance = form_task.save(commit=False)
			form_instance.user = request.user
			form_instance.save()
			new_obj = Task.objects.get(id=form_instance.id)
			# print new_obj
			a = Activity(ac_type = 4, task = new_obj)
			a.save()
	
		return HttpResponseRedirect(reverse('manager_task:home'))

	else:
		form_task = TaskForm()
		return render(request, 'manager_task/edittask.jinja', {'form': form_task, 'existing_name':existing_name, 'existing_deadline':existing_deadline })

@login_required
def sort_name(request):
	tasklist = request.user.task_set.all().order_by('task_name')
	act = Activity.objects.all()[::-1]
	act = act[0:25]
	return render(request, 'manager_task/home.jinja', {'tasklist': tasklist, 'act':act})

@login_required
def sort_addedon(request):
	tasklist = request.user.task_set.all().order_by('added_on') 
	act = Activity.objects.all()[::-1]
	act = act[0:25]
	return render(request, 'manager_task/home.jinja', {'tasklist': tasklist, 'act':act})

@login_required
def sort_completeby(request):
	tasklist = request.user.task_set.all().order_by('complete_by')
	act = Activity.objects.all()[::-1]
	act = act[0:25]
	return render(request, 'manager_task/home.jinja', {'tasklist': tasklist, 'act':act})

class TaskList(generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
