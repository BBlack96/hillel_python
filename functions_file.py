def unique_check(x):
    numbers_values = []
    str_values = []

    if len(x) > 8 or len(x) < 8:
        print("Ошибка! Вы ввели значение с некорректной длиной")
        return False

    for i in x:
        if i.isdigit():
            numbers_values.append(int(i))
    print("Ваше значение содержит следующие цифры: ", numbers_values[0:4])

    for i in x:
        if i.isalpha():
            str_values.append(str(i))
    print("Ваше значение содержит следующие буквы: ", str_values[0:2])


def summ(x):
    new_list = []
    for i in x:
        if i.isdigit():
            new_list.append(int(i))
    print("Сумма всех чисел вашего значения равна: ", sum(new_list))
    return sum(new_list)
