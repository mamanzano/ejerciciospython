# -*- coding: utf-8 -*-

one_colombian_money = 179.18

def run():
    print('Calculadora de divisas')
    print('Convierte pesos méxicanos a pesos colombianos')
    print('')

    ammoutn = float(input('Pesos Méxicanos: '))

    result = foreign_exchange_calculator(ammoutn)
    print('${} pesos méxicanos son ${} pesos colombianos'.format(ammoutn,result))
    print('')

def foreign_exchange_calculator(ammoutn):
    colombians_money = ammoutn * one_colombian_money
    return colombians_money



if __name__ == "__main__":
    run()