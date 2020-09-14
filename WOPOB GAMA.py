from selenium import  webdriver
import time
import PySimpleGUI as sg
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
import PySimpleGUI as sg

class wppbot:
    #interface
    def __init__(self):
        layout = [
            [sg.Text('Contato ou Grupos',size=(10,0)),sg.Input(size=(50,0),key='nome')],
            [sg.Text('Mensagem',size=(10,0)),sg.Input(size=(50,0),key='mensagem')],
            [sg.Button('Enviar')]
        ]
        janela = sg.Window("WOPOB").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']# digite o nome
        texto  = self.values['mensagem']# digite a mensagem
        driver.get('https://web.whatsapp.com/')#site
        time.sleep(30)# time
        #passando dados
        contatos = nome 
        mensagem = texto
        #execultando interface
tela = wppbot()
tela.Iniciar()
def buscar_contato(contato):# buscando nome
    compo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    compo_pesquisa.click()
    compo_pesquisa.send_keys(contato)
    compo_pesquisa.send_keys(Keys.ENTER)
def enviar_mensagem(mensagem):# buscando mensagem
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
for contato in contatos:#fazer o envio
    buscar_contato(contato)
    enviar_mensagem(mensagem)
