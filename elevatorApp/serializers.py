from elevatorApp.models import Elevator, ElevatorRequest
from rest_framework import serializers

class ElevatorSeriazers(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        exclude = ('createdAt', 'updatedAt')
        

class ElevatorRequestSeriazers(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        exclude = ('createdAt', 'updatedAt')