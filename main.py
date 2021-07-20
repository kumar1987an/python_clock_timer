import PySimpleGUI as sg

sg.theme("BluePurple")

font1 = ("Arial, 60")
font2 = ("Hack, 60")
font3 = ("Hack, 10")
layout = [[sg.Text('Welcome to Python Timer', font=font3, text_color="black", justification='center')],

          [sg.InputText(size=(2, 2), font=font1, key="-HOURS-", pad=(32, 32)), sg.Text(":", font=font2, text_color="black"),
          sg.InputText(size=(2, 2), font=font1, key="-MINUTES-", pad=(32, 32)), sg.Text(":", font=font2, text_color="black"),
          sg.InputText(size=(2, 2), font=font1, key="-SECONDS-", pad=(32, 32))],

          [sg.Text("", key='-OUTPUT-')],
        
          [sg.Button("Start", size=(5, 4), border_width=3, pad=(32, 20)), 
          sg.Button("Stop", size=(5, 4), border_width=3, pad=(32, 20)), 
          sg.Button("Reset", size=(5, 4), border_width=3, pad=(35, 20)), 
          sg.Button("Exit", size=(5, 4), border_width=3, pad=(32, 20))]
]

window = sg.Window('Python Timer', layout)

while True:
    event, values = window.read()
    if event == "Start":
        hours = values['-HOURS-']
        minutes = values['-MINUTES-']
        seconds = values['-SECONDS-']
        # window['-OUTPUT-'].update(f"{hours}:{minutes}:{seconds}")
        print(int(hours)+1, int(minutes)+60, int(seconds)+60)

    if event == sg.WIN_CLOSED or event == "Exit":
        window.close()
