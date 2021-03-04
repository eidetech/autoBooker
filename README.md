<a href="#"><img src="https://www.timeedit.net/assets/images/te_icon_gradient_vit_rounded@1x.png" width="50" height="50"></a> 
# autoBooker
TimeEdit autoBooker script (is all you need, and life is easy :grin:)

## Installation
```bash
python3 -m pip install pyautogui
python3 -m pip install pynput
python3 -m pip install gspread
```

## Usage
Put preferred rooms in preferredRooms.csv, one room per line.
```csv
C3 090
C3 091
C3 092
```

## File structure/hierarchy
- autoBooker.py - Main
  - selectDay.py  - Try next room in preferredRooms.csv list if the top preferred room is already booked.
  - scan.py - Function to completely scan the day block to be booked in TimeEdit.
        * RGBchecker.py - Check if room is already booked. 
  - sheets.py - Google Sheets integration -> interts booking data to spreadsheet.

## Tasks
- [x] Initial concept!
- [x] Avoid already booked rooms detection
- [x] If room is already booked: choose new room from a list of preferred rooms
- [ ] Dual user booking
- [x] Automatic Google Sheets integration (Sheets API) 
- [ ] Automatic Google Calendar integration (Calendar API)
## Check number of code lines
```bash
cd /home/pi/autoBooker/
git ls-files | xargs wc -l
```
Last checked: 15.02.2021 --> 471

