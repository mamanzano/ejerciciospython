# -*- coiding: utf-8 -*-

def binary_serch (numbers, number_to_find, low, high):

    if low > high:
        return False

    mid = int((low + high) / 2)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_serch(numbers, number_to_find, low, mid - 1)
    else:
        return binary_serch(numbers, number_to_find, mid + 1, high)



if __name__ == "__main__":
    numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]
    number_to_find = int(input('Ingresa un número: '))
    
    resul = binary_serch(numbers, number_to_find, 0, len(numbers) - 1)
    if resul :
        print('El número {} sí esta en la lista'.format(number_to_find))
    else:
        print('El número {} no esta en la lista'.format(number_to_find))
