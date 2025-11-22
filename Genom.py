# "Поиск геномных последовательностей.
# Задать массив целых чисел длиной 10 элементов.
# Заполнить его числами.
# Затем реализовать сортировку этой последовательности от меньшего к большему.
# Результат вывести в консоль компьютера.
# Нельзя использовать метод Arrays.sort и подобные ему."
import random

arr=[]
n=10

for i in range(n):
    arr.append(random.randint(1,10))
print(arr)
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            num=arr[j]
            arr[j]=arr[i]
            arr[i]=num
print(arr)