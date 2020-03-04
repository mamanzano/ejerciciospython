# -*- coiding: utf-8 -*-

def imprime_nemeros(number):
    print('Ciclo for')
    for i in range(number):
        print(i + 1)
    
    j = 1
    print('ciclo while')
    while j < number:
        print(j)
        j += 1 

if __name__ == "__main__":
    number = int(input('Escribe un número: '))
    imprime_nemeros(number)

    #Se agrega un comentario para prueba otra