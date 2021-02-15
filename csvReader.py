import pynput
from pynput.keyboard import Key, Controller
import time
from time import sleep
import csv

rooms = {}
i = 0
with open('preferredRooms.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rooms[i] = (row[0])
            i = i+1


print("First recorded room, with index 0:") 
print(rooms[0])
print("First recorded room, with index 1:") 
print(rooms[1])     

# Printing rooms by index:
keyboard = Controller()
for char in rooms[1]:
    keyboard.press(char)
    keyboard.release(char)
    sleep(0.12)

