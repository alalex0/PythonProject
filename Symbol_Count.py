# "Анализ Креативности Текста.
# Подсчитать количество слов и букв в строке. Слово - это последовательность символов, 
# разделенных одним или несколькими символами-разделителями. Буква - это символ, не являющийся
# разеделителем. 
# Разделители слов: пробел, табуляция, перевод каретки, знаки препинания. Полный список: "",.!?:;()""
# Нельзя использовать для разбора строки класс StringTokenizer, String.split(), substring() и 
# подобные им.
# В программе нельзя использовать вложенные циклы. Так же не рекомендуется использовать метод 
# String.indexOf().
# Программа не должна создавать дополнительные строки сравнимого размера с введенной строкой.
# Программа должна проходить тест на следующих данных: 
# 1) ""    xxx,    xx x   x""
# 2) ""xxxxxxx""
# 3) ""xxxxxxx.    ""
# 4) ""xxx,xxxx""
# 5) ""xxx,xxxx""
# 6) ""........""
# 7) ""... xxx...  ""
# 8) """" - пустая строка"

s="Программа не должна создавать дополнительные строки сравнимого размера с введенной строкой."


def isDelimetr(ch):
    return ch == ' ' or ch == '\t' or ch == '\n' or   ch == '\r' or ch == ',' or ch == '.' or ch == '!' or ch == '?' or ch == ':' or ch == ';'or ch == '('or ch == ')'or ch == '"'
def Wordcount(s):
    if s is None and not s:
        return 0
    count=0
    isWord=False

    for i in s:
        if isDelimetr(i):
            if isWord:
                isWord=False
        else:
            if isWord ==False:
                count+=1
                isWord=True
    return count
def Lettercount(s):
    if s is None and not s:
        return 0
    count=0
    for i in s:
        if isDelimetr(i)==False:
            count+=1
    return count
    
countWord=Wordcount(s)
countLetter=Lettercount(s)
print("Количество слов", countWord,"Количество букв", countLetter)