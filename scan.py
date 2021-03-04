import pynput
from pynput.mouse import Button, Controller
from time import sleep
import RGBreader
mouse = Controller()

#DEBUG show mouse pos:
#print(mouse.position)

def scanDay(day):
    isBooked = {} # Define return variable
    if (day == "Monday"):
        # Check if selected room is booked next Tuesday
        x = 832
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    elif(day == "Tuesday"):
        # Check if selected room is booked next Wednesday
        x = 999
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    elif(day == "Wednesday"):
        # Check if selected room is booked next Thursday
        x = 1166
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    elif(day == "Thursday"):
        # Check if selected room is booked next Friday
        x = 1334
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    elif(day == "Friday"):
        # Check if selected room is booked next Saturday
        x = 1502
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    elif(day == "Saturday"):
        # Check if selected room is booked next Sunday
        x = 1668
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    elif(day == "Sunday"):
        # Check if selected room is booked next Monday
        x = 665
        y = 815
        xPos = x
        #DEBUG move mouse pos to start:
        #mouse.position=(x,y)
    else:
        return "The argument provided is not a day."
        
    while(x<(xPos+164)):
        if (RGBreader.checkIfRoomIsBooked(x, y) == True):
            isBooked = True
            break
        else:
            isBooked = False

        #DEBUG show mouse pos on screen:
        #mouse.position=(x,y)
        x=x+10
        sleep(0.1)
    return isBooked

print(scanDay("Saturday"))
