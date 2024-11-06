import PySimpleGUI as sg
from datetime import datetime, timedelta #Pegar as datas
import sqlite3



#Alimentando aplicação com dados do SQL
from Banco_de_dados import alimentando_aplicação
dados = alimentando_aplicação()

reservas = []
for i in range(len(dados)):
    nova_reserva = []
    for contador in range(4):
        nova_reserva.append(dados[i][contador])
    reservas.append(nova_reserva)


sg.theme('SystemDefault')


# Captura a data atual
data_atual = datetime.now().date()

# Define o limite de 7 dias após a data atual
limite_data = data_atual + timedelta(days=7)

id = 1

#Armazena os dados de todas as reservas


pasta = r'C:\Users\vfari\Documents\GitHub\CRUD-Python\CRUD\assets\Foto.png'

    

#----------------------------------------------------------------------------------------------------------------------------------------           

# Função responsável por validar o registro
def validar_registro(pessoas,nome, data):

    if nome.isdigit() == True or nome == "" or len(nome) < 3:
        erro = "Por favor, verifique o campo do nome!"
        return erro

    elif data == "":
        erro = "O campo da data está vazio!"
        return erro

    elif data > limite_data or data < data_atual:
        erro = "Selecione uma data válida para a reserva"
        return erro
    else: 
        return True
    

# TELA DE LEITURA DOS DADOS ------------------------------------------------------
def exibir_dados():

    #Alimentando aplicação com dados do SQL
    from Banco_de_dados import alimentando_aplicação
    dados = alimentando_aplicação()

    # Layout da minha tela
    layout_popup = [
            [sg.Push(), sg.Text(f"Reservas ativas - {len(dados)}"), sg.Push()],
            [sg.Text("")],

            [sg.Table(values = dados, key = "Tabela",
                      headings=["ID", "Pessoas", "Nome do cliente", "Data"], size=(100,1), 
                      col_widths=[5, 8, 30, 10], auto_size_columns=False, num_rows=10, expand_x=True, justification='center')],

            #Botões inferiores
            [sg.Text("")],
            [sg.Push(), sg.Button('Update'), sg.Button('Delete'), sg.Push()] 
            ]

    janela_popup = sg.Window("Leitura dos dados", layout_popup, modal=True)

    # Execução em loop para a tela funcionar de forma constante
    while True:

        # Captura de eventos e valores na tela
        event, values = janela_popup.read()

        if event in (sg.WIN_CLOSED, "Fechar"):
            break

        
        if event == "Update":
            campo_da_tabela = values["Tabela"]
            if campo_da_tabela == []:
                sg.popup("Selecione um campo para atualizar")
            else:
                campo_da_tabela = campo_da_tabela[0]
                janela_popup.close()
                atualizar_dados(campo_da_tabela)

        # Capturando o clique na linha da tabela
        if event == "Delete":
            campo_da_tabela = values["Tabela"]
            if campo_da_tabela == []:
                sg.popup("Selecione um campo para atualizar")
            else:
                campo_da_tabela = campo_da_tabela[0]
                
                reservas.pop(campo_da_tabela)
                sg.popup("Dado excluído com sucesso!") 
                janela_popup.close()   
                 
                
    # Fecha o popup após o usuário clicar em "Fechar"
    janela_popup.close()



# TELA DE ATUALIZAÇÃO DOS DADOS ------------------------------------------------------
def atualizar_dados(campo_da_tabela):

    
       
    layout_update = [
            [sg.Push(), sg.Text("Reservas ativas"), sg.Push()],
            [sg.Text("")],

            [sg.Text("Pessoas"), sg.VerticalSeparator(), sg.Text("Nome do solicitante", size=(16, 1)),sg.VerticalSeparator(),  sg.Text("Data da reserva")],
            [sg.Spin([i for i in range(1, 11)], initial_value=reservas[campo_da_tabela][1], size=(6, 1), key="pessoas"), sg.Input(reservas[campo_da_tabela][2],size=(20, 1), key="nome"), sg.Input(reservas[campo_da_tabela][3],key='data', size=(10, 1)), sg.CalendarButton('Escolher Data', target='data', format='%d/%m/%Y')],

            #Botões inferiores
            [sg.Text("")],
            [sg.Push(), sg.Button('Update'), sg.Push()] 
            ]


    janela_popup = sg.Window("Popup de Detalhes", layout_update, modal=True)

    # Lê eventos da janela popup até que o usuário feche
    while True:
        event, values = janela_popup.read()

        if event in (sg.WIN_CLOSED, "Fechar"):
            break
        if event == "Update":
           

            #coletando dados do registro
            pessoas = values['pessoas']
            nome = values['nome']

            #Validando antes de guardar a data. A data vazia pré-formatada com datetime, quebra o programa
            if values["data"] == "":
                data = values['data']
            else:
                data = datetime.strptime(values['data'], '%d/%m/%Y').date()

            #Chamadno uma função para validar os dados antes de persistí-los.
            registro = validar_registro(pessoas,nome, data)

            #Se tudo estiver correto, ele armazena e atualiza a tabela na tela
            if registro == True:
                data = data.strftime('%d/%m/%Y')


                # AQUI VOU ATUALIZAR O BANCO DE DADOS


                sg.popup("Atualização feita com sucesso")
                janela_popup.close()
            else:
                sg.popup(registro)






 
#Layout da tela principal ----------------------------------------------------------------------------------------------------------------------------
layout = [  

            #Parte superior da tela
            [sg.Push(), sg.Text("Sistema de reservas - Restaurante"), sg.Push()],
            [sg.Image(filename=pasta, size=(400,200), subsample=2)],
            [sg.HorizontalSeparator()],
            [sg.Text("")],
            

            #Conteúdo
            [sg.Push(), sg.Text("Faça uma reserva aqui"), sg.Push()],
            [sg.Text("")],
            [sg.Text("Pessoas"), sg.VerticalSeparator(), sg.Text("Nome do solicitante", size=(16, 1)),sg.VerticalSeparator(),  sg.Text("Data da reserva")],
            [sg.Spin([i for i in range(1, 11)], initial_value=1, size=(6, 1), key="pessoas"), sg.Input(size=(20, 1), key="nome"), sg.Input(key='data', size=(10, 1)), sg.CalendarButton('Escolher Data', target='data', format='%d/%m/%Y')],
            [sg.Text("")],
            [sg.Push(), sg.Text("* Reservas com até 7 dias de antecedência! "), sg.Push()],
            [sg.Text("")],
            [sg.Push(),sg.Button('Create'), sg.Button('Read'), sg.Push()]]
            
           
    
window = sg.Window('Sistema CRUD', layout)

while True:
    event, values = window.read()

    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == "Create":
        #coletando dados do registro
        pessoas = values['pessoas']
        nome = values['nome']
        
        #Validando antes de guardar a data
        if values["data"] == "":
            data = values['data']
        else:
            data = datetime.strptime(values['data'], '%d/%m/%Y').date()
        
        
        
        
        #Chamando uma função para validar os dados antes de persistí-los.
        registro = validar_registro(pessoas,nome, data)
        #Se tudo estiver correto, ele armazena e atualiza a tabela na tela
        if registro == True:

            data = data.strftime('%d/%m/%Y')

            # Preenchendo banco de dados com os valores
            from Banco_de_dados import inserção_de_dados
            inserção_de_dados(pessoas, nome, data)
            sg.popup("Reserva feita com sucesso!")
            
            # Atualizando a tela para o usuário
            window['nome'].update("")
            window['data'].update("")
        else:
            sg.popup(registro)


    #Selecionando o input
    if event == "Read":
        exibir_dados()

window.close()

