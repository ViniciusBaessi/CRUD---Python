import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Exemplo de Popup com Seleção de Horário"
    page.window.height = 300
    page.window.width = 400

    # Criando o AlertDialog (popup)
    alert_dialog = ft.AlertDialog(
        title=ft.Text("Alerta"),
        content=ft.Text("Este é um popup de alerta."),
        actions=[ft.TextButton("Fechar", on_click=lambda e: toggle_popup())]
    )
    page.overlay.append(alert_dialog)

    # Função para abrir/fechar o popup
    def toggle_popup(e=None):
        alert_dialog.open = not alert_dialog.open
        page.update()

    # Campo de seleção de horário com intervalo das 10:00 às 11:00
    horarios = [
        "10:00", "10:05", "10:10", "10:15", "10:20", "10:25", "10:30", 
        "10:35", "10:40", "10:45", "10:50", "10:55", "11:00"
    ]
    horario_dropdown = ft.Dropdown(
        label="Selecione o horário",
        options=[ft.dropdown.Option(h) for h in horarios],
        width=200,
    )

    # Botão para abrir o popup
    open_popup_button = ft.ElevatedButton("Mostrar Popup", on_click=toggle_popup)

    # Adicionando os elementos à página
    page.add(horario_dropdown, open_popup_button)

ft.app(target=main)
