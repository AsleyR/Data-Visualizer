import PySimpleGUI as sg
# import util
# import winds.layouts
from .layouts import fw_layout as fwl
from data_visualizer.util import search_functions as sf, csv_data as cf, dict_functions as df
from data_visualizer.util.errorHandling import playErrorSound

def file_window(data, headings, dictionary):
    file_w_layout = fwl.fileWindowLayout()
    file_w_layout = file_w_layout.create_layout(data, headings, dictionary)

    search_data = sf.searchFunctions(dictionary)
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
            print('EXITING FILE WINDOW')
            window.close()
            return event_list

        # * FILTER BY SECTION *
        elif event == "-FILTER COMBOBOX-":
            filter_selection = values["-FILTER COMBOBOX-"]
            try:
                if filter_selection != "No Selection":
                    combobox_value = search_data.get_all_specific_items(filter_selection)
                    combobox_value.sort()
                    combobox_value.insert(0, 'No selection')

                    window["-SHOW ONLY-"].update(visible=True)
                    window["-SHOW COMBOBOX-"].update(
                        values=combobox_value, visible=True)
                else:
                    table_value = data # Reset table_value to the original data values
                    table_dict = dictionary
                    window["-SHOW ONLY-"].update(visible=False)
                    window["-SHOW COMBOBOX-"].update(
                        values=[], visible=False)
                    window["-DATA TABLE-"].update(values=table_value)
                    print('RESETING TABLE VALUES')
                window.refresh()
            except:
                window["-ERROR MESSAGE-"].update("ERROR WITH FILTER COMBOBOX - CLICK 'RESTART' BUTTON!")
                window["-FILTER RESET-"].update(visible=True)
                playErrorSound()
                print('ERROR WITH FILTER COMBOBOX')
                pass
        
        elif event == "-SHOW COMBOBOX-":
            try:
                show_value = values["-SHOW COMBOBOX-"]
                delimiter = values["-FILTER COMBOBOX-"]

                table_dict = search_data.update_data(delimiter, show_value)
                table_value = df.convert_dict_to_list(table_dict, with_keys=False)
                
                window["-DATA TABLE-"].update(values=table_value)
                print('FILTERING')
            except:
                window["-ERROR MESSAGE-"].update("ERROR FILTERING DATA - CLICK 'RESET' BUTTON!")
                window["-FILTER RESET-"].update(visible=True)
                playErrorSound()
                print('ERROR FILTERING DATA')
                pass
        
        elif event == "-FILTER RESET-":
            try:
                window['-FILTER RESET-'].update(visible=False)
                window['-ERROR MESSAGE-'].update('')
                pass
            except:
                window["-ERROR MESSAGE-"].update("ERROR RESETING DATA - RESTART PROGRAM!")
                playErrorSound()
                print('ERROR SEARCHING DATA')
                pass

        # * SEARCH SECTION *
        elif event == "Search":
            try:
                search_input = values["-SEARCH-"]
                search_combobox = values["-SEARCH FILTER-"]
                table_dict = table_dict

                search_dict = df.search_dict(table_dict, search_input, search_combobox)
                search_result = df.convert_dict_to_list(search_dict, with_keys=False)

                window["-DATA TABLE-"].update(values=search_result)
                window["-SEARCH RESULT TEXT-"].update(f'{len(search_result)} results', visible=True)
                print('SEARCHING')
            except:
                window["-ERROR MESSAGE-"].update("ERROR SEARCHING DATA - CLICK 'RESET' BUTTON!")
                playErrorSound()
                print('ERROR SEARCHING DATA')
                pass

        elif event == "-SEARCH RESET-":
            try:
                window["-ERROR MESSAGE-"].update('')
                window["-SEARCH-"].update('')
                window["-DATA TABLE-"].update(values=table_value)
                window["-SEARCH RESULT TEXT-"].update('', visible=False)
                print('RESETING TABLE VALUES')
            except:
                window["-ERROR MESSAGE-"].update('ERROR RESETING DATA - RESTART PROGRAM!')
                playErrorSound()
                print('ERROR RESETING DATA')
                pass

    # If window close, open main window
    window.close()