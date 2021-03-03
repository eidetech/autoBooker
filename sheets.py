import gspread # pip install gspread

# Variable gc stores the credential info from the credentials file (JSON)
gc = gspread.service_account(filename='credentials.json')
# Variable sh stores the key to the specific worksheet (from URL)
sh = gc.open_by_key('1PF8u1zsIfxwgVQ7HzSBXVOaQBf1z3PiXdIXXLeSkc7M')

# Select sheet in the spreadsheet (sheet1, sheet2, sheet3, etc ...)
worksheet = sh.worksheet("2021")
backend = sh.worksheet("backend")

# Get the row to put the booked room details into from backend sheet
todaysRow = backend.acell('A2').value
# Generate the next row number
nextRow = int(todaysRow)+1
# Update the row value in backend sheet to nextRow
backend.update('A2', (nextRow))

# New entry data
room = "C3 090"
time = "08:30 - 11:30"

# Skip values for weekends
weekendDays = backend.col_values(2)
if todaysRow in weekendDays:
    print("todaysRow is in weekendDays: skipping weekend.")
    todaysRow = int(todaysRow)+2

# Insert booking data to worksheet
worksheet.update("C"+str(todaysRow)+":D"+str(todaysRow), [[room, time]])
