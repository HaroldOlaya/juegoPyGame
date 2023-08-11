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

# bucle para que se mantenga la ventana abierta
while True:
    for event in pygame.event.get():
        # condicional en un evento para poder cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse_post=pygame.mouse.get_pos()
    print(mouse_post)
    x=mouse_post[0]
    y=mouse_post[1]
    screen.fill(white)

    pygame.draw.rect(screen,red,(x,y,100,100))

    pygame.display.flip()


