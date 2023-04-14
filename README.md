# ElevatorSystem

This Django project provides an API for an Elevator Management System. It allows users to request an elevator, fetch the status of their request, check the next destination of the elevator, and change the state of the elevator and its doors.

Dependencies
This project requires the following dependencies to be installed:
  Python 3.x
  Django 4.
  Django Rest Framework
  
Installation
  Clone the repository to your local machine
  Create a virtual environment and activate it
  Install the dependencies using the command pip install -r requirements.txt
  Run migrations using the command python manage.py migrate
  Start the server using the command python manage.py runserver
  
API Endpoints
The following API endpoints are available in this project:

1. Elevator
URL: /elevator
Method: POST
Request format: {"numberOfElevator"}
Description: Returns the status of the elevator

2. Fetch Request
URL: /fetchrequest/<int:id>
Method: GET
Description: Returns ALL requersts by elevator ID

3. Next Destination
URL: /nextdestination/<int:id>
Method: GET
Description: Returns the next destination of the elevator by Elevator ID

4. Elevator Movement
URL: /elevatormovement/<int:id>
Method: GET
Description: Fetch the elevator movcement for elevaor

5. Save Request
URL: /saverequest
Method: POST
Request  {
    "type",
    "requestId",
    "destinationFloor"
    "sourceFloor"
}
Description: Saves a new elevator request

6. Elevator State Change
URL: /statechange
Method: POST
REQUEST {"STATE"}
Description: Changes the state of the elevator

7. Elevator Door State Change
URL: /doorstatechange
Method: POST
REQUEST {"STATE"}
Description: Changes the state of the elevator doors

Conclusion
This API provides a simple way to manage elevators and elevator requests.





