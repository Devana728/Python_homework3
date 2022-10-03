#Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным
#  значением дробной части элементов.

#*Пример:*

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

mass = [1.1, 1.2, 3.1, 5.1, 10.01]
mass1 =[]
for i in range(len(mass)):
    
    mass1.append(mass[i]%1)
maximum = max(mass1)
minimum = min(mass1)

sum = str(maximum-minimum)
print(sum[:sum.find('.')+3])