from selenium import  webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
c=input("digite o nome: ")
contatos = [c]
s=input("digite a mensagem: ")
mensagem  = [s]
#time.sleep(10)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')#site
time.sleep(30)# time
b='True'
while b=='True':
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
        b=input("digite True se  quer continuar ou False para parar: ")
        if b=='True':
                c=input("digite o nome: ")
                contatos = [c]
                s=input("digite a mensagem: ")
                mensagem  = [s]
        else:
                break