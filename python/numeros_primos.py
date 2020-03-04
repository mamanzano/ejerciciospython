# -*- coding: utf-8 -*-

def run():
    print('NUMEROS PRIMOS')
    num = int(input('Escribe un número entero '))

    result = is_prime(num)

    if result :
        print('El número {} es primo'.format(num))
    else:
        print('El número {} no es primo'.format(num))


def is_prime(num):
    if(num < 1):
        return False
    elif(num == 2):
        return True
    elif(num > 2 and num % 2 == 0):
        return False
    else:
        for i in range(3, num):
            if(num % i == 0):
                return False
    return True

if __name__ == '__main__':
    run()
    