import json
from functions_file import unique_check
from functions_file import summ

with open("list.json", "r") as f:
    data_list = json.load(f)

plates_list_1 = set(data_list)
print("В вашем списке", len(plates_list_1), "уникальных значений")

user_value = input("Введите ваше значение: ").upper()
x = user_value
plates_list_1 = set(data_list)
if user_value in plates_list_1:
    print("Такое значение уже есть в списке")
else:
    print("Введенное значение отсутствует в списке")

unique_check(x)

summ(x)
