import flet as ft

def main(page: ft.Page):
    
    
    
    # Função chamada ao pressionar o botão "Enviar"
    def enviar_click(e):
        print("Texto enviado:", input_text.value)  # Exemplo: imprimi o valor no console
        input_text.value = ""  # Limpa o campo de texto
        page.dialog.open = False
        page.update()

    # Abre o popup
    def abrir_popup(e):
        page.dialog.open = True
        page.update()

    # Campo de texto no popup
    input_text = ft.TextField(label="Digite algo", multiline=False)

    # Definição do AlertDialog
    popup = ft.AlertDialog(
        modal=True,
        title=ft.Text("Meu Popup"),
        content=input_text,
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: fechar_popup()),
            ft.ElevatedButton("Enviar", on_click=enviar_click),
        ],
    )

    # Função para fechar o popup
    def fechar_popup():
        popup.open = False
        page.update()

    # Configura o dialog no Page
    page.dialog = popup

    # Botão para abrir o popup
    abrir_button = ft.ElevatedButton("Abrir Popup", on_click=abrir_popup)

    page.add(abrir_button)

ft.app(target=main)
