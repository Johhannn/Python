from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class Task_list_view(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'


class Task_Detail_view(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class Task_add_view(UpdateView):
    model = Task
    template_name = 'add.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class Task_delete_view(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home1')


# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "home.html", {'task1': task1})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f, 'task': task})
