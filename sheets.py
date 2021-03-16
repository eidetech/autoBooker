def insertToSheets(room, time):
    import gspread # pip install gspread
    import datetime
    currentTime  = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")

    # Variable gc stores the credential info from the credentials file (JSON)
    gc = gspread.service_account(filename='credentials.json')
    # Variable sh stores the key to the specific worksheet (from URL)
    sh = gc.open_by_key('1PF8u1zsIfxwgVQ7HzSBXVOaQBf1z3PiXdIXXLeSkc7M')

    # Select sheet in the spreadsheet (sheet1, sheet2, sheet3, etc ...)
    worksheet = sh.worksheet("2021")
    backend = sh.worksheet("backend")

    # New entry data
    #room = "C3 090"
    #time = "08:30 - 11:30"

    # Get the row to put the booked room details into from backend sheet
    todaysRow = backend.acell('A2').value

    # Return all row numbers that are weekend days:
    weekendDays = backend.col_values(2)
    if todaysRow in weekendDays:
        # If todaysRow is in the list of rows that are weekend days:
        print("todaysRow is in weekendDays: skipping weekend.")
        todaysRow = int(todaysRow)+2
        print("Todays row is a weekend day: " + str(todaysRow))
        nextRow = int(todaysRow)+1
        print("Next row: " + str(nextRow))
        # Update the row value in backend sheet to nextRow
        backend.update('A2', (nextRow))
        # Insert booking data to worksheet
    else:
        # If the current row is a weekday:
        print("todaysRow is not in weekendDays, proceeding:")
        # Generate the next row number
        nextRow = int(todaysRow)+1
        print("Next row: " + str(nextRow))
        # Update the row value in backend sheet to nextRow
        backend.update('A2', (nextRow))


    worksheet.update("C"+str(todaysRow)+":E"+str(todaysRow), [[room, time, "autoBooker @ " + currentTime]])
