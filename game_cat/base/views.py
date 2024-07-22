from django.http import HttpResponse
from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Adam'},
    {'id': 2, 'name': 'Adam2'},
    {'id': 3, 'name': 'Adam3'},
    {'id': 4, 'name': 'Adam4'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
