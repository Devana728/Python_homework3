#Напишите программу, которая найдёт произведение пар 
# чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

#*Пример:*

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]#

from random import randint
N = int(input("Введите число N: "))
mass = []

for i in range(N):
    mass.append(randint(0, N))
print(mass)
mass1 = []
mult=0
for  i  in range(0, (N)//2, 1) :   
   
    mult = mass [i]*mass[N-1-i]
    mass1.append(mult)
if N % 2 !=0 :
    mass1.append(mass[N//2]**2)    

print (mass1)     
#print(f'произведение пар элементов списка : {sum}')
