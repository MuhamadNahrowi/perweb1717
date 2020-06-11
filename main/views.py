from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_list = Todo.objects.all().order_by("-added_date")
    context = {'todo_list': todo_list}
    return render(request, 'main/index.html', context=context)


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")


def del_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect("/")