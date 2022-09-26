from util.class_templates.base_window import BaseWindow
from new_layout.open_file_layout import OpenFileLayout

class OpenFileWindow(BaseWindow):
    def __init__(self, window_name, window_layout):
        super().__init__(window_name, window_layout)
    
    def init_window(self):
        window = self.create_window()

        # Init program loop
        while True:
            event, values = window.read()

open_file_window = OpenFileWindow("Data Visualizer", OpenFileLayout())
open_file_window.init_window()