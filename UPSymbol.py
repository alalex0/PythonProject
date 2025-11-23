# Проверить, что все слова в строке начинаются с заглавной буквы.

#s="Проверить, что все слова в строке Начинаются. с заглавной буквы."
s="Проверить, что либо Все Слова в Строке Начинаются. с Заглавной Буквы."


def Words(s):
    maket=str.maketrans({',':' ','.':''})
    words=s.translate(maket)
    words=words.split(' ')
    count=0
    count_word=0
    for i in words:
        i=i.replace(" ","")
        if(len(i)>2 and chekword(i)):
            UpAlfa(i)
            count_word+=1
            if UpAlfa(i):
                count+=1
    if count ==count_word:
            return print("Все слова начинаются с заглавной буквы")
    return print("Не все слова начинаются с заглавной буквы")

#смотрим верхний регистр
def UpAlfa(word):
    for i in word:
        if i.isalpha():
            return i.isupper()

#проверяем союзя
def chekword(word_chek):
    word=['что','или','либо']
    for i in word:
        if i ==word_chek:
            return False
    return True


Words(s)