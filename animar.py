import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Car import Carro
import semaforo
import contSem
import mamalon
import Carro
import json


def animar():
    # vl, ddd, x, vueltaa, y, angulo)

    car1 = Carro.Carro(100, 80, 0, 0, 90, 0)
    car2 = Carro.Carro(100, 75, 0, 170, 270, 1)
    car3 = Carro.Carro(100, 0, 0, 110, 0, 2)
    sem = semaforo.Sem(80, 40, 0, 2)
    sem2 = semaforo.Sem(75, 35, 1, 0)
    sem3 = semaforo.Sem(75, 40, 2, 1)
    sem4 = semaforo.Sem(80, 35, 3, 3)

    semaforos = [sem, sem2, sem3, sem4]
    sema0 = contSem.ContSem(0, "que te", semaforos)

    sem = semaforo.Sem(80, 115, 10, 2)
    sem2 = semaforo.Sem(75, 110, 11, 0)
    sem3 = semaforo.Sem(75, 115, 12, 1)
    sem4 = semaforo.Sem(80, 110, 13, 3)

    semaforos = [sem, sem2, sem3, sem4]
    sema1 = contSem.ContSem(1, "que te", semaforos)

    sem = semaforo.Sem(175, 115, 20, 2)
    sem2 = semaforo.Sem(170, 110, 21, 0)
    sem3 = semaforo.Sem(170, 115, 22, 1)
    sem4 = semaforo.Sem(175, 110, 23, 3)

    semaforos = [sem, sem2, sem3, sem4]
    sema2 = contSem.ContSem(2, "que te", semaforos)

    semM = [sema0, sema1, sema2]

    car = [car1, car2, car3]
    tabla = mamalon.table(car, semM)

    for i in range(1, 2400):
        tabla.regreso()

    points = tabla.imprime()

    todo = []
    l = 0
    for i in points[0]:
        pp = []
        for p in i:

            pp.append(p[0])
            pp.append(p[1])
            pp.append(p[2])
            pp.append(p[3])
            pp.append(p[4])
            pp.append(p[5])
        todo.append(pp)
        l = l + 1

    x = {
        "dicc":
            {
                "carros": {
                    "cantidad": len(points[0]),
                    "posiciones": {
                        "car1": {"lista": todo[0]},
                        "car2": {"lista": todo[1]},
                        "car3": {"lista": todo[2]},
                        "car4": {"lista": todo[3]},
                        "car5": {"lista": todo[4]},
                        "car6": {"lista": todo[5]},
                        "car7": {"lista": todo[6]},
                        "car8": {"lista": todo[7]},
                        "car9": {"lista": todo[8]},
                        "car10": {"lista": todo[9]},
                        "car11": {"lista": todo[10]},
                        "car12": {"lista": todo[11]},
                        "car13": {"lista": todo[12]},
                        "car14": {"lista": todo[13]},
                        "car15": {"lista": todo[14]},
                        "car16": {"lista": todo[15]},
                        "car17": {"lista": todo[16]},
                        "car18": {"lista": todo[17]},
                        "car19": {"lista": todo[18]},
                        "car20": {"lista": todo[19]},
                        "car21": {"lista": todo[20]},
                        "car22": {"lista": todo[21]},
                        "car23": {"lista": todo[22]},
                        "car24": {"lista": todo[23]},
                        "car25": {"lista": todo[24]},
                        "car26": {"lista": todo[25]},
                        "car27": {"lista": todo[26]},
                        "car28": {"lista": todo[27]},
                        "car29": {"lista": todo[28]},
                        "car30": {"lista": todo[29]},
                        "car31": {"lista": todo[30]},
                        "car32": {"lista": todo[31]}
                    }
                },
                "semaforos": {
                    "sem1": {
                        "id": 6001,
                        "estados": points[1][0][0][1]
                    },
                    "sem2": {
                        "id": 6002,
                        "estados": points[1][0][1][1]
                    },
                    "sem3": {
                        "id": 6003,
                        "estados": points[1][0][2][1]
                    },
                    "sem4": {
                        "id": 6004,
                        "estados": points[1][0][3][1]
                    },
                    "sem5": {
                        "id": 6005,
                        "estados": points[1][1][0][1]
                    },
                    "sem6": {
                        "id": 6006,
                        "estados": points[1][1][1][1]
                    },
                    "sem7": {
                        "id": 6007,
                        "estados": points[1][1][2][1]
                    },
                    "sem8": {
                        "id": 6008,
                        "estados": points[1][1][3][1]
                    },
                    "sem9": {
                        "id": 6009,
                        "estados": points[1][2][0][1]
                    },
                    "sem10": {
                        "id": 6010,
                        "estados": points[1][2][1][1]
                    },
                    "sem11": {
                        "id": 6011,
                        "estados": points[1][2][2][1]
                    },
                    "sem12": {
                        "id": 6012,
                        "estados": points[1][2][3][1]
                    }
                }
            }
    }

    jsonStr = json.dumps(x)
    return jsonStr
