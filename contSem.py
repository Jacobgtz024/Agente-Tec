class ContSem():
    
    def __init__(self, id, carriles, semaforos):
        self.id = id
        self.carriles =  [[0, 5], [1, 6], [2, 2], [3, 1]]
        self.estados = [None, None, None, None]
        self.semaforos = semaforos
        self.cambio = 1
        self.prender = 99
        self.prendido = 99
        self.prenderdespues = 99
        self.turno = 0
        self.semid = 99
        self.count = 0


    def isParalelo(self, carril1, carril2):
        if carril1 == 0 and carril2 == 1:
            return True
        elif carril1 == 1 and carril2 == 0:
            return True
        elif carril1 == 2 and carril2 == 3:
            return True
        elif carril1 == 3 and carril2 == 2:
            return True
        else:
            return False

    def prenderSemaforo(self):
        safe = 0
        
        if self.cambio != 2:
                self.cambio = 1
        
        for i in self.semaforos:            
            """self.nada = 0
            if i.estado != 0 and self.cambio != 2:
                self.nada = 1
            """            
            if i.estado != 0 and self.cambio == 1:
                self.cambio = 0
                
                
            
        tiempo = -25
        for i in self.semaforos:    
            
            if i.tiempoRestante < tiempo and self.cambio == 1:
                tiempo = i.tiempoRestante
                safe = 1
                self.turno = 2
                self.semid = i.id - self.id *10
            
            if i.tiempoRestante < -10 and safe == 0 and self.cambio == 1:
                safe = 1
                if self.turno == 0:
                    self.turno = 1
                else:
                    self.turno = 0
    
        if self.cambio == 1:
        
            if self.turno == 2:
                self.turno = 0
                self.prender = self.semid
                self.cambio = 1
                self.prendido = self.semid
                calculoCarril = []
                for i in self.carriles:
                    calculoCarril.append(i[1])
                
                calculoCarril[self.prender] = 0
                
                carrilMax2 = calculoCarril.index(max(calculoCarril))
                carrosM2 = max(calculoCarril)

                
                if self.isParalelo(self.prender, carrilMax2):
                    self.prenderdespues = carrilMax2
                    self.cambio = 2
                    
                else:
                    self.prenderdespues = 99
                    self.cambio = 1
                
                
            else:
            
                calculoCarril = []
                for i in self.carriles:
                    calculoCarril.append(i[1])
                
                
                
                if self.turno == 0:    
                    carrilMax = calculoCarril.index(max(calculoCarril))
                    carrosM = max(calculoCarril)
                    calculoCarril[carrilMax] = 0
                else:
                    carrilMax = calculoCarril.index(min(calculoCarril))
                    carrosM = min(calculoCarril)
                    calculoCarril[carrilMax] = 9999            
                
                
                
                if self.turno == 0:
                    carrilMax2 = calculoCarril.index(max(calculoCarril))
                    carrosM2 = max(calculoCarril)
                else:
                    carrilMax2 = calculoCarril.index(min(calculoCarril))
                    carrosM2 = min(calculoCarril)
                
                #if carrosM != 0:
                    
                if self.isParalelo(carrilMax, carrilMax2):
                    if carrosM > carrosM2:
                        self.prender = carrilMax
                        self.prenderdespues = carrilMax2
                        self.prendido = carrilMax
                        self.cambio = 2
                    else:
                        self.prender = carrilMax2
                        self.prenderdespues = carrilMax
                        self.prendido = carrilMax2
                        self.cambio = 2
                else:
                    self.prender = carrilMax
                    self.prendido = carrilMax
                    self.prenderdespues = 99
                    self.cambio = 1
        
            if self.prender != 99:
                self.semaforos[self.prender].estado = 1
                if self.prenderdespues == 99:
                    self.semaforos[self.prender].fl = 0
                else:
                    self.semaforos[self.prender].fl = 1
                
                self.semaforos[self.prender].tiempoRestante = 10
                self.prender = 99
                
        elif self.cambio == 2:
            if self.prenderdespues != 99:
                if self.semaforos[self.prendido].tiempoRestante == 5:
                    self.semaforos[self.prenderdespues].estado = 1
                    self.semaforos[self.prenderdespues].fl = 2
                    self.semaforos[self.prenderdespues].tiempoRestante = 10
                    self.cambio = 1
                    self.prender = 99
                    self.prendido = 99
                    self.prenderdespues = 99
        
        for i in self.semaforos:
            i.update()
        
        j = 0
        for i in self.semaforos:
            self.estados[j] = i.estados
            j += 1
            
    def run(self, carriles):
        if self.count%(1/0.05) == 0:
            self.carriles =  carriles
            self.prenderSemaforo()
            j = 0
            for i in self.semaforos:
                self.estados[j] = i.estados
                j += 1
        else:
            for i in self.semaforos:
                i.updatenon()
        self.count += 1