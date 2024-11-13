import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Exemplo de Popup"
    page.window.height = 300
    page.window.width = 400

    # Função para mostrar o popup
    def show_popup(e):
        # Criando um AlertDialog (popup)
        alert_dialog = ft.AlertDialog(
            title=ft.Text("Alerta"),
            content=ft.Text("Este é um popup de alerta."),
            actions=[ft.TextButton("Fechar", on_click=lambda e: close_popup(alert_dialog))]
        )
        # Exibindo o popup através de overlay
        page.overlay.append(alert_dialog)
        alert_dialog.open = True
        page.update()

    # Função para fechar o popup
    def close_popup(dialog):
        dialog.open = False
        page.update()

    # Botão para abrir o popup
    open_popup_button = ft.ElevatedButton("Mostrar Popup", on_click=show_popup)

    # Adicionando o botão à página
    page.add(open_popup_button)

ft.app(target=main)
