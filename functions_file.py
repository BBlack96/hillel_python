def unique_check(x):
    numbers_values = []
    str_values = []

    if len(x) > 8 or len(x) < 8:
        print("Ошибка! Вы ввели значение с некорректной длиной")
        return False

    for i in x:
        if i.isdigit():
            numbers_values.append(int(i))

    for i in x:
        if i.isalpha():
           str_values.append(str(i))
    return numbers_values[0:4], str_values[0:2]


def summ(x):
    new_list = []
    for i in x:
        if i.isdigit():
            new_list.append(int(i))
    return sum(new_list)