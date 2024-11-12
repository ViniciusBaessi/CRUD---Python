import flet as ft

def principal(page: ft.Page):

    page.title = "Tela principal"
    page.window.width = 420
    page.window.height = 720

    #Não permite Esticar
    page.window.resizable = False

    #Não permite tela cheia
    page.window.maximizable = False

    #Sobreposição em outras janelas
    page.window.always_on_top =True
    ft.Text(value="Pedro", size=20)


    class MyButton(ft.ElevatedButton):
        def __init__(self, text):
            super().__init__()

            self.bgcolor = ft.colors.ORANGE_300
            self.color = ft.colors.GREEN_800
            self.text = text    
            
    quadrado = ft.Container(
        width=page.window_width,               # Largura do quadrado
        height=100,              # Altura do quadrado
        bgcolor=ft.colors.BLUE,   # Cor de fundo do quadrado
        border_radius=1          # Borda arredondada, ajuste para zero se quiser bordas retas
    )

    texto_sobreposto = ft.Text(
        value="Texto",
        color=ft.colors.WHITE,
        size=20,
        weight="bold",
        
    )


    stack = ft.Stack(
        [
            quadrado,
            texto_sobreposto
        ]
        
    )

    imagem_local = ft.Image(
        src=r"C:\Users\vfari\Documents\GitHub\Estudo-Python\Python\Pessoal\Flet\teste.png",
        width=200,  # Largura da imagem
        height=200  # Altura da imagem
    )

    page.add(
        
            ft.Row([
                MyButton(text="OK"), MyButton(text="Cancel")
            ],alignment="CENTER"), 
            
            quadrado,

            stack,

            imagem_local
            
            )
    
   
        
        


ft.app(target=principal)