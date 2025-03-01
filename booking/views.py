from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import  Room, Table, Visitor


# Create your views here.
def rooms_list(request:HttpRequest):
    rooms = Room.objects.all()

    context = {"rooms_list": rooms}

    return render(request,"booking/rooms_list.html",context = context)



def tables_list(request:HttpRequest, room_id:int):
    # room = Room.objects.get(id=room_id)
    # tables = Table.objects.filter(room=room)

    tables = Table.objects.filter(room__id =room_id)

    context = {"tables": tables}

    return render(request,"booking/tables_list.html", context=context)

def visitors_list(request:HttpRequest):
    visitors = Visitor.objects.all()

    context = {"visitors_list": visitors}

    return render(request,"booking/visitors_list.html",context = context)

def create_room(request:HttpRequest):
    if request.method=="GET":
        return render(request,"booking/create_room.html")
    if request.method=="POST":
        room_number = request.POST.get("room_number")
        tables_num = request.POST.get("tables_num", 0)

        Room.objects.create(number=room_number,tables_num=tables_num)
        return redirect(reverse("rooms-list"))