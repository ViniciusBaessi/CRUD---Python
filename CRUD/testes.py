import flet as ft
from datetime import datetime, timedelta
import sqlite3
from Banco_de_dados import alimentando_aplicação

# Trazendo dados do SQL
dados = alimentando_aplicação()

# Estruturando a lista com os dados
lista = []
for i in range(len(dados)):
    nova_reserva = []
    for contador in range(4):
        nova_reserva.append(dados[i][contador])
    lista.append(nova_reserva)

# Função principal
def principal(page: ft.Page):
    # Atributos da tela
    page.title = "Tela principal"
    page.window.width = 350
    page.window.height = 750
    page.bgcolor = "#e8e8e8"
    page.window.resizable = False
    page.window.maximizable = False
    page.window.always_on_top = True
    page.scroll = "adaptive"

    # Cabeçalho
    cabeçalho = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_ROUNDED, icon_color=ft.colors.BLACK),
            ft.Text("Menu de reservas", color=ft.colors.BLACK, size=20, weight="bold"),
            ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.BLACK),
        ]
    )

    # Divider
    linha = ft.Divider(height=1, color="grey")
    espaço = ft.Container(height=5)

    # Arte
    fundo_laranja = ft.Container(
        height=100,
        bgcolor=ft.colors.ORANGE,
        border_radius=10,
    )

    foto1 = ft.Image(src=r"C:\Users\vfari\Documents\GitHub\CRUD-Python\CRUD\assets\Foto.png", width=80, height=100)
    foto2 = ft.Image(src=r"C:\Users\vfari\Documents\GitHub\CRUD-Python\CRUD\assets\Restaurant.png", width=150, height=100)

    conteúdo_fundo_laranja = ft.Container(
        content=ft.Row(controls=[foto1, foto2], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.padding.only(left=10, right=10),
        alignment=ft.alignment.center
    )

    stack = ft.Stack([fundo_laranja, conteúdo_fundo_laranja])

    # Formulário e validação
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
        "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30",
        "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00"
    ]
    horario = ft.Dropdown(
        label="10h-AM até 11-PM",
        options=[ft.dropdown.Option(h) for h in horarios],
        width=350,
        border_width=3,
        border_color="#999999",
        label_style=ft.TextStyle(color="#8a8a8a"),
        text_style=ft.TextStyle(color=ft.colors.BLACK),
        bgcolor="#e8e8e8",
        value=""
    )

    Menu1 = ft.Container(
        content=ft.Column(controls=[nome, quantidade, data, horario]),
    )

    # Funções de popups
    def abrir_popup(a):
        alert_dialog = ft.AlertDialog(
            title=ft.Text("Campo incorreto", size=20),
            content=ft.Text(a),
            actions=[ft.TextButton("Fechar", on_click=lambda e: fechar_popup(alert_dialog))]
        )
        page.overlay.append(alert_dialog)
        alert_dialog.open = True
        page.update()

    def fechar_popup(dialog):
        dialog.open = False
        page.update()

    # Função para validar o registro
    def validar_registro(e):
        data_atual = datetime.now().date()
        limite_data = data_atual + timedelta(days=7)

        if nome.value == "" or quantidade.value == "" or data.value == "" or horario.value == "":
            abrir_popup("Existem campos vazios!")
            return

        # Validação do nome
        elif nome.value.isdigit() or len(nome.value) in range(1, 3):
            abrir_popup("Por favor, verifique o campo do nome!")
            return

        # Validação da quantidade
        elif not quantidade.value.isdigit() or int(quantidade.value) < 1 or int(quantidade.value) > 10:
            abrir_popup("Verifique a quantidade de reservas!")
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

        # Armazenando os dados em uma lista e jogando para o banco SQL
        lista = [nome.value, quantidade.value, data_formatada, horario.value]
        abrir_popup("Registro realizado com sucesso!")
        from Banco_de_dados import inserção_de_dados
        inserção_de_dados(lista[0], lista[1], lista[2], lista[3])

        # Limpa os campos do formulário
        nome.value = ""
        quantidade.value = ""
        data.value = ""
        horario.value = ""

        # Adiciona o novo registro à lista de reservas
        adicionar_reserva(lista)

        page.update()

    # Lista para armazenar os containers de reservas
    reservas_containers = []

    # Função para adicionar nova reserva
    def adicionar_reserva(dados_reserva):
        reserva_container = ft.Container(
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
                        ft.Text(f"Nome: {dados_reserva[0]}", color=ft.colors.BLACK, size=13),
                        ft.Text(f"Reserva: {dados_reserva[1]} pessoas", color=ft.colors.BLACK, size=13),
                        ft.Text(f"Data: {dados_reserva[2]}", color=ft.colors.BLACK, size=13),
                        ft.Text(f"Horário: {dados_reserva[3]}", color=ft.colors.BLACK, size=13),
                    ]
                ),
            ),
        )

        # Adiciona o novo container à lista e à interface
        reservas_containers.append(reserva_container)
        page.add(reserva_container)
        page.update()

    # Botão de salvar e hover
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
                border_radius=10,
                alignment=ft.alignment.center,
                on_click=validar_registro,
                on_hover=hover_botão,
            ),
        ]
    )

    # Adicionar o botão de salvar e os dados à tela
    page.add(cabeçalho, linha, espaço, stack, Menu1, salvar)

ft.app(target=principal)
