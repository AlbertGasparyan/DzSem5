from random import randint

FirstList=int(input('Enter len first list:'))
SecondList=int(input('Enter len second list:'))



list1=[randint(0,11) for el in range(FirstList)]
list2=[randint(0,11) for el in range(SecondList)]

list1_set=list(set(list1))
list2_set=list(set(list2))
print(list1_set,'<--list1 list2-->',list2_set)

result = list(filter(lambda elem: elem in list1_set, list2_set))

print(f'Общие элементы списка = {result}')