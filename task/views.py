from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Task


def todo(request):
	td = Task.objects.all()
        if request.method == "POST":
            if "Add" in request.POST:
                title = request.POST["title"]
                description = request.POST["description"]
                dl = str(request.POST["dl"])
                Todo = Task(title=title, description=description, dl=dl, done=False)
                Todo.save()
                return redirect("/todo")
            elif Task.done:
                Todo = Task(title=title, description=description, dl=dl, done=True)
                Todo.save()
                return redirect("/todo/<id:int>/execute")
        elif request.method == "PATCH":
            if "Change" in request.PATCH:
                title = request.PATCH["title"]
                description = request.PATCH["description"]
                dl = str(request.PATCH["dl"])
                Todo = Task(title=title, description=description, dl=dl, done=False)
                Todo.save()
                return redirect("/todo/<id:int>")
        elif request.method == "DELETE":
            if "Delete" in request.DELETE:
                checkedlist = request.DELETE.getlist('checkedbox')
                for i in range(len(checkedlist)):
                    todo = Task.objects.filter(id=int(checkedlist[i]))
                    todo.delete()
        elif request.method == "GET":
            id = Task.ID
            title = request.GET["title"]
            description = request.GET["description"]
            dl = str(request.GET["dl"])
            done = request.GET["done"]
            Todo = Task(title=title, description=description, dl=dl, done=done)
            return redirect("/todo/<id:int>")
        return render(request, "todo.html", {"td": td})

