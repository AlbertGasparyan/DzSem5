# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a,b):
    if b>0:
        a=sum(a+1,b-1)
    return a
a=int(input('Enter number one:'))
b=int(input('Enter number two:'))
res=sum(a,b)
print(res)