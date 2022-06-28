import PySimpleGUI as sg

class fileWindowLayout:
    def create_layout(self, data, headings, dictionary):

        sg.theme('SystemDefault')
        sg.set_options(font=('Arial', 13))
        headings = headings
        d_value = data

        header = [
            sg.Text('Data Visualizer', font=('Arial', 25),
            justification='center')
        ]

        data_table = [
            sg.Table(
                values=d_value, headings=headings, 
                size=(30,20), max_col_width=25,
                justification='center', auto_size_columns=True,
                expand_x=True, expand_y=True,
                text_color='black', enable_events=True,
                # row_colors=((0,"red"),(2,"yellow")),
                alternating_row_color=sg.theme_button_color('lightgrey')[1],
                key="-DATA TABLE-"
            )
        ]

        combobox_value = ["No Selection"]
        combobox_value.extend(headings)

        error_text = [
            [sg.Text('', enable_events=True, text_color='red', key="-ERROR MESSAGE-")]
        ]


        filter_selection = [
            [
                sg.Text('Search in:'),
                sg.Combo(
                    headings, enable_events=True,
                    key="-SEARCH FILTER-"
                ),
                sg.Input(size=(25,1), enable_events=True, key="-SEARCH-"),
                sg.Text(
                    '', enable_events=True, visible=False, 
                    key="-SEARCH RESULT TEXT-"
                    ),
                sg.Button('Search', button_color='royal blue'),
                sg.Button('Reset', size=(5,1), enable_events=True, 
                button_color='black', key="-SEARCH RESET-")
            ],
            [sg.Text('', enable_events=True, key="-FILTER STATUS-")],
            [
                sg.Text('Filter by:'),
                sg.Combo(
                    combobox_value, 
                    enable_events=True, key="-FILTER COMBOBOX-"
                    ),
                sg.Text('Show only: ', visible=False, key="-SHOW ONLY-"),
                sg.Combo(
                    [], 
                    size=(25,1),
                    enable_events=True, visible=False, 
                    key="-SHOW COMBOBOX-"
                    ),
                # sg.In(size=(25,1), enable_events=True, key="-FILTER-"),
                sg.Button('Reset', size=(5,1), enable_events=True,
                visible=False,
                button_color='black', key="-FILTER RESET-")
            ]
        ]

        layout = [
            # header,
            data_table,
            error_text,
            filter_selection,
        ]

        return layout