import numpy as np
import cv2
from utils.constants import WIDTH, HEIGHT

class Canvas:
    def __init__(self):
        # Canvas preto (onde desenharemos com cores)
        self.buffer = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    def draw_line(self, pt1, pt2, color, thickness):
        cv2.line(self.buffer, pt1, pt2, color, thickness)

    def clear(self):
        self.buffer = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    def get_canvas(self):
        return self.buffer
