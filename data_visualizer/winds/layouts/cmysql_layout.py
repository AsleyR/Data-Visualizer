import PySimpleGUI as sg

class connectMysqlWindow:
    def create_layout(self):
        sg.theme('SystemDefault')
        header = [
            sg.Text('Connect to Mysql Server', font=('Arial', 25)),
        ]

        connect_database = [
            [sg.Text('Ip:'), sg.Input("", size=(15,1))],
            [sg.Text('Port:'), sg.Input("", size=(15,1))],
            [sg.Text('User:'), sg.Input("", size=(15,1))],
            [sg.Text('User password:'), sg.Input("", size=(15,1))],
            [sg.Button("Connect", key="-CONNECT BUTTON-")]
        ]

        layout = [
            header,
            connect_database
        ]

        return layout