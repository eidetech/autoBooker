import pyautogui # https://pyautogui.readthedocs.io/

"""
Command for installing pyautogui on linux: python3 -m pip install pyautogui
Command for installing pyautogui on windows: py -m pip install pyautogui
"""

# pyautogui.displayMousePosition() # Function to get RGB values current mouse position

def checkIfRoomIsBooked(x, y):
    bookedColor = [228, 228, 228] # RGB color for booked room
    cursorPosition = [x, y] # The cursor position to check the color for

    screenshot = pyautogui.screenshot() # Takes screenshoot of current image
    pix = screenshot.getpixel((cursorPosition[0], cursorPosition[1])) # Captures rgb values for the pixel at coordinate (x,y)

    r = (pix[0])
    g = (pix[1])
    b = (pix[2])

    if (r == bookedColor[0] and g == bookedColor[1] and b == bookedColor[2]):
        return True
        """
        The current position of the cursor is a booked room.
        The code in here should choose a new room and check again.
        """
    else:
        return False
        """
        The room is not booked, continue to book it.
        """
