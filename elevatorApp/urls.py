from django.urls import path
from elevatorApp.views import ElevatorView, FetchRequest, StateChange
urlpatterns = [
    path('elevator',ElevatorView.as_view(),name='elevator'),
    path("fetchrequest/<int:id>", FetchRequest.as_view(), name="fetch-request"),
    path('statechange',StateChange.as_view(),name='statechange'),
]
