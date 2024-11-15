import flet as ft

def main(page: ft.Page):
    # Inicializa dois containers com conteúdo diferente
    container1 = ft.Container(
        content=ft.Text("Container 1 Ativo"),
        bgcolor="lightblue",
        padding=20,
        visible=True  # Inicialmente visível
    )

    container2 = ft.Container(
        content=ft.Text("Container 2 Ativo"),
        bgcolor="lightgreen",
        padding=20,
        visible=False  # Inicialmente oculto
    )

    # Função para alternar a visibilidade
    def toggle_containers(e):
        # Alterna a visibilidade
        container1.visible = not container1.visible
        container2.visible = not container2.visible
        page.update()  # Atualiza a página para refletir as mudanças

    # Botão para alternar entre os containers
    toggle_button = ft.ElevatedButton("Alternar Containers", on_click=toggle_containers)

    # Adiciona os widgets à página
    page.add(
        container1,
        container2,
        toggle_button
    )

ft.app(target=main)
