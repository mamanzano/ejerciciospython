  
import random

def run():
    number_found = False
    ramdom_number = random.randint(0, 30)

    while not number_found:
        number = int (input('Intenta un número entero: '))

        if number == ramdom_number:
            print('Felicidades encontraste el número')
            number_found = True
        elif ramdom_number < number:
                print('El número es más pequeño')
        else:
            print('El número es más grande')



if __name__ == "__main__":
    print('ENCUENTRA EL NÚMERO')
    run()