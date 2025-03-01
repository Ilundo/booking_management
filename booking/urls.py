from django.urls import path
from .views import create_room, rooms_list, tables_list, visitors_list
urlpatterns = [
    path("rooms/list/",rooms_list,name="rooms-list" ),
    path("tables/list/<int:room_id>",tables_list,name="tables-list"),
    path("visitors/list/",visitors_list, name="visitors-list" ),
    path("room/create/",create_room,name="create-room")
]
