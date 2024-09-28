from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from todo_app.form import TodoForm, UserForm
from todo_app.models import Todo1


# Create your views here.
def index_dashboard(request):
    return render(request,'index_dashboard.html')

def test(request):

    data =TodoForm()
    if request.method == "POST":
        todo1 =TodoForm(request.POST)
        if todo1.is_valid():
            todo1.save()
    return render(request,'test.html',{"form":data})

def read(request):
    data =Todo1.objects.all
    return render(request,'read.html',{'data':data})

# delete

def remove(request,id):
    data =Todo1.objects.get(id=id)
    data.delete()
    return redirect("read")

def update(request,id):
    data =Todo1.objects.get(id=id)
    form =TodoForm(instance=data)

    if request.method =="POST":
        todo =TodoForm(request.POST,instance=data)
        if todo.is_valid():
            todo.save()
            return redirect("read")
    return render(request,'update.html',{'form':form})

def  user(request):
    data =UserCreationForm()
    if request.method == "POST":
        user =UserCreationForm(request.POST)
        print(user)
        if user.is_valid():
            print("ok")
            user.save()
    return render(request,'user.html',{"form":data})