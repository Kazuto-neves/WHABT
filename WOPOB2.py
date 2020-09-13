from selenium import  webdriver
import time
import PySimpleGUI as sg
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
class wppbot:
    def __init__(self):
        layout = [
            [sg.Text('Contato ou Grupos'),sg.Input()],
            [sg.Text('Mensagem'),sg.Input()],
            [sg.Button('Enviar')]
        ]
        janela = sg.Window("WOPOB").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        contatos = ['Fags faeterj']
        mensagem  = 'bolinha de golfe'

        def buscar_contato(contato):
            compo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
            time.sleep(3)
            compo_pesquisa.click()
            compo_pesquisa.send_keys(contato)
            compo_pesquisa.send_keys(Keys.ENTER)

        def enviar_mensagem(mensagem):
            campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
            campo_mensagem[1].click()
            time.sleep(3)
            campo_mensagem[1].send_keys(mensagem)
            campo_mensagem[1].send_keys(Keys.ENTER)

        for contato in contatos:
            buscar_contato(contato)
            enviar_mensagem(mensagem)