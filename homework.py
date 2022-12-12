import json
with open("list.json", "r") as f:
    data_list = json.load(f)
    f.close()


plates_list_1 = set(data_list)
print("В вашем списке", len(plates_list_1), "уникальных значений")
user_value = input("Введите ваше значение: ").upper()

if user_value in data_list:
    print("Такое значение уже есть в списке")
else:
    print("Введенное значение отсутствует в списке")


new_list = []
for i in user_value:
    if i.isdigit():
        new_list.append(int(i))
print("Сумма всех чисел вашего значения равна: ", sum(new_list))