from django.shortcuts import render, redirect
from .models import Room, Topic, Message
from .forms import RoomForm

# Create your views here.

# rooms = [
#      {'id': 1, 'name': 'Lets learn python!'},
#      {'id': 2, 'name': 'Design with me'},
#      {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all()    
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    #room = None
    room = Room.objects.get(id=pk)    
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room':room}

    return render(request,'base/room.html',context)

#@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method=='POST':
        #print(request.POST)
        #request.POST.get('name')
        form  = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)

#@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)

    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request,'base/delete.html', {'obj':room})
