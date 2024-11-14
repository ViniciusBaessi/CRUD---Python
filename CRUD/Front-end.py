import flet as ft
from datetime import datetime, timedelta #Pegar as datas

def principal(page: ft.Page):

    # Atributos da minha tela
    page.title = "Tela principal"
    page.window.width = 350
    page.window.height = 750
    page.bgcolor = "#e8e8e8" 
    page.window.resizable = True
    page.window.maximizable = False
    page.window.always_on_top = True
  

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
    data = Input_dados(label="Data", hint_text="DD/MM/AAAA")
    
    
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
        bgcolor="#e8e8e8"
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
            title=ft.Text("Campo incorreto"),
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

        # Captura a data atual
        data_atual = datetime.now().date()
        
        # Define o limite de 7 dias após a data atual
        limite_data = data_atual + timedelta(days=7)

        #Validação do nome
        if nome.value.isdigit() == True or nome.value == "" or len(nome.value) < 3:
            abrir_popup("Por favor, verifique o campo do nome!")
        
        #Validação da quantidade
        elif quantidade.value.isdigit() == True:
            valor = int(quantidade.value)
            if valor == 0 :
                abrir_popup("Não pode reservar para zero pessoas!")
            elif valor < 1 or valor > 10:
                abrir_popup("Verifique o limite de reservas!")

        #Validação da data
        if not data.value == "":
            valor = datetime.strptime(data.value, '%d/%m/%Y').date()

            if valor > limite_data or valor < data_atual:
                abrir_popup("Selecione uma data válida para a reserva")
            else:
                valor = valor.strftime('%d/%m/%Y')

    # Botão e estilização ----------------------------------------------------------------
    def hover_botão(e):
        e.control.width = 199 if e.data == "true" else 200
        e.control.height = 39 if e.data == "true" else 40
        e.control.opacity = 0.9 if e.data == "true" else 1  
        e.control.update()  
        

    def hover(e):
        e.control.opacity = 0.7 if e.data == "true" else 1  
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
            
    dados = ft.Container(
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
                    ft.Container(
                        width=35,
                        height=35,
                        bgcolor="green",
                        content=Interatíveis(icon=ft.icons.EDIT),
                        alignment=ft.alignment.center,
                        border_radius=6,
                        on_hover=hover,
                    ),
                    # Segundo Container interno
                    ft.Container(
                        width=35,
                        height=35,
                        bgcolor="red",
                        content=Interatíveis(icon=ft.icons.DELETE),
                        alignment=ft.alignment.center,
                        border_radius=6,
                        on_hover=hover,
                    ),
                    # Terceiro Container interno
                    ft.Container(
                        width=35,
                        height=35,
                        bgcolor="blue",
                        content=Interatíveis(icon=ft.icons.VISIBILITY),
                        alignment=ft.alignment.center,
                        border_radius=6,
                        on_hover=hover,
                    ),

                    #Espaçamento entre o botão e o texto
                    ft.Container(width=5),  

                    ft.Text(
                        "ID: 01",
                        color=ft.colors.BLACK,
                        size=13,
                        weight="bold"
                    ),
                    ft.Container(width=5),  

                    ft.Text(
                        "Nome: Paulo",
                        color=ft.colors.BLACK,
                        size=13,
                        weight="bold"
                    ),
                ]
            )
        )
    )
    
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
        cabeçalho, linha, espaço, stack, Menu1, salvar, espaço, dados, dados, mensagem
    )

ft.app(target=principal)
