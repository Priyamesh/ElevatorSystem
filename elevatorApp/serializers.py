from elevatorApp.models import Elevator, ElevatorRequest
from rest_framework import serializers

class ElevatorSeriazers(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'

class ElevatorRequestSeriazers(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = '__all__'