from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from elevatorApp.models import Elevator, ElevatorRequest
from elevatorApp.serializers import ElevatorSeriazers, ElevatorRequestSeriazers
from rest_framework.response import Response
import json
from elevatorApp.models import ELEVATOR_STATE_CHOICES, DOOR_STATE_CHOICES, ELEVATOR_STATUS_CHOICES, ELEVATOR_REQUEST_CHOICES
# Create your views here.


# Initialise the elevator system to create ‘n’ elevators in the system
class ElevatorView(APIView):

    def post(self,request):
        data = json.loads(request.body)
        numberOfElevator=data.get('numberOfElevator')

        elevatorList=[]
        for i in range(numberOfElevator):
            elevatorList.append(Elevator())

        try:
            elevators = Elevator.objects.bulk_create(elevatorList)
            serialized_elevator = ElevatorSeriazers(elevators, many=True)
        except Exception as err:
            return Response({'message':'Unable to create elevators'})

        return Response(data=serialized_elevator.data, status=status.HTTP_201_CREATED)

# Fetch all requests for a given elevator
class FetchRequest(APIView):

    def get(self,request,id):
        try:
            requestList = ElevatorRequest.objects.filter(elevator__id=id)
            serialized_req_list = ElevatorRequestSeriazers(requestList, many=True)
            return Response(data=serialized_req_list.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'message':'unable to fetch request for given elevator'})
    

# Fetch the next destination floor for a given elevator
class NextDestination(APIView):

    def get(self,request,id):
        max_diff=1000
        nextdestinationfloor=0
        try:
            requestList = ElevatorRequest.objects.filter(elevator__id=id,destinationFloor__isnull=False, status='pending' ).values_list('destinationFloor')
            ele_obj = Elevator.objects.filter(id=id).first()
            elecurrentFloor= ele_obj.currentFloor

            for tup in requestList:
                if tup[0]-elecurrentFloor  < max_diff :
                    nextdestinationfloor = tup[0]
            
            data={
                'nextdestination':nextdestinationfloor
            }
            return Response({'message':'nextdestination fetched','data':data})
        except Exception as err:
            return Response({'message':'unable to fetch next destination for given elevator',"error":err})



# Fetch if the elevator is moving up or down currently
class ElevatorMovement(APIView):
    def get(self,request,id):
        try:
            ele_movement = Elevator.objects.filter(id=id).first().status
            data={
                'movement':ele_movement
            }
            return Response({'message':'Movement fetched','data':data})
        except Exception as err:
            return Response({'message':'Unable to fetch movement for given elevator','error':err})




# Saves user request to the list of requests for a elevator
class SaveElevatorRequest(APIView):

    def post(self,request):
        print("inside save request api")

        data=json.loads(request.body)
        requestType=data.get('type')
        requestId=data.get('requestId')
        sourceFloor =  data.get('sourceFloor')
        destinationFloor = data.get('destinationFloor')
        
        if requestType=='external':
            if sourceFloor == None:
                return Response({'message':'incomplete request data'})
            
            max_diff=1000
            destinedElevator=None

            try:
                elevators = Elevator.objects.filter(state='working')
                for ele_obj in elevators:
                    if abs(ele_obj.currentFloor-sourceFloor)  < max_diff :
                        destinedElevator = ele_obj

                requestObj = ElevatorRequest.objects.create(elevator=destinedElevator, sourceFloor=sourceFloor)
                # if destinedElevator.currentFloor < sourceFloor:
                #     destinedElevator.status=ELEVATOR_STATUS_CHOICES[1][0] # moving up
                # else:
                #     destinedElevator.status=ELEVATOR_STATUS_CHOICES[2][0] # moving down
                destinedElevator.currentFloor=sourceFloor
                destinedElevator.save()
                
                data={
                    'elevatorId':destinedElevator.id,
                    'requestId':requestObj.id
                }
                return Response({'message':'Elevator assigned', 'data':data})
            except Exception as err:
                return Response({'message':'Unable to assign elevator for given request','error':err})
        
        elif requestType=='internal':
            if destinationFloor == None or requestId == None:
                return Response({'message':'incomplete request data'})
            
            try:
                requestObj = ElevatorRequest.objects.filter(id=requestId).first()
                requestObj.destinationFloor=destinationFloor
                requestObj.status=ELEVATOR_REQUEST_CHOICES[1][0]

                elevatorObj=requestObj.elevator
                # elevatorObj.status=ELEVATOR_STATUS_CHOICES[0][0] #making idel
                elevatorObj.currentFloor=destinationFloor
                elevatorObj.save()
                requestObj.save()

                data={
                    'elevator_id':elevatorObj.id,
                    'request_id':requestObj.id,
                    'destination_floor':destinationFloor
                }
                return Response({'message':'Elevator Reachead to Destination','data':data})
            except Exception as err:
                return Response({'message':'Unable to process Elevator for given destionation','error':err})

        return Response({'message':'Invalid request type'})




# Mark a elevator as not working or in maintenance
class ElevatorStateChange(APIView):

    def post(self,request):
        data = json.loads(request.body)
        state = data.get('state')
        id = data.get('id')

        try:
            elevator_obj = Elevator.objects.filter(id=id).first()
            for sub_state in ELEVATOR_STATE_CHOICES:
                if state == sub_state[0]:
                    elevator_obj.state=sub_state[0]
                    elevator_obj.save()
            return Response({'message':'Updated state for given elevator'})
            
        except Exception as err:
            return Response({'messge':'Unable to change state fotr given elevator','error':err})
        
        


# Open/close the door.
class ElevevatorDoorStateChange(APIView):

    def post(self,request):
        data = json.loads(request.body)
        state = data.get('state')
        id = data.get('id')

        try:
            elevator_obj = Elevator.objects.filter(id=id).first()
            for sub_state in DOOR_STATE_CHOICES:
                if state == sub_state[0]:
                    elevator_obj.doorState=sub_state[0]
                    elevator_obj.save()
            return Response({'message':'Updated door status for given elevator'})
        
        except Exception as err:
            return Response({'messge':'Unable to change door status fotr given elevator','error':err})