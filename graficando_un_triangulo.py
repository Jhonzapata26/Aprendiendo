
from turtle import *

def triangulo():
    color('red', 'yellow')
    begin_fill()
    i = 0
    while i <3:
        fd(100)
        rt(-120)
        i += 1
    end_fill()
    done()
    

triangulo()

#ejemplo de triangulo con bucle for
from turtle import * 

def triangulo():
    color('red', 'yellow')
    begin_fill()
    i = 0
    for i in range (0,3):
        fd (100)
        rt (-120)
    end_fill ()
    done ()

triangulo()