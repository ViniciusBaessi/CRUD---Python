import flet as ft

def dados(id, nome):
    # Verifica se o ID ou nome é válido
    if id and nome:
        return ft.Container(
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
                        ft.Container(
                            width=35,
                            height=35,
                            bgcolor="green",
                            content=Interatíveis(icon=ft.icons.EDIT),
                            alignment=ft.alignment.center,
                            border_radius=6,
                            on_hover=hover,
                        ),
                        ft.Container(
                            width=35,
                            height=35,
                            bgcolor="red",
                            content=Interatíveis(icon=ft.icons.DELETE),
                            alignment=ft.alignment.center,
                            border_radius=6,
                            on_hover=hover,
                        ),
                        ft.Container(
                            width=35,
                            height=35,
                            bgcolor="blue",
                            content=Interatíveis(icon=ft.icons.VISIBILITY),
                            alignment=ft.alignment.center,
                            border_radius=6,
                            on_hover=hover,
                        ),
                        ft.Container(width=5),  # Espaçamento
                        ft.Text(
                            f"ID: {id}",
                            color=ft.colors.BLACK,
                            size=13,
                            weight="bold"
                        ),
                        ft.Container(width=5),  # Espaçamento
                        ft.Text(
                            f"Nome: {nome}",
                            color=ft.colors.BLACK,
                            size=13,
                            weight="bold"
                        ),
                    ]
                )
            )
        )
    return None


# Função principal da aplicação
def principal(page: ft.Page):
    lista = [[1, "Paulo"], [2, "Maria"]]  # Exemplo de dados
    page.title = "Reservas"
    page.scroll = True

    cabeçalho = ft.Text("Reservas", size=20, weight="bold", color=ft.colors.BLUE)
    linha = ft.Divider()
    espaço = ft.Container(height=10)

    stack = []  # Lista de containers a serem exibidos
    if len(lista) > 0:
        for item in lista:
            container = dados(item[0], item[1])
            if container:
                stack.append(container)
    else:
        stack.append(
            ft.Container(
                content=ft.Text(
                    "Não existem reservas cadastradas!",
                    color=ft.colors.BLACK,
                    size=14,
                ),
                alignment=ft.Alignment(0, 0),
                padding=ft.Padding(top=30, left=0, right=0, bottom=0),
            )
        )

    page.add(cabeçalho, linha, espaço, *stack)


ft.app(target=principal)
