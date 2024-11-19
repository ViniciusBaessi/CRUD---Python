import flet as ft
from datetime import datetime, timedelta #Pegar as datas
import sqlite3

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
            ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_ROUNDED, icon_color=ft.colors.BLACK),
            ft.Text("Menu de reservas", color=ft.colors.BLACK, size=20, weight="bold"),
            ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.BLACK),
        ]
    )
    
    linha = ft.Divider(height=1, color="grey")
    espaço = ft.Container(height=5)

    # Exibição de Dados ----------------------------------------------------------------
    reservas_container = ft.Column(spacing=10, scroll="adaptive")

    def adicionar_dados(lista):
        reservas_container.controls.clear()  # Limpa a lista de reservas atuais
        for item in lista:
            reservas_container.controls.append(
                ft.Container(
                    height=50,
                    bgcolor=None,
                    border=ft.border.all(2, ft.colors.GREY),
                    border_radius=8,
                    padding=ft.padding.all(10),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f"ID: {item[0]}", size=14, color=ft.colors.BLACK),
                            ft.Text(f"Nome: {item[1]}", size=14, color=ft.colors.BLACK),
                            ft.Text(f"Pessoas: {item[2]}", size=14, color=ft.colors.BLACK),
                            ft.Text(f"Data: {item[3]}", size=14, color=ft.colors.BLACK),
                        ]
                    )
                )
            )
        reservas_container.update()
    
    # Inicialização dos dados
    if lista:
        adicionar_dados(lista)

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
                on_click=lambda _: adicionar_dados(lista),
                on_hover=hover_botão,
            )
        ],
        alignment="center"
    )

    # Layout final
    page.add(
        cabeçalho, linha, espaço, reservas_container, espaço, salvar
    )

    
ft.app(target=principal)
