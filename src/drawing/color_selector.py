import math

from utils.constants import (
    COLOR_PALETTE,
    PALETTE_SWATCH_GAP,
    PALETTE_SWATCH_SIZE,
    PALETTE_X,
    PALETTE_Y,
    PINCH_THRESHOLD,
)


def _swatch_rect(index):
    x1 = PALETTE_X + index * (PALETTE_SWATCH_SIZE + PALETTE_SWATCH_GAP)
    y1 = PALETTE_Y
    x2 = x1 + PALETTE_SWATCH_SIZE
    y2 = y1 + PALETTE_SWATCH_SIZE
    return x1, y1, x2, y2


def _point_inside_rect(point, rect):
    x, y = point
    x1, y1, x2, y2 = rect
    return x1 <= x <= x2 and y1 <= y <= y2


def get_pinched_color(thumb_tip, index_tip):
    distance = math.dist(thumb_tip, index_tip)
    if distance > PINCH_THRESHOLD:
        return None

    pinch_center = (
        int((thumb_tip[0] + index_tip[0]) / 2),
        int((thumb_tip[1] + index_tip[1]) / 2),
    )

    for i, (_, color) in enumerate(COLOR_PALETTE):
        rect = _swatch_rect(i)
        if _point_inside_rect(pinch_center, rect) or _point_inside_rect(index_tip, rect):
            return color

    return None


def draw_color_selector(frame, selected_color):
    import cv2

    for i, (name, color) in enumerate(COLOR_PALETTE):
        x1, y1, x2, y2 = _swatch_rect(i)
        border_color = (255, 255, 255) if color == selected_color else (40, 40, 40)
        border_thickness = 4 if color == selected_color else 2

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, cv2.FILLED)
        cv2.rectangle(frame, (x1, y1), (x2, y2), border_color, border_thickness)
        cv2.putText(
            frame,
            name,
            (x1, y2 + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

    return frame
