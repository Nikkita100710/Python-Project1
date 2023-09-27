import json

# Загрузка словаря из файла (если файл существует)
try:
    with open("g.json", "r") as file:
        json_input = json.load(file)
except FileNotFoundError:
    json_input = {}

while True:
    data_input = input("Введите данные в формате 'user_id|user_key2|user_key2_text': ")
    data_parts = data_input.split('|')

    if len(data_parts) != 3:
        print("Неверный формат данных. Пожалуйста, используйте формат 'user_id|user_key2|user_key2_text'.")
        continue

    user_id, user_key2, user_key2_text = data_parts

    # Проверяем, существует ли ключ user_id в словаре json_input
    if user_id not in json_input:
        json_input[user_id] = {}  # Если нет, создаем вложенный словарь

    json_input[user_id][user_key2] = user_key2_text

    user_exit = input("Завершить ввод? (да - 1, нет - 2): ")
    if user_exit == "1":
        break

# Записываем обновленный словарь в файл
with open("g.json", "w") as file:
    json.dump(json_input, file, indent=4)

print("Данные сохранены в файл g.json")
