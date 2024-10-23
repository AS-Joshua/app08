import flet as ft


def main(page: ft.Page):
    #Establecer tamaño de pantalla
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="Black"
    page.title="Mictlan"
    page.fgcolor="gray"
    
    #Tamañpo imagenes
    image_wid=150
    image_height=150
    
    #Audios
    intro=ft.Audio(
        src="Intro.mp3",volume=1,balance=0
    )
    
    page.overlay.append(intro)
    
    Nivel1=ft.Audio(
        src="Primer_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel1)
    
    Nivel2=ft.Audio(
        src="Segundo_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel2)
    
    Nivel3=ft.Audio(
        src="Terce_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel3)
    
    Nivel4=ft.Audio(
        src="Cuarto_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel4)
    
    Nivel5=ft.Audio(
        src="Quinto_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel5)
    
    Nivel6=ft.Audio(
        src="Sexto_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel6)
    
    Nivel7=ft.Audio(
        src="Septimo_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel7)
    
    Nivel8=ft.Audio(
        src="Octavo_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel8)
    
    Nivel9=ft.Audio(
        src="Noveno_Nivel.mp3",volume=1,balance=0
    )
    page.overlay.append(Nivel9)
    
    #Creación del interfaz
    btnIntro=ft.FilledButton(
        text="Escucha el intro".disabled=filterfalse
    )
    
    btnNivel1=ft.ElevatedButton(
        text="Primer Nivel"
    )
    
    btnNivel2=ft.ElevatedButton(
        text="Segundo Nivel"
    )
    
    
    
ft.app(main)
