import PySimpleGUI as sg

#layout = [[sg.Radio('Tema Claro     ',group_id="RADIO1",i=1, default=True, size=(10,1)),sg.Radio('My second Radio!',group_id="RADIO1",i=2)],
#[sg.Button('Ok')]]

#window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
#event, values,i = window.read()
#if i==1: # if user closes window or clicks cancel
#    sg.theme('lightGreen3')# Add a touch of color
    # All the stuff inside your window.
 #   layouts = [[sg.Image(r"E:\git\pytom\WOPOB\resources\branco.png")],
 #              [sg.Text('Nome:        '), sg.InputText(key='nome',size=(50,1))],
   #            [sg.Text('Mensagem:'),sg.Multiline(size=(50, 3),key='men')],
  #             [sg.Button('Ok'),
 #              sg.Button('Cancel')] ]

# Create the Window
#    window2 = sg.Window('Window Title', layouts)
# Event Loop to process "events" and get the "values" of the inputs
 #   while True:
  #      event, values = window2.read()
   #     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    #        break
     #   print('Nome: ', values['nome'])
      #  print('Mensagem: ',values['men'])
    #window2.close()
#else:
sg.theme('DarkGreen4')   # Add a touch of color
# All the stuff inside your window.
layouts = [[sg.Image(r"E:\git\pytom\WOPOB\resources\preto.png")],
           [sg.Text('Nome:        '), sg.InputText(key='nome',size=(50,1))],
           [sg.Text('Mensagem:'),sg.Multiline(size=(50, 3),key='men')],
           [sg.Button('Enviar'),
           sg.Button('Sair')] ]

# Create the Window
window2 = sg.Window('WHABT', layouts)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window2.read()
    if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
        break
    print('Nome: ', values['nome'])
    print('Mensagem: ',values['men'])
window2.close()