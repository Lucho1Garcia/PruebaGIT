import pygame
from pygame.locals import *
import random
import os
import sys

# Inicializar Pygame y el mezclador de audio
pygame.init()
pygame.mixer.init()

# Configuración de pantalla y colores
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mario Bros - Juego Extendido")
CELESTE, BLANCO, AZUL, AMARILLO, ROJO, VERDE, GRIS_CLARO = (135, 206, 250), (255, 255, 255), (0, 0, 255), (255, 255, 0), (255, 0, 0), (0, 255, 0), (200, 200, 200)
fuente = pygame.font.SysFont(None, 36)

# Configuración inicial de volumen y brillo
volumen_actual = 0.25
opacidad_brillo = 0  # Opacidad del filtro de brillo (0: brillo máximo, 128: brillo mínimo)

# Obtener la ruta actual y luego acceder a la carpeta de imágenes
carpeta_imagenes = os.path.join(os.path.dirname(__file__), "Juego Mario Bros", "Archivos para grafica")

# Cargar imágenes de fondo y elementos del juego
try:
    fondo_inicio = pygame.image.load(os.path.join(carpeta_imagenes, "fondoinicio.png")).convert()
    fondo_cielo = pygame.image.load(os.path.join(carpeta_imagenes, "cielo.png")).convert()
    cesped_imagen = pygame.image.load(os.path.join(carpeta_imagenes, "cesped.png")).convert_alpha()
    nube_imagen = pygame.image.load(os.path.join(carpeta_imagenes, "nube.png")).convert_alpha()
    npc_base_image = pygame.image.load(os.path.join(carpeta_imagenes, "npc.png")).convert_alpha()
    powerup_image = pygame.image.load(os.path.join(carpeta_imagenes, "powerup.png")).convert_alpha()
except pygame.error as e:
    print(f"No se pudo cargar una de las imágenes: {e}")
    pygame.quit()
    sys.exit()

# Funciones para ajustar volumen y brillo
def ajustar_volumen(cambio):
    global volumen_actual
    volumen_actual = max(0, min(1, volumen_actual + cambio))
    pygame.mixer.music.set_volume(volumen_actual)

def ajustar_brillo(cambio):
    global opacidad_brillo
    opacidad_brillo = max(0, min(128, opacidad_brillo + cambio))

