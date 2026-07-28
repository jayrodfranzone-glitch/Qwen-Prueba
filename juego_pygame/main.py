import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Cuadrado Azul - WASD")

# Colores
AZUL = (0, 100, 255)
NEGRO = (0, 0, 0)

# Configuración del cuadrado
lado = 50
x = ANCHO // 2 - lado // 2
y = ALTO // 2 - lado // 2
velocidad = 5

# Reloj para controlar FPS
reloj = pygame.time.Clock()
FPS = 60

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Controlar FPS
    reloj.tick(FPS)
    
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Obtener estado de las teclas
    teclas = pygame.key.get_pressed()
    
    # Mover el cuadrado con WASD
    if teclas[pygame.K_w] and y > 0:
        y -= velocidad
    if teclas[pygame.K_s] and y < ALTO - lado:
        y += velocidad
    if teclas[pygame.K_a] and x > 0:
        x -= velocidad
    if teclas[pygame.K_d] and x < ANCHO - lado:
        x += velocidad
    
    # Dibujar fondo negro
    ventana.fill(NEGRO)
    
    # Dibujar el cuadrado azul
    pygame.draw.rect(ventana, AZUL, (x, y, lado, lado))
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
