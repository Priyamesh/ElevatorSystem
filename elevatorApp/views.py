from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from elevatorApp.models import Elevator, ElevatorRequest
from elevatorApp.serializers import ElevatorSeriazers, ElevatorRequestSeriazers
from rest_framework.response import Response
import json
# Create your views here.

class ElevatorView(APIView):

    def post(self,request):
        data = json.loads(request.body)
        print(data)
        numberOfElevator=data.get('numberOfElevator')
        print(numberOfElevator)

        elevatorList=[]
        for i in range(numberOfElevator):
            elevatorList.append(Elevator())

        elevators = Elevator.objects.bulk_create(elevatorList)
        serialized_elevator = ElevatorSeriazers(elevators, many=True)

        return Response(data=serialized_elevator.data, status=status.HTTP_201_CREATED)

        
class FetchRequest(APIView):

    def get(self,request,id):
        requestList = ElevatorRequest.objects.filter(elevator__id=id)
        serialized_req_list = ElevatorRequestSeriazers(requestList, many=True)
        return Response(data=serialized_req_list.data, status=status.HTTP_200_OK)
    


class NextDestination(APIView):

    def get(self,request,id):
        pass

class StateChange(APIView):

    def post(self,request):
        data = json.loads(request.body)
        print(data)
        state = data.get('state')
        id = data.get('id')
        print(state)

        try:
            elevator_obj = Elevator.objects.filter(id=id).first()
            elevator_obj.state=state
            elevator_obj.currentFloor=15
            elevator_obj.save()
        except Exception as err:
            return Response({'messge':'gaand fat gyi'})
        
        return Response({'message':'ho gya update'})
