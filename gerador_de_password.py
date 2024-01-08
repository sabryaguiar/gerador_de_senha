import random
import PySimpleGUI as sg
import string as st
import os

class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        self.tipos_caracteres = ['Letras Maiúsculas', 'Letras Minúsculas', 'Números', 'Caracteres Especiais']
        layout = [
            [sg.Text('Site/Software', size=(12, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(12, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'),
             sg.Combo(values=list(range(30)), key='total_chars', default_value=12, size=(3, 1))],
            [sg.Text('Tipos de caracteres:')],
            [sg.Checkbox(tipo, key=f'tipo_{tipo}', default=True) for tipo in self.tipos_caracteres],
            [sg.Output(size=(32, 5), key='output')],
            [sg.Button('Gerar Senha')],
        ]

        # Declarar janela
        self.janela = sg.Window('Password Generator', layout)

    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        tipos_selecionados = [tipo for tipo in self.tipos_caracteres if valores[f'tipo_{tipo}']]
        algoritmos = ''
        if 'Letras Maiúsculas' in tipos_selecionados:
            algoritmos += st.ascii_uppercase
        if 'Letras Minúsculas' in tipos_selecionados:
            algoritmos += st.ascii_lowercase
        if 'Números' in tipos_selecionados:
            algoritmos += st.digits
        if 'Caracteres Especiais' in tipos_selecionados:
            algoritmos += st.punctuation

        chars = random.choices(algoritmos, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        site = valores['site']
        usuario = valores['usuario']

        # Atualizar a área de saída
        self.janela['output'].update(f"Site: {site}, Usuário: {usuario}, Senha: {new_pass}\n")
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a') as file:
            file.write(f"Site: {valores['site']}, Usuário: {valores['usuario']}, Senha: {nova_senha}\n")
        print('Senha salva para o arquivo "senhas.txt"')

gen = PassGen()
gen.iniciar()
