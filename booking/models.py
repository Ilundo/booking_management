from django.db import models

# Create your models here.

class Visitor(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name
    
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats=models.IntegerField()
    smooking = models.BooleanField()
    is_premium= models.BooleanField()
    
    room = models.ForeignKey("Room",on_delete=models.CASCADE)

    
    def __str__(self):
        return f"Table №{self.number} in room №{self.room.number} with {self.seats} seats"
    

class BookedTable(models.Model):
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)   

    datetime = models.DateTimeField()


    def __str__(self):
        return f"Booked Table №{self.table.number} on {self.datetime}"


class Room(models.Model):
    number = models.IntegerField(unique=True)
    tables_num = models.IntegerField()


    def __str__(self):
        return f"Room №{self.number} with {self.tables_num} tables"
    
class BookedRoom(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)

    datetime= models.DateTimeField()


    def __str__(self):
        return f"Booked Room №{self.room.number} on {self.datetime}"
    

