from django.contrib import admin
from elevatorApp.models import Elevator, ElevatorRequest
# Register your models here.



class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'currentFloor', 'status')

class ElevatorRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'elevator', 'sourceFloor', 'destinationFloor', 'status')

admin.site.register(Elevator,ElevatorAdmin)
admin.site.register(ElevatorRequest,ElevatorRequestAdmin)