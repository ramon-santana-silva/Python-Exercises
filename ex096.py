""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
retangular (largura e comprimento) e mostre a área do terreno."""

def area(l,c):
    ar=l*c
    return ar


a=float(input('Digite a largura: \n'))
b=float(input('digite o comprimento: \n'))
#area(a,b)
print(f'a area do retangulo é {area(a,b)}')