#Percobaan
from openpyxl import load_workbook
import PySimpleGUI as sg
from datetime import datetime


sg.theme('TealMono')

layout = [[sg.Text('Nama Lengkap'),sg.Push(), sg.Input(key='Nama_Lengkap')],
          [sg.Text('Nomor HP'),sg.Push(), sg.Input(key='Nomor_HP')],
          [sg.Button('Submit'), sg.Button('Close')]]

window = sg.Window('Data Entry', layout, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    if event == 'Submit':
        try:
            wb = load_workbook('Tubes.xlsx')
            sheet = wb['Sheet1']
            NO = len(sheet['NO']) + 1
            time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            data = [NO, values['Nama_Lengkap'], values['Nomor_HP'], time_stamp]

            sheet.append(data)

            wb.save('Tubes.xlsx')

            window['Nama_Lengkap'].update(value='')
            window['Nomor_HP'].update(value='')
            window['Nama_Lengkap'].set_focus()

            sg.popup('Success', 'Data Saved')
        except PermissionError:
            sg.popup('File in use', 'File is being used by another User.\nPlease try again later.')
        


window.close()