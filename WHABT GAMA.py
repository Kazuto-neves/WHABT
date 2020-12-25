from selenium import  webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg
#import datetime
def Escolha():
        b=0
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
        #Today = datetime.date.today()
        #People_layouts =  [[sg.T('This is inside tab 1')]]
        #Nature_layouts = [[sg.T('This is inside tab 2')]]
        #Objects_layouts = [[sg.T('This is inside tab 3')]]
        #Places_layouts = [[sg.T('This is inside tab 4')]]
        #Symbols_layouts = [[sg.T('This is inside tab 5')]]
        layouts = [[sg.Image(r"E:\git\pytom\WOPOB\resources\branco.png") if values['1']==True else sg.Image(r"E:\git\pytom\WOPOB\resources\preto.png")],
                #[sg.Text("Hoje:"),sg.Print('{}'.format('Today.now'))],
                [sg.Text('Nome:        '), sg.InputText(key='nome',size=(50,1))],
                [sg.Text('Mensagem:'),sg.Multiline(size=(50, 3),key='men')],
                #[sg.Checkbox('emoji',key='3')],
                #[sg.TabGroup([[sg.Tab('Tab 1',People_layouts), sg.Tab('Tab 2',Nature_layouts),sg.Tab('Tab 3',Objects_layouts), sg.Tab('Tab 4',Places_layouts),sg.Tab('Tab 5',Symbols_layouts)]])],
                [sg.Button('Ok'),
                sg.Button('Cancel')]]

                # Create the Window
        window2 = sg.Window('WHABT', layouts)
        def nomewpp():
                c=values['nome']
                return c
        def menwpp():
                m=values['men']
                return m
                # Event Loop to process "events" and get the "values" of the inputs
        while True:
                event, values = window2.read()
                if event == sg.WIN_CLOSED or event == 'Cancel':break
                c=values['nome']
                contatos = [c]
                s=values['men']
                mensagem  = [s]
                window.close()
                if b==0:
                        driver = webdriver.Chrome(ChromeDriverManager().install())
                        driver.get('https://web.whatsapp.com/')#site
                        b=1
                time.sleep(30)# time
                def buscar_contato(contato):# buscando nome
                        compo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
                        time.sleep(2)
                        compo_pesquisa.click()
                        compo_pesquisa.send_keys(contato)
                        compo_pesquisa.send_keys(Keys.ENTER)
                def enviar_mensagem(mensagem):# buscando mensagem
                        campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
                        campo_mensagem[1].click()
                        time.sleep(2)
                        campo_mensagem[1].send_keys(mensagem)
                        campo_mensagem[1].send_keys(Keys.ENTER)
                for contato in contatos:#fazer o envio
                        buscar_contato(contato)
                        enviar_mensagem(mensagem)
        window2.close()
Escolha()