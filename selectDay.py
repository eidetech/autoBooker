def selectNewRoom(y):
    import RGBreader
    import scan
    import pynput
    from pynput.mouse import Button, Controller
    mouse = Controller()
    from time import sleep
    import datetime
    import csv

    rooms = {}
    i = 0
    with open('/home/pi/autoBooker/preferredRooms.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rooms[i] = (row[0])
            i = i+1

    # Room searchbox click
    mouse.position=(220, 675)
    mouse.click(Button.left, 1)
    sleep(3)

    print("Clicked searchbox.")

    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    # Remove old room text (backspace 6 seconds)
    keyboard = Controller()
    for i in range(5):
        keyboard.press(Key.backspace)
        sleep(1)

    keyboard.release(Key.backspace)
    print("Removed text from searchbox.")
    sleep(2)
    
    # Room searchbox click
    mouse.position=(220, 675)
    mouse.click(Button.left, 1)
    sleep(1)
    print("Clicked searchbox before entering new room.")
    # Select room
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    for char in rooms[y]:
        keyboard.press(char)
        keyboard.release(char)
        sleep(0.12)

    print("Entered new room into searchbox.")
    sleep(10)
    from pynput.mouse import Button, Controller
    mouse = Controller()
    
    x = datetime.datetime.now()
    xSkip = 170 # Pixels to skip for each week day
    if (x.strftime("%A") == "Monday"):
        if(scan.scanDay("Monday") == False):
            # Choose next Tuesday
            mouse.position=(740+xSkip,815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)
    elif(x.strftime("%A") == "Tuesday"):
        if(scan.scanDay("Tuesday") == False):
            # Choose next Wednesday
            mouse.position=(740+(2*xSkip),815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)
    elif(x.strftime("%A") == "Wednesday"):
        if(scan.scanDay("Wednesday") == False):
            # Choose next Thursday
            mouse.position=(740+(3*xSkip),815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)
    elif(x.strftime("%A") == "Thursday"):
        if(scan.scanDay("Thursday") == False):
            # Choose next Friday
            mouse.position=(740+(4*xSkip),815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)
    elif(x.strftime("%A") == "Friday"):
        if(scan.scanDay("Friday") == False):
            # Choose next Saturday
            mouse.position=(740+(5*xSkip),815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)
    elif(x.strftime("%A") == "Saturday"):
        if(scan.scanDay("Saturday") == False):
            # Choose next Sunday
            mouse.position=(740+(6*xSkip),815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)
    elif(x.strftime("%A") == "Sunday"):
        if(scan.scanDay("Sunday") == False):
            # Choose next Monday
            mouse.position=(740,815)
            mouse.click(Button.left, 1)
            sleep(3)
            mouse.position=(715, 820)
            mouse.click(Button.left, 1)
            sleep(3)
        else:
            print("Preferred room " + rooms[y] + " is booked, trying next one.")
            selectNewRoom(y+1)


    preferredRoom = rooms[y]
    return preferredRoom
            
