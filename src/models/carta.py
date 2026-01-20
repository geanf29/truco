class Carta:
    NAIPES = ('Ouros', 'Espadas', 'Copas', 'Paus')
    
    FACES = ('4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3')

    def __init__(self, face, naipe):
        self.face = face
        self.naipe = naipe
        self.virada = False

    def __str__(self):
        return f"{self.face} de {self.naipe}" 
    def ismanilha(self, carta_vira):
        indice_face_vira = Carta.FACES.index(carta_vira.face) 
        indice_manilha = (indice_face_vira + 1) % len(Carta.FACES) 
        return self.face == Carta.FACES[indice_manilha]
    def valor(self, carta_vira):
        if self.virada:
            return -1 
        else:
            if self.ismanilha(carta_vira):
                return 20 + Carta.NAIPES.index(self.naipe) 
                return Carta.FACES.index(self.face)
