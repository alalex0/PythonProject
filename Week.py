# "Вспомнить все.
# По введенному номеру дня недели вывести название дня недели,
# используя оператор множественного выбора (switch).
# Нумерация дней недели начинается с 1 – понедельник, 2 — вторник и т. д."

def process(day):
    match day:
        case "1":return "Понедельник"
        case "2":return "Вторник"
        case "3":return "Среда"
        case "4":return "Четверг"
        case "5":return "Пятница"
        case "6":return "Суббота"
        case "7":return "Воскресенье"
day=str(input())
print(process(day))