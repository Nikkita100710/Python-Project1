
from config_scoll import factori
from config_scoll import parc
from config_scoll import history
"""
   InlineKeyboardMarkup та InlineKeyboardButton - ці класи відповідають за створення та відображення
інтерактивних (інлайн) клавіатур. Вони дозволяють створювати кнопки з різними діями, які користувач
може натискати під час взаємодії з ботом.
"""
#import random
from aiogram import Bot, Dispatcher, types
# Bot, Dispatcher, та types - ці класи та об'єкти з бібліотеки aiogram дозволяють
# спілкуватися з API Telegram та обробляти різні типи повідомлень та подій. Bot - це об'єкт бота,
# Dispatcher - обробник подій, а types - класи для створення та роботи з типами повідомлень
# та клавіатурами.

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# ReplyKeyboardMarkup та KeyboardButton - ці класи дозволяють створювати та відображати клавіатури
# з кнопками, які користувач може використовувати для взаємодії з ботом. Вони дозволяють створювати
# клавіатури для звичайних повідомлень.
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# LoggingMiddleware - цей клас відповідає за логування подій та дій, які відбуваються в боті.
# Він допомагає відстежувати та аналізувати події для відладки та моніторингу роботи бота.

# Ініціалізація бота та диспетчера
bot = Bot(token="6363138289:AAEqWC7jTMGIQ1ocaPozyRvBlUOSkodrdys")
dp = Dispatcher(bot)
"""
dp = Dispatcher(bot) -  об'єкт диспетчера (Dispatcher) - пов'язуємо його з ботом. 
 Диспетчер відповідає за обробку та маршрутизацію повідомлень,
які надходять від користувачів бота.
"""

# Middleware для логування
logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)
"""
  logging_middleware = LoggingMiddleware() - Цей рядок створює об'єкт middleware для логування 
(LoggingMiddleware). Middleware - це проміжний шар, який може обробляти і логувати дані перед тим,
 як вони досягнуть обраних обробників повідомлень. 
 В даному випадку, middleware для логування буде використовуватися для запису логів, 
 що допоможе відстежувати роботу бота та виявляти можливі помилки.

  dp.middleware.setup(logging_middleware) - Ця лінія додає middleware для логування до диспетчера 
(Dispatcher). Тепер будь-які повідомлення та події, які обробляються ботом, можуть бути записані
в журналі для подальшого аналізу та налагодження.
"""

# Клавіатура з кнопками "CODE" і "DECODE"
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ℹ️ історія"),
            KeyboardButton(text="🏭 підприемства"),
            KeyboardButton(text="🌳 парки та архітектура"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)





# Обробник команди /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("""👋 Привіт! \n🤴 Я гід бот я розповім багато цікавого про наше місто 
    \n🐍 Оберіть дію:""", reply_markup=keyboard)



"""
  @dp.message_handler(commands=['start']) - Цей рядок встановлює обробник повідомлень для команди
/start. Коли користувач відправляє цю команду боту, він активує цей обробник.

  async def start_command(message: types.Message): - Ця функція start_command буде викликана,
коли користувач відправить команду /start. Вона приймає параметр message, 
який містить інформацію про отримане повідомлення від користувача.

  await message.reply("👋 Привіт! \n🤴 Я Цезар бот!\n🐍 Оберіть дію:", reply_markup=keyboard) 
- Цей рядок відправляє відповідь користувачу за допомогою методу reply об'єкта message.
У відповіді вказано текст, який буде відображатися користувачеві. 
Також, reply_markup=keyboard вказує на те, що відповідь має містити клавіатуру (keyboard),
яка відображається для користувача для подальшої взаємодії.
"""


# Обробник команди /help
@dp.message_handler(commands=['factory'])
async def help_command(message: types.Message):
    await message.reply(factori)


# Обробник команди /about
@dp.message_handler(commands=['park'])
async def about_command(message: types.Message):
    await message.reply(parc)


@dp.message_handler(commands=['history'])
async def send_presentation(message: types.Message):
        await message.reply(history)




# Обробник текстового повідомлення після натискання кнопки "CODE"
"""
 lambda message: message.text перевіряє, чи повідомлення має текстовий контент, тобто чи відсутній або не є 
порожнім текстовим рядком.

 Потім, за допомогою message.text.split()[0].isdigit(), перевіряється, чи перший слово (або слово, яке є першим, якщо 
текст розділено пробілами) є числом. isdigit() - це метод для рядків, який повертає True, якщо рядок складається лише 
з цифр і False в іншому випадку. Якщо перший символ (слово) повідомлення є числом, то умова виконується, 
і обробник не спрацьовує.

 Також, через and message.text not in ["ℹ️ About", "🆘 Help"] перевіряється, щоб текст повідомлення не був одним 
з двох варіантів: "ℹ️ About" або "🆘 Help". Якщо текст повідомлення є одним з цих двох варіантів,
обробник також не спрацьовує.
"""


@dp.message_handler(lambda message: message.text == "ℹ️ історія")
async def about_button(message: types.Message):
    await message.reply(history)


# Обробник кнопки "Help"
@dp.message_handler(lambda message: message.text == "🏭 підприемства")
async def help_button(message: types.Message):
    await message.reply(factori)


# Обробник кнопки "Presentation"
# @dp.message_handler(lambda message: message.text == "Presentation")
# async def presentation_button(message: types.Message):
#     await message.reply(presentation_text)
@dp.message_handler(lambda message: message.text == "🌳 парки та архітектура")
async def presentation_button(message: types.Message):
    await message.reply(parc)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
