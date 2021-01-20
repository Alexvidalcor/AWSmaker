# Importación de librerías
import PySimpleGUI as sg
from src.ConfigAWS import *


def LoginGui():
    layout = [[sg.Text('Introduce tus credenciales de AWS'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.HorizontalSeparator()],
            [sg.Text('Secret Key:')],      
            [sg.Input(key='-INsecret-')],
            [sg.Text('')],      
            [sg.Text('Access Key:')],
            [sg.Input(key='-INaccess-')],
            [sg.Text('')],      
            [sg.Button('Aceptar',key="ACEPTAR"), sg.Exit()]]      
    window = sg.Window('Login Window', layout)      

    while True:
        event, values = window.read() 
        if event == "ACEPTAR":
            CheckDirectories()
            CreateCredentials(values['-INsecret-'],values['-INaccess-'])
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      

    window.close()


def ChooseGui():

    image_S3 = "input/Circle_S3.png"
    image_EC2 = "input/Circle_EC2.png"

    layout= [[sg.Text('Elige servicio:',size=(17,1), font=("Helvetica", 15))],

            [sg.Button(button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_S3, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text('' * 2),

            sg.Button(button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_EC2, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text(' ' * 2)],
            
            [sg.Text('S3')]]
                    

    window = sg.Window('AWS choice', layout)      

    while True:
        event, values = window.read() 
        if event == "ACEPTAR":
            CheckDirectories()
            CreateCredentials(values['-INsecret-'],values['-INaccess-'])
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      

    window.close()

            
