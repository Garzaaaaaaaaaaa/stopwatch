import time
import math
import os
from pynput import keyboard

"""
    print('')
    running = True
    total_time = 0
    while running == True:
        trackingSec = int(time.strftime('%S'))
        if trackingSec == 60
        trackingMin = int(time.strftime('%M'))
        trackingHour = int(time.strftime('%H'))
        time.sleep(1)
        currentSec = int(time.strftime('%S'))
        currentMin = int(time.strftime('%M'))
        currentHour = int(time.strftime('%H')) 
        printedSec = currentSec - trackingSec
        printedMin = currentMin - trackingMin
        printedHour = currentHour - trackingHour
        total_time = total_time + printedSec
        print("total time elapsed: " + str(total_time))
        print(time.strftime('%H:%M:%S'))
        print()
"""

def draw_art(bar, seconds):
    if seconds % 2 == 0:
        bar.append('<')
    else:
        bar.append('>')
    return bar

def main():
    running = True
    conversion_factor = 60
    second_counter = 0
    mins_counter = 0
    hour_counter = 0
    progress_art = []

    while running == True:
        progress_bar = draw_art(progress_art, int(second_counter))
        if len(progress_bar) == 60:
            progress_bar.clear()
        second_counter = second_counter + 1
        if second_counter / conversion_factor == 1:
            mins_counter = mins_counter + 1
            second_counter = 0
            if mins_counter / conversion_factor == 1:
                hour_counter = hour_counter + 1
                mins_counter = 0
        if second_counter < 10:
            second_counter = '0' + str(second_counter)
        if mins_counter < 10:
            mins_counter = '0' + str(mins_counter)
        if hour_counter < 10:
            hour_counter = '0' + str(hour_counter)

        time.sleep(1) # very accurate keeper of seconds, try time.ctime()
        print('Time elapsed: ' + str(hour_counter) + ':' + str(mins_counter) + ':' + str(second_counter))
        for filling in progress_bar:
            print(filling, end="")
        print()

        second_counter = int(second_counter)
        mins_counter = int(mins_counter)
        hour_counter = int(hour_counter)

main()
