import flet as ft

def fechar_popup(alert_dialog):
    alert_dialog.open = False

a = "Mensagem de erro aqui"

alert_dialog = ft.AlertDialog(
    title=ft.Text("Campo incorreto", size=20),
    content=ft.Container(
        content=ft.Text(a),
        width=300  # Ajuste a largura desejada aqui
    ),
    actions=[
        ft.TextButton("Fechar", on_click=lambda e: fechar_popup(alert_dialog))
    ]
)

# Mostrar o popup, se necessário, com o código para exibir a tela
ft.app(target=lambda page: page.add(alert_dialog))
