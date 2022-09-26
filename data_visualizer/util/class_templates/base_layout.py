import PySimpleGUI as sg

class BaseWindowLayout:
    def __init__(self, theme="SystemDefault"):
        self.window_theme = theme
        self.layout = []

    def create_window_layout(self):
        sg.theme = self.window_theme
        layout = self.layout
        return layout