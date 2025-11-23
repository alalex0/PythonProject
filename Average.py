# "Средний по больнице
# Разработать функцию, в которую передается в качестве аргументов массив типа float. 
# Функция должна возвращать среднее арифметическое элементов массива.
# Если размер массива - нуль, то среднее арифметическое должно быть также нуль."

import random

print("Введите размер массива")
n=int(input())
arr=[]

for i in range(n):
    arr.append(random.uniform(0,10))

def Average(arr):
    sum=0
    if(len(arr)==0):
        return 0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum/len(arr)  
print(Average(arr))


