#pgzero
"""
M6.L3: Actividad #3 - "Añadiendo bonificaciones"
Objetivo: Agregar botones de bonus, (sólo dibujarlos)

PACK DE ASSETS: 
ANIMALES: https://kenney.nl/assets/animal-pack-redux 
BOTONES:  https://kenney.nl/assets/ui-pack

Paso Nº 1: Crear Actores bonus_1 y bonus_2 así como sus valores : {precio (int), potenciador (int), ya_activado (bool)} 
Paso Nº 2: Modificar nuestro draw() para que los muestre por pantalla, así como el texto que explica su función

NOTA: La lógica de activar los botones la programaremos en el próximo ejercicio (no hay que agregar collidepoint todavía)

Extra: Crear un token personalizado para nuestro juego

"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo

# VARIABLES
puntuacion = 0
click_mult = 1 # multiplicador del valor por click
token = "₽"

#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

bonus_1 = Actor("bonus", (450, 100))
bonus_1.precio = 15
bonus_1.potenciador = 1
bonus_1.ya_activado = False

bonus_2 = Actor("bonus", (450, 200))
bonus_2.precio = 200
bonus_2.potenciador = 15
bonus_2.ya_activado = False

"""
bonus_3 = Actor("bonus", (450, 300))
bonus_3.precio = 600
bonus_3.potenciador = 50
bonus_3.ya_activado = False
"""

def draw():
    fondo.draw()
    animal.draw()
    
    # Dibujamos puntuacion
    # To-do: Agregar control que chequee que el texto no se salga de la pantalla (ajusta vble fontsize) 
    screen.draw.text((str(puntuacion) + token), center=(150, 70), color="white", fontsize = 96)

    # Dibujamos botones bonus

    bonus_1.draw()
    screen.draw.text(("+" + str(bonus_1.potenciador) + " " + token + " cada 2 seg"), center = (450, 80), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_1.precio) + " " + token), center = (450, 110), color = "black", fontsize = 20)
        
    bonus_2.draw()
    screen.draw.text(("+" + str(bonus_2.potenciador) + " " + token + " cada 2 seg"), center = (450, 180), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_2.precio) + " " + token), center = (450, 210), color = "black", fontsize = 20)

    """bonus_3.draw()
    screen.draw.text(("+" + str(bonus_3.potenciador) + " " + token + " cada 2 seg"), center = (450, 280), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_3.precio) + " " + token), center = (450, 310), color = "black", fontsize = 20)
    """

    
def on_mouse_down(button, pos):
    global puntuacion
    if (button == mouse.LEFT):
        if (animal.collidepoint(pos)):
            # Si el click fue en nuestro animal:
            puntuacion += click_mult
            # Animación:
            animal.y = 200
            animate(animal, tween="bounce_end", duration = 0.5, y = 250)