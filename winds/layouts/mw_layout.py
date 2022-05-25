import PySimpleGUI as sg

class mainWindowLayout:
    def create_layout(self):
        sg.theme('SystemDefault')
        header = [
            sg.Text('Data Visualizer', font=('Arial', 25)),
        ]

        file_selection = [
            [
                sg.Text('Open File'),
                sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse('Open'),
            ],
            [sg.Text('', key="-FILE STATUS-")]
        ]

        file_display = [
            [sg.Listbox(values=[], enable_events=True, size=(40,10), key="-FILE LIST-")]
        ]

        open_window = [
            sg.Button('Open Window', key="-OPEN FILE-", visible=False)
        ]

        layout = [
            header,
            file_selection,
            file_display,
            open_window,
        ]
        return layout
