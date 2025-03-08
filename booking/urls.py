from django.urls import path
from .views import book_room, book_table, create_room, create_table, rooms_list, tables_list, visitors_list
urlpatterns = [
    path("rooms/list/",rooms_list,name="rooms-list" ),
    path("tables/list/<int:room_id>",tables_list,name="tables-list"),
    path("visitors/list/",visitors_list, name="visitors-list" ),
    path("room/create/",create_room,name="create-room"),
    path("room/book/", book_room,name="book-room"),
    path("table/book/", book_table, name="book-table"),
    path("table/create/",create_table,name="create-table"),
    
]