# Función para pantalla de inicio
def pantalla_inicio():
    start_button = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 50, 200, 50)
    options_button = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 20, 200, 50)
    
    # Reproducir la canción de inicio
    pygame.mixer.music.load(os.path.join(carpeta_imagenes, "cancioninicial.mp3"))
    pygame.mixer.music.play(-1)  # Reproducir en bucle

    running = True
    while running:
        pantalla.blit(fondo_inicio, (0, 0))
        pantalla.blit(fuente.render("Inicio", True, BLANCO), (ANCHO // 2 - 60, ALTO // 2 - 150))
        pygame.draw.rect(pantalla, GRIS_CLARO, start_button)
        pygame.draw.rect(pantalla, GRIS_CLARO, options_button)
        pantalla.blit(fuente.render("Start", True, BLANCO), (start_button.x + 60, start_button.y + 10))
        pantalla.blit(fuente.render("Options", True, BLANCO), (options_button.x + 50, options_button.y + 10))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            elif event.type == MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    # Detener la canción de inicio y comenzar con la música del juego
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join(carpeta_imagenes, "musica.mp3"))
                    pygame.mixer.music.play(-1)  # Reproducir música del juego en bucle
                    return True
                elif options_button.collidepoint(event.pos):
                    mostrar_opciones_menu()

def mostrar_opciones_menu():
    running = True
    boton_volumen_up = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 40, 200, 40)
    boton_volumen_down = pygame.Rect(ANCHO // 2 - 100, ALTO // 2, 200, 40)
    boton_brillo_up = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 40, 200, 40)
    boton_brillo_down = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 80, 200, 40)
    boton_cerrar_opciones = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 120, 200, 40)
    
    while running:
        pantalla.fill(GRIS_CLARO)
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_volumen_up)
        pantalla.blit(fuente.render("Subir Volumen", True, BLANCO), (boton_volumen_up.x + 10, boton_volumen_up.y + 10))
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_volumen_down)
        pantalla.blit(fuente.render("Bajar Volumen", True, BLANCO), (boton_volumen_down.x + 10, boton_volumen_down.y + 10))
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_brillo_up)
        pantalla.blit(fuente.render("Subir Brillo", True, BLANCO), (boton_brillo_up.x + 10, boton_brillo_up.y + 10))
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_brillo_down)
        pantalla.blit(fuente.render("Bajar Brillo", True, BLANCO), (boton_brillo_down.x + 10, boton_brillo_down.y + 10))
        pygame.draw.rect(pantalla, GRIS_CLARO, boton_cerrar_opciones)
        pantalla.blit(fuente.render("Cerrar Opciones", True, BLANCO), (boton_cerrar_opciones.x + 10, boton_cerrar_opciones.y + 10))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            elif event.type == MOUSEBUTTONDOWN:
                if boton_volumen_up.collidepoint(event.pos):
                    ajustar_volumen(0.1)
                elif boton_volumen_down.collidepoint(event.pos):
                    ajustar_volumen(-0.1)
                elif boton_brillo_up.collidepoint(event.pos):
                    ajustar_brillo(-10)
                elif boton_brillo_down.collidepoint(event.pos):
                    ajustar_brillo(10)
                elif boton_cerrar_opciones.collidepoint(event.pos):
                    return True

# Clase PowerUp
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(powerup_image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))

