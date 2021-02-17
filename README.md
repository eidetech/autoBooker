<a href="#"><img src="https://www.timeedit.net/assets/images/te_icon_gradient_vit_rounded@1x.png" width="50" height="50"></a> 
# autoBooker
TimeEdit autoBooker script (is all you need, and life is easy.)

## Installation
```bash
python3 -m pip install pyautogui
python3 -m pip install pynput
```

## Usage
Put preferred rooms in preferredRooms.csv, one room per line.
```csv
C3 090
C3 091
C3 092
```

## File structure/hierarchy
autoBooker.py - Main
RGBchecker.py - Check if room is already booked
selectDay.py  - Try next room in preferredRooms.csv list if the top preferred room is already booked

## Check number of code lines
```bash
cd /home/pi/autoBooker/
git ls-files | xargs wc -l
```
Last checked: 15.02.2021 --> 471

