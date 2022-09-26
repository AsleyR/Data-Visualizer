from util.class_templates.base_layout import BaseWindowLayout

class OpenFileLayout(BaseWindowLayout):
    def __init__(self, theme="SystemDefault"):
        super().__init__(theme)
        self.layout = self.create_window_layout()

    def create_window_layout(self):
        sg.theme = self.window_theme

        layout = [
            [sg.Text("DATA")]
            [sg.Button("PUSH ME")]
        ]

        return layout