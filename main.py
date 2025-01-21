#pgzero
"""
M6.L4: Actividad # 4 - "Morsa"
Objetivo: Agregar un nuevo personaje

PACK DE ASSETS: 
ANIMALES: https://kenney.nl/assets/animal-pack-redux 
BOTONES:  https://kenney.nl/assets/ui-pack

Paso Nº 1 Lo creamos
Paso Nº 2 Le asignamos precio y potenciador de click
Paso Nº 3 Lo agregamos a la lista coleccion_completa

"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo

# VARIABLES
puntuacion = 0
click_mult = 1 # multiplicador del valor por click
token = "₽"
modo_actual = "menu" # Valores posibles: "menu"//"juego"//"tienda"//"coleccion"
tam_fuente_punt = 96 # Altura en píxeles del indicador de puntuacion

#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

# ANIMALES

cocodrilo = Actor("crocodile", (120, 200))
cocodrilo.precio = 500
cocodrilo.mult = 2

hipopotamo = Actor("hippo", (300, 200))
hipopotamo.precio = 2500
hipopotamo.mult = 3

morsa = Actor("walrus", (480, 200))
morsa.precio = 7000
morsa.mult = 4

bonus_1 = Actor("bonus", (450, 100))
bonus_1.precio = 15
bonus_1.potenciador = 1
bonus_1.ya_activado = False

bonus_2 = Actor("bonus", (450, 200))
bonus_2.precio = 200
bonus_2.potenciador = 15
bonus_2.ya_activado = False

bonus_3 = Actor("bonus", (450, 300))
bonus_3.precio = 600
bonus_3.potenciador = 50
bonus_3.ya_activado = False

boton_jugar =     Actor("play", (300, 100))
boton_tienda =    Actor("tienda", (300, 200))
boton_coleccion = Actor("coleccion", (300, 300))
boton_salir =     Actor("cross", (WIDTH - 20, 20))

# Listas skins
coleccion_skins = [] # lista de skins desbloqueadas/compradas

coleccion_completa = [] # lista que contiene todas las skins desbloqueables por el jugador
coleccion_completa.append(cocodrilo)
coleccion_completa.append(hipopotamo)
coleccion_completa.append(morsa)

""" #####################
   # FUNCIONES PROPIAS #
  ##################### """

def el_bonus_1():
    global puntuacion
    puntuacion += bonus_1.potenciador

def el_bonus_2():
    global puntuacion
    puntuacion += bonus_2.potenciador
    
def el_bonus_3():
    global puntuacion
    puntuacion += bonus_3.potenciador

def actualizar_tam_fuente_punt():
  global tam_fuente_punt

  # Ajustar el tamaño de la fuente según el tamaño de la puntuación
  if puntuacion < 1000:
    tam_fuente_punt = 96
  elif puntuacion < 10000:
    tam_fuente_punt = 72
  else:
    tam_fuente_punt = 48

""" ####################
   # FUNCIONES PGZERO #
  #################### """

