from tkinter import E
import PySimpleGUI as sg
# import csv
# from csv_data import csvData
import os.path
import winds
import util

# Create Windows
main_window = winds.main_window
file_window = winds.file_window


# I do not know what the fuck does this function does LMAO
def dlt_retrun_values(a):
    for value in range(len(a)):
        a.remove(a[value])


# Program Controller
# Event loop
while True:
    
    # Initialize main window
    # event_main has to equal the window in order to get the return values
    event_main = main_window()

    if event_main[0] == "EXIT":
        print('Exiting loop')
        break

    # I HATE these nested functions, but it works >:(    
    elif event_main[0] == "Open Window":
        print('Opening File Window')
        # set data values
        csv_data = event_main[1]
        csv_headings = event_main[2]
        csv_data_dict = event_main[3]

        event_file = file_window(csv_data, csv_headings, csv_data_dict)

        if event_file[0] == "EXIT":
            print('Exiting loop and closing file window')
            break

        if event_file[0] == "CLICK ME":
            print('EVENT EXECUTED!')
            pass
        pass
