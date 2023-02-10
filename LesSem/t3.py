from random import randint

def replace(n):
    for el in range(len(n)):
        if n[el]==4 or n[el]==5:
            n[el]=1
    return n

enter = int(input("Enter your grade for replace:"))

grade=[randint(1,5) for el in range(enter)]
print(f'Оценки Василия до изменения --> {grade}')

res=replace(grade)
print(f'Оценки Василия после изменения --> {res}')






