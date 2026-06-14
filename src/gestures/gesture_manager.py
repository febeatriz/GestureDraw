class GestureManager:
    @staticmethod
    def get_mode(fingers):
        # Modo Desenho: [0, 1, 0, 0, 0]
        if fingers == [0, 1, 0, 0, 0]:
            return "DRAWING"
        
        # Modo Apagar: [0, 0, 0, 0, 1]
        elif fingers == [0, 0, 0, 0, 1]:
            return "ERASING"
        
        # Modo Neutro: [1, 1, 1, 1, 1]
        elif fingers == [1, 1, 1, 1, 1]:
            return "NEUTRAL"
            
        return "NONE"