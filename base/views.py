from django.shortcuts import render
from .models import Room


# Create your views here.

rooms = [
    {'id': 1, 'name': 'Ngobrol Anime'},
    {'id': 2, 'name': 'Ngobrol Kuliah'},
    {'id': 3, 'name': 'Ngobrol Teknologi'},
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
