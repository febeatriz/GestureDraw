from utils.constants import FINGER_TIPS

def get_raised_fingers(landmarks):
    fingers = []
    if not landmarks:
        return [0, 0, 0, 0, 0]

    # Polegar (Lógica baseada na horizontal para mão direita/esquerda espelhada)
    if landmarks[FINGER_TIPS[0]][1] < landmarks[FINGER_TIPS[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Outros 4 dedos (Lógica baseada na vertical - Ponta acima da articulação anterior)
    for i in range(1, 5):
        if landmarks[FINGER_TIPS[i]][2] < landmarks[FINGER_TIPS[i] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
            
    return fingers