def draw():

    if (modo_actual == "menu"):
        fondo.draw()
        boton_jugar.draw()
        boton_tienda.draw()
        boton_coleccion.draw()

    elif (modo_actual == "juego"):
    
        fondo.draw()
        animal.draw()
        
        # Dibujamos puntuacion
        # Ahora nuestra puntuación cambia de tamaño según la cantidad de créditos/tokens que tengo
        screen.draw.text((str(puntuacion) + token), center=(150, 70), color="white", fontsize = tam_fuente_punt)
    
        # Dibujamos botones bonus
    
        bonus_1.draw()
        screen.draw.text(("+" + str(bonus_1.potenciador) + " " + token + " cada 2 seg"), center = (450, 80), color = "black", fontsize = 20)
        screen.draw.text(("PRECIO: " + str(bonus_1.precio) + " " + token), center = (450, 110), color = "black", fontsize = 20)
            
        bonus_2.draw()
        screen.draw.text(("+" + str(bonus_2.potenciador) + " " + token + " cada 2 seg"), center = (450, 180), color = "black", fontsize = 20)
        screen.draw.text(("PRECIO: " + str(bonus_2.precio) + " " + token), center = (450, 210), color = "black", fontsize = 20)
    
        bonus_3.draw()
        screen.draw.text(("+" + str(bonus_3.potenciador) + " " + token + " cada 2 seg"), center = (450, 280), color = "black", fontsize = 20)
        screen.draw.text(("PRECIO: " + str(bonus_3.precio) + " " + token), center = (450, 310), color = "black", fontsize = 20)

        boton_salir.draw()

    elif (modo_actual == "tienda"):
        fondo.draw()

        # Si ya desbloqueamos TODAS las skins
        if set(coleccion_skins) == set(coleccion_completa):
            screen.draw.text("¡FELICIDADES!", center=(WIDTH/2, HEIGHT/3), color = "white", background = "black" , fontsize = 42)
            screen.draw.text("Has adquirido todas las skins", center=(WIDTH/2, HEIGHT/3*2), color = "white", background = "black" , fontsize = 32)

        else:
            for skin in coleccion_completa:
                if skin not in coleccion_skins:
                    # Si NO la hemos adquirido:
                    skin.draw()
                    screen.draw.text((str(skin.precio) + token), center=(skin.x, 300), color = "white" , fontsize = 36)


            # NOTA: Ponemos acá la puntuación porque no la queremos mnostrar cuando el jugador ya haya desbloqueado todo
            # Dibujamos puntuacion
            screen.draw.text((str(puntuacion) + token), center=(150, 70), color="white", fontsize = tam_fuente_punt)
        
        boton_salir.draw()

    elif (modo_actual == "coleccion"):
        fondo.draw()

        # Dibujamos puntuacion
        screen.draw.text((str(puntuacion) + token), center=(150, 70), color="white", fontsize = tam_fuente_punt)

        # Dibujar Skins desbloqueables - ( lo vamos a modificar más adelante)

        for skin in coleccion_skins:
            skin.draw()

        # Dibujar ? para las NO-desbloqueadas

        for skin in coleccion_completa:
            if skin not in coleccion_skins:
                screen.draw.text(("⚫"), center=(skin.pos), color = "white" , fontsize = 120)
                screen.draw.text("?", center=(skin.pos), color = "white", fontsize = 96)

            # mostramos habilidades/multiplicadores skins
            screen.draw.text((str(skin.mult) + "x " + token ), center=(skin.x, 300), color = "white" , fontsize = 36)
        
        boton_salir.draw()
    
