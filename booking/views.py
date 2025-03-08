from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import  BookedRoom, BookedTable, Room, Table, Visitor


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

def create_table(request: HttpRequest):
    if request.method == "GET":
        return render(request, "booking/create_table.html")

    if request.method == "POST":
        table_number = request.POST.get("table_number")
        room_id = request.POST.get("room_id")

        room = get_object_or_404(Room, id=room_id)
        Table.objects.create(number=table_number, room=room)

        return redirect(reverse("rooms-list"))

def book_room(request:HttpRequest):
    if request.method== "GET":
        return render(request, "booking/book_room.html")
    if request.method=="POST":
        room_number = request.POST.get("room_num")
        visitor_name = request.POST.get("visitor_name")
        datetime = request.POST.get("datetime")

        room = Room.objects.get(number=room_number)
        visitor, new= Visitor.objects.get_or_create(name=visitor_name)

        new_booked_room = BookedRoom.objects.create(room = room,visitor=visitor,datetime=datetime)

        return redirect(reverse("rooms-list"))
    
def book_table(request: HttpRequest):
    if request.method == "GET":
        return render(request, "booking/book_table.html")

    if request.method == "POST":
        table_number = request.POST.get("table_num")
        visitor_name = request.POST.get("visitor_name")
        datetime = request.POST.get("datetime")

        table = Table.objects.get(number=table_number)
        visitor, new = Visitor.objects.get_or_create(name=visitor_name)

        new_booked_table = BookedTable.objects.create(table = table,visitor=visitor,datetime=datetime)
        return redirect(reverse("rooms-list"))
