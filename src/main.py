import cv2
import numpy as np
from hand_tracking.detector import HandDetector
from hand_tracking.finger_utils import get_raised_fingers
from gestures.gesture_manager import GestureManager
from drawing.canvas import Canvas
from drawing.color_selector import draw_color_selector, get_pinched_color
from utils.constants import WIDTH, HEIGHT, COLOR_BRUSH, COLOR_ERASER, BRUSH_THICKNESS, ERASER_THICKNESS, COLOR_CURSOR

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)

    detector = HandDetector()
    canvas = Canvas()
    xp, yp = 0, 0  # Coordenadas anteriores
    current_brush_color = COLOR_BRUSH

    while True:
        success, frame = cap.read()
        if not success: break
        
        frame = cv2.flip(frame, 1)
        
        # 1. Detectar Mão
        frame = detector.find_hands(frame)
        landmarks = detector.get_landmarks(frame)
        
        if landmarks:
            # Pegar ponta do indicador (ID 8) e mindinho (ID 20)
            x1, y1 = landmarks[8][1:]
            x_thumb, y_thumb = landmarks[4][1:]
            x5, y5 = landmarks[20][1:]

            selected_color = get_pinched_color((x_thumb, y_thumb), (x1, y1))
            if selected_color:
                current_brush_color = selected_color
                xp, yp = 0, 0
            
            # 2. Identificar Gestos
            fingers = get_raised_fingers(landmarks)
            mode = GestureManager.get_mode(fingers)
            
            # 3. Executar Ações
            if selected_color:
                cv2.circle(frame, (x1, y1), 18, current_brush_color, cv2.FILLED)

            elif mode == "DRAWING":
                cv2.circle(frame, (x1, y1), 15, current_brush_color, cv2.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1
                
                canvas.draw_line((xp, yp), (x1, y1), current_brush_color, BRUSH_THICKNESS)
                xp, yp = x1, y1

            elif mode == "ERASING":
                cv2.circle(frame, (x5, y5), 25, (255, 255, 255), cv2.FILLED) # Cursor borracha
                if xp == 0 and yp == 0:
                    xp, yp = x5, y5
                
                canvas.draw_line((xp, yp), (x5, y5), COLOR_ERASER, ERASER_THICKNESS)
                xp, yp = x5, y5
            
            else:
                xp, yp = 0, 0  # Reseta para não criar linhas contínuas ao voltar a desenhar

        # 4. Combinar Canvas com o Frame da Webcam
        img_gray = cv2.cvtColor(canvas.get_canvas(), cv2.COLOR_BGR2GRAY)
        _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
        img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
        
        # Onde houver desenho no canvas, "limpa" o frame da webcam e adiciona a cor
        frame = cv2.bitwise_and(frame, img_inv)
        frame = cv2.bitwise_or(frame, canvas.get_canvas())
        frame = draw_color_selector(frame, current_brush_color)

        cv2.imshow("AirDraw - Painel Principal", frame)
        
        if cv2.waitKey(1) & 0xFF == 27: # ESC para sair
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
