from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Room, Topic, Message
from .forms import RoomFrom
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# rooms = [
#     {'id': 1, 'name': 'Adam'},
#     {'id': 2, 'name': 'Adam2'},
#     {'id': 3, 'name': 'Adam3'},
#     {'id': 4, 'name': 'Adam4'},
# ]

def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is wrong')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    if request.GET.get('q') is not None:
        q = request.GET.get('q')
    else:
        q = ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        messages = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomFrom()
    if request.method == 'POST':
        form = RoomFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomFrom(instance=room)

    if request.user != room.host and not request.user.is_superuser:
        return HttpResponseForbidden('You are not allowed to do this.')

    if request.method == 'POST':
        form = RoomFrom(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host and not request.user.is_superuser:
        return HttpResponseForbidden('You are not allowed to do this.')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user and not request.user.is_superuser:
        return HttpResponseForbidden('You are not allowed to do this.')

    if request.method == 'POST':
        message.delete()
        return redirect('home') # dodać room/id zamiast home
    return render(request, 'base/delete.html', {'obj': message})
