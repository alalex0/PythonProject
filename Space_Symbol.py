# Посчитать количество пробельных символов в строке.

s="Пример строки с пробелами"
count_str=s.count(' ')
print("Количество пробелов ", count_str)

count_str=0
for i in s:
    if(i==' '):
        count_str+=1
print("Количество пробелов ", count_str)
