import math

class Carro():
    def __init__(self, vl, x, vueltaa, y, angulo, id):
        self.id = id
        self.step = 0
        self.safeToTurn = 1
        self.v = 0
        self.vt = 0
        self.vx = 0
        self.vy = 0
        self.vl = vl
        self.vls = vl
        self.x = x
        self.y = y
        self.ta = 3
        self.ax = 0
        self.v2 = 0
        self.start_lag = 0 
        self.posiciones = []
        ddd = 9999
        self.ddd = ddd
        self.di = ddd
        self.df = ddd
        self.evitar = 0
        self.aver = 0
        self.distancia = 0
        self.tiempo_control = 0.05
        self.angulo = angulo
        self.ddd_pas = ddd
        self.xx = 9999
        self.yy = 0
        self.trabajo = x
        self.pointing = 0
        self.vueltaa = vueltaa
        self.pasosG = 0
        if self.vueltaa == 1:
            self.pasosG = 80
        elif self.vueltaa == 2:
            self.pasosG = 120
        self.vuelta = self.pasosG
        self.superx = 1
        self.supery = 1
        self.direccionM = 1
        self.skin = 0
        
        if self.angulo == 0:
            self.direccionS = 0
        elif self.angulo == 90:
            self.direccionS = 1
        elif self.angulo == 180:
            self.direccionS = 2
        elif self.angulo == 270:
            self.direccionS = 3
        elif self.angulo == 360:
            self.direccionS = 0
    
    def angulos(self):
        if 0 <= self.angulo <= 90:
            self.superx = 1
            self.supery = 1
        elif self.angulo <= 180:
            self.superx = -1
            self.supery = 1
        elif self.angulo <= 270:
            self.superx = -1
            self.supery = -1
        else:
            self.superx = 1
            self.supery = -1
    
    def aceleracion(self, vl, ta):
        self.angulos()
        self.x = self.x + self.vx*self.tiempo_control#*self.superx
        self.y = self.y + self.vy*self.tiempo_control#*self.supery
        self.ax = (vl - self.v)/(ta)
        self.v = self.v + self.ax*self.tiempo_control
        self.vx = math.cos(math.radians(self.angulo)) * self.v
        self.vy = math.sin(math.radians(self.angulo)) * self.v
        
    
    def check_distance(self):
        if(self.ddd_pas == 9999 or self.ddd == 9999 or self.ddd_pas == -9999 or self.ddd == -9999):
            self.distancia = -100
            self.v2 = self.v
            self.aver = (self.vt + ((self.vl - self.vt)/self.ta*self.tiempo_control))*self.tiempo_control
        else:
            self.di = (self.ddd_pas - self.trabajo + self.vt * self.direccionM ) * self.direccionM
            self.df = (self.ddd - self.trabajo) * self.direccionM
            self.v2 = round(((self.vt) + ((self.df - self.di)/self.tiempo_control) * 1)) * self.direccionM            
            self.v2 = (self.v2 - (self.v2 / 15))
            self.distancia = (self.vt * self.ta) - (self.v2*self.ta)
            self.aver = (self.vt + ((self.vl - self.vt)/self.ta*self.tiempo_control))*self.tiempo_control
            
            if(self.vueltaa == 33):
                print("AAAAA", self.x)
                print(self.distancia * self.direccionM)
                print(self.ddd  - self.trabajo - self.aver)
                print( self.ddd * self.direccionM - self.trabajo * self.direccionM )
        
 
    def decide(self):
        if  1 <= self.vuelta < self.pasosG and self.vueltaa == 1 or (self.vueltaa == 1 and self.v < 0.01 and self.pointing == 2) and self.ddd == 9999 or self.ddd == -9999 and (self.vueltaa == 1 and self.v < 0.01 and self.pointing == 2):
            if self.vuelta%2 == 0:
                self.vl = 6
                self.turnleft()
            self.vuelta = self.vuelta-1
            #print(self.x, self.y, self.vuelta, self.v, self.ddd, self.pointing)
        elif 1 <= self.vuelta < self.pasosG and self.vueltaa == 2 or (self.vueltaa == 2 and self.v < 0.01 and self.pointing != 0) and self.ddd == 9999 or self.ddd == -9999 and (self.vueltaa == 2 and self.v < 0.01 and self.pointing != 0):
            if self.vuelta%2 == 0:
                self.vl = 10
                self.turnright()
            self.vuelta = self.vuelta-1
            #print(self.x, self.y, self.vuelta, self.v, self.ddd, self.pointing)
            
 
    def movimiento(self):
        self.decide()
        self.check_distance()
        ta = self.ta
        if self.evitar == 999 or self.distancia < (self.ddd - self.trabajo - self.aver)*self.direccionM and self.evitar == 0 and self.ddd * self.direccionM - self.trabajo * self.direccionM > 0:
            if self.start_lag < 7:
                ta = self.ta + 14 - 2*self.start_lag
                self.start_lag += 1
            self.aceleracion(self.vl, ta)
            vl = self.vl
        else:
            self.evitar = 0
            vl = self.v2
            self.aceleracion(vl, ta)

        
    
    def reset(self):
        self.evitar = 999
    
    def turnleft(self):
        #print(self.x, self.y)
        self.angulo = self.angulo + 2.25
        #print(self.x)
        if self.angulo > 360:
            self.angulo = self.angulo - 360
    
    def turnright(self):
        
        
        self.angulo = self.angulo - 1.5
        if self.angulo < 0:
            self.angulo = 360 + self.angulo
    
    def update(self, ddd, xx, yy, pointing):
        self.xx = xx
        self.yy = yy
        self.pointing = pointing
        trabaja = math.cos(math.radians(self.angulo)) * 1        
        if trabaja == 1 or trabaja == -1:
            self.trabajo = self.x
            self.vt = self.vx
            if trabaja == 1:
                self.direccionM = 1
            if trabaja == -1:
                self.direccionM = -1
        elif trabaja < 0.0001:
            self.trabajo = self.y
            self.vt = self.vy
            trabaja = round(math.sin(math.radians(self.angulo)) * 1)  

            if trabaja == 1:
                self.direccionM = 1
            else:
                self.direccionM = -1
                #print("Si se lo que ago")
        if ddd != 9999 and ddd !=  -9999:
            if self.v != 0:
                ddd = ddd - ddd % self.v
            ddd = ddd - self.v/1 - 5*self.direccionM
            
        if(self.ddd_pas == 9999 or self.ddd_pas == -9999):
            self.ddd_pas = ddd
        else:   
            self.ddd_pas = self.ddd
        self.ddd = ddd
        
        if(self.ddd == 9999 and self.ddd_pas == 9999 or self.ddd == -9999 and self.ddd_pas == -9999):
            self.evitar = 0
            if self.start_lag > 7:
                self.start_lag = 0
        
        if self.vuelta == 0:
            self.vuelta = self.pasosG
            self.vl = self.vls
            self.safeToTurn = 1
            
        if self.angulo == 0:
            self.direccionS = 0
        elif self.angulo == 90:
            self.direccionS = 1
        elif self.angulo == 180:
            self.direccionS = 2
        elif self.angulo == 270:
            self.direccionS = 3
        elif self.angulo == 360:
            self.direccionS = 0
            
    def Carro_corre(self):
        #if self.vueltaa == 2:
            #print(self.ddd, self.pointing, self.angulo, self.x, self.y, self.supery)
        
        self.movimiento()
        

        if self.step %1 == 0:
            self.posiciones.append([self.x, self.y, self.id, self.skin, self.vl, self.vuelta])
        self.step = self.step + 1
        return self.posiciones
    
    