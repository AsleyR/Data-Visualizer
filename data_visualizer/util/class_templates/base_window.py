import PySimpleGUI as sg

class BaseWindow:
    def __init__(self, window_name, window_layout):
        self.window_name = window_name
        self.window_layout = window_layout
        self.font = ("Arial", 16)

    def create_window(self):
        window = sg.Window(self.window_name, self.window_layout, font=self.font)
        return window
    
    # Checks if window is closed by user or by a program process
    def close_window(self, event, window):
        if event == "EXIT" or event == sg.WIN_CLOSED:
            window.close()
            return
    
    # Init Program Window
    # Basic window setup
    def init_window(self):
        window = self.create_window()
        while True:
            event, values = window.read()

            # Check if window is closed
            if self.close_window(event, window):
                break
