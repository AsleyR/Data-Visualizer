import winds


def init_program():
    # Create Windows
    main_window = winds.main_window
    file_window = winds.file_window


    # Program Controller
    # Event loop
    while True:
        
        # Initialize main window
        # event_main has to equal the window in order to get the return values
        event_main = main_window()

        if event_main[0] == "EXIT":
            print('EXISTING LOOP - CLOSING PROGRAM!')
            break

        # I HATE these nested functions, but it works >:(
        # obvs a temporal solution  
        elif event_main[0] == "Open Window":
            print('OPENING FILE WINDOW')
            # set data values
            csv_data = event_main[1]
            csv_headings = event_main[2]
            csv_data_dict = event_main[3]

            event_file = file_window(csv_data, csv_headings, csv_data_dict)

            if event_file[0] == "EXIT":
                print('EXITING LOOP - CLOSING FILE WINDOW')
                break
            pass

# Init script
if __name__ == "__main__":
    init_program();
