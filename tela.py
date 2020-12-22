import PySimpleGUI as sg

layout =  [
    [sg.Radio('Tema Claro', "RADIO1", default=True,key='1'),
    sg.Radio('Tema Escuro', "RADIO1",key='2')],
    [sg.Button('Ok')]]

window = sg.Window('Escolha', layout)
# Event Loop to process "events" and get the "values" of the inputs
event, values = window.read()
# if user closes window or clicks cancel
sg.theme('lightGreen3') if values['1']==True else sg.theme('DarkGreen4')
    # All the stuff inside your window.
layouts = [[sg.Image(r"E:\git\pytom\WOPOB\resources\branco.png") if values['1']==True else sg.Image(r"E:\git\pytom\WOPOB\resources\preto.png")],
           [sg.Text('Nome:        '), sg.InputText(key='nome',size=(50,1))],
           [sg.Text('Mensagem:'),sg.Multiline(size=(50, 3),key='men')],
           [sg.Button('Ok'),
           sg.Button('Cancel')]]

# Create the Window
window2 = sg.Window('WHABT', layouts)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window2.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Nome: ', values['nome'])
    print('Mensagem: ',values['men'])
window.close()
window2.close()