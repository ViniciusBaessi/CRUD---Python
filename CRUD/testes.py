import flet as ft

def principal(page: ft.Page):
    # Container com fundo transparente e apenas borda visível
    container_transparente = ft.Container(
        width=200,
        height=100,
        bgcolor=None,               # Fundo transparente
        border=ft.border.all(2, ft.colors.BLUE),  # Borda azul com 2px de largura
        border_radius=8,            # Bordas arredondadas (opcional)
        alignment=ft.alignment.center,  # Centraliza o conteúdo dentro do container
        
        
    )

    # Adiciona o container à página
    page.add(container_transparente)

ft.app(target=principal)
