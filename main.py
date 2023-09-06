persons = int(input("Введите количество посетителей (количество должно быть больше 0):"))
summa = 0

for i in range(persons):
    age = int(input("Введите возраст посетителя (возраст должен быть больше 0):"))
    if 1 <= age < 18:
        summa += 0
        print("Посетителям меньше 18 - проход бесплатно!")
        print("Ваша текущая сумма покупки:", summa, "рублей!")
    elif 18 <= age < 25:
        summa += 990
        print("Билет добавлен, стоимость 990 рублей")
        print("Ваша текущая сумма покупки:", summa, "рублей!")
    elif age >= 25:
        summa += 1390
        print("Билет добавлен, стоимость 1390 рублей")
        print("Ваша текущая сумма покупки:", summa, "рублей!")

if persons < 4:
    print("Ваша итоговая сумма к оплате: ", summa, "рублей!")
else: print("Ваша сумма к оплате с учетом скидки 10% за количество билетов: ", summa - summa // 10, "рублей!")