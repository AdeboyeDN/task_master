from django.shortcuts import render,redirect
from .models import task
from .forms import TaskForm

def home(request):
  table = task.objects.all()
  form = TaskForm()
  if request.method=='POST':
    form = TaskForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('/')
  context = {
    'form':form,'task':table
  }
  return render(request,'home.html',context)

def update(request, pk):
  table = task.objects.get(id=pk)
  form = TaskForm( instance=table)
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=table)
    if form.is_valid:
      form.save()
      return redirect('/')
  context = {
  'form':form
  }
  return render(request,'update.html', context)

def delete(request,pk):
   table = task.objects.get(id=pk)
   form = TaskForm(instance=table)
   if request.method == 'POST':
       table.delete()
       return redirect('/')
   context = {
   'form':form , 'task':table
   } 
   return render(request,'delete.html',context)
  

