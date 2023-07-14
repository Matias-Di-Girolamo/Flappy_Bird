import os

WIDTH = 576
HEIGHT = 1024
# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (64, 64, 64)

# ruta del directorio actual del script y carga de archivos
script_dir = os.path.dirname(os.path.abspath(__file__))
font_dir = os.path.join(script_dir, "assets", "04B_19.TTF")
background_dir = os.path.join(script_dir, "assets", "background-dia.png")
base_dir = os.path.join(script_dir, "assets", "base.png")
pipe_dir = os.path.join(script_dir, "assets", "pipe-green.png")
message_dir = os.path.join(script_dir, "assets", "message.png")
flap_sound_dir = os.path.join(script_dir, "sounds", "sfx_wing.wav")
death_sound_dir = os.path.join(script_dir, "sounds", "sfx_hit.wav")
score_sound_dir = os.path.join(script_dir, "sounds", "sfx_point.wav")
