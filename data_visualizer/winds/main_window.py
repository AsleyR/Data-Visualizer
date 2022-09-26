import PySimpleGUI as sg
import os.path
import util
import winds.layouts
from pydub import AudioSegment
from pydub.playback import play


def main_window():
    main_layout = winds.layouts.mainWindowLayout()
    main_layout = main_layout.create_layout()
    font = ("Arial", 12)

    ERROR_SOUND = "./media/audio/computer-error.wav"

    csv_data = []
    csv_data_dict = {}
    csv_headings = []

    window = sg.Window("Data Visualizer", main_layout, font=font)

    # Event loop
    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WINDOW_CLOSED:
            event_list = ['EXIT']
            print('EXITING MAIN WINDOW')
            window.close()
            return event_list

        # Show files in selected folder
        elif event == "-FOLDER-":
            folder = values['-FOLDER-']
            try:
                file_list = os.listdir(folder)
                print('FOLDER FOUND SUCCESFULLY')
        
            except:
                file_list = []
                window["-FILE STATUS-"].update(
                    'ERROR FINDING FOLDER',
                    text_color="red"
                    )
                try:
                    error_sound = AudioSegment.from_wav(ERROR_SOUND)
                    play(error_sound)
                except:
                    pass
                print('ERROR FINDING FOLDER')

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".csv")) # Show files with only this extension
            ]
            window["-FILE LIST-"].update(fnames)
        
        # Select file from FILE LIST
        elif event == "-FILE LIST-":
            try:
                filename = os.path.join(
                    values["-FOLDER-"],
                    values["-FILE LIST-"][0]
                )

                # Convert data from CSV file to a dict list
                csv_file = filename
                data_class= util.csvData(csv_file)
                data_dict = data_class.create_data_dict()

                csv_data = util.get_dict_values(data_dict)
                csv_headings = util.get_dict_keys(data_dict)
                csv_data_dict = data_dict

                window["-FILE STATUS-"].update(
                    'File succesfully selected',
                    text_color="green"
                    )
                window["-OPEN FILE-"].update(visible=True)
                event_list = ["-FILE LIST-", csv_data, csv_headings, csv_data_dict]
                # return event_list
                print('FILE SUCCESFULLY SELECTED')
                pass

            # Error selecting file. Horrible except usage tho lmao
            except:
                window["-FILE STATUS-"].update(
                    'ERROR SELECTING FILE',
                    text_color="red"
                    )
                try:
                    error_sound = AudioSegment.from_wav(ERROR_SOUND)
                    play(error_sound)
                except:
                    pass
                print('ERROR SELECTING FILE')
                pass
            
        elif event == "-OPEN FILE-":
            try:
                event_list = ["Open Window", csv_data, csv_headings, csv_data_dict]
                print('CLOSING MAIN WINDOW - OPENING FILE WINDOW')
                window.close()
                return event_list
            except:
                window["-FILE STATUS-"].update(
                    'ERROR OPENING FILE',
                    text_color="red"
                    )
                try:
                    error_sound = AudioSegment.from_wav(ERROR_SOUND)
                    play(error_sound)
                except:
                    pass
                print('ERROR OPENING FILE')
                pass


    window.close()