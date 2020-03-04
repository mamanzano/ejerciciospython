# -*- coding: utf-8 -*-

def promedio_cal(calificaciones):

    suma_calificaciones = 0

    for key in calificaciones:
        calificaciones[key] = float(input('Calificación de {}: '.format(key)))

    for values in calificaciones.values():
        suma_calificaciones = suma_calificaciones + values

    return suma_calificaciones / len(calificaciones)


if __name__ == "__main__":
    calificaciones = {}
    calificaciones['Matematicas'] = 0
    calificaciones['Programación'] = 0
    calificaciones['Base de Datos'] = 0

    promedio = promedio_cal(calificaciones)

    print('Promedio: {}'.format(promedio))