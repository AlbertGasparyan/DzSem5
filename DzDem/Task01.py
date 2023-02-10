# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


def step_num(a,b):
    if a==0 and b==0:
        return 1
    if b>0:
        a*=a
        step_num(a,b-1)
    return a

a=int(input('Enter number:'))
b=int(input('Enter number step:'))
res=step_num(a,b)
print(res)