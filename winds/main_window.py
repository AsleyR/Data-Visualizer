from ftplib import error_perm
import PySimpleGUI as sg
import csv
import os.path
import util
import winds.layouts
from pydub import AudioSegment
from pydub.playback import play


def main_window():
    main_layout = winds.layouts.mainWindowLayout()
    main_layout = main_layout.create_layout()
    font = ("Arial", 12)

    csv_data = []
    csv_data_dict = {}
    csv_headings = []

    window = sg.Window("Data Tool", main_layout, font=font)

    # Event loop
    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WINDOW_CLOSED:
            event_list = ['EXIT']
            window.close()
            return event_list

        # Show files in selected folder
        elif event == "-FOLDER-":
            folder = values['-FOLDER-']
            try:
                file_list = os.listdir(folder)
        
            except:
                file_list = []

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
                    'Archivo seleccionado con éxito',
                    text_color="green"
                    )
                window["-OPEN FILE-"].update(visible=True)
                event_list = ["-FILE LIST-", csv_data, csv_headings, csv_data_dict]
                # return event_list
                pass

            # Error selecting file. Horrible except usage tho lmao
            except:
                window["-FILE STATUS-"].update(
                    'Error selecionando archivo',
                    text_color="red"
                    )
                error_sound = AudioSegment.from_wav("media/audio/computer-error.wav")
                play(error_sound)
                pass
            
        elif event == "-OPEN FILE-":
            event_list = ["Open Window", csv_data, csv_headings, csv_data_dict]
            window.close()
            return event_list


    window.close()