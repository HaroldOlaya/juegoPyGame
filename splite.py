import random
import pygame,sys

def juego():
    # inicializar el programa
    pygame.init()
    #Nombrar la ventana
    pygame.display.set_caption("Marte 13")
    # definir los colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    # contador de impactos
    score = 0
    aux=1
    Fuente = pygame.font.SysFont("Arial",30)


    # creacion de clases
    class Avion(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("avion.png").convert()
            self.image = pygame.transform.scale(self.image, (60,60))
            self.image.set_colorkey((0,0,0))
            self.rect = self.image.get_rect()


        def update(self):
            mouse_pos = pygame.mouse.get_pos()
            player.rect.x = mouse_pos[0]
            player.rect.y = 450


    class Meteoro(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("meteoro.png").convert()
            self.image = pygame.transform.scale(self.image, (30,30))
            self.image.set_colorkey((0,0,0))
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.y += 1
            if self.rect.y > 500:
                self.rect.y = -20
                self.rect.x = random.randrange(700)
    class Laser(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("laser.png").convert()
            self.image.set_colorkey((0,0,0))
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.y -= 5



    # configuracion de la ventana
    screen = pygame.display.set_mode((700, 500))
    # controlar los FPS
    clock = pygame.time.Clock()
    # eliminar la visivilidad del mouse
    pygame.mouse.set_visible(0)
    # fondo de pantalla
    background = pygame.image.load("fondodebatalla.jpg").convert()
    #creacion de listas
    meteor_list = pygame.sprite.Group()
    all_sprite_list = pygame.sprite.Group()
    laser_list=pygame.sprite.Group()
    for i in range(15):
        m = Meteoro()
        m.rect.x = random.randrange(700)
        m.rect.y = random.randrange(0, 100)
        meteor_list.add(m)
        all_sprite_list.add(m)
    player = Avion()
    all_sprite_list.add(player)
    #cargar sonido
    sound = pygame.mixer.Sound("disparo.mp3")
    # bucle para que se mantenga la ventana abierta
    while True:
        Tiempo=pygame.time.get_ticks()//1000
        TiempoRestante=20-Tiempo
        if aux == Tiempo:
            aux+=1
        for event in pygame.event.get():
            # condicional en un evento para poder cerrar la ventana
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                laser=Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 25
                all_sprite_list.add(laser)
                laser_list.add(laser)
                sound.play()
        all_sprite_list.update()
        for laser in laser_list:
            meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
            for met in meteor_hit_list:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
                score +=1
            if laser.rect.y <-10:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)

        meta=15
        contador =Fuente.render("Tiempo: "+ str(TiempoRestante),0,(120,70,0))
        aciertos =Fuente.render("Faltantes: "+str(meta-score),0,(120,70,0))
        all_sprite_list.update()
        screen.blit(background, [0, 0])
        screen.blit(contador, (0, 0))
        resultado=meta-score
        screen.blit(aciertos, (0, 50))
        pygame.display.update()
        pygame.display.update()
        all_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(20)
        if TiempoRestante==0:
            pygame.quit()
            sys.exit()
        if resultado == 0:
            pygame.quit()
            sys.exit()





