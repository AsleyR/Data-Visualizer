import PySimpleGUI as sg
import winds.layouts

def connect_mysql_window():
    c_mysql_layout = winds.layouts.connectMysqlWindow()
    c_mysql_layout = c_mysql_layout.create_layout()
    font = ("Arial", 12)

    window = sg.Window("Connect - Mysql Server", c_mysql_layout, font=font)

    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WINDOW_CLOSED:
            break