# Clase Nube (decorativa)
class Nube(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, velocidad):
        super().__init__()
        self.image = pygame.transform.scale(nube_imagen, (int(ancho * 1.5), int(alto * 1.5)))
        self.image.set_alpha(150)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidad = velocidad

    def update(self):
        self.rect.x += self.velocidad
        if self.rect.x > ANCHO:
            self.rect.x = -self.rect.width

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_original = pygame.image.load(os.path.join(carpeta_imagenes, "mario.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image_original, (120, 180))
        self.rect = self.image.get_rect(topleft=(50, ALTO - 180))
        self.vel_x = self.vel_y = 0
        self.salto, self.vidas, self.monedas, self.cayendo = False, 3, 0, False
        self.velocidad_base = 6
        self.velocidad_actual = self.velocidad_base
        self.tiempo_powerup = 0
        self.energia = 100

    def update(self, plataformas, huecos):
        if self.cayendo:
            self.vel_y += 2
        else:
            self.vel_y += 1

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if not self.cayendo:
            colisiones = pygame.sprite.spritecollide(self, plataformas, False)
            if colisiones:
                for plataforma in colisiones:
                    if self.vel_y > 0:
                        self.rect.bottom = plataforma.rect.top
                        self.vel_y = 0
                        self.salto = False

        if not self.cayendo and pygame.sprite.spritecollide(self, huecos, False):
            self.caer()

        if self.tiempo_powerup > 0:
            self.tiempo_powerup -= 1
            if self.tiempo_powerup == 0:
                self.velocidad_actual = self.velocidad_base

    def mover(self, direccion):
        if not self.cayendo:
            self.vel_x = direccion * self.velocidad_actual

    def saltar(self):
        if not self.salto and not self.cayendo:
            self.vel_y, self.salto = -20, True

    def caer(self):
        self.cayendo = True
        self.vel_x = 0

    def morir(self):
        self.vidas -= 1
        self.energia = max(0, self.energia - 20)  # Reduce energía solo cuando muere
        self.rect.topleft = (50, ALTO - 180)
        self.vel_y = 0
        self.cayendo = False

    def recolectar_moneda(self):
        self.monedas += 1

    def activar_powerup(self):
        self.velocidad_actual = self.velocidad_base * 1.5
        self.tiempo_powerup = 300
        self.energia = min(100, self.energia + 20)

# Clase NPC
class NPC(pygame.sprite.Sprite):
    def __init__(self, limite_izq, limite_der, velocidad, colorize=None):
        super().__init__()
        new_width = int(120 * 0.8)
        new_height = int(180 * 0.8)
        self.image_original = pygame.transform.scale(npc_base_image, (new_width, new_height))
        
        if colorize:
            self.image = self.image_original.copy()
            self.image.fill(colorize, special_flags=pygame.BLEND_RGBA_MULT)
        else:
            self.image = self.image_original
        self.rect = self.image.get_rect(midbottom=(limite_der, ALTO - 40))
        self.limite_izq = limite_izq
        self.limite_der = limite_der
        self.velocidad = -abs(velocidad)
        self.alive = True  # Estado del NPC

    def update(self):
        if self.alive:
            self.rect.x += self.velocidad
            if self.rect.left <= self.limite_izq:
                self.rect.left = self.limite_izq
                self.velocidad = abs(self.velocidad)
            elif self.rect.right >= self.limite_der:
                self.rect.right = self.limite_der
                self.velocidad = -abs(self.velocidad)

    def handle_collision_with_player(self, player):
        if self.alive and player.rect.colliderect(self.rect):
            if player.rect.bottom <= self.rect.top + 10:
                self.alive = False
                player.vel_y = -10  # Rebote hacia arriba
            else:
                if player.rect.right > self.rect.left and player.rect.left < self.rect.right:
                    player.rect.x -= player.vel_x

# Clase Plataforma usando imagen de césped
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, movil=False, velocidad=0, direccion="horizontal"):
        super().__init__()
        self.image = pygame.transform.scale(cesped_imagen, (ancho, alto))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.movil, self.velocidad, self.direccion = movil, velocidad, direccion

    def update(self):
        if self.movil:
            if self.direccion == "horizontal":
                self.rect.x += self.velocidad
                if not 200 < self.rect.x < 1000: self.velocidad *= -1
            else:
                self.rect.y += self.velocidad
                if not 200 < self.rect.y < 600: self.velocidad *= -1

# Clase Hueco
class Hueco(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft=(x, y))

# Clase Moneda
class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_original = pygame.image.load("Juego Mario Bros/Archivos para grafica/moneda.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_original, (60, 60))
        self.rect = self.image.get_rect(topleft=(x, y))

# Clase Nivel
class Nivel:
    def __init__(self, jugador, plataformas, huecos, monedas, nubes, powerups=None, npc=None):
        self.jugador, self.npc = jugador, npc
        self.plataformas, self.huecos, self.monedas, self.nubes = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        for p in plataformas: self.plataformas.add(Plataforma(*p))
        for h in huecos: self.huecos.add(Hueco(*h))
        for m in monedas: self.monedas.add(Moneda(*m))
        for n in nubes: self.nubes.add(Nube(*n))
        if powerups:
            for pwr in powerups:
                self.powerups.add(PowerUp(*pwr))

    def update(self):
        self.plataformas.update()
        self.monedas.update()
        self.nubes.update()
        self.jugador.update(self.plataformas, self.huecos)
        if self.npc:
            self.npc.update()
            self.npc.handle_collision_with_player(self.jugador)

    def dibujar(self, pantalla):
        self.nubes.draw(pantalla)
        self.plataformas.draw(pantalla)
        self.huecos.draw(pantalla)
        self.monedas.draw(pantalla)
        self.powerups.draw(pantalla)
        pantalla.blit(self.jugador.image, self.jugador.rect)
        if self.npc and self.npc.alive:
            pantalla.blit(self.npc.image, self.npc.rect)

    def verificar_colisiones(self):
        if self.jugador.rect.y > ALTO:
            self.jugador.morir()
        
        colisiones_monedas = pygame.sprite.spritecollide(self.jugador, self.monedas, True)
        for moneda in colisiones_monedas:
            self.jugador.recolectar_moneda()

        colisiones_powerups = pygame.sprite.spritecollide(self.jugador, self.powerups, True)
        for powerup in colisiones_powerups:
            self.jugador.activar_powerup()

def generar_elementos_aleatorios(jugador):
    plataformas_aleatorias = []
    huecos_aleatorios = []
    
    for _ in range(random.randint(1, 3)):  # Genera entre 1 y 3 huecos aleatorios
        x = random.randint(200, ANCHO - 300)
        ancho = random.randint(100, 150)
        huecos_aleatorios.append((x, ALTO - 40, ancho, 40))
        
    for _ in range(random.randint(1, 2)):  # Genera entre 1 y 2 plataformas adicionales
        x = random.randint(100, ANCHO - 300)
        y = random.randint(300, ALTO - 200)
        ancho = random.randint(100, 200)
        plataformas_aleatorias.append((x, y, ancho, 20, True, random.choice([2, 3]), random.choice(["horizontal", "vertical"])))


    return plataformas_aleatorias, huecos_aleatorios

# Definir los niveles
def crear_niveles(jugador):
    nubes_nivel1 = [(50, 100, 100, 50, 1), (500, 150, 120, 60, 1), (900, 120, 80, 40, 1)]
    nubes_nivel2 = [(100, 120, 150, 70, 1), (700, 130, 100, 50, 1)]
    nubes_nivel3 = [(150, 120, 150, 70, 1), (500, 100, 100, 50, 1)]
    nubes_nivel4 = [(200, 120, 120, 60, 1), (500, 150, 100, 50, 1)]
    nubes_nivel5 = [(50, 50, 150, 80, 1), (700, 130, 100, 50, 1), (1050, 100, 120, 70, 1)]
    nubes_nivel6 = [(75, 80, 150, 60, 1), (600, 130, 130, 55, 1)]
    nubes_nivel7 = [(120, 90, 140, 50, 1), (400, 100, 120, 60, 1)]
    nubes_nivel8 = [(60, 60, 150, 70, 1), (600, 120, 110, 60, 1)]
    
    # Nivel adicional
    nubes_nivel9 = [(150, 100, 100, 50, 1), (700, 130, 100, 50, 1), (1100, 120, 120, 60, 1)]

    npc_nivel1 = NPC(0, ANCHO, 3)
    npc_nivel2 = NPC(0, ANCHO, 3, colorize=VERDE)
    npc_nivel3 = NPC(0, ANCHO, 3, colorize=ROJO)
    npc_nivel4 = NPC(0, ANCHO, 3, colorize=AMARILLO)
    npc_nivel5 = NPC(0, ANCHO, 3, colorize=GRIS_CLARO)
    npc_nivel6 = NPC(0, ANCHO, 3, colorize=AZUL)
    npc_nivel7 = NPC(0, ANCHO, 3, colorize=ROJO)
    npc_nivel8 = NPC(0, ANCHO, 3, colorize=AZUL)
    
    # NPC adicional para el nivel 9
    npc_nivel9 = NPC(0, ANCHO, 3, colorize=AMARILLO)

    powerups_nivel1 = [(600, ALTO - 140)]
    powerups_nivel2 = [(700, ALTO - 140)]
    powerups_nivel5 = [(800, ALTO - 140)]
    
    plataformas_aleatorias1, huecos_aleatorios1 = generar_elementos_aleatorios(jugador)
    plataformas_aleatorias2, huecos_aleatorios2 = generar_elementos_aleatorios(jugador)
    plataformas_aleatorias9, huecos_aleatorios9 = generar_elementos_aleatorios(jugador)

    return [
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40)] + plataformas_aleatorias1, huecos_aleatorios1, [(400, ALTO - 120), (700, ALTO - 120)], nubes_nivel1, powerups=powerups_nivel1, npc=npc_nivel1),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (300, 500, 200, 20, True, 3, "horizontal")] + plataformas_aleatorias2, huecos_aleatorios2, [(550, ALTO - 120), (850, ALTO - 120)], nubes_nivel2, powerups=powerups_nivel2, npc=npc_nivel2),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (400, 500, 150, 20, True, 2, "horizontal")], [(250, ALTO - 40, 100, 40), (650, ALTO - 40, 150, 40)], [(300, ALTO - 120), (700, ALTO - 120), (1000, ALTO - 120)], nubes_nivel3, npc=npc_nivel3),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (800, 500, 150, 20, True, 2, "horizontal")], [(600, ALTO - 40, 100, 40), (1000, ALTO - 40, 150, 40)], [(650, ALTO - 120), (900, ALTO - 120), (1150, ALTO - 120)], nubes_nivel4, npc=npc_nivel4),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (300, 400, 200, 20, True, 4, "horizontal")], [(500, ALTO - 40, 150, 40), (1050, ALTO - 40, 100, 40)], [(450, ALTO - 120), (750, ALTO - 120), (1150, ALTO - 120)], nubes_nivel5, powerups=powerups_nivel5, npc=npc_nivel5),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (500, 450, 170, 20, True, 3, "horizontal")], [(550, ALTO - 40, 150, 40), (950, ALTO - 40, 100, 40)], [(600, ALTO - 120), (800, ALTO - 120)], nubes_nivel6, npc=npc_nivel6),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (400, 470, 160, 20, True, 3, "horizontal")], [(550, ALTO - 40, 100, 40), (900, ALTO - 40, 150, 40)], [(500, ALTO - 120), (850, ALTO - 120)], nubes_nivel7, npc=npc_nivel7),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (600, 500, 150, 20, True, 2, "horizontal")], [(350, ALTO - 40, 100, 40), (900, ALTO - 40, 150, 40)], [(500, ALTO - 120), (750, ALTO - 120), (1000, ALTO - 120)], nubes_nivel8, npc=npc_nivel8),
        Nivel(jugador, [(0, ALTO - 40, ANCHO, 40), (600, 450, 150, 20, True, 2, "horizontal")], [(350, ALTO - 40, 100, 40), (900, ALTO - 40, 150, 40)], [(500, ALTO - 120), (700, ALTO - 120), (1000, ALTO - 120)], nubes_nivel9, npc=npc_nivel9)
    ]

