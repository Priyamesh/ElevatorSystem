from django.urls import path
from elevatorApp.views import ElevatorView, FetchRequest, ElevatorStateChange,ElevevatorDoorStateChange, \
    NextDestination, ElevatorMovement, SaveElevatorRequest
urlpatterns = [
    path('elevator',ElevatorView.as_view(),name='elevator'),
    path("fetchrequest/<int:id>", FetchRequest.as_view(), name="fetch-request"),
    path('nextdestination/<int:id>',NextDestination.as_view(),name='nextdestination'),
    path('elevatormovement/<int:id>',ElevatorMovement.as_view(),name='elevatormovement'),
    path('saverequest',SaveElevatorRequest.as_view(),name='saverequest'),
    path('statechange',ElevatorStateChange.as_view(),name='statechange'),
    path('doorstatechange',ElevevatorDoorStateChange.as_view(),name='doorstatechange'),
    
]
