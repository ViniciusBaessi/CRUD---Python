import flet as ft

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

    # Formulário  ----------------------------------------------------------------
    class Input_dados(ft.TextField):
        def __init__(self, label, hint_text):
            super().__init__()
            self.label = label  
            self.label_style = ft.TextStyle(color="#8a8a8a")
            self.border_color = "Orange"
            self.hint_text = hint_text 
            self.border_width = 3
            self.width = 350
            self.text_style = ft.TextStyle(color=ft.colors.BLACK)

    nome = Input_dados(label="Nome", hint_text="Responsável pela reserva")
    quantidade = Input_dados(label="Quantidade de pessoas", hint_text="De 0 a 10")
    data = Input_dados(label="Data", hint_text="DD/MM/AAAA")
    horario = Input_dados(label="Horário", hint_text="10h-AM até 11h-PM")

    Menu1 = ft.Container(
        content=ft.Column(
            controls=[nome, quantidade, data, horario],
        )
    )

    def capturar_dados(e):
        nome_valor = nome.value
        quantidade_valor = quantidade.value
        data_valor = data.value
        horario_valor = horario.value
        
      
        print(f"Nome: {nome_valor}")
        print(f"Quantidade de pessoas: {quantidade_valor}")
        print(f"Data: {data_valor}")
        print(f"Horário: {horario_valor}")
    


    # Botão ----------------------------------------------------------------
    def hover(e):
        e.control.width = 199 if e.data == "true" else 200
        e.control.height = 49 if e.data == "true" else 50
        e.control.opacity = 0.9 if e.data == "true" else 1  
        e.control.update()  

    salvar = ft.Row(
        [
            ft.Container(
                content=ft.Text("Registrar reserva", color="black", size=18, weight="bold"),
                width=200,
                height=50,
                bgcolor="ORANGE",              
                border_radius=8,
                alignment=ft.alignment.center,  
                on_click=capturar_dados,  # Agora chamando a função capturar_dados
                on_hover=hover,  
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
        height=60,
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
                    ),
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
    
    page.add(
        cabeçalho, linha, espaço, stack, Menu1, salvar, espaço, dados
    )

ft.app(target=principal)