# Función principal
def main():
    reloj = pygame.time.Clock()
    jugador = Jugador()
    if not pantalla_inicio():
        return
    niveles = crear_niveles(jugador)
    nivel_actual = 0
    en_juego = True
    pausado = False
    mostrar_opciones = False
    boton_pausa_rect = pygame.Rect(10, 40, 100, 40)
    barra_energia_rect = pygame.Rect(10, 90, 100, 10)
    boton_opciones_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 100, 200, 40)
    boton_volumen_up = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 40, 200, 40)
    boton_volumen_down = pygame.Rect(ANCHO // 2 - 100, ALTO // 2, 200, 40)
    boton_brillo_up = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 40, 200, 40)
    boton_brillo_down = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 80, 200, 40)
    boton_cerrar_opciones = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 120, 200, 40)

    def toggle_pausa():
        nonlocal pausado
        pausado = not pausado
        if pausado:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    while en_juego:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                en_juego = False
            elif evento.type == KEYDOWN:
                if evento.key == K_a and not pausado:
                    jugador.mover(-1)
                elif evento.key == K_d and not pausado:
                    jugador.mover(1)
                elif evento.key == K_w and not pausado:
                    jugador.saltar()
                elif evento.key == K_ESCAPE:
                    if mostrar_opciones:
                        mostrar_opciones = False
                    else:
                        toggle_pausa()
            elif evento.type == KEYUP and evento.key in (K_a, K_d):
                jugador.mover(0)
            elif evento.type == MOUSEBUTTONDOWN:
                if boton_pausa_rect.collidepoint(evento.pos):
                    toggle_pausa()
                if pausado and boton_opciones_rect.collidepoint(evento.pos):
                    mostrar_opciones = True
                if mostrar_opciones:
                    if boton_volumen_up.collidepoint(evento.pos):
                        ajustar_volumen(0.1)
                    elif boton_volumen_down.collidepoint(evento.pos):
                        ajustar_volumen(-0.1)
                    elif boton_brillo_up.collidepoint(evento.pos):
                        ajustar_brillo(-10)
                    elif boton_brillo_down.collidepoint(evento.pos):
                        ajustar_brillo(10)
                    elif boton_cerrar_opciones.collidepoint(evento.pos):
                        mostrar_opciones = False

        pantalla.blit(fondo_cielo, (0, 0))
        nivel = niveles[nivel_actual]

        if not pausado:
            nivel.update()
            nivel.verificar_colisiones()

            if jugador.rect.x > ANCHO - jugador.rect.width and nivel_actual < len(niveles) - 1:
                nivel_actual += 1
                jugador.rect.x = 50

            elif jugador.rect.x < 0 and nivel_actual > 0:
                nivel_actual -= 1
                jugador.rect.x = ANCHO - jugador.rect.width

        nivel.dibujar(pantalla)

        pygame.draw.rect(pantalla, GRIS_CLARO, boton_pausa_rect)
        pantalla.blit(fuente.render("Pausar" if not pausado else "Reanudar", True, BLANCO), (boton_pausa_rect.x + 10, boton_pausa_rect.y + 10))

        pygame.draw.rect(pantalla, ROJO, barra_energia_rect)
        pygame.draw.rect(pantalla, VERDE, (10, 90, int(jugador.energia), 10))

        pantalla.blit(fuente.render(f"Monedas: {jugador.monedas}", True, BLANCO), (10, 10))

        if pausado:
            pygame.draw.rect(pantalla, GRIS_CLARO, boton_opciones_rect)
            pantalla.blit(fuente.render("Opciones", True, BLANCO), (boton_opciones_rect.x + 10, boton_opciones_rect.y + 10))

        if mostrar_opciones:
            pygame.draw.rect(pantalla, GRIS_CLARO, boton_volumen_up)
            pantalla.blit(fuente.render("Subir Volumen", True, BLANCO), (boton_volumen_up.x + 10, boton_volumen_up.y + 10))
            pygame.draw.rect(pantalla, GRIS_CLARO, boton_volumen_down)
            pantalla.blit(fuente.render("Bajar Volumen", True, BLANCO), (boton_volumen_down.x + 10, boton_volumen_down.y + 10))
            pygame.draw.rect(pantalla, GRIS_CLARO, boton_brillo_up)
            pantalla.blit(fuente.render("Subir Brillo", True, BLANCO), (boton_brillo_up.x + 10, boton_brillo_up.y + 10))
            pygame.draw.rect(pantalla, GRIS_CLARO, boton_brillo_down)
            pantalla.blit(fuente.render("Bajar Brillo", True, BLANCO), (boton_brillo_down.x + 10, boton_brillo_down.y + 10))
            pygame.draw.rect(pantalla, GRIS_CLARO, boton_cerrar_opciones)
            pantalla.blit(fuente.render("Cerrar Opciones", True, BLANCO), (boton_cerrar_opciones.x + 10, boton_cerrar_opciones.y + 10))

        brillo_overlay = pygame.Surface((ANCHO, ALTO))
        brillo_overlay.fill(BLANCO)
        brillo_overlay.set_alpha(opacidad_brillo)
        pantalla.blit(brillo_overlay, (0, 0))

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
