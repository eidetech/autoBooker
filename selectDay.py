def selectNewRoom():
    # Room searchbox click
    mouse.position=(107, 675)
    mouse.click(Button.left, 1)
    sleep(3)

    # Remove old room text (backspace 6 times)
    keyboard = Controller()
    for i in range(5):
    keyboard.press(Key.backspace)
    sleep(1)
    
    # Select room
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    for char in "C3 090":
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

    x = datetime.datetime.now()
    xSkip = 170 # Pixels to skip for each week day
    if (x.strftime("%A") == "Monday"):
        # Choose next Tuesday
        mouse.position=(740+xSkip,815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    elif(x.strftime("%A") == "Tuesday"):
        # Choose next Wednesday
        mouse.position=(740+(2*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    elif(x.strftime("%A") == "Wednesday"):
        # Choose next Thursday
        mouse.position=(740+(3*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    elif(x.strftime("%A") == "Thursday"):
        # Choose next Friday
        mouse.position=(740+(4*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    elif(x.strftime("%A") == "Friday"):
        # Choose next Saturday
        mouse.position=(740+(5*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    elif(x.strftime("%A") == "Saturday"):
        # Choose next Sunday
        mouse.position=(740+(6*xSkip),815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    elif(x.strftime("%A") == "Sunday"):
    if(checkIfRoomIsBooked(740, 815) == False):
        # Choose next Monday
        mouse.position=(740,815)
        mouse.click(Button.left, 1)
        sleep(3)
        mouse.position=(715, 820)
        mouse.click(Button.left, 1)
        sleep(3)
    else:
        selectNewRoom()
