# TimeEdit autoBooker v0.5
# Raspberry Pi desktop

# Libraries
from sys import path
path.append("/home/pi/autoBooker/")
import RGBreader
import selectDay
import sheets
import time
import random
from time import sleep
import pynput
from pynput.mouse import Button, Controller

"""
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
"""

mouse = Controller()
preferredRoom = "A2 071"
xOffset = 182
yOffset = 63

def bookingDesc(x):
    texts ={
    1 : "Ibsens ripsbaerbusker og andre buskvekster",
    2 : "retskevksub erdna go reksubreabspir snesbI",
    3 : "The Big Bang Theory",
    4 : "Fylkestrafikksikkerhetsutvalgssekretariatslederfunksjon",
    5 : "Landsdelsberedskapsfylkesmannsembetene",
    6 : "Forsiktighetsforanstaltning",
    7 : "Pneumonoultramicroscopicsilicovolcanoconiosis",
    8 : "Honorificabilitudinitatibus",
    9 : "Floccinaucinihilipilification",
    10 : "Eit ord, ein stein i ei kald elv. Ein stein til.",
    11 : "Eg lyt ha fleire steinar skal eg koma over."
}
    return (texts.get(x, "Whoops, Python n00bed"))

# Open Chromium
mouse.position=(66, 20)
mouse.click(Button.left, 1)
sleep(10)

# Chromium settings button
mouse.position=(1897, 114)
mouse.click(Button.left, 1)
sleep(1)

# Open new incognito window
mouse.position=(1682, 204)
mouse.click(Button.left, 1)
sleep(3)

# TimeEdit click
mouse.position=(158,149)
mouse.click(Button.left, 1)
sleep(3)

# Feide palogging click
mouse.position=(739+xOffset,409+yOffset)
mouse.click(Button.left, 1)
sleep(5)

# Input field click
mouse.position=(792, 568)
mouse.click(Button.left, 1)
sleep(2)
# Select user data click
mouse.position=(792, 618)
mouse.click(Button.left, 1)
sleep(2)
# Login button click
mouse.position=(959, 793)
mouse.click(Button.left, 1)
sleep(8)
# Room searchbox click
mouse.position=(107, 675)
mouse.click(Button.left, 1)
sleep(3)

# Select room
from pynput.keyboard import Key, Controller
keyboard = Controller()
for char in preferredRoom:
    keyboard.press(char)
    keyboard.release(char)
    sleep(0.12)

sleep(10)
from pynput.mouse import Button, Controller
mouse = Controller()

# Choose next week click
mouse.position=(1053, 730)
mouse.click(Button.left, 1)
sleep(3)

import datetime
x = datetime.datetime.now()
xSkip = 170 # Pixels to skip for each week day
if (x.strftime("%A") == "Monday"):
    if(RGBreader.checkIfRoomIsBooked(740+xSkip, 815) == False):
        # Choose next Tuesday
        mouse.position=(740+xSkip,815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)
elif(x.strftime("%A") == "Tuesday"):
    if(RGBreader.checkIfRoomIsBooked(740+(2*xSkip), 815) == False):
        # Choose next Wednesday
        mouse.position=(740+(2*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)
elif(x.strftime("%A") == "Wednesday"):
    if(RGBreader.checkIfRoomIsBooked(740+(3*xSkip), 815) == False):
        # Choose next Thursday
        mouse.position=(740+(3*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)
elif(x.strftime("%A") == "Thursday"):
    if(RGBreader.checkIfRoomIsBooked(740+(4*xSkip), 815) == False):
        # Choose next Friday
        mouse.position=(740+(4*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)
elif(x.strftime("%A") == "Friday"):
    if(RGBreader.checkIfRoomIsBooked(740+(5*xSkip), 815) == False):
        # Choose next Saturday
        mouse.position=(740+(5*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)
elif(x.strftime("%A") == "Saturday"):
    if(RGBreader.checkIfRoomIsBooked(740+(6*xSkip), 815) == False):
        # Choose next Sunday
        mouse.position=(740+(6*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)
elif(x.strftime("%A") == "Sunday"):
    if(RGBreader.checkIfRoomIsBooked(740, 815) == False):
        # Choose next Monday
        mouse.position=(740,815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        print("Preferred room is booked, trying next one.")
        preferredRoom = selectDay.selectNewRoom(0)


# Select end time dropdown
mouse.position=(856, 775)
mouse.click(Button.left, 1)
sleep(2)
# Select 1130 end time
mouse.position=(861, 1007)
mouse.click(Button.left, 1)
sleep(2)
# Select textbox for heading
mouse.position=(900, 950)
mouse.click(Button.left, 1)
sleep(1)

# Write booking heading
from pynput.keyboard import Key, Controller
keyboard = Controller()

randomInt = random.randint(1,10)
bookingText = bookingDesc(randomInt)

for char in bookingText:
    keyboard.press(char)
    keyboard.release(char)
    sleep(0.12)

from pynput.mouse import Button, Controller
mouse = Controller()

# Reserve
mouse.position=(964, 1051)
mouse.click(Button.left, 1)
sleep(5)

# Send confirmation
mouse.position=(1019, 903)
mouse.click(Button.left, 1)
sleep(5)

# Scroll down
mouse.position=(1912, 519)
sleep(2)
mouse.press(Button.left)
sleep(1)
mouse.move(0,300)
sleep(3)
mouse.release(Button.left)

# Send confirmation email to Marcus
mouse.position=(858, 993)
mouse.click(Button.left, 1)
sleep(10)

# Insert booking data to Google spreadsheet
sheets.insertToSheets(preferredRoom, "08:30 - 11:30")
print(preferredRoom)

# Close incognito window
mouse.position=(1905, 48)
mouse.click(Button.left, 2)
sleep(2)

# Close low voltage warning
mouse.position=(1905, 48)
mouse.click(Button.left, 2)
sleep(2)

# Close Chromium browser
mouse.position=(1905, 48)
mouse.click(Button.left, 2)
sleep(2)