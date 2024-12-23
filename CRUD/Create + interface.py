import flet as ft
from datetime import datetime, timedelta #Pegar as datas
import sqlite3

def trazendo_dados():
    from Banco_de_dados import alimentando_aplicação
    dados = alimentando_aplicação()
    print(dados)

    # Trazendo dados do SQL -----------------------------------------------------------
    lista = []
    for i in range(len(dados)):
        nova_reserva = []
        for contador in range(5):
            nova_reserva.append(dados[i][contador])
        lista.append(nova_reserva)

    for i in range (len(lista)):
        print(f"{i+1}° Usuário {lista[i]}")

    maior_id = 0
    for i in lista:
        if i[0] > maior_id:
            maior_id = i[0]
    
    return lista, maior_id

lista, maior_id = trazendo_dados()


def principal(page: ft.Page):   

    # Atributos da minha tela -----------------------------------------------------------
    page.title = "Tela principal"
    page.window.width = 350
    page.window.height = 750
    page.bgcolor = "#e8e8e8" 
    page.window.resizable = False
    page.window.maximizable = False
    page.window.always_on_top = True
    page.scroll = "adaptive"
  
    # Cabeçalho ----------------------------------------------------------------
    cabeçalho = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS_ROUNDED, 
                icon_color=ft.colors.BLACK
            ),
            ft.Text(
                "Menu de reservas",
                color=ft.colors.BLACK,
                size=20,
                weight="bold"
            ),
            ft.IconButton(
                icon=ft.icons.MENU, 
                icon_color=ft.colors.BLACK
            ),
        ]
    )
    
    linha = ft.Divider(height=1, color="grey")
    espaço = ft.Container(height=5)  

    # Arte ----------------------------------------------------------------
    fundo_laranja = ft.Container(
        height=100,               
        bgcolor=ft.colors.ORANGE, 
        border_radius=10,      
    )

    foto1 = ft.Image(
        src=r"C:\Users\vfari\Documents\GitHub\CRUD-Python\CRUD\assets\Foto.png",
        width=80,  
        height=100 
    )

    foto2 = ft.Image(
        src=r"C:\Users\vfari\Documents\GitHub\CRUD-Python\CRUD\assets\Restaurant.png",
        width=150,  
        height=100  
    )
    
    conteúdo_fundo_laranja = ft.Container(
        content=ft.Row(
            controls=[foto1, foto2],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=ft.padding.only(left=10, right=10),  
        alignment=ft.alignment.center  
    )

    stack = ft.Stack(
            [
                fundo_laranja,
                conteúdo_fundo_laranja
            ]
            
        )

    # Formulário e validação ----------------------------------------------------------------
    class Input_dados(ft.TextField):
        def __init__(self, label, hint_text):
            super().__init__()
            self.label = label  
            self.label_style = ft.TextStyle(color="#8a8a8a")
            self.border_color = "#999999"
            self.hint_text = hint_text 
            self.border_width = 3
            self.width = 350
            self.text_style = ft.TextStyle(color=ft.colors.BLACK)

    nome = Input_dados(label="Nome", hint_text="Responsável pela reserva")
    quantidade = Input_dados(label="Quantidade de pessoas", hint_text="De 1 a 10")
    data = Input_dados(label="Data", hint_text="DD/MM/AAAA - Limite até 7 dias!")
    
    horarios = [
    "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00",
    "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30",
    "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00"
    ]
    horario = ft.Dropdown(
        label="10h-AM até 11-PM",
        options=[ft.dropdown.Option(h) for h in horarios],
        width=350,
        border_width = 3,
        border_color = "#999999",
        label_style = ft.TextStyle(color="#8a8a8a"),
        text_style = ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#e8e8e8",
        value=""
        )
        
    Menu1 = ft.Container(
        content=ft.Column(
            controls=[nome, quantidade, data, horario],
        )
    )

    # popups ----------------------------------------------------------------
    def abrir_popup(a):
        # Criando um AlertDialog (popup)
        alert_dialog = ft.AlertDialog(
            title=ft.Text("Campo incorreto", size=20),
            content=ft.Text(a),
            actions=[ft.TextButton("Fechar", on_click=lambda e: fechar_popup(alert_dialog))]
        )
        # Exibindo o popup através de overlay
        page.overlay.append(alert_dialog)
        alert_dialog.open = True
        page.update()  
    
    def fechar_popup(dialog):
        dialog.open = False
        page.update()


    def validar_registro(e):

        global maior_id
        
        # Captura a data atual
        data_atual = datetime.now().date()
        
        # Define o limite de 7 dias após a data atual
        limite_data = data_atual + timedelta(days=7)


        if nome.value == "" or quantidade.value == "" or data.value == "" or horario.value == "":
            abrir_popup("Existem campos vazios!")
            return


        #Validação do nome
        elif nome.value.isdigit() == True or len(nome.value) in range(1,3):
            abrir_popup("Por favor, verifique o campo do nome!")
            return
        
        #Validação da quantidade
        elif quantidade.value.isdigit() == True:
            valor1 = int(quantidade.value)
            if valor1 == 0 :
                abrir_popup("Não pode reservar para zero pessoas!")
                return
            elif valor1 < 1 or valor1 > 10:
                abrir_popup("Verifique o limite de reservas!")
                return
        elif quantidade.value.isdigit() == False and quantidade.value != "":
            abrir_popup("A quantidade deve ser numérica!")
            return
        
        try:
            valor2 = datetime.strptime(data.value, '%d/%m/%Y').date()
            
            if valor2 > limite_data or valor2 < data_atual:
                abrir_popup("Selecione uma data válida para a reserva")
                return
            else:
                data_formatada = valor2.strftime('%Y-%m-%d')

        except ValueError:
            abrir_popup("Escreva no formato (dia/mês/ano)!")
            return

        # Armazenando os dados em uma lista de forma organizada e jogando para o banco SQL
        maior_id  = maior_id + 1
        novos_dados = [maior_id, nome.value,quantidade.value,data_formatada, horario.value]
        abrir_popup("Registro realizado com sucesso!")
        from Banco_de_dados import inserção_de_dados
        inserção_de_dados(novos_dados[1], novos_dados[2], novos_dados[3], novos_dados[4])

        nome.value = ""
        quantidade.value = ""
        data.value = ""
        horario.value = ""

        lista, maior_id = trazendo_dados()
        adicionar_dados(lista, len(lista) -1)
        
        
        page.update()
        

    # Botão e estilização ----------------------------------------------------------------
    def hover_botão(e):
        e.control.width = 199 if e.data == "true" else 200
        e.control.height = 39 if e.data == "true" else 40
        e.control.opacity = 0.9 if e.data == "true" else 1  
        e.control.update()  

    salvar = ft.Row(
        [
            ft.Container(
                content=ft.Text("Registrar reserva", color="black", size=18, weight="bold"),
                width=200,
                height=40,
                bgcolor="ORANGE",              
                border_radius=8,
                alignment=ft.alignment.center,  
                on_click=validar_registro,  # Agora chamando a função capturar_dados
                on_hover=hover_botão,  
            )
        ],
        alignment="center"  # Centraliza o Row na página
    )

    # Dados ----------------------------------------------------------------
    class Interatíveis(ft.IconButton):
        def __init__(self, icon):
            super().__init__(icon=icon)  
            self.label_style = ft.TextStyle(color="#8a8a8a")
            self.border_color = "Orange"
            self.icon_color = ft.colors.BLACK  
            self.icon_size = 18
            
     
    reservas = []
    
    lista, maior_id = trazendo_dados()

    edit_dialog = ""

    
    
    def editar_reserva(id):
        lista, maior_id = trazendo_dados()
        print(f"No ponto para a edição {lista}")
        page.update()
        global edit_dialog

        # Encontrar os dados do usuário pelo ID
        dados_usuario = next((item for item in lista if item[0] == id), None)
        if not dados_usuario:
            abrir_popup(f"Erro: Reserva com ID {id} não encontrada!")
            return

        # Criar o diálogo de edição
        edit_dialog = ft.AlertDialog(
            title=ft.Text(f"Editar Reserva ({id})", size=20),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            label="Nome",
                            value=dados_usuario[1],
                            autofocus=True
                        ),
                        ft.TextField(
                            label="Quantidade de pessoas",
                            value=dados_usuario[2]
                        ),
                        ft.TextField(
                            label="Data",
                            value=dados_usuario[3]
                        ),
                        ft.Dropdown(
                            label="Horário",
                            options=[ft.dropdown.Option(h) for h in horarios],
                            value=dados_usuario[4]  # Exibe o horário atual
                        ),
                    ]
                ),
                width=400,  # Largura personalizada do container
                height=270,  # Altura personalizada do container
                padding=20  # Adicionando padding interno para espaçamento
            ),
            actions=[
                ft.TextButton("Salvar", on_click=lambda e: salvar_edicao(id)),
                ft.TextButton("Cancelar", on_click=lambda e: fechar_popup(edit_dialog)),
            ]
        )

        # Exibindo o popup de edição
        page.overlay.append(edit_dialog)
        edit_dialog.open = True
        page.update()


    def salvar_edicao(id):
        global edit_dialog
        # Aqui você implementaria a lógica para salvar as edições feitas
        print(f"Salvando as edições da reserva {id}")
        fechar_popup(edit_dialog)
        page.update()

    def ler_reserva(id):
        print(f"lido {id}")
        
    def apagar_reserva(id):
        global maior_id
        from Banco_de_dados import deleção_no_banco
        deleção_no_banco(id)
        
        key_do_container_dados = f"container_{id}"
        removedor_de_container = next((container for container in reservas if container.key == key_do_container_dados), None)

        if removedor_de_container:
            reservas.remove(removedor_de_container)  
            page.controls.remove(removedor_de_container) 

        lista, maior_id = trazendo_dados() 

        if len(reservas) == 0:  
            mensagem.visible = True
        else:
            mensagem.visible = False

        page.update()  




    def adicionar_dados(lista, a):
        dados = ft.Container(
            key=f"container_{lista[a][0]}",
            visible=True,
            height=50,
            bgcolor=None,              
            border=ft.border.all(2, ft.colors.GREY),  
            border_radius=8,           
            padding=ft.padding.only(left=5, right=20, top=0, bottom=0),
            content=ft.Container(
                border_radius=8, 
                bgcolor="#e8e8e8", 
                content=ft.Row(
                    spacing=3,
                    alignment=ft.MainAxisAlignment.START, 
                    controls=[
                        # Primeiro Container interno
                        ft.IconButton(
                            icon=ft.icons.EDIT,
                            icon_size=17,
                            icon_color=ft.colors.WHITE,
                            bgcolor="green",
                            on_click=lambda e, id=lista[a][0]: editar_reserva(id),
                        ),                                  
                        # Segundo Container interno
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_size=17,
                            icon_color=ft.colors.WHITE,
                            bgcolor="red",
                            on_click=lambda e, id=lista[a][0]: apagar_reserva(id),
                        ),   
                        # Terceiro Container interno
                        ft.IconButton(
                            icon=ft.icons.VISIBILITY,
                            icon_size=17,
                            icon_color=ft.colors.WHITE,
                            bgcolor="blue",
                            on_click=lambda e, id=lista[a][0]: ler_reserva(id),
                        ), 

                        #Espaçamento entre o botão e o texto
                        ft.Container(width=5),  

                        ft.Text(
                            f"ID: {lista[a][0]}",
                            color=ft.colors.BLACK,
                            size=13,
                            weight="bold"
                        ),
                        ft.Container(width=5),  

                        ft.Text(
                            f"Nome: {lista[a][1]}",
                            color=ft.colors.BLACK,
                            size=13,
                            weight="bold"
                        ),
                    ]
                )
            ) 
        )   

        if len(lista) == 0:
            mensagem.visible = True
        else: 
            mensagem.visible = False
        
        reservas.append(dados)
        
        page.add(dados)
        page.update()



    # Mensagem ----------------------------------------------------------------
    mensagem = ft.Container(
        content=ft.Text(
            "Não existem reservas cadastradas!",
            color=ft.colors.BLACK,
            size=14,
        ),
        alignment=ft.Alignment(0, 0) ,
        padding=ft.Padding(top=30, left=0, right=0, bottom=0),
      
    )
    

    page.add(
        cabeçalho, linha, espaço, stack, Menu1, salvar, espaço, mensagem
    )
    for i in range(len(lista)):
        adicionar_dados(lista, i)

ft.app(target=principal)