def on_mouse_down(button, pos):
    global puntuacion, modo_actual, click_mult
    
    if (button == mouse.LEFT) and (modo_actual == "menu"):
        if boton_jugar.collidepoint(pos):
            # Si el click fue sobre el boton "Jugar":
            modo_actual = "juego"

        if boton_tienda.collidepoint(pos):
            # Si el click fue sobre el boton "Tienda":
            modo_actual = "tienda"

        if boton_coleccion.collidepoint(pos):
            # Si el click fue sobre el boton "Colección":
            modo_actual = "coleccion"

    elif (button == mouse.LEFT) and (modo_actual == "juego"):
        
        if (animal.collidepoint(pos)):
            # Si el click fue en nuestro animal:
            puntuacion += click_mult
            actualizar_tam_fuente_punt()
            # Animación:
            animal.y = 200
            animate(animal, tween="bounce_end", duration = 0.5, y = 250)

        elif bonus_1.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 1:
            if (puntuacion >= bonus_1.precio):
                # Chequeamos si tiene suficientes puntos para comprarlo:
                # Chequeamos si ya está activo
                if (not bonus_1.ya_activado):
                    schedule_interval(el_bonus_1, 2)
                    bonus_1.ya_activado = True
                else:
                    bonus_1.potenciador += 1
                # Restamos los puntos gastados para compar el bonus:
                puntuacion -= bonus_1.precio
                bonus_1.precio *= 2

                # Animamos el botón cuando pueda comprarlo
                bonus_1.y = 105
                animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            
            else:
                # Si no tiene suficientes puntos para comprarlo
                bonus_1.x = 445
                animate(bonus_1, tween='bounce_end', duration=0.25, x=450)
                bonus_1.x = 455
                animate(bonus_1, tween='bounce_end', duration=0.25, x=450)

        elif bonus_2.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 2:
            if (puntuacion >= bonus_2.precio):
                # Chequeamos si tiene suficientes puntos para comprarlo:
                # Chequeamos si ya está activo
                if (not bonus_2.ya_activado):
                    schedule_interval(el_bonus_2, 2)
                    bonus_2.ya_activado = True
                else:
                    bonus_2.potenciador += 15
                    
                # Restamos los puntos gastados para compar el bonus:
                puntuacion -= bonus_2.precio
                bonus_2.precio *= 2

                # Animamos el botón cuando pueda comprarlo
                bonus_2.y = 205
                animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
                
            else:
                # Si no tiene suficientes puntos para comprarlo
                bonus_2.x = 445
                animate(bonus_2, tween='bounce_end', duration=0.25, x=450)
                bonus_2.x = 455
                animate(bonus_2, tween='bounce_end', duration=0.25, x=450)

        elif bonus_3.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 3:
            if (puntuacion >= bonus_3.precio):
                # Chequeamos si tiene suficientes puntos para comprarlo:
                # Chequeamos si ya está activo
                if (not bonus_3.ya_activado):
                    schedule_interval(el_bonus_3, 2)
                    bonus_3.ya_activado = True
                else:
                    bonus_3.potenciador += 50
                    
                # Restamos los puntos gastados para compar el bonus:
                puntuacion -= bonus_3.precio
                bonus_3.precio *= 2

                # Animamos el botón cuando pueda comprarlo
                bonus_3.y = 305
                animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
                
            else:
                # Si no tiene suficientes puntos para comprarlo
                bonus_3.x = 445
                animate(bonus_3, tween='bounce_end', duration=0.25, x=450)
                bonus_3.x = 455
                animate(bonus_3, tween='bounce_end', duration=0.25, x=450)
                
        elif boton_salir.collidepoint(pos):
            # Si el click fue sobre el botón de salir:
            modo_actual = "menu"
    
    if (button == mouse.LEFT) and (modo_actual == "tienda"):
         
        if boton_salir.collidepoint(pos):
            # Si el click fue sobre el botón de salir:
            modo_actual = "menu"

        # Nota: modificar por un bucle para todas las skins...
        # Nota 2: Agregar animación horizontal cuando NO tenga tokens suficientes para comprarlo

        """
        Paso 1: Chequear el click (collidepoint)
        Paso 2: Verificar que el jugador tenga suficientes créditos
        SI LOS TIENE:
        Paso 3: Restar los créditos
        Paso 4: Cambiar la skin actual (y el modificador de click)
        Paso 5: Agregarlo a la lista de skins desbloqueadas
        """

        for skin in coleccion_completa:
            if (  skin.collidepoint(pos) and         # Si le doy click a una skin 
                 (skin not in coleccion_skins) and   # Y esa skin NO la tenga desbloqueada
                 (puntuacion >= skin.precio) ):      # Y tengo suficientes créditos/tokens

                puntuacion -= skin.precio            # Restamos los créditos para comprar
                animal.image = skin.image            # Cambiamos la skin de nuestro PJ
                click_mult = skin.mult               # Actualizamos el mult de click
                coleccion_skins.append(skin)         # Agrego la skin comprada a mi lista

        # NOTA: Este método funcionará para otros animales SIEMPRE y cuando los incluya en coleccion_completa 

    if (button == mouse.LEFT) and (modo_actual == "coleccion"):
         if boton_salir.collidepoint(pos):
            # Si el click fue sobre el botón de salir:
            modo_actual = "menu"

         """
         Paso 1: Verificar si hice click sobre una skin
         Paso 2: Validar que esté desbloqueada (ya comprada)
         SI ES ASÍ:
         Paso 3: Cambiar la imágen de nuestro PJ y su click_mult
         """

         for skin in coleccion_skins:
             if ( skin.collidepoint(pos) ):     # Si hice click sobre una skin YA DESBLOQUEADA:
                 animal.image = skin.image      # Cambiamos la skin de nuestro PJ
                 click_mult = skin.mult         # Actualizamos el mult de click
             
# CHEAT:

def on_key_down(key):
    global puntuacion, modo_actual, click_mult
    
    if keyboard.d:
        puntuacion += 500
        
    if keyboard.a:
        puntuacion -= 500

    if keyboard.j:
        animal.image = "giraffe"
        click_mult = 1