# "Незадачливый строитель.
# Напишите программу, которая должна определить, пройдет ли кирпич в отверстие. 
# Размеры отверстия (длина и высота) вводит пользователь. 
# Тоже самое касается габаритов кирпича, пользователь вводит в программу значения длины,
# ширины и высоты кирпича.
# Умный строитель умеет вращать кирпич и может пытаться пропихнуть кирпич в отверстие
# разными сторонами."

print("Введите длину отверстия")
lenght=int(input())
print("Введите ширину отверстия")
width=int(input())
print("Введите длину кирпича")
lenght_brick=int(input())
print("Введите ширину кирпича")
width_brick=int(input())
print("Введите высоту кирпича")
height_brick=int(input())



def check(lenght,width,lenght_brick,width_brick):
    if(lenght>=lenght_brick & width>=width_brick):
        return True
    else:return False
def process(lenght,width,lenght_brick,width_brick,height_brick):
    match(lenght,width,lenght_brick,width_brick,height_brick):
        case (lenght,width,lenght_brick,width_brick,height_brick) if(check(lenght,width,lenght_brick,width_brick)):return "кирпич пройдет"
        case (lenght,width,lenght_brick,width_brick,height_brick) if(check(lenght,width,lenght_brick,height_brick)):return "кирпич пройдет"
        case (lenght,width,lenght_brick,width_brick,height_brick) if(check(lenght,width,height_brick,lenght_brick)):return "кирпич пройдет"
        case (lenght,width,lenght_brick,width_brick,height_brick) if(check(lenght,width,height_brick,width_brick)):return "кирпич пройдет"
        case (lenght,width,lenght_brick,width_brick,height_brick) if(check(lenght,width,width_brick,height_brick)):return "кирпич пройдет"
        case (lenght,width,lenght_brick,width_brick,height_brick) if(check(lenght,width,width_brick,lenght_brick)):return "кирпич пройдет"
        case _:return "кирпич не пройдет"

print(process(lenght,width,lenght_brick,width_brick,height_brick))