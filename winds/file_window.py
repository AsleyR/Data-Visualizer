import PySimpleGUI as sg
import util
import winds.layouts

def file_window(data, headings, dictionary):
    file_w_layout = winds.layouts.fileWindowLayout()
    file_w_layout = file_w_layout.create_layout(data, headings, dictionary)

    search_data = util.searchFunctions(dictionary)
    table_dict = dictionary

    font = ("Arial", 12)
    table_value = data

    window = sg.Window('Data Visualizer', file_w_layout, font, finalize=True)

    # table = window["-DATA TABLE-"]
    # table.bind('<Button-1>', "Click")
    
    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            event_list = "EXIT"
            window.close()
            return event_list

        elif event == "-FILTER-":
            filter_selection = values["-FILTER-"]
            if filter_selection != "No Selection":
                combobox_value = search_data.get_all_specific_items(filter_selection)
                combobox_value.sort()
                combobox_value.insert(0, 'No selection')

                window["-SHOW ONLY-"].update(visible=True)
                window["-SHOW COMBOBOX-"].update(
                    values=combobox_value, visible=True)
            else:
                # Reset table_value to the original data values
                table_value = data
                window["-SHOW ONLY-"].update(visible=False)
                window["-SHOW COMBOBOX-"].update(
                    values=[], visible=False)
                window["-DATA TABLE-"].update(values=table_value)
            window.refresh()
        
        elif event == "-SHOW COMBOBOX-":
            print('Executing')
            show_value = values["-SHOW COMBOBOX-"]
            delimiter = values["-FILTER-"]

            table_dict = search_data.update_data(delimiter, show_value)
            table_value = util.convert_dict_to_list(table_dict, with_keys=False)
            
            window["-DATA TABLE-"].update(values=table_value)
            print(len(table_value))

        elif event == "Search":
            search_input = values["-SEARCH-"]
            search_combobox = values["-SEARCH FILTER-"]
            table_dict = table_dict

            search_dict = util.search_dict(table_dict, search_input, search_combobox)
            search_result = util.convert_dict_to_list(search_dict, with_keys=False)

            window["-DATA TABLE-"].update(values=search_result)
            window["-SEARCH RESULT TEXT-"].update(f'{len(search_result)} results', visible=True)

        elif event == "Reset":
            window["-SEARCH-"].update('')
            window["-DATA TABLE-"].update(values=table_value)
            window["-SEARCH RESULT TEXT-"].update('', visible=False)
            print('RESETING TABLE VALUES')

    # If window close, open main window
    window.close()