from config import TOKEN_BOT as TOKEN
from config import presentation_text
from config import about_
from config import commands
from config import UKRAINIAN_ALPHABET

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # inline
"""
   InlineKeyboardMarkup та InlineKeyboardButton - ці класи відповідають за створення та відображення
інтерактивних (інлайн) клавіатур. Вони дозволяють створювати кнопки з різними діями, які користувач
може натискати під час взаємодії з ботом.
"""
import random
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
bot = Bot(token=TOKEN)
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
            KeyboardButton(text="🔐 CODE"),
            KeyboardButton(text="🔓 DECODE"),
        ],
        [
            KeyboardButton(text="ℹ️ About"),
            KeyboardButton(text="🆘 Help"),
            KeyboardButton(text="🐍 Presentation"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

def coder(inp_str):
    code_caesar = random.randint(1, 30)  # Генеруємо випадковий код
    coder_inp_str = ""
    for char in inp_str:
        if char in UKRAINIAN_ALPHABET:
            index = UKRAINIAN_ALPHABET.index(char)
            new_index = index + code_caesar
            if new_index >= len(UKRAINIAN_ALPHABET):
                new_index -= len(UKRAINIAN_ALPHABET)
            coder_inp_str += UKRAINIAN_ALPHABET[new_index]
        else:
            coder_inp_str += char

    return code_caesar, coder_inp_str


# Розшифрування тексту за допомогою алгоритму Цезаря
def decoder(code_caesar, inp_str):
    decoded_text = ""
    for char in inp_str:
        if char in UKRAINIAN_ALPHABET:
            index = UKRAINIAN_ALPHABET.index(char)
            new_index = index - code_caesar
            if new_index < 0:
                new_index += len(UKRAINIAN_ALPHABET)
            decoded_char = UKRAINIAN_ALPHABET[new_index]
            decoded_text += decoded_char
        else:
            decoded_text += char

    return decoded_text


# Обробник команди /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("👋 Привіт! \n🤴 Я Цезар бот!\n🐍 Оберіть дію:", reply_markup=keyboard)

    with open('Go-ITeens.jpg', 'rb') as photo:
        await message.reply_photo(photo=types.InputFile(photo))
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
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    help_text = "\n".join(commands)
    await message.reply(f"Ласкаво просимо до нашого бота Цезаря!\nКоманди:\n\n{help_text}")


# Обробник команди /about
@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    await message.reply(about_)


@dp.message_handler(commands=['presentation'])
async def send_presentation(message: types.Message):
    for i in range(0, len(presentation_text), 4096):
        await message.reply(presentation_text[i:i + 4096])


# Обробник кнопки "CODE"
@dp.message_handler(lambda message: message.text == "🔐 CODE")
async def code_button(message: types.Message):
    await message.reply("Введіть текст для кодування:")


# Обробник кнопки "DECODE"
@dp.message_handler(lambda message: message.text == "🔓 DECODE")
async def decode_button(message: types.Message):
    await message.reply(
        "Введіть ключ і зашифрований текст для декодування \nнаприклад:\n 5       оІ.Ч6Щ1 2, ЩІ.ф}ІхІ г6лІ ц}6(}Іг4лІЩЩФ7")


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
@dp.message_handler(
    lambda message: message.text and not message.text.split()[0].isdigit() and message.text not in ["ℹ️ About", "🆘 Help",
                                                                                                    "🐍 Presentation"])
async def code_text(message: types.Message):
    input_text = message.text
    key, coded_text = coder(input_text)
    coded_text_ = f"<b>{coded_text}</b>"

    if len(coded_text) <= 25:
        # Текст короткий, створюємо інлайн-клавіатуру з кнопкою "DECODE"
        decode_button = InlineKeyboardButton("🔓 DECODE", callback_data=f"decode_{key}_{coded_text}")
        keyboard = InlineKeyboardMarkup().add(decode_button)
        await message.reply(f"Ключ Закодований_текст:\n{key}        {coded_text_}", reply_markup=keyboard, parse_mode="HTML")
    else:
        # Текст занадто довгий, відправляємо без кнопки
        await message.reply(f"Ключ Закодований_текст:\n{key}       {coded_text_}", parse_mode="HTML")


# Обробник текстового повідомлення після натискання кнопки "DECODE"
@dp.message_handler(lambda message: len(message.text.split()) > 1 and message.text.split()[0].isdigit())
async def decode_text(message: types.Message):
    try:
        key, input_text = message.text.split(maxsplit=1)
        key = int(key)
        if key > 30:
            await message.reply("Неправильний формат. Ключ повинен бути числом не більше 30.")
        else:
            decoded_text = decoder(key, input_text)
            decoded_text = '<b>' + decoded_text + '</b>'
            await message.reply(f"Розкодований текст:\n {decoded_text}",  parse_mode="HTML")
    except ValueError:
        await message.reply("Неправильний формат команди. Використовуйте <ключ> <текст>.")


# Обробник callback-запитів для кнопки "DECODE"
@dp.callback_query_handler(lambda c: c.data.startswith('decode_'))
async def decode_callback(query: types.CallbackQuery):
    # Отримайте дані з callback-запиту
    data = query.data.split('_')
    key = int(data[1])
    coded_text = data[2]

    # Виконайте декодування
    decoded_text = decoder(key, coded_text)
    decoded_text = '<b>' + decoded_text + '</b>'

    # Відправте результат у чат
    # await query.answer(f"Розкодований текст:\n{decoded_text}") # на чёрном фоне окно
    await bot.send_message(query.from_user.id, f"Розкодований текст:\n{decoded_text}",  parse_mode="HTML")


# Обробник кнопки "About"
@dp.message_handler(lambda message: message.text == "ℹ️ About")
async def about_button(message: types.Message):
    await message.reply(about_)


# @dp.message_handler(lambda message: message.text == "About")
# async def about_button(message: types.Message):
#     await message.reply(about_, parse_mode="HTML")


# Обробник кнопки "Help"
@dp.message_handler(lambda message: message.text == "🆘 Help")
async def help_button(message: types.Message):
    help_text = "\n".join(commands)
    await message.reply(f"Ласкаво просимо до нашого бота Цезаря!\nКоманди:\n\n{help_text}")


# Обробник кнопки "Presentation"
# @dp.message_handler(lambda message: message.text == "Presentation")
# async def presentation_button(message: types.Message):
#     await message.reply(presentation_text)
@dp.message_handler(lambda message: message.text == "🐍 Presentation")
async def presentation_button(message: types.Message):
    await message.reply(presentation_text, parse_mode="HTML")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
