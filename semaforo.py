class Sem():
    def __init__(self, x, y, id, direccionS):
        self.id = id
        self.estado = 0
        self.tiempoRestante = 0
        self.x = x
        self.y = y
        self.fl = 0
        self.estados = [[self.id],[]]
        self.direccionS = direccionS
    def update(self):
        if self.fl == 0:
            if self.estado == 1:
                self.estado = 2
        elif self.fl == 1:
            if self.estado == 1 and self.tiempoRestante > 5:
                self.estado = 2
            elif self.estado == 2 and self.tiempoRestante <= 5:
                self.estado = 1
        elif self.fl == 2:
            if self.estado == 2 and self.tiempoRestante >= 5:
                self.estado = 1
            elif self.estado == 1 and self.tiempoRestante < 5:
                self.estado = 2
                
        self.estados[1].append(self.estado)
        self.tiempoRestante = self.tiempoRestante - 1
        if self.tiempoRestante <= 0:
            self.estado = 0
            self.fl = 0
        
        #print(self.id, self.estado, self.tiempoRestante)
        
    def updatenon(self):
        self.estados[1].append(self.estado)