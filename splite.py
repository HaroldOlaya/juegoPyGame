import random
import pygame,sys

# menu inicial
print("1.empezar el juego")
print("2.finalizar")
opcion=input()
if opcion=="1":
    empezar=True
    while (empezar):
        print("ingrese")
        # inicializar el programa
        pygame.init()
        # definir los colores
        black = (0, 0, 0)
        white = (255, 255, 255)
        # contador de impactos
        score = 0


        # creacion de clases
        class Avion(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("avion.png").convert()
                self.image = pygame.transform.scale(self.image, (60,60))
                self.image.set_colorkey((255,255,255))
                self.rect = self.image.get_rect()


            def update(self):
                mouse_pos = pygame.mouse.get_pos()
                player.rect.x = mouse_pos[0]
                player.rect.y = mouse_pos[1]


        class Meteoro(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load(
                    "meteoro.png").convert()
                self.image.set_colorkey(white)
                self.rect = self.image.get_rect()

            def update(self):
                self.rect.y += 1
                if self.rect.y > 500:
                    self.rect.y = -20
                    self.rect.x = random.randrange(700)


        # configuracion de la ventana
        screen = pygame.display.set_mode((700, 500))
        # controlar los FPS
        clock = pygame.time.Clock()
        # eliminar la visivilidad del mouse
        pygame.mouse.set_visible(0)
        # fondo de pantalla
        background = pygame.image.load(
            "fondodebatalla.jpg").convert()
        gameover = pygame.image.load("gameover.png").convert()
        # creacion de las personas
        meteor_list = pygame.sprite.Group()
        all_sprite_list = pygame.sprite.Group()
        for i in range(30):
            m = Meteoro()
            m.rect.x = random.randrange(700)
            m.rect.y = random.randrange(100, 500)

            meteor_list.add(m)
            all_sprite_list.add(m)
        player = Avion()
        all_sprite_list.add(player)
        # bucle para que se mantenga la ventana abierta
        while (empezar):
            for event in pygame.event.get():
                # condicional en un evento para poder cerrar la ventana
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
            for meteorito in meteor_hit_list:
                score += 1
                print(score)
                if score > 4:
                    print("game over")
                    empezar=False

            all_sprite_list.update()
            screen.blit(background, [0, 0])
            all_sprite_list.draw(screen)
            pygame.display.flip()
            clock.tick(30)

else:
    print("saliendo")
