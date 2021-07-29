from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse,HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json
from django.contrib.humanize.templatetags.humanize import naturaltime


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
    users = User.objects.all()
    context={
        'users':users,
    }
    return render(request,'index.html',context)

def profileView(request):
    logged_in_user=request.user #logged in user
    user=Profile.objects.get(user=logged_in_user)
    print(user)
    
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfleUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfleUpdateForm(instance=request.user.profile)
    ctx={
        "user":user,
        'u_form':u_form,
        'p_form':p_form
    }
   
    return render(request,'profile.html',ctx)


@login_required(login_url='/login')
def room(request, room=""):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkroom(request):
    room=request.POST['room_name']
    username=request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('room')

    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('room')

def send(request):
    messages = request.POST['messages']
    form=messageForm()
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            savemess = form.save(commit=False)
            savemess.user = request.user.profile
            savemess.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form =messageForm()
    params = {
        'form': form,
    }
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=messages, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room=""):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

