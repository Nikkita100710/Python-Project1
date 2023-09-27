import json

# json_input = dict()
with open("g.json", "r") as file:
    json_input = json.load(file)
    print(json_input)
# json_input = {
#     "key1": {
#         "nested_key1": "nested_value1",
#         "nested_key2": "nested_value2"
#     },
#     "key2": {
#         "nested_key3": "nested_value3",
#         "nested_key4": "nested_value4"
#     }
# }
while True:
    user_select = input("введіть дію 1 додати 2 видалити 3 лист ")
    if user_select == "1":
        user_id = input("Введите ключ (user_id): ")
        user_key2 = input("Введите ключ (user_key2): ")
        user_key2_text = input("Введите значение (user_key2_text): ")
        # Проверяем, существует ли ключ user_id в словаре json_input
        if user_id not in json_input:
            json_input[user_id] = {}  # Если нет, создаем вложенный словарь
        json_input[user_id][user_key2] = user_key2_text
        user_exit = input("все? так 1 ні 2 ")
        if user_exit == "1":
            break
        else:
            continue

    elif user_select == "2":
        user_id = input("Введите ключ (user_id): ")
        if user_id not in json_input:
            print("Такого ключа нет")
        code = input("введіть код для очистки ")
        if code == "1234":
            json_cler = dict()
            json_input[user_id] = json_cler
        else:
            print("ключ не вірний ")
        user_exit = input("все? так 1 ні 2 ")
        if user_exit == "1":
            break
        else:
            continue


    elif user_select == "3":
        user_id = input("Введите ключ (user_id): ")
        if user_id not in json_input:
            print("помилка")
        print(json_input[user_id])
        user_exit = input("все? так 1 ні 2 ")
        if user_exit == "1":
            break
        else:
            continue

with open("g.json", "w") as file:
    json.dump(json_input, file, indent=4)
