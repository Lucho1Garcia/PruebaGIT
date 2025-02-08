import pygame
from pygame.locals import *

# Inicializar Pygame
pygame.init()

# Configuración de pantalla y colores
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mario Bros - Juego Extendido")
CELESTE, BLANCO = (135, 206, 250), (255, 255, 255)
fuente = pygame.font.SysFont(None, 36)

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, ALTO - 100)
        self.vel_x = self.vel_y = 0
        self.velocidad = 6

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def mover(self, direccion):
        self.vel_x = direccion * self.velocidad

# Función de inicio del juego
def pantalla_inicio():
    start_button = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 50, 200, 50)

    running = True
    while running:
        pantalla.fill(CELESTE)
        pygame.draw.rect(pantalla, BLANCO, start_button)
        pantalla.blit(fuente.render("Start", True, (0, 0, 0)), (start_button.x + 60, start_button.y + 10))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            elif event.type == MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return True

# Función principal
def main():
    reloj = pygame.time.Clock()
    jugador = Jugador()

    if not pantalla_inicio():
        return

    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                running = False
            elif evento.type == KEYDOWN:
                if evento.key == K_a:
                    jugador.mover(-1)
                elif evento.key == K_d:
                    jugador.mover(1)
            elif evento.type == KEYUP:
                if evento.key in (K_a, K_d):
                    jugador.mover(0)

        pantalla.fill(CELESTE)
        jugador.update()
        pantalla.blit(jugador.image, jugador.rect)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
