from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json


# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context={'form':form}
    return render(request,'registration/registration.html',context)

def index(request):
    return render(request,'index.html')

def chatroom(request,pk:int):
    other_user=get_object_or_404(User,pk=2)
    messages=Message.objects.filter(Q(receiver=other_user,sender=request.user)|Q(receiver=request.user,sender=other_user))
    messages.update(seen=True)
    context={
        'other_user':other_user,
        'messages':messages,
    }
     
    return render(request,'room.html',context)