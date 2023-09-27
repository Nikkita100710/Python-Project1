from config import TOKEN_BOT as TOKEN
import random
import string
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
logging.basicConfig(level=logging.INFO)

# Налаштовуємо рівень логування на INFO, щоб отримувати інформацію про події.
logging.basicConfig(level=logging.INFO)
# Створюємо об'єкт бота, використовуючи токен зі змінної TOKEN.
bot = Bot(token=TOKEN)
# Створюємо диспетчер, який відповідає за обробку повідомлень бота.
dp = Dispatcher(bot)
# Встановлюємо середовище реєстрації логів, щоб відстежувати події.
dp.middleware.setup(LoggingMiddleware())

# Визначаємо обробник для команди /start.
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(text="Створити Пароль")
    keyboard.add(button)
    await message.answer("Ласкаво просимо! Натисніть кнопку 'Створити Пароль', щоб згенерувати пароль.",
                         reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Створити Пароль")
async def generate_password(message: types.Message):
    await message.answer("Скільки букв має мати пароль?")
    await message.answer("Довжина паролю повинна бути більше 0.")

@dp.message_handler(lambda message: message.text.isdigit() and int(message.text) > 0, state=None)
async def process_password_length(message: types.Message):
    password_length = int(message.text)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(password_length))
    try:
        await message.answer(f"Згенерований пароль:\n{password}")
    except Exception as e:
        print(f"An error occurred: {e}")

@dp.message_handler(lambda message: not message.text.isdigit() or int(message.text) <= 0, state=None)
async def process_password_length_invalid(message: types.Message):
    await message.answer("Будь ласка, введіть коректну довжину паролю (ціле число).")


# Перевіряємо, чи файл виконується безпосередньо (а не імпортується як модуль).
if __name__ == '__main__':
    # Імпортуємо метод `start_polling` з модуля `executor` для запуску бота з використанням dp (диспетчера).
    from aiogram import executor

    # Запускаємо бота в режимі відстеження нових повідомлень (полінгу), ігноруючи оновлення (skip_updates=True).
    executor.start_polling(dp, skip_updates=True)
    """"""