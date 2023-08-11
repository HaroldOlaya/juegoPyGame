import pygame,sys
# inicializar el programa
pygame.init()
# definir los colores
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
# configuracion de la ventana
screen = pygame.display.set_mode((800, 500))
# controlar los FPS
clock =pygame.time.Clock()
#coordenadas del cuadrado
cord_x = 400
cord_y = 200

#Velocidad de movimiento
speed_x=3
speed_y=3
# bucle para que se mantenga la ventana abierta
while True:
    for event in pygame.event.get():
        # condicional en un evento para poder cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #---Logica del juego
    if (cord_x >780 or cord_x<0):
        speed_x*=-1
    if (cord_y >480 or cord_y<0):
        speed_y*=-1
    # cambiar la posicion del objeto
    cord_x+=speed_x
    cord_y+=speed_y

    #--- Fin de la logica
    #color a mi pantalla
    screen.fill(white)
    #-- zona de dibujo

    # valores en x,y y luego el tamaño
    pygame.draw.rect(screen,black,(cord_x,cord_y,20,20))


    ##-- finalizacion de la zona de dibujo
    #actualizar pantalla
    pygame.display.flip()
    clock.tick(30)


