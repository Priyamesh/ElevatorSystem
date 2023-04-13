from django.db import models

ELEVATOR_STATE_CHOICES = (('working','WORKING'),
                          ('maintenance ','MAINTENANCE'))

ELEVATOR_STATUS_CHOICES = (('idle','IDLE'),
                          ('moving ','MOVING'))

DOOR_STATE_CHOICES = (
    ("open", "OPEN"),
    ("close", "CLOSE"),  
)


class TimestampModel(models.Model):
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

  class Meta:
      abstract = True

class Elevator(TimestampModel):
    state = models.CharField(choices=ELEVATOR_STATE_CHOICES, default=ELEVATOR_STATE_CHOICES[0][0], max_length=20)
    currentFloor = models.IntegerField(default=0) #assuming we don't have basement
    doorState = models.CharField(choices=DOOR_STATE_CHOICES, default=DOOR_STATE_CHOICES[0][0], max_length=20)
    status = models.CharField(choices=ELEVATOR_STATUS_CHOICES, default=ELEVATOR_STATUS_CHOICES[0][0], max_length=20)

class ElevatorRequest(TimestampModel):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    sourceFloor = models.IntegerField()
    destinationFloor = models.IntegerField()

