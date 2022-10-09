from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.

def add_show(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    user=User.objects.all()
    context={'form':fm,'user':user}
    return render(request,"app/addshow.html",context)


def update(request,id):
    if request.method=="POST":
        user=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=user)
        
        if fm.is_valid():
            fm.save()
    else:
           user=User.objects.get(pk=id)
           fm=StudentRegistration(instance=user)
    context={'form':fm}
    return render(request,"app/update.html",context)

def delete(request,id):
    if request.method=="POST":
        user=User.objects.get(pk=id)
        user.delete()

    return HttpResponseRedirect('/')
