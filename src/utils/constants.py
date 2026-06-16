import cv2

# Configurações de Tela
WIDTH, HEIGHT = 1280, 720

# Cores (BGR)
COLOR_BRUSH = (247, 5, 157)   # Azul
COLOR_ERASER = (0, 0, 0)    # Preto (para o canvas)
COLOR_CURSOR = (0, 255, 0)  # Verde

# Espessuras
BRUSH_THICKNESS = 10
ERASER_THICKNESS = 50

# Mapeamento de Dedos (MediaPipe Index)
FINGER_TIPS = [4, 8, 12, 16, 20]