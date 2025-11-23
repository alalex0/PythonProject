# "Длинный и короткий
# Поиск в массиве целых чисел минимума и максимума значений.
# Нельзя использовать метод Arrays.sort и подобные ему. Нельзя сортировать массив значений."

import random

n=10
arr=[]
for i in range(n):
    arr.append(random.randint(1,n))
print(arr)
min_val=max_val=arr[0]
for i in range(len(arr)):
    if arr[i]<min_val:
        min_val=arr[i]
    elif arr[i]>max_val:
        max_val=arr[i]
print("Min=", min_val,"Max=", max_val)

