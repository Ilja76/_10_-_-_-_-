from math import *

#1. Напишите программу, печатающую столбик строк такого вида:
#1 0 0 0 0 0 0 0 0
#0 2 0 0 0 0 0 0 0
#0 0 3 0 0 0 0 0 0
#0 0 0 4 0 0 0 0 0
#0 0 0 0 5 0 0 0 0
#0 0 0 0 0 6 0 0 0
#0 0 0 0 0 0 7 0 0
#0 0 0 0 0 0 0 8 0
#0 0 0 0 0 0 0 0 9

#print("Ulesanne 1")

#for r in range(9):
#    for c in range (9):
#        if r==c:
#            print(r+1, end=" ")
#        else:
#            print(0, end=" ")
#    print()

#print()



#2. Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
#print("Ulesanne 2")

#for n in range(10,20):
#    print(n**2)


#3.В бригаде, работающей на уборке сена, имеется N сенокосилок.
#Первая сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем предыдущая.
#Сколько часов проработала вся бригада?
#print("Ulesanne 3")

#N=int(input("Kogus: "))
#m=int(input("Min: "))
#m*=60
#summa=0
#for i in range(1,N):
#    summa+=m
#    m+=10
#print(summa/60)


#4. Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.

#from random import *
#print("Ulesanne 4")
#for i in range(1,11):
#    arv1=randint(-100,100)
#    arv2=randint(-100,100)
#    if arv1>arv2:
#        print(f"{arv1} on suurem kui {arv2}")
#    elif arv2>arv1:
#        print(f"{arv2} on suurem kui {arv1}")
#    else:
#        print(f"{arv1},{arv2} on vordsed")



#5.Напишите программу, печатающую столбик таблицу умножения такого вида:
#2*1=2
#2*2=4
#2*3=6
#2*4=8
#2*5=10
#2*6=12
#2*7=14
#2*8=16
#2*9=18

#print("Ulesanne 5")
#n = int(input('Sisesta n: '))
#for i in range(1, 11):
#    print(f'{n} * {i} = {n*i}')


#6.Напишите программу, печатающую столбик строк такого вида:
# x 0 0 0 0 0 0 0 0
# x x 0 0 0 0 0 0 0
# x 0 x 0 0 0 0 0 0
# x 0 0 x 0 0 0 0 0
# x 0 0 0 x 0 0 0 0
# x 0 0 0 0 x 0 0 0
# x 0 0 0 0 0 x 0 0
# x 0 0 0 0 0 0 x 0
# x 0 0 0 0 0 0 0 x

#print("Ulesanne 6")
#for r in range(9):
#    for c in range (9):
#        if r==c:
#            print("x", end=" ")
#        elif c==0:
#            print("x", end=" ")
#        else:
#            print(0, end=" ")
#    print()

#print()


#7.  Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =
#2,5 см) для значений длин от 1 до 20 дюймов.

#print("Ulesanne 7")
#for i in range(0, 20):
#    print(i, "сm = ",i * 2.5, "inch")



#8. Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.

#print("Ulesanne 8")
#n = int(input("number: "))
#r = 0
#for i in range(1, n + 1):
#    r += i
#print(r)

#9. Найти сумму чисел от 100 до 200, кратных 17.

#print("Ulesanne 9")
#a= 0
#for i in range(100,200):
#    if(i % 17 == 0):
#        a+= i
#print(a)

