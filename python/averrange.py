# -*- coiding: utf-8 -*-

def averrange_temps(temps):
    sum_temps = 0
    for temp in temps:
        sum_temps += float(temp)
    
    print('La suma de las temperaturas es: {}'.format(sum_temps))
    return sum_temps / len(temps)



if __name__ == "__main__":
    days_of_week = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    temps = list()
    for day in days_of_week:
        temps.append(int(input('Temperatura del día {}: '.format(day))))
    result = averrange_temps(temps)
    print('La lista de las temperaturas a promediar es: {}'.format(temps))
    print('El promedio de las temperaturas es: {}'.format(result))