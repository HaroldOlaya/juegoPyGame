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
# eliminar la visivilidad del mouse
pygame.mouse.set_visible(0)
# CORDENADAS DEL OBJETO
coord_x=10
coord_y=10
# Velocidad
x_speed =0
y_speed =0
# bucle para que se mantenga la ventana abierta
while True:
    for event in pygame.event.get():
        # condicional en un evento para poder cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed= -3
            if event.key == pygame.K_RIGHT:
                x_speed=3
            if event.key == pygame.K_UP:
                y_speed= -3
            if event.key == pygame.K_DOWN:
                y_speed=3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0

    screen.fill(white)
    coord_x += x_speed
    coord_y += y_speed
    pygame.draw.rect(screen,red,(coord_x,coord_y,100,100))

    pygame.display.flip()


