import PySimpleGUI as sg

class wppbot:
    def _init_(self):
        layout = [
            [sg.Text('Contato ou Grupos',size=(10,0)),sg.Input(size=(50,0),key='nome')],
            [sg.Text('Mensagem',size=(10,0)),sg.Input(size=(50,0),key='mensagem')],
            [sg.Button('Enviar')]
        ]
        janela = sg.Window("WHABT").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        mensagem = self.values['mensagem']
        print(f'nome: {nome}')
        print(f'mensagem: {mensagem}')

tela = wppbot()
tela.Iniciar()