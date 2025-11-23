# "Вычисление Функции Высшего Порядка.
# Посчитать факториал числа, вводимого с клавиатуры пользователем. Пользователь
# может ввести отрицательное число или буквенные символы. Алгоритм не должен использовать рекурсию."

try:
    numder=int(input())
    if(numder<0):
        print("Введите положительное число")
    n=10/numder
except (ValueError, ZeroDivisionError):
    print("Введите число")
else:
    multiplication=1
    for i in range(1,numder+1):
        multiplication *=i
    print(multiplication)
