import random
import math
import Carro


class table():
    def __init__(self, Carros, seM):
        self.Carros = Carros
        self.posiciones = [None] * len(self.Carros)
        self.numeroCarros = (len(self.Carros))
        self.sema = seM
        self.vuelta = 90
        self.count = 0
        self.carriles = [[0, 5], [1, 6], [2, 2], [3, 1]]

    def regreso(self):
        i = 0
        for sem in self.sema:
            sem.run(self.carriles)
        for car in self.Carros:

            if -5 > car.x or -5 > car.y or 290 < car.x or 200 < car.y:
                posicionesguardadas = self.posiciones[car.id]

                restantess = (4500-self.count)
                restantess = restantess - restantess % 1
                restantes = [9999, 9999, 0, 0, 0, 0]

                for j in range(0, int(restantess)):
                    posicionesguardadas.append(restantes)

                self.posiciones[car.id] = posicionesguardadas

                self.Carros.pop(i)
                continue

            if car.v != 0:
                v = car.v
            else:
                v = 1

            if car.superx == 1:
                powerx = 1
            else:
                powerx = -1
            if car.supery == 1:
                powery = 1
            else:
                powery = -1
            x = car.x * powerx
            y = car.y * powery

            # if powery == -1:
            #   print ("powery = -1", car.yy)
            card = math.sqrt((x**2) + (y**2))
            pointing = 0

            if car.angulo == 0 or car.angulo == 180:
                limite = car.y * powery
                usa = x
            else:
                limite = car.x * powerx
                usa = y

            distancia = 9999

            if usa >= 0:
                distancia = 9999
            else:
                distancia = 9999
            xx = math.cos(math.radians(car.angulo)) * 9999
            yy = math.sin(math.radians(car.angulo)) * 9999

            for car2 in self.Carros:

                x2 = car2.x * powerx
                y2 = car2.y * powery
                dis = math.sqrt((x2*x2)+(y2*y2))
                if usa >= 0:
                    limi = dis
                else:
                    limi = -dis

                if car.angulo == 0 or car.angulo == 180:
                    limi = y2
                    dis = x2
                elif car.angulo == 90 or car.angulo == 270:
                    limi = x2
                    dis = y2

                # and car2.x-car.x <= v*15:
                if usa < dis and dis <= distancia and car != car2 and -1 < limi - limite < 1 and car.direccionS == car2.direccionS:
                    pointing = 0
                    xx = x2*powerx - 3 * powerx
                    yy = y2*powery - 3 * powery
                    if car.v == 0:
                        distancia = dis
                    elif car.vy == 0:
                        distancia = car2.x - 3 * powerx
                    elif car.vx == 0:
                        distancia = car2.y - 3 * powery
                    elif car.angulo == 0 or car.angulo == 180:
                        distancia = car2.x - 3 * powerx
                    elif car.angulo == 90 or car.angulo == 270:
                        distancia = car2.y - 3 * powery
                    elif xx-x > yy-y:
                        distancia = car2.y - 3 * powery
                    else:
                        distancia = car2.x - 3 * powerx

            for sin in self.sema:
                for sem in sin.semaforos:

                    if car.angulo == 0 and -2 < sem.y-car.y < 2 or car.angulo == 180 and -2 < sem.y-car.y < 2:
                        car.y = sem.y
                    if car.angulo == 90 and -2 < sem.x-car.x < 2 or car.angulo == 270 and -2 < sem.x-car.x < 2:
                        car.x = sem.x

                    x2 = sem.x * powerx
                    y2 = sem.y * powery
                    dis = math.sqrt((x2*x2)+(y2*y2))
                    if usa >= 0:
                        limi = dis
                    else:
                        limi = -dis

                    if car.angulo == 0 or car.angulo == 180:
                        limi = y2
                        dis = x2
                    elif car.angulo == 90 or car.angulo == 270:
                        limi = x2
                        dis = y2
                        #print(car.trabajo, car.distancia, car.v2, car.direccionM, car.y, car.ddd)

                    if usa < dis and dis <= distancia and limi == limite and car.direccionS == sem.direccionS and not (dis-usa < 15 and car.v > 7):
                        if(sem.estado == 0):
                            pointing = 0
                            xx = x2*powerx
                            yy = y2*powery
                            if car.v == 0:
                                distancia = dis
                            elif car.vy == 0:
                                distancia = sem.x
                            elif car.vx == 0:
                                distancia = sem.y
                            elif car.angulo == 0 or car.angulo == 180:
                                distancia = sem.x
                            elif car.angulo == 90 or car.angulo == 270:
                                distancia = sem.y
                            elif xx-x > yy-y:
                                distancia = sem.y
                            else:
                                distancia = sem.x
                        elif sem.estado == 1:
                            if car.vueltaa == 1 and car.safeToTurn == 1 or car.vueltaa == 2 and car.safeToTurn == 1:
                                pointing = 0
                                xx = x2*powerx
                                yy = y2*powery
                                if car.v == 0:
                                    distancia = dis
                                elif car.vy == 0:
                                    distancia = sem.x
                                elif car.vx == 0:
                                    distancia = sem.y
                                elif car.angulo == 0 or car.angulo == 180:
                                    distancia = sem.x
                                elif car.angulo == 90 or car.angulo == 270:
                                    distancia = sem.y
                                elif xx-x > yy-y:
                                    distancia = sem.y
                                else:
                                    distancia = sem.x

                                if car.v < 0.05:
                                    car.safeToTurn = 0
                            else:
                                pointing = 1
                                xx = math.cos(math.radians(
                                    car.angulo)) * 9999 * powerx
                                yy = math.sin(math.radians(
                                    car.angulo)) * 9999 * powery
                                distancia = 9999
                        else:
                            if car.vueltaa == 1 and car.safeToTurn == 1 or car.vueltaa == 2 and car.safeToTurn == 1:
                                pointing = 0
                                xx = x2*powerx
                                yy = y2*powery
                                if car.v == 0:
                                    distancia = dis
                                elif car.vy == 0:
                                    distancia = sem.x
                                elif car.vx == 0:
                                    distancia = sem.y
                                elif car.angulo == 0 or car.angulo == 180:
                                    distancia = sem.x
                                elif car.angulo == 90 or car.angulo == 270:
                                    distancia = sem.y
                                elif xx-x > yy-y:
                                    distancia = sem.y
                                else:
                                    distancia = sem.x

                                if car.v < 0.05:
                                    car.safeToTurn = 0
                            else:
                                pointing = 2
                                xx = math.cos(math.radians(
                                    car.angulo)) * 9999 * powerx
                                yy = math.sin(math.radians(
                                    car.angulo)) * 9999 * powery
                                distancia = 9999

            if math.sqrt((dis - usa)**2) > 100:
                if math.sqrt((dis - usa)**2) > v*6:
                    xx = math.cos(math.radians(car.angulo)) * 9999
                    yy = math.sin(math.radians(car.angulo)) * 9999

                    if usa >= 0:
                        distancia = 9999  # maybe
                    else:
                        distancia = 9999 * -1  # maybe

            if distancia == 9999 and usa < 0:
                distancia = 9999 * -1

            # if self.count%100 == 0:
             #   print(car.x,car.y)

            ddd = distancia

            car.update(ddd, xx, yy, pointing)
            self.posiciones[car.id] = car.Carro_corre()
            i += 1

        self.count = self.count + 1

        if self.count % 150 == 0 and self.count != 0:

            vl = 10
            vueltaa = random.randint(0, 2)

            cosas = [[vl, 80, vueltaa, 0, 90, self.numeroCarros],
                     [vl, 75, vueltaa, 170, 270, self.numeroCarros],
                     [vl, 0, vueltaa, 110, 0, self.numeroCarros],
                     [vl, 250, vueltaa, 115, 180, self.numeroCarros],
                     [vl, 175, vueltaa, 45, 90, self.numeroCarros],
                     [vl, 170, vueltaa, 165, 270, self.numeroCarros]]

            select = random.randint(0, 5)

            carNuevo = Carro.Carro(cosas[select][0], cosas[select][1], cosas[select]
                                   [2], cosas[select][3], cosas[select][4], cosas[select][5])
            posicionN = [[9999, 9999, 0, 9999, 0, 0]] * (self.count + 2)
            carNuevo.posiciones = posicionN
            self.numeroCarros = self.numeroCarros + 1
            self.Carros.append(carNuevo)
            self.posiciones.append(posicionN)

        return self.posiciones

    def imprime(self):
        obsemaforos = []
        carros = self.posiciones
        # print(carros)
        for sem in self.sema:
            obsemaforos.append(sem.estados)
        objetoRegreso = [carros, obsemaforos]
        return objetoRegreso
