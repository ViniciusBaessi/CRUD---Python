import flet as ft

def main(page: ft.Page):
    # Variável para guardar o valor do TextField
    nome_usuario = ""

    # Função para capturar o valor do TextField
    def pegar_valor(e):
        nonlocal nome_usuario
        nome_usuario = campo_nome.value  # Captura o valor
        print(f"Valor capturado: {nome_usuario}")  # Exibe no console
        # Você pode fazer qualquer coisa com o valor aqui

    # Campo de texto
    campo_nome = ft.TextField(
        label="Nome",
        value="",
        autofocus=True,
    )

    # Botão para salvar o valor
    botao_salvar = ft.ElevatedButton("Salvar", on_click=pegar_valor)

    # Adicionando os elementos à página
    page.add(campo_nome, botao_salvar)

# Executando o app
ft.app(target=main)
