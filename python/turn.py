# -*- coding: utf-8 -*-

import turtle 

angule = 90

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_squre(dave)

    turtle.mainloop()

def make_squre(dave):
    length = int(input('Tamaño del cuadrado: '))
    
    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(angule)
    

if __name__ == "__main__":
    main()