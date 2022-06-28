import PySimpleGUI as sg
import util
import winds.layouts
from pydub import AudioSegment
from pydub.playback import play

def file_window(data, headings, dictionary):
    file_w_layout = winds.layouts.fileWindowLayout()
    file_w_layout = file_w_layout.create_layout(data, headings, dictionary)

    search_data = util.searchFunctions(dictionary)
    table_dict = dictionary

    font = ("Arial", 12)
    table_value = data
    ERROR_SOUND = "media/audio/computer-error.wav"

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
                    # Reset table_value to the original data values
                    table_value = data
                    window["-SHOW ONLY-"].update(visible=False)
                    window["-SHOW COMBOBOX-"].update(
                        values=[], visible=False)
                    window["-DATA TABLE-"].update(values=table_value)
                    print('RESETING TABLE VALUES')
                window.refresh()
            except:
                window["-ERROR MESSAGE-"].update("ERROR WITH FILTER COMBOBOX - CLICK 'RESTART' BUTTON!")
                window["-FILTER RESET-"].update(visible=True)
                error_sound = AudioSegment.from_wav(ERROR_SOUND)
                play(error_sound)
                print('ERROR WITH FILTER COMBOBOX')
                pass
        
        elif event == "-SHOW COMBOBOX-":
            try:
                show_value = values["-SHOW COMBOBOX-"]
                delimiter = values["-FILTER COMBOBOX-"]

                table_dict = search_data.update_data(delimiter, show_value)
                table_value = util.convert_dict_to_list(table_dict, with_keys=False)
                
                window["-DATA TABLE-"].update(values=table_value)
                print('FILTERING')
            except:
                window["-ERROR MESSAGE-"].update("ERROR FILTERING DATA - CLICK 'RESET' BUTTON!")
                window["-FILTER RESET-"].update(visible=True)
                error_sound = AudioSegment.from_wav(ERROR_SOUND)
                play(error_sound)
                print('ERROR FILTERING DATA')
                pass
        
        elif event == "-FILTER RESET-":
            try:
                window['-FILTER RESET-'].update(visible=False)
                window['-ERROR MESSAGE-'].update('')
                pass
            except:
                window["-ERROR MESSAGE-"].update("ERROR RESETING DATA - RESTART PROGRAM!")
                error_sound = AudioSegment.from_wav(ERROR_SOUND)
                play(error_sound)
                print('ERROR SEARCHING DATA')
                pass

        # * SEARCH SECTION *
        elif event == "Search":
            try:
                search_input = values["-SEARCH-"]
                search_combobox = values["-SEARCH FILTER-"]
                table_dict = table_dict

                search_dict = util.search_dict(table_dict, search_input, search_combobox)
                search_result = util.convert_dict_to_list(search_dict, with_keys=False)

                window["-DATA TABLE-"].update(values=search_result)
                window["-SEARCH RESULT TEXT-"].update(f'{len(search_result)} results', visible=True)
                print('SEARCHING')
            except:
                window["-ERROR MESSAGE-"].update("ERROR SEARCHING DATA - CLICK 'RESET' BUTTON!")
                error_sound = AudioSegment.from_wav(ERROR_SOUND)
                play(error_sound)
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
                error_sound = AudioSegment.from_wav(ERROR_SOUND)
                play(error_sound)
                print('ERROR RESETING DATA')
                pass

    # If window close, open main window
    window.close()