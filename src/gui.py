# Importación de librerías
import PySimpleGUI as sg
from src.ConfigAWS import *
from src.s3Create import S3_CreateBucket, S3_ListBuckets, S3_Upload
import os
import sys

def LoginFix():
    layout = [[sg.T('Credenciales inválidas')],
            [sg.Text('')],
            [sg.ReadFormButton('Reintentar')]]

    window = sg.Window('Validación', layout, no_titlebar = True) 

    while True:
        button, values = window.read()
        if button is None or button == 'Exit':
                break
        elif button == 'Reintentar':
                os.execv(sys.executable, ['python'] + sys.argv)

def collapse(layout, key, visible):
    return sg.pin(sg.Column(layout, key=key, visible=visible, pad=(0,0)))

def LoginGui():

    layout1 = [[sg.Text('Introduce tus credenciales de AWS'), sg.Text(size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('Access Key:')],
            [sg.Input(key='-INaccess1-')],
            [sg.Text('')],  
            [sg.Text('Secret Key:')],      
            [sg.Input(key='-INkey1-', password_char='*')],
            [sg.Text('')], 
            [sg.Checkbox('¿Introducir Token? (opcional)', enable_events=True, key='-OPEN Token1-Checkbox-')],
            [collapse([[sg.Multiline(size=(40, 5), key='-INtoken1-')]], '-Token1-', False)],
            [sg.Text('')],       
            [sg.Button('Aceptar',key="-ACEPTAR1-"), sg.Button('Validación',key="-VALID1-")]]   

    layout2 = [[sg.Text('Introduce tus credenciales de AWS'), sg.Text(size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('Access Key:')],
            [sg.Input(key='-INaccess2-')],
            [sg.Text('')],  
            [sg.Text('Secret Key:')],      
            [sg.Input(key='-INkey2-', password_char='*')],
            [sg.Text('')],
            [sg.Checkbox('¿Introducir Token? (opcional)', enable_events=True, key='-OPEN Token2-Checkbox-')],
            [collapse([[sg.Multiline(size=(40, 5), key='-INtoken2-')]], '-Token2-', False)],
            [sg.Text('')],      
            [sg.Button('Aceptar',key="-ACEPTAR2-"), sg.Button('Validación',key="-VALID2-")],
            [sg.HorizontalSeparator()],
            [sg.Text('Credenciales incompletas',visible=True,key='-OUTPUT-', font=('Helvetica', 10), text_color="black")],
            [sg.Button('Continuar',key="-CONT2-")]]

   
    layout = [[sg.Column(layout1, key='-COL1-'), 
            sg.Column(layout2, visible=False, key='-COL2-')]]

    window = sg.Window('Login Window', layout)      

    layout=1
    opened=False
    while True:
        event, values = window.read()
        if event.startswith(f'-OPEN Token{layout}-'):
            opened = not opened
            window[f'-OPEN Token{layout}-Checkbox-'].update(opened)
            window[f'-Token{layout}-'].update(visible=opened) 
        if event == f"-ACEPTAR{layout}-":
            CheckDirectories()
            if values[f'-INkey{layout}-'] != "" and values[f'-INaccess{layout}-']:
                CreateCredentials(values[f'-INaccess{layout}-'],values[f'-INkey{layout}-'], values[f"-INtoken{layout}-"])
                window.close()
                return True
            else:
                print("Credenciales incompletas")
                window[f'-COL{layout}-'].update(visible=False)
                layout = layout + 1 if layout < 2 else 1
                window[f'-COL{layout}-'].update(visible=True)

        if event == f"-VALID{layout}-":
            CheckDirectories()
            try:
                with open(f'/home/{gp.getuser()}/.aws/credentials', 'r') as file:
                    originalCredentials = file.read()
            except FileNotFoundError:
                sg.Popup("Credenciales vacías", no_titlebar = True)

            CreateCredentials(values[f'-INaccess{layout}-'],values[f'-INkey{layout}-'], values[f"-INtoken{layout}-"])
            checkCredentials = ValidCredentials()
            if checkCredentials == "Invalid":
                LoginFix()
                f = open(f"/home/{gp.getuser()}/.aws/credentials", "w")
                f.write(originalCredentials)
                f.close()
            elif checkCredentials == "Valid":
                sg.Popup("Credenciales válidas", no_titlebar = True)
            else:
                sg.Popup("Pánico en el edén")
        if event =="-CONT2-":
            window.close()
            return True

        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            return False    


def MainGui():
    image_S3 = "input/Circle_S3.png"
    image_EC2 = "input/Circle_EC2.png"
    
    layout1= [[sg.Text('Elige servicio:',size=(17,1), font=("Helvetica", 15))],

            [sg.Button(key="S3-1", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_S3, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text('' * 2),
            sg.Button(key="EC2-1", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_EC2, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text(' ' * 2)],
            [sg.Text(' ' * 4),sg.Text('S3'), sg.Text(' ' * 14), sg.Text('EC2')]]

    layout2 = [[sg.Text('Elige servicio:',size=(17,1), font=("Helvetica", 12))],

            [sg.Button(key="S3-2", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_S3, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text('' * 2),
            sg.Button(key="EC2-2", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_EC2, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text(' ' * 2)],
            [sg.Text(' ' * 4),sg.Text('S3'), sg.Text(' ' * 14), sg.Text('EC2')],
            [sg.HorizontalSeparator()],
            [sg.Text('Configurador S3:',size=(15,1), font=("Helvetica", 10))],
            [sg.Text('Nombre:',font=("Helvetica", 8)), sg.Input(key='-S3Access-')],
            [sg.Text('Region:',font=("Helvetica", 8)), sg.Combo(['us-east-1', 'us-east-2'], enable_events=True, key='-S3Region-')],
            [sg.Button('Crear Bucket',key="BUCK")],
            [sg.Text('')],
            [sg.HorizontalSeparator()],
            [sg.Text('Seleccionar Bucket:',size=(18,1), font=("Helvetica", 10)), sg.Text("Elige objeto:")],
            [sg.Listbox(values=[element for element in S3_ListBuckets()], size=(17, 6), key='-LIST-', enable_events=True),  sg.Input(key="-FILE-" ,change_submits=True), sg.FileBrowse("Objeto", key="-FILEBROWSER-", disabled=True)],
            [sg.Button('Refrescar lista',key="-UPDATE_LIST-"), sg.Text(' ' * 20), sg.Button('Subir objeto al bucket seleccionado',key="-UPLOAD-")]
            ]

    layout3 = [[sg.Text('Elige servicio:',size=(17,1), font=("Helvetica", 12))],

            [sg.Button(key="S3-3", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_S3, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text('' * 2),
            sg.Button(key="EC2-3", button_color=(sg.theme_background_color(),sg.theme_background_color()),
                image_filename=image_EC2, image_size=(80, 80), image_subsample=2, border_width=0),
                    sg.Text(' ' * 2)],
            [sg.Text(' ' * 4),sg.Text('S3'), sg.Text(' ' * 14), sg.Text('EC2')],
            [sg.HorizontalSeparator()],
            [sg.Text('Configurador EC2:',size=(15,1), font=("Helvetica", 10))]
            ]
            

    layout = [[sg.Column(layout1, key='-COL1-'),
            sg.Column(layout2, visible=False, key='-COL2-'),
            sg.Column(layout3, visible=False, key='-COL3-')]]

    window = sg.Window('AWS choice', layout)      

    layout=1
    while True:
        event, values = window.read() 
        if event == "S3-0" or event == "S3-1" or event == "S3-2":
            print("OK")
            window[f'-COL{layout}-'].update(visible=False)
            layout = 2
            window[f'-COL{layout}-'].update(visible=True)
        elif event == "BUCK":
            bucketCreate = S3_CreateBucket(values['-S3Access-'],region=values['-S3Region-'])
            if bucketCreate:
                sg.Popup("¡Bucket creado con éxito")
        elif event == "-LIST-":
            window.Element('-FILEBROWSER-').Update(disabled=False)
        elif event == "-UPDATE_LIST-":
            print("OK")
            window.Element('-LIST-').Update(values=S3_ListBuckets())
            print(S3_ListBuckets)
        elif event =="-UPLOAD-":
            filename = sg.popup_get_text('Nombre para subida')
            S3_Upload(values["-FILEBROWSER-"], values["-LIST-"],object_name=filename)
            sg.Popup("¡Objeto subido con éxito!")
        elif event == sg.WIN_CLOSED or event == 'Exit':
            break 
        elif event == "EC2-0" or event == "EC2-1" or event == "EC2-2":
            print("OK")
            window[f'-COL{layout}-'].update(visible=False)
            layout = 3
            window[f'-COL{layout}-'].update(visible=True)
            

    window.close()