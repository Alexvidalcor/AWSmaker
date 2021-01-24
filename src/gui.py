# Importación de librerías
import PySimpleGUI as sg
from src.ConfigAWS import *
from src.s3Create import S3_CreateBucket


def LoginGui():
    layout1 = [[sg.Text('Introduce tus credenciales de AWS'), sg.Text(size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('Access Key:')],
            [sg.Input(key='-INaccess1-')],
            [sg.Text('')],  
            [sg.Text('Secret Key:')],      
            [sg.Input(key='-INsecret1-', password_char='*')],
            [sg.Text('')],      
            [sg.Button('Aceptar',key="ACEPTAR"), sg.Exit()]]   

    layout2 = [[sg.Text('Introduce tus credenciales de AWS'), sg.Text(size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('Access Key:')],
            [sg.Input(key='-INaccess2-')],
            [sg.Text('')],  
            [sg.Text('Secret Key:')],      
            [sg.Input(key='-INsecret2-', password_char='*')],
            [sg.Text('')],      
            [sg.Button('Aceptar',key="ACEPTAR")],
            [sg.HorizontalSeparator()],
            [sg.Text('Credenciales vacías',visible=True,key='-OUTPUT-', font=('Helvetica', 10), text_color="black")],
            [sg.Button('Continuar',key="CONT"), sg.Exit()]]
   
    layout = [[sg.Column(layout1, key='-COL1-'), 
            sg.Column(layout2, visible=False, key='-COL2-')]]

    window = sg.Window('Login Window', layout)      

    layout=1
    while True:
        event, values = window.read() 
        if event == "ACEPTAR":
            CheckDirectories()
            if values['-INsecret1-'] != "" and values['-INaccess1-'] != "":
                CreateCredentials(values['-INsecret1-'],values['-INaccess1-'])
                window.close()
                return True
            else:
                print("Credenciales vacías")
                window[f'-COL{layout}-'].update(visible=False)
                layout = layout + 1 if layout < 2 else 1
                window[f'-COL{layout}-'].update(visible=True)
        if event == "CONT":
            window.close()
            return True

        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            return False    


def MainGui():

    image_S3 = "input/Circle_S3.png"
    image_EC2 = "input/Circle_EC2.png"

    layout1= [[sg.Text('Elige servicio:',size=(17,1), font=("Helvetica", 15))],

            [sg.Button(key="S3", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_S3, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text('' * 2),

            sg.Button(key="EC2", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_EC2, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text(' ' * 2)],
            
            [sg.Text(' ' * 4),sg.Text('S3'), sg.Text(' ' * 14), sg.Text('EC2')]]

    layout2 = [[sg.Text('Elige servicio:',size=(17,1), font=("Helvetica", 12))],

            [sg.Button(key="S3", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_S3, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text('' * 2),

            sg.Button(key="EC2", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_EC2, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text(' ' * 2)],
            
            [sg.Text(' ' * 4),sg.Text('S3'), sg.Text(' ' * 14), sg.Text('EC2')],
            
            [sg.HorizontalSeparator()],

            [sg.Text('Configurador S3:',size=(15,1), font=("Helvetica", 10))],
            [sg.Text('Nombre:',font=("Helvetica", 8)), sg.Input(key='-S3Access-')],
            [sg.Text('Region:',font=("Helvetica", 8)), sg.Combo(['us-east-1', 'us-east-2'], enable_events=True, key='-S3Region-')],
            [sg.Button('Crear Bucket',key="BUCK")]
            ]      


    layout = [[sg.Column(layout1, key='-COL1-'),
            sg.Column(layout2, visible=False, key='-COL2-')]]

    window = sg.Window('AWS choice', layout)      

    layout=1
    while True:
        event, values = window.read() 
        if event == "S3":
            window[f'-COL{layout}-'].update(visible=False)
            layout = layout + 1 if layout < 2 else 1
            window[f'-COL{layout}-'].update(visible=True)
        if event == "BUCK":
            bucketCreate = S3_CreateBucket(values['-S3Access-'],region=values['-S3Region-'])
            if bucketCreate:
                sg.Popup("¡Bucket creado con éxito")
            
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      

    window.close()