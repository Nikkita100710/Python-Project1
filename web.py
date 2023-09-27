import requests
from config import TOKEN_BOT as TOKEN


# BOT_TOKEN = "6529360532:AAErdH8EpcdzUk_RqAoUTgtZTHAGHmgNQVo"
# ADMINS = [1070559942]
# IP = "localhost"
# Замените "ВАШ_ТОКЕН_БОТА" на фактический токен вашего бота
# TOKEN = "ВАШ_ТОКЕН_БОТА"
# TOKEN = "AAErdH8EpcdzUk_RqAoUTgtZTHAGHmgNQVo"
# Замените <chat_id> на ID чата или пользователя, которому вы хотите отправить сообщение
## chat_id = "1255505205"
chat_id = "6529360532"
# Замените "Hello, World!" на текст вашего сообщения
text = "Як ваші справи??"
# text = "Привіт групі юних пайтоністів!"
# text = "Марк Охріменко у Вас навчається? Передавайте йому полум'яний привіт"
# Создаем URL для отправки сообщения
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
# Параметры запроса (chat_id и text)
params = {"chat_id": chat_id, "text": text}

# Отправляем POST-запрос к Telegram API
response = requests.post(url, data=params)

# Проверяем, получен ли успешный ответ
if response.status_code == 200:
    print("Сообщение успешно отправлено!")
else:
    print("Ошибка при отправке сообщения:", response.status_code, response.text